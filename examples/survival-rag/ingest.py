#!/usr/bin/env python3
"""
Ingest survival analysis materials into ChromaDB for RAG.

Two separate collections are built:
  textbook_chunks   — PDF pages split into overlapping chunks, embedded and stored.
                      Handles questions like "What is the log-rank test?"
  dataset_codebook  — Variable descriptions + summary statistics for the lung
                      dataset, embedded as structured documents.
                      Handles questions like "What does the status variable mean?"

Usage:
  python ingest.py --pdf-path /path/to/klein_moeschberger.pdf
  python ingest.py --pdf-path /path/to/textbook.pdf --lung-csv data/lung.csv
  python ingest.py --dataset-only   # skip PDF, just ingest the dataset codebook

Environment:
  OPENAI_API_KEY must be set (or in .env).
  To use a local embedding model instead, see the OLLAMA section below.

ChromaDB is written to ./chroma_db/ (gitignored). Delete that folder to rebuild.
"""

import argparse
import hashlib
import os
import sys
from pathlib import Path

import chromadb
import pandas as pd
from dotenv import load_dotenv
from openai import OpenAI
from tqdm import tqdm

load_dotenv()

# ─── Paths ────────────────────────────────────────────────────────────────────

BASE_DIR = Path(__file__).parent
CHROMA_PATH = BASE_DIR / "chroma_db"
DEFAULT_LUNG_CSV = BASE_DIR / "data" / "lung.csv"

# ─── Constants ────────────────────────────────────────────────────────────────

EMBED_MODEL = "text-embedding-3-small"
CHUNK_SIZE = 800        # characters per chunk — balances context vs precision
CHUNK_OVERLAP = 150     # overlap keeps sentences from splitting across chunks

TEXTBOOK_COLLECTION = "textbook_chunks"
DATASET_COLLECTION = "dataset_codebook"

# ─── Embedding ────────────────────────────────────────────────────────────────

def make_embed_fn(client: OpenAI):
    """Return an embedding function that batches requests to stay under API limits."""

    def embed(texts: list[str]) -> list[list[float]]:
        # OpenAI accepts up to 2048 texts per request for small models
        results = []
        batch_size = 100
        for i in range(0, len(texts), batch_size):
            batch = texts[i : i + batch_size]
            resp = client.embeddings.create(model=EMBED_MODEL, input=batch)
            results.extend([item.embedding for item in resp.data])
        return results

    return embed


# ─── Ollama alternative ───────────────────────────────────────────────────────
# To use a local embedding model instead of OpenAI, replace make_embed_fn with:
#
#   import ollama
#   def make_embed_fn(_):
#       def embed(texts):
#           return [
#               ollama.embeddings(model="nomic-embed-text", prompt=t)["embedding"]
#               for t in texts
#           ]
#       return embed
#
# Then `pip install ollama` and run `ollama pull nomic-embed-text`.
# Dimension is 768 instead of 1536, so delete chroma_db/ if switching.


# ─── Book ingestion ───────────────────────────────────────────────────────────

def load_pdf_pages(pdf_path: Path) -> list[dict]:
    """Extract text from each page of a PDF. Returns list of {page, text} dicts."""
    try:
        from pypdf import PdfReader
    except ImportError:
        print("ERROR: pypdf not installed. Run: pip install pypdf")
        sys.exit(1)

    reader = PdfReader(str(pdf_path))
    pages = []
    for i, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        if text.strip():  # skip blank/image-only pages
            pages.append({"page": i + 1, "text": text})

    print(f"  Extracted text from {len(pages)} pages (of {len(reader.pages)} total)")
    return pages


def chunk_text(text: str, chunk_size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP) -> list[str]:
    """
    Split text into overlapping chunks using LangChain's RecursiveCharacterTextSplitter.
    Tries to split on paragraph and sentence boundaries before falling back to characters.
    """
    try:
        from langchain_text_splitters import RecursiveCharacterTextSplitter
    except ImportError:
        print("ERROR: langchain-text-splitters not installed.")
        print("Run: pip install langchain-text-splitters")
        sys.exit(1)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=overlap,
        separators=["\n\n", "\n", ". ", " ", ""],
    )
    return splitter.split_text(text)


def ingest_textbook(pdf_path: Path, collection, embed_fn) -> int:
    """
    Full pipeline: PDF → pages → chunks → embeddings → ChromaDB.
    Returns the number of chunks ingested.
    """
    print(f"\n[BOOK] Loading PDF: {pdf_path.name}")
    pages = load_pdf_pages(pdf_path)

    # Check for existing chunks to avoid re-embedding if collection already has data
    existing = collection.count()
    if existing > 0:
        print(f"  Collection already has {existing} chunks. Skipping re-ingest.")
        print("  Delete chroma_db/ and re-run to force rebuild.")
        return existing

    # Chunk all pages
    print(f"  Chunking {len(pages)} pages (chunk_size={CHUNK_SIZE}, overlap={CHUNK_OVERLAP})...")
    all_chunks = []
    for p in pages:
        chunks = chunk_text(p["text"])
        for j, chunk in enumerate(chunks):
            chunk_id = hashlib.md5(f"p{p['page']}_c{j}".encode()).hexdigest()[:12]
            all_chunks.append({
                "id": f"book_{chunk_id}",
                "text": chunk,
                "metadata": {
                    "source": "textbook",
                    "pdf_name": pdf_path.name,
                    "page": p["page"],
                    "chunk_index": j,
                },
            })

    print(f"  Created {len(all_chunks)} chunks. Embedding...")

    # Embed in batches with progress bar
    texts = [c["text"] for c in all_chunks]
    embeddings = []
    batch_size = 100
    for i in tqdm(range(0, len(texts), batch_size), desc="  Embedding batches"):
        batch_embeddings = embed_fn(texts[i : i + batch_size])
        embeddings.extend(batch_embeddings)

    # Store in ChromaDB
    print("  Writing to ChromaDB...")
    collection.add(
        ids=[c["id"] for c in all_chunks],
        embeddings=embeddings,
        documents=[c["text"] for c in all_chunks],
        metadatas=[c["metadata"] for c in all_chunks],
    )
    print(f"  Done. {len(all_chunks)} textbook chunks stored.")
    return len(all_chunks)


# ─── Dataset ingestion ────────────────────────────────────────────────────────

# Variable codebook for the NCCTG lung cancer dataset (survival::lung in R).
# Reference: Loprinzi et al. (1994), J Clin Oncol 12:601-607.
LUNG_CODEBOOK = {
    "inst": (
        "Institution code. There are 19 participating NCCTG member institutions. "
        "This variable identifies the treatment center and is not typically used "
        "as a predictor in standard analyses — it is a clustering variable."
    ),
    "time": (
        "Survival time in days. This is the primary outcome variable. "
        "For censored observations (status=1), this is the follow-up time — the patient "
        "was alive at last contact. For dead observations (status=2), this is the time "
        "from study registration to death."
    ),
    "status": (
        "Censoring status: 1 = censored (patient was alive or lost to follow-up at end of "
        "study period), 2 = dead. In survival analysis, a censored observation means we know "
        "the patient survived at least 'time' days but do not observe the event. "
        "Censoring is informative about the study design, not a data quality problem."
    ),
    "age": (
        "Patient age in years at time of study entry. Ranges from 39 to 82. "
        "Age is a standard clinical covariate in cancer survival models."
    ),
    "sex": (
        "Patient sex: 1 = Male, 2 = Female. Sex is a well-established prognostic factor "
        "in lung cancer — female patients tend to have longer survival. In the lung dataset, "
        "approximately 60% of patients are male."
    ),
    "ph.ecog": (
        "ECOG performance score as rated by the treating physician. "
        "Scale: 0 = fully active/asymptomatic, 1 = symptomatic but ambulatory, "
        "2 = in bed less than 50% of day, 3 = in bed more than 50% of day, "
        "4 = bedbound, 5 = dead. "
        "Higher scores indicate worse functional status and typically predict worse survival. "
        "This is the most widely used performance status scale in oncology trials. "
        "One observation has ph.ecog = 3; most patients are 0, 1, or 2."
    ),
    "ph.karno": (
        "Karnofsky performance score as rated by the treating physician. "
        "Scale: 0–100 in 10-point increments. 100 = normal functioning, "
        "80–90 = normal activities with minor symptoms, 70 = cares for self but unable to work, "
        "60 = requires occasional assistance, 50 = requires considerable assistance, "
        "lower values indicate increasing dependence. The Karnofsky scale is the inverse "
        "of the ECOG scale: a lower Karnofsky score corresponds to a higher ECOG score."
    ),
    "pat.karno": (
        "Karnofsky performance score as rated by the patient themselves (patient self-report). "
        "Patients and physicians sometimes rate performance status differently. "
        "Discordance between ph.karno and pat.karno can itself be clinically informative. "
        "Has missing values for some observations."
    ),
    "meal.cal": (
        "Calories consumed at meals per day. Missing data is common for this variable "
        "(approximately 47 missing values out of 228 total observations — about 21%). "
        "A nutritional indicator: low caloric intake often co-occurs with unintentional "
        "weight loss in advanced cancer patients."
    ),
    "wt.loss": (
        "Weight loss in pounds over the six months prior to study entry. "
        "Negative values are possible (indicating weight gain). "
        "Missing in approximately 14 observations. "
        "Unintentional weight loss > 5% of body weight over 6 months is a standard "
        "clinical marker of cancer cachexia and a known prognostic factor."
    ),
}

DATASET_OVERVIEW = """
NCCTG Lung Cancer Dataset (survival::lung in R)
Reference: Loprinzi CL. et al. (1994). Prospective evaluation of prognostic variables
from patient-completed questionnaires. Journal of Clinical Oncology 12:601-607.

228 patients with advanced lung cancer. All patients were enrolled at NCCTG member
institutions between 1980 and 1988.

Primary outcome: overall survival (days).
Censoring: approximately 28% of patients were censored (alive at end of study).
Event rate: approximately 72% of patients died during follow-up.

Missing data summary:
  meal.cal: ~47 missing (~21%)
  pat.karno: ~3 missing
  ph.ecog: 1 missing
  ph.karno: 1 missing
  wt.loss: ~14 missing (~6%)
  All other variables: complete

Key relationships:
  - ph.ecog and ph.karno measure the same construct on different scales (inversely).
  - ph.karno and pat.karno measure the same construct but can diverge (physician vs patient).
  - meal.cal and wt.loss together index nutritional status.
  - time and status together define the survival outcome (the pair used in Surv() in R).
"""

DATASET_MODELING_NOTES = """
Common analysis patterns for the lung dataset:

Kaplan-Meier survival curves:
  - Overall KM curve: Surv(time, status==2) ~ 1
  - Stratified by sex: Surv(time, status==2) ~ sex
  - Stratified by ECOG: Surv(time, status==2) ~ ph.ecog
  Log-rank test compares group survival curves; assumes proportional hazards between groups.

Cox proportional hazards model:
  - Standard model: Surv(time, status==2) ~ age + sex + ph.ecog + ph.karno + wt.loss
  - ph.karno and ph.ecog are correlated — avoid including both without checking.
  - meal.cal has many missing values — impute or exclude depending on analysis goal.
  Interpretation: hazard ratio for sex (male vs female) typically 1.5–2.0, indicating
  male patients have 50–100% higher instantaneous risk of death at any given time.

Status coding note:
  The lung dataset uses status = 2 for the event (death), not status = 1.
  In Python's lifelines library: event_observed = (status == 2).
  In R's survival package: Surv(time, status==2).
"""


def build_codebook_documents(csv_path: Path) -> list[dict]:
    """
    Build a list of embedded documents from the dataset codebook.
    Returns list of {id, text, metadata} dicts.
    One document per variable + overview + modeling notes.
    """
    docs = []

    # Dataset overview
    docs.append({
        "id": "dataset_overview",
        "text": DATASET_OVERVIEW.strip(),
        "metadata": {"source": "dataset_codebook", "type": "overview"},
    })

    # Modeling notes
    docs.append({
        "id": "dataset_modeling_notes",
        "text": DATASET_MODELING_NOTES.strip(),
        "metadata": {"source": "dataset_codebook", "type": "modeling_notes"},
    })

    # Per-variable documents
    for var_name, description in LUNG_CODEBOOK.items():
        docs.append({
            "id": f"dataset_var_{var_name}",
            "text": f"Variable: {var_name}\n\n{description}",
            "metadata": {"source": "dataset_codebook", "type": "variable", "variable": var_name},
        })

    # If CSV exists, add summary statistics per variable
    if csv_path.exists():
        df = pd.read_csv(csv_path)
        for col in df.columns:
            if col in LUNG_CODEBOOK:
                desc = df[col].describe().to_dict()
                stats_text = (
                    f"Variable: {col} — Summary statistics\n"
                    f"  Count (non-missing): {int(desc.get('count', 0))}\n"
                    f"  Missing: {int(df[col].isnull().sum())}\n"
                )
                if col not in ("status", "sex", "inst"):
                    stats_text += (
                        f"  Mean: {desc.get('mean', 'N/A'):.1f}\n"
                        f"  Std:  {desc.get('std', 'N/A'):.1f}\n"
                        f"  Min:  {desc.get('min', 'N/A'):.1f}\n"
                        f"  Max:  {desc.get('max', 'N/A'):.1f}\n"
                    )
                docs.append({
                    "id": f"dataset_stats_{col}",
                    "text": stats_text.strip(),
                    "metadata": {"source": "dataset_codebook", "type": "stats", "variable": col},
                })

    return docs


def ingest_dataset(csv_path: Path, collection, embed_fn) -> int:
    """
    Dataset pipeline: codebook + summary stats → embeddings → ChromaDB.
    Does not require the CSV to exist — falls back to codebook-only if missing.
    Returns the number of documents ingested.
    """
    print(f"\n[DATASET] Building codebook documents...")

    existing = collection.count()
    if existing > 0:
        print(f"  Collection already has {existing} documents. Skipping re-ingest.")
        print("  Delete chroma_db/ and re-run to force rebuild.")
        return existing

    if not csv_path.exists():
        print(f"  NOTE: {csv_path} not found — using codebook only (no summary stats).")
        print(f"  Run python data/get_lung.py to add real summary statistics.")

    docs = build_codebook_documents(csv_path)
    print(f"  Built {len(docs)} codebook documents. Embedding...")

    texts = [d["text"] for d in docs]
    embeddings = embed_fn(texts)

    collection.add(
        ids=[d["id"] for d in docs],
        embeddings=embeddings,
        documents=[d["text"] for d in docs],
        metadatas=[d["metadata"] for d in docs],
    )
    print(f"  Done. {len(docs)} dataset documents stored.")
    return len(docs)


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Ingest survival analysis materials into ChromaDB.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python ingest.py --pdf-path ~/books/klein_moeschberger.pdf
  python ingest.py --pdf-path ~/books/textbook.pdf --lung-csv data/lung.csv
  python ingest.py --dataset-only
        """,
    )
    parser.add_argument(
        "--pdf-path",
        type=Path,
        help="Path to your survival analysis textbook PDF.",
    )
    parser.add_argument(
        "--lung-csv",
        type=Path,
        default=DEFAULT_LUNG_CSV,
        help=f"Path to lung.csv (default: {DEFAULT_LUNG_CSV}). Run data/get_lung.py first.",
    )
    parser.add_argument(
        "--dataset-only",
        action="store_true",
        help="Skip PDF ingestion — only ingest the dataset codebook.",
    )
    args = parser.parse_args()

    if not args.dataset_only and args.pdf_path is None:
        parser.error("Either --pdf-path or --dataset-only is required.")
    if args.pdf_path and not args.pdf_path.exists():
        parser.error(f"PDF not found: {args.pdf_path}")

    # OpenAI client
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("ERROR: OPENAI_API_KEY not set. Add it to your environment or .env file.")
        sys.exit(1)

    openai_client = OpenAI(api_key=api_key)
    embed_fn = make_embed_fn(openai_client)

    # ChromaDB setup
    CHROMA_PATH.mkdir(exist_ok=True)
    db = chromadb.PersistentClient(path=str(CHROMA_PATH))

    # Run ingestion pipelines
    if not args.dataset_only:
        textbook_col = db.get_or_create_collection(
            name=TEXTBOOK_COLLECTION,
            metadata={"hnsw:space": "cosine"},
        )
        n_book = ingest_textbook(args.pdf_path, textbook_col, embed_fn)

    dataset_col = db.get_or_create_collection(
        name=DATASET_COLLECTION,
        metadata={"hnsw:space": "cosine"},
    )
    n_dataset = ingest_dataset(args.lung_csv, dataset_col, embed_fn)

    print("\n✓ Ingest complete.")
    if not args.dataset_only:
        print(f"  Textbook chunks : {n_book}")
    print(f"  Dataset docs    : {n_dataset}")
    print(f"  ChromaDB path   : {CHROMA_PATH.resolve()}")
    print("\nRun query.py to start asking questions:")
    print('  python query.py "What is the hazard function?"')


if __name__ == "__main__":
    main()
