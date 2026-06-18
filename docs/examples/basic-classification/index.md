---
description: A classification walkthrough using the Cleveland Heart Disease dataset — predicting cardiac risk with the Codex Batman backbone.
---

# Basic Classification Example

This example runs the full Codex Batman workflow on a real clinical dataset: predicting the presence of heart disease from patient features to support a referral decision.

The dataset is the [Cleveland Heart Disease dataset](https://www.kaggle.com/datasets/cherngs/heart-disease-cleveland-uci) (UCI). 303 patients, 13 features — age, sex, chest pain type, cholesterol, resting heart rate, and others measured at a cardiology clinic. The target is whether heart disease is present (binary: no disease vs. disease detected). The decision it supports: should this patient be referred for further cardiac evaluation?

This is a genuine classification problem with real stakes. The leakage question is non-trivial (several features are only available after a stress test). The threshold decision matters clinically — false negatives send sick patients home. And the model card has to say something honest about who this model was trained on and where it shouldn't be deployed.

## What ends up in the repository

```text
cardiac-risk-classifier/
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

## Same backbone, different problem type

The housing-price example targets a continuous outcome and optimizes RMSE. This example targets a binary outcome and optimizes ROC-AUC — but the gate structure is identical. Problem framing, data audit, split strategy, baseline, candidate models, evaluation, experiment logging. The discipline is the same; what changes is how you reason about the metric, the threshold, and the failure modes.

## Three lenses on the same project

- [Learning lens →](learning.md) — tutor mode with attempt-before-answer coaching and a 7-step interactive demo
- [Execution lens →](execution.md) — practitioner pace, direct gate traversal, same artifact standards
- [Manager lens →](manager.md) — artifact review and go/no-go decisions; no code, no modeling calls

## Related

- [Analytics Repo Example](../analytics-repo/index.md) — the regression counterpart with the same backbone
- [Core Data Science Workflow](../../workflows/data-science/index.md)
- [Backbone Protocol](../../backbone/index.md)
