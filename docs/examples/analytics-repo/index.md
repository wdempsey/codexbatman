---
description: Canonical example of a real analytics repository built around the Codex Batman backbone using a Kaggle-style housing price project.
---

# Analytics Repo Example

This is the clearest answer to "what does a real Codex Batman project look like?" — a Kaggle-style housing-price analysis built through all eight workflow gates, with durable artifacts at each stage.

The project uses the [Ames Housing dataset](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques) to predict `SalePrice`. It's approachable enough to learn from, but structured like real work: explicit target, fixed validation set, baseline before model comparison, and a written record of every decision.

## What ends up in the repository

```text
housing-prices-repo/
  README.md
  PROJECT_STATE.md
  analysis/
    problem_frame.md
    analysis_plan.md
    decision_log.md
  data/
    data_card.md
  runs/
    experiment_log.md
  reports/
    model_card.md
  memory/
    workflow_trace.md
```

These aren't documentation files bolted on afterward — they're produced during the workflow, one gate at a time. The `experiment_log.md` gets a new entry every time you run a model. The `workflow_trace.md` captures what happened and what comes next so the next session can start from real project state.

## Same backbone, different delivery

Both paths run the same eight-gate sequence: problem framing, data audit, split strategy, baseline model, feature handling, model comparison, evaluation, and workflow trace. The backbone and artifact standards are identical.

What changes is how Codex helps you move through it. On the student path, Codex asks for your attempt before revealing the output — the goal is to build your understanding alongside the artifact. On the practitioner path, Codex executes more directly and compresses the working sequence.

## Choose your path

- [Student path →](student.md) — attempt-before-answer coaching, interactive 8-step demo, and a live session example
- [Practitioner path →](practitioner.md) — direct execution, same standards, shorter sequence

## Related

- [For Students](../../students/index.md)
- [For Researchers & Data Scientists](../../data-scientists/index.md)
- [Core Data Science Workflow](../../workflows/data-science/index.md)
- [Backbone Protocol](../../backbone/index.md)
