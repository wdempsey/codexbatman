# PROJECT_STATE

_Updated end-of-session_

---

## Current State

**Status**: Baseline complete. Model selected. Ready for geographic residual analysis or handoff.

**Selected model**: Ridge Regression, alpha=1.0
**Last RMSE**: 0.724 ($72,400 typical prediction error)
**Last R²**: 0.609

## What Is Done

- [x] Problem framing (decision, metric, ceiling artifact risk)
- [x] Data audit (no missing values, ceiling artifact quantified, multicollinearity flagged)
- [x] Analysis plan (split, preprocessing, model candidates)
- [x] Baseline OLS (RMSE=0.728)
- [x] Ridge comparison (RMSE=0.724, selected)
- [x] Lasso comparison (RMSE=0.726, not selected)
- [x] Model card (performance, ceiling/non-ceiling split, limitations)
- [x] Workflow trace

## What Is Not Done

- [ ] Geographic residual map (plot residuals on Lat/Lon to visualize coastal underprediction)
- [ ] Geographic region dummies (coastal/inland/valley/mountain) — test if they improve ceiling RMSE
- [ ] XGBoost comparison (optional — only if the geographic dummies don't solve it)
- [ ] Project README for practitioner handoff

## Next Session Start

Open this file and the workflow trace, then:

```text
I'm resuming the California Housing regression project.
Context: examples/analytics-repo/student-run/PROJECT_STATE.md and workflow_trace.md
I want to plot residuals on a lat/lon map and test whether geographic region dummies
(coastal/inland/valley/mountain) improve the ceiling RMSE.
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
