# Skill Evals

This directory contains runnable skill eval task sets.

The runner validates eval structure and can optionally score saved response text files with deterministic `must_include` and `must_not_include` checks. It does not call an LLM.

## Layout

```text
evals/
  improvement/  # editable examples used to diagnose and improve skills
  heldout/      # frozen regression checks; do not use for drafting improvements
  schemas/      # documented JSON shape
```

## Run

From the repository root:

```bash
./.venv/bin/python scripts/evals/run_skill_evals.py
```

With response files:

```bash
./.venv/bin/python scripts/evals/run_skill_evals.py --responses-dir evals/responses
```

Response files are plain text files named `<case-id>.txt`.

## Eval File Shape

Each JSON file has:

- `schema_version`
- `skill`
- `split`: `improvement` or `heldout`
- `cases`

Each case has:

- `id`
- `input`
- `expected_route`
- `must_include`
- `must_not_include`
- `notes`

See `evals/schemas/skill-eval.schema.json`.

## Held-Out Rule

Use `evals/improvement/` to diagnose and draft skill improvements.

Use `evals/heldout/` only after a proposal exists. Do not edit held-out evals in the same PR as a skill improvement.
