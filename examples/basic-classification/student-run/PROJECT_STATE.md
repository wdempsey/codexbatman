# PROJECT_STATE

_Updated end-of-session_

---

## Current State

**Status**: Baseline complete. Model selected. Ready for threshold sensitivity analysis or handoff.

**Selected model**: Random Forest, n_estimators=100, threshold=0.38
**Last AUC**: 0.891 (test set, n=61)
**Last sensitivity**: 0.882 at threshold 0.38

## What Is Done

- [x] Problem framing (decision, metric, prediction time)
- [x] Data audit (missingness plan, class balance, target binarization)
- [x] Analysis plan (split, preprocessing, model candidates)
- [x] Baseline (logistic regression, AUC=0.871)
- [x] Model comparison (random forest, AUC=0.891)
- [x] Threshold tuning (0.38, sensitivity=0.882)
- [x] Model card (performance, limitations, intended use)
- [x] Workflow trace

## What Is Not Done

- [ ] Threshold sensitivity analysis at 0.30 (open question 3 from workflow trace)
- [ ] Permutation test on ca_missing indicator
- [ ] XGBoost comparison (optional — only if RF AUC is insufficient)
- [ ] Project README for practitioner handoff

## Next Session Start

Open this file and the workflow trace. Pick up from:

```text
I'm resuming a cardiac risk classification project.
Context files: examples/basic-classification/student-run/PROJECT_STATE.md and workflow_trace.md
I want to explore threshold 0.30 and check whether sensitivity reaches 0.95.
Load the experiment log and continue from Run 003.
```

## Files

```
student-run/
├── README.md
├── problem_frame.md
├── data_card.md
├── analysis_plan.md
├── experiment_log.md
├── model_card.md
├── workflow_trace.md
├── PROJECT_STATE.md      ← you are here
└── session-summary.md
```
