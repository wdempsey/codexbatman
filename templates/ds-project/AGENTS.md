# AGENTS.md

## Purpose

This project uses the Codex Batman Backbone Protocol v0.1.

The goal is to keep analytical work reproducible, artifact-first, and legible to both humans and agents.

## Core Rules

1. Do not start modeling before problem framing is complete.
2. Do not start modeling before the data audit is complete.
3. Record substantial runs in `runs/experiment_log.md`.
4. Record material decisions in `analysis/decision_log.md`.
5. Update `PROJECT_STATE.md` when the project phase or risks change.
6. Draft shared outputs conservatively and document limits clearly.
7. Preserve raw data and do not edit it in place.

## Canonical Artifacts

- `PROJECT_STATE.md`
- `analysis/problem_frame.md`
- `data/data_card.md`
- `analysis/analysis_plan.md`
- `runs/experiment_log.md`
- `reports/model_card.md`
- `memory/workflow_trace.md`
- `analysis/decision_log.md`

## Workflow Order

```text
bootstrap
-> frame
-> audit
-> plan
-> execute
-> evaluate
-> communicate
-> trace
-> distill
-> improve
```

## Working Style

- Prefer small, reversible changes.
- Keep artifacts human-readable.
- Use markdown as the default memory layer.
- Treat these files as durable project memory, not scratch notes.
