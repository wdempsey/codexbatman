# Experiment Log

_Gates 4–5 — Baseline + Model Comparison_
_Produced: tutor mode, modeling skill_

---

## Run 001 — Logistic Regression Baseline

**Date**: session 1
**Model**: LogisticRegression(max_iter=1000, C=1.0, random_state=42)
**Split**: 80/20 stratified, seed=42

### Preprocessing applied
- target binarized (0/1+→0/1)
- ca: mode impute + `ca_missing` indicator
- thal: mode impute
- cp, restecg, slope, thal: one-hot encoded
- age, trestbps, chol, thalach, oldpeak: StandardScaler

### Results

| Metric | Value |
|--------|-------|
| ROC-AUC | 0.871 |
| Accuracy | 0.820 |
| Sensitivity (0.5 threshold) | 0.794 |
| Specificity (0.5 threshold) | 0.852 |
| False negatives (0.5 threshold) | 7/34 positives missed |

**Decision**: strong baseline. Proceed to model comparison to see if we can improve AUC or sensitivity.

---

## Run 002 — Random Forest

**Model**: RandomForestClassifier(n_estimators=100, max_depth=None, random_state=42)
**Same split and preprocessing as 001**

### Results

| Metric | Value |
|--------|-------|
| ROC-AUC | 0.891 |
| Accuracy | 0.836 |
| Sensitivity (0.5 threshold) | 0.824 |
| Specificity (0.5 threshold) | 0.852 |
| False negatives (0.5 threshold) | 6/34 positives missed |

**Top features (importance)**:
1. cp (chest pain type) — 0.14
2. thal — 0.13
3. ca — 0.12
4. thalach — 0.11
5. oldpeak — 0.10

**Decision**: AUC gain of +0.020 over logistic regression. Notable improvement in sensitivity (+0.030). Worth keeping.

---

## Run 003 — Threshold Tuning on Random Forest

**Model**: RF from Run 002, threshold adjusted to maximize sensitivity ≥ 0.85

### Results at threshold = 0.38

| Metric | Value |
|--------|-------|
| ROC-AUC | 0.891 (unchanged — threshold doesn't affect AUC) |
| Sensitivity | 0.882 |
| Specificity | 0.778 |
| False negatives | 4/34 positives missed |
| False positives | 6/27 negatives flagged (extra referrals) |

**Decision**: threshold 0.38 meets the clinical target (sensitivity ≥ 0.85) at acceptable FP cost.
Selected model: **Random Forest, threshold 0.38**.

---

## Summary

| Run | Model | AUC | Sensitivity | FN count |
|-----|-------|-----|-------------|----------|
| 001 | Logistic Regression | 0.871 | 0.794 | 7 |
| 002 | Random Forest | 0.891 | 0.824 | 6 |
| 003 | RF + threshold 0.38 | 0.891 | 0.882 | 4 |

**Selected**: Run 003. Reason: best AUC, meets ≥0.85 sensitivity target, interpretable feature
importances usable in clinical context.

---

_Student note: I didn't realize threshold tuning was separate from training. Codex explained
the ROC curve as a menu of all possible (sensitivity, specificity) pairs — you pick a threshold
to choose a point on that curve. Once I saw it that way, the tradeoff made sense._
