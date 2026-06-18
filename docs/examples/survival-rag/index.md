# Survival Analysis RAG Example

This example shows how to build a local RAG (Retrieval-Augmented Generation) pipeline that lets you query your own survival analysis textbook and the lung cancer dataset through a Socratic tutor.

It is the canonical **bring your own materials** demo for this repo — a template any student can adapt when they have a PDF textbook, a course reader, or any structured dataset.

**Source:** [`examples/survival-rag/`](https://github.com/wdempsey/codexbatman/tree/main/examples/survival-rag) in the repo root.

---

## What it does

You provide a PDF textbook. The pipeline:

1. Extracts and chunks the PDF into overlapping text segments
2. Embeds them with `text-embedding-3-small` into a local ChromaDB index
3. Embeds the dataset codebook (variable descriptions, summary statistics) into a second collection
4. On each query: retrieves the most relevant passages from both collections, then passes them to a Socratic wrapper that guides rather than answers

The tutor signals clearly where it is drawing from: *"The textbook introduces this as..."* vs. *"From the dataset codebook for this variable..."*

---

## Two-pronged architecture

| Collection | Source | Handles |
|---|---|---|
| `textbook_chunks` | PDF pages → chunked → embedded | Conceptual questions: "What is the hazard function?" |
| `dataset_codebook` | Variable descriptions + summary stats | Applied questions: "What does `status` mean?" |

Separating them matters: conceptual retrieval needs semantic search over prose; dataset retrieval needs precise variable-level matching. Mixing them degrades both.

---

## Stack

- **PDF extraction:** `pypdf`
- **Chunking:** `langchain-text-splitters` — `RecursiveCharacterTextSplitter` with sentence-boundary awareness
- **Embeddings:** OpenAI `text-embedding-3-small` — fast, cheap, excellent for technical text
- **Vector store:** ChromaDB — local, no external service, persists to `examples/survival-rag/chroma_db/`
- **Chat layer:** OpenAI `gpt-4o-mini` with a Socratic system prompt
- **Interface:** CLI (`query.py`) and Jupyter notebook

Swap any layer: see the Ollama comment in `ingest.py` for local embeddings, or the `SOCRATIC_SYSTEM_PROMPT` in `query.py` to change the tutor's style.

---

## Quickstart

**1. Get the dataset**
```bash
cd examples/survival-rag
python data/get_lung.py      # downloads lung.csv from public Rdatasets mirror
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Set your API key**
```bash
export OPENAI_API_KEY=sk-...
```

**4. Ingest**
```bash
# Dataset codebook only (no PDF needed to try it out)
python ingest.py --dataset-only

# With your textbook PDF
python ingest.py --pdf-path ~/books/klein_moeschberger.pdf
```

**5. Query**
```bash
python query.py "What is the hazard function?"
python query.py "What does the status variable mean?"
python query.py --verbose "How do I interpret a hazard ratio?"
python query.py   # interactive mode
```

---

## What the textbook retrieval looks like

With the PDF ingested, a conceptual question like *"What is the hazard function?"* returns something like:

```
Question: What is the hazard function?
────────────────────────────────────────────────────────────
[Retrieved 3 textbook passage(s)]
  Page 11 — similarity 0.87
  Page 14 — similarity 0.84
  Page 22 — similarity 0.81

Tutor:

The textbook retrieved here introduces the hazard function as
the instantaneous risk of the event occurring at time t, given
survival up to that point. Before I explain it further — can
you tell me what "instantaneous risk" means in this context?
What would it mean for the hazard to be constant over time
vs. increasing?
```

Without the PDF, the same question returns a Socratic response from general knowledge — the framing is similar but there is no `[Retrieved N textbook passage(s)]` line and no page attribution.

---

## Dataset

NCCTG Lung Cancer Dataset (`survival::lung` in R).

228 patients with advanced lung cancer enrolled at 19 NCCTG institutions (1980–1988). Primary outcome: overall survival in days. Approximately 72% of patients experienced the event (death) during follow-up.

Key variables: `time` (days), `status` (1=censored, 2=dead), `age`, `sex`, `ph.ecog` (ECOG performance score), `ph.karno` (Karnofsky score by physician), `pat.karno` (Karnofsky by patient), `meal.cal`, `wt.loss`.

Missing data in `meal.cal` (~21%) and `wt.loss` (~6%) — relevant for data audit exercises.

**Reference:** Loprinzi CL. et al. (1994). Prospective evaluation of prognostic variables from patient-completed questionnaires. *Journal of Clinical Oncology* 12:601-607.

---

## Recommended textbooks

Point `ingest.py` at any of these:

- **Klein & Moeschberger** — *Survival Analysis: Techniques for Censored and Truncated Data* (2nd ed., Springer 2003). The most commonly used applied textbook. Good for KM, log-rank, and Cox with clinical examples.
- **Kalbfleisch & Prentice** — *The Statistical Analysis of Failure Time Data* (2nd ed., Wiley 2002). More theoretical; useful if you want to understand the partial likelihood derivation.
- **Harrell** — *Regression Modeling Strategies* (2nd ed., Springer 2015). Broader than survival but has excellent chapters on Cox and on model validation.

The PDF is never committed to the repo. The `README.md` explains where to obtain your copy.

---

## Walkthrough notebook

[`notebooks/survival-rag-walkthrough.ipynb`](https://github.com/wdempsey/codexbatman/tree/main/examples/survival-rag/notebooks/survival-rag-walkthrough.ipynb) — runs end-to-end without a PDF (Section 1–5 use the dataset codebook alone). Includes a with-vs-without-RAG comparison and a section on extending to your own materials.

---

## Extending to your own book

- **Different dataset:** edit `LUNG_CODEBOOK` and `DATASET_OVERVIEW` in `ingest.py`
- **Different textbook:** point `--pdf-path` at any PDF — chunking is book-agnostic
- **Local embeddings:** see the Ollama comment in `ingest.py` (`nomic-embed-text`, 768-dim)
- **Larger context:** increase `N_RESULTS` in `query.py` to retrieve more passages per query

---

## Related

- [Basic Classification Example](../basic-classification/index.md) — the introductory worked example; start here before the RAG pipeline
- [Linear Regression Example](../analytics-repo/index.md) — California Housing, continuous prediction
- [Data Science Workflow](../../workflows/data-science/index.md) — the seven workflow gates underlying all examples
- [Textbook Resources](../../system/textbook-resources.md) — Klein, Kalbfleisch, Harrell overview
