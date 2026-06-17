---
description: Canonical example of a real analytics repository built around the Codex Batman backbone using a Kaggle-style housing price project.
---

# Analytics Repo Example

This is the clearest answer to the question:

> What does a real Codex Batman data science repository look like?

The shared project is a Kaggle-style housing price analysis using a standard supervised ML pipeline.

It is still a learning-friendly project, but it is structured like real work:

- the target is explicit
- the train/test split is explicit
- the baseline comes before model comparison
- artifacts are updated as the project advances
- the result is not just a chat transcript

## Shared Scenario

Dataset:

- Kaggle House Prices: Advanced Regression Techniques

Primary objective:

- predict `SalePrice`

Shared pipeline shape:

1. problem framing
2. data audit
3. split and prediction-time check
4. baseline model
5. feature handling
6. model comparison
7. evaluation
8. model card
9. workflow trace

## What The Repository Should Contain

```text
housing-prices-repo/
  README.md
  PROJECT_STATE.md
  project.yaml
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

## Why This Example Matters

This page is not only about the model.

It is about showing that a serious but approachable analytics repo has:

- a bounded problem
- durable project memory
- explicit decisions
- reproducible run records
- a final explanation of what the model should and should not be used for

## Same Standards, Different Delivery

The student and practitioner paths use the same backbone and should produce the same class of artifacts.

The difference is interaction style:

- student path: Codex teaches step by step, asks for attempts, and does not simply hand over the solution
- practitioner path: Codex executes more directly and compresses the path into a shorter working sequence

## Choose The Lens

- [Student path](student.md)
- [Practitioner path](practitioner.md)

## Related Pages

- [First Session - Predict Housing Prices with Tutor Mode](../../students/first-session.md)
- [For Students](../../students/index.md)
- [For Researchers & Data Scientists](../../data-scientists/index.md)
- [Core Data Science Workflow](../../workflows/data-science/index.md)
- [Backbone Protocol](../../backbone/index.md)
