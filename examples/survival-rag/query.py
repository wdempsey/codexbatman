#!/usr/bin/env python3
"""
Query survival analysis materials via Socratic RAG.

Retrieves relevant passages from two ChromaDB collections:
  textbook_chunks   — textbook content (conceptual questions)
  dataset_codebook  — dataset variable descriptions and stats (applied questions)

Then wraps the retrieved context in a Socratic system prompt: the tutor
uses the passages to guide the student toward the answer rather than
reciting it back. Source attribution ("Based on the textbook..." vs.
"From the dataset codebook...") is preserved in every response.

Usage:
  python query.py "What is the hazard function?"
  python query.py "What does the status variable mean?"
  python query.py "How do I interpret a hazard ratio?"
  python query.py   # interactive mode

Environment:
  OPENAI_API_KEY must be set (or in .env).
  Run ingest.py first to build the ChromaDB index.
"""

import argparse
import os
import sys
from pathlib import Path

import chromadb
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# ─── Paths and constants ──────────────────────────────────────────────────────

BASE_DIR = Path(__file__).parent
CHROMA_PATH = BASE_DIR / "chroma_db"

TEXTBOOK_COLLECTION = "textbook_chunks"
DATASET_COLLECTION = "dataset_codebook"

EMBED_MODEL = "text-embedding-3-small"
CHAT_MODEL = "gpt-4o-mini"      # fast and cost-effective for Socratic responses
N_RESULTS = 3                    # passages retrieved per collection

# ─── Retrieval ────────────────────────────────────────────────────────────────

def embed_query(question: str, client: OpenAI) -> list[float]:
    resp = client.embeddings.create(model=EMBED_MODEL, input=[question])
    return resp.data[0].embedding


def retrieve(question: str, db: chromadb.ClientAPI, query_embedding: list[float]) -> dict:
    """
    Query both collections. Returns a dict with textbook and dataset results.
    Gracefully handles missing collections (e.g., if --dataset-only was used).
    """
    results = {"textbook": [], "dataset": []}

    collection_names = [c.name for c in db.list_collections()]

    if TEXTBOOK_COLLECTION in collection_names:
        col = db.get_collection(TEXTBOOK_COLLECTION)
        if col.count() > 0:
            r = col.query(query_embeddings=[query_embedding], n_results=N_RESULTS)
            for doc, meta, dist in zip(
                r["documents"][0], r["metadatas"][0], r["distances"][0]
            ):
                results["textbook"].append({
                    "text": doc,
                    "page": meta.get("page", "?"),
                    "pdf": meta.get("pdf_name", "textbook"),
                    "distance": dist,
                })

    if DATASET_COLLECTION in collection_names:
        col = db.get_collection(DATASET_COLLECTION)
        if col.count() > 0:
            r = col.query(query_embeddings=[query_embedding], n_results=N_RESULTS)
            for doc, meta, dist in zip(
                r["documents"][0], r["metadatas"][0], r["distances"][0]
            ):
                results["dataset"].append({
                    "text": doc,
                    "type": meta.get("type", "?"),
                    "variable": meta.get("variable", ""),
                    "distance": dist,
                })

    return results


# ─── Context formatting ───────────────────────────────────────────────────────

def format_context(results: dict) -> str:
    """
    Format retrieved passages into a context block for the system prompt.
    Source attribution is embedded in the text so the LLM can reference it naturally.
    """
    parts = []

    if results["textbook"]:
        parts.append("=== RETRIEVED FROM TEXTBOOK ===")
        for i, r in enumerate(results["textbook"], 1):
            parts.append(f"[Textbook passage {i} — page {r['page']}]")
            parts.append(r["text"].strip())
            parts.append("")

    if results["dataset"]:
        parts.append("=== RETRIEVED FROM DATASET CODEBOOK ===")
        for i, r in enumerate(results["dataset"], 1):
            label = f"[Dataset: {r['type']}"
            if r["variable"]:
                label += f" — {r['variable']}"
            label += "]"
            parts.append(label)
            parts.append(r["text"].strip())
            parts.append("")

    if not parts:
        return "[No relevant passages retrieved from either collection.]"

    return "\n".join(parts)


# ─── Socratic wrapper ─────────────────────────────────────────────────────────

SOCRATIC_SYSTEM_PROMPT = """You are a Socratic tutor for survival analysis. A student has asked you a question. You have retrieved relevant passages from two sources: their textbook and their dataset codebook. Both are included below.

Your role is to guide the student toward understanding — not to answer the question for them.

How to use the retrieved context:
- When drawing on a textbook passage, signal it: "The textbook introduces this as..." or "Based on the Klein & Moeschberger passage retrieved..." — then ask a guiding question, not state the answer.
- When drawing on a dataset codebook entry, signal it: "Looking at the dataset codebook..." or "From the codebook for this variable..." — then connect it to the student's question.
- If retrieved context is not directly relevant to the student's question, acknowledge that briefly and reason from first principles instead.

Rules:
1. Ask one or two focused Socratic questions per response — do not ask three or four.
2. Do not answer the student's question directly. Guide them to the insight.
3. Keep responses concise: two to four sentences plus one or two questions.
4. If the student has already shown reasoning, build on it — don't start from scratch.
5. Never cite page numbers verbatim — paraphrase the concept and ask about it.

Retrieved context:
{context}"""


def socratic_response(question: str, context: str, client: OpenAI) -> str:
    system_prompt = SOCRATIC_SYSTEM_PROMPT.format(context=context)

    resp = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question},
        ],
        temperature=0.4,   # low temp keeps responses focused and consistent
        max_tokens=400,
    )
    return resp.choices[0].message.content.strip()


# ─── Display ──────────────────────────────────────────────────────────────────

def print_response(question: str, results: dict, response: str, verbose: bool = False):
    print()
    print(f"Question: {question}")
    print("─" * 60)

    if verbose:
        if results["textbook"]:
            print(f"\n[Retrieved {len(results['textbook'])} textbook passage(s)]")
            for r in results["textbook"]:
                print(f"  Page {r['page']} — similarity {1 - r['distance']:.2f}")
        if results["dataset"]:
            print(f"[Retrieved {len(results['dataset'])} dataset codebook entry(ies)]")
            for r in results["dataset"]:
                label = r["variable"] if r["variable"] else r["type"]
                print(f"  {label} — similarity {1 - r['distance']:.2f}")
        print()

    print("Tutor:\n")
    print(response)
    print()


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Query survival analysis materials via Socratic RAG.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python query.py "What is the hazard function?"
  python query.py "What does the status variable mean?"
  python query.py "How do I interpret a hazard ratio?"
  python query.py --verbose "Why do we use the log-rank test?"
  python query.py   # interactive mode
        """,
    )
    parser.add_argument("question", nargs="?", help="Question to ask (omit for interactive mode)")
    parser.add_argument(
        "--verbose", "-v", action="store_true",
        help="Show retrieved passage metadata (page numbers, similarity scores)"
    )
    args = parser.parse_args()

    # Check ChromaDB exists
    if not CHROMA_PATH.exists():
        print("ERROR: ChromaDB not found. Run ingest.py first:")
        print("  python ingest.py --pdf-path /path/to/textbook.pdf")
        print("  python ingest.py --dataset-only   # just the dataset codebook")
        sys.exit(1)

    # OpenAI client
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("ERROR: OPENAI_API_KEY not set. Add it to your environment or .env file.")
        sys.exit(1)

    openai_client = OpenAI(api_key=api_key)
    db = chromadb.PersistentClient(path=str(CHROMA_PATH))

    def ask(question: str):
        query_embedding = embed_query(question, openai_client)
        results = retrieve(question, db, query_embedding)
        context = format_context(results)
        response = socratic_response(question, context, openai_client)
        print_response(question, results, response, verbose=args.verbose)

    if args.question:
        ask(args.question)
    else:
        # Interactive mode
        print("Survival Analysis RAG Tutor — interactive mode")
        print("Type a question and press Enter. Ctrl-C or 'quit' to exit.")
        print()
        while True:
            try:
                question = input("Your question: ").strip()
            except (KeyboardInterrupt, EOFError):
                print("\nGoodbye.")
                break
            if question.lower() in ("quit", "exit", "q"):
                break
            if not question:
                continue
            ask(question)


if __name__ == "__main__":
    main()
