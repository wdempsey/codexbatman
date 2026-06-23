# Workflow Trace

_Gate 7 — Workflow Trace_
_Produced: tutor mode, workflow-trace skill_

---

## What Happened This Session

### Gate 1 — Problem Framing
- Defined decision: cardiac referral triage (post-stress-test)
- Set metric: ROC-AUC + sensitivity at threshold
- Resolved prediction time question (post-stress-test → no leakage)
- Artifact: `problem_frame.md`

### Gate 2 — Data Audit
- Confirmed 303 rows, 13 features
- Found 6 missing values (ca: 4, thal: 2); imputation plan set
- Class balance acceptable (55/45); no resampling needed
- Binarized target (0–4 → 0/1)
- Artifact: `data_card.md`

### Gate 3 — Analysis Plan
- Split: 80/20 stratified, seed=42
- Preprocessing: one-hot encode 4 categoricals, scale 5 numerics, add ca_missing indicator
- Model candidates: logistic regression baseline → random forest
- EDA hypotheses: cp distribution, thalach trend, ca count, age×sex interaction
- Artifact: `analysis_plan.md`

### Gate 4 — Baseline
- Logistic regression: AUC=0.871, sensitivity=0.794 at 0.5 threshold
- Artifact: `experiment_log.md` (Run 001)

### Gate 5 — Model Comparison
- Random forest: AUC=0.891 (+0.020), sensitivity=0.824 (+0.030)
- Threshold tuned to 0.38: sensitivity=0.882, FN reduced from 7 → 4
- Selected: RF + threshold 0.38
- Artifact: `experiment_log.md` (Runs 002–003)

### Gate 6 — Evaluation
- Confirmed performance on held-out test set
- Documented known limitations (small test set, single site, no temporal validation)
- Artifact: `model_card.md`

### Gate 7 — Workflow Trace (this file)

---

## Decisions Made

| Gate | Decision | Reasoning |
|------|----------|-----------|
| 1 | Predict post-stress-test | All 13 features available; no leakage risk |
| 1 | Primary metric: ROC-AUC | Threshold-independent; clinical cost asymmetry addressed separately |
| 2 | Binarize target | Decision is referral vs. no referral, not severity |
| 2 | ca_missing indicator | Missingness may be informative (harder to visualize = more disease?) |
| 3 | Stratified split | Preserve class balance in train/test |
| 5 | Choose RF over LR | +0.020 AUC, better sensitivity, acceptable feature importances for clinical use |
| 5 | Threshold 0.38 | Meets ≥0.85 sensitivity target at acceptable FP cost |

## Open Questions

1. Would the model generalize to other clinical sites? Single-site data is a real limitation.
2. Is the ca_missing indicator actually predictive? Worth checking with a permutation test.
3. What happens at threshold 0.30? Would sensitivity reach 0.95 — and is the FP cost acceptable?
4. Would XGBoost further improve AUC? Stopped after RF based on the plan; could revisit.

## Where To Resume

Next session: answer open question 3 (threshold sensitivity at 0.30), then write the project
README for handoff to a practitioner who'd run this in production.

---

_Student note: I didn't think I'd need a workflow trace. But when Codex asked me to write it,
I realized I'd already forgotten why I chose threshold 0.38. The trace is for the version of
me who opens this file in two weeks and has no idea what happened._
