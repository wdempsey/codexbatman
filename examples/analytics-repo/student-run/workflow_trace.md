# Workflow Trace

_Gate 7 — Workflow Trace_
_Produced: tutor mode, workflow-trace skill_

---

## What Happened This Session

### Gate 1 — Problem Framing
- Defined decision: census tract value estimation for housing policy
- Set metric: RMSE (interpretable in dollar terms) over R² (relative)
- Identified ceiling artifact ($500K cap) as the primary data risk
- Artifact: `problem_frame.md`

### Gate 2 — Data Audit
- Confirmed 20,640 rows, 8 features, zero missing values
- Found ceiling artifact: 965 tracts (4.7%) at MedHouseVal == 5.0
- Flagged multicollinearity: AveRooms/AveBedrms r=0.847
- Found AveOccup outlier (max=1,243); left in place
- Artifact: `data_card.md`

### Gate 3 — Analysis Plan
- Split: 80/20 random, seed=42
- Preprocessing: StandardScaler on all features
- Baseline: OLS → compare ridge and lasso for multicollinearity
- Decided to report RMSE on ceiling vs. non-ceiling tracts separately
- Artifact: `analysis_plan.md`

### Gate 4 — Baseline
- OLS: RMSE=0.728, R²=0.606
- AveBedrms negative coefficient identified as multicollinearity artifact
- Ceiling RMSE (1.113) much worse than non-ceiling (0.669) — expected
- Artifact: `experiment_log.md` (Run 001)

### Gate 5 — Model Comparison
- Ridge (α=1.0): RMSE=0.724, AveBedrms shrunk from -0.198 → -0.061
- Lasso (α=0.001): zeroed AveBedrms; RMSE=0.726 — no gain
- Selected: Ridge. Reason: best RMSE, more interpretable coefficients
- Artifact: `experiment_log.md` (Runs 002–003)

### Gate 6 — Evaluation
- Confirmed ceiling RMSE, geographic residual pattern documented
- Four known limitations written before looking at summary metrics
- Artifact: `model_card.md`

### Gate 7 — Workflow Trace (this file)

---

## Decisions Made

| Gate | Decision | Reasoning |
|------|----------|-----------|
| 1 | RMSE as primary metric | Interpretable in dollars; R² is relative |
| 1 | Ceiling artifact: document, don't fix | Fixing requires out-of-distribution assumptions |
| 2 | Leave AveOccup outlier | Influential but not erroneous; note in card |
| 3 | Scale all features | Required for ridge/lasso penalty fairness; apply to OLS for comparability |
| 5 | Ridge over OLS | Multicollinearity suppression + marginal RMSE gain |
| 5 | Ridge over Lasso | Same performance, no reason to zero AveBedrms |

## Open Questions

1. What does the geographic residual pattern look like plotted on a map? (Suspected: coastal
   underprediction visible clearly in LA and Bay Area)
2. Would geographic region dummies (coastal/inland/valley/mountain) reduce the ceiling RMSE?
3. Would a nonlinear model (random forest, XGBoost) meaningfully improve on 0.724?
4. Is the 1990 Census data predictive of current housing patterns at all? (Out of scope for
   this session but worth flagging)

## Where To Resume

```text
I'm resuming the California Housing regression project.
Context: examples/analytics-repo/student-run/PROJECT_STATE.md and workflow_trace.md
I want to explore whether geographic region dummies improve ceiling RMSE,
and plot residuals on a map to visualize the coastal underprediction pattern.
```
