# Data Card

_Gate 2 — Data Audit_
_Produced: tutor mode, data-audit skill_

---

## Source

Cleveland Heart Disease Dataset — UCI ML Repository
URL: https://archive.ics.uci.edu/dataset/45/heart+disease
Download: `python examples/basic-classification/data/get_heart.py`

## Shape

- **Rows**: 303 patients
- **Columns**: 14 (13 features + 1 target)
- **Collected**: Cleveland Clinic Foundation, Detrano et al. 1989

## Features

| Column | Type | Range / Values | Notes |
|--------|------|----------------|-------|
| age | numeric | 29–77 | age in years |
| sex | binary | 0=female, 1=male | 68% male |
| cp | ordinal | 1–4 | chest pain type (4=asymptomatic) |
| trestbps | numeric | 94–200 | resting blood pressure (mm Hg) |
| chol | numeric | 126–564 | serum cholesterol (mg/dl) |
| fbs | binary | 0/1 | fasting blood sugar > 120 mg/dl |
| restecg | ordinal | 0–2 | resting ECG results |
| thalach | numeric | 71–202 | max heart rate achieved |
| exang | binary | 0/1 | exercise-induced angina |
| oldpeak | numeric | 0–6.2 | ST depression (exercise vs rest) |
| slope | ordinal | 1–3 | slope of peak exercise ST segment |
| ca | ordinal | 0–3 | vessels colored by fluoroscopy |
| thal | ordinal | 3/6/7 | thalassemia type |
| target | ordinal → binary | 0–4 → 0/1 | 0=no disease; we binarize 1–4 → 1 |

## Missingness

| Column | Missing | Plan |
|--------|---------|------|
| ca | 4 (1.3%) | Add binary indicator `ca_missing`; impute with mode (0) |
| thal | 2 (0.7%) | Mode impute (value=3, normal); small enough to not add indicator |
| all others | 0 | No action needed |

## Class Balance

- Negative (0, no disease): 138 (45.5%)
- Positive (1+, disease present): 165 (54.5%)
- **Decision**: balanced — no resampling needed; stratified split sufficient

## Target Binarization

Original target has 5 levels (0–4). We collapse to binary:
```python
df['target'] = (df['target'] > 0).astype(int)
```
Rationale: the clinical decision is referral vs. no referral, not severity staging.

## Leakage Check

Prediction time confirmed post-stress-test (from problem_frame.md).
Features collected during stress test (thalach, exang, oldpeak, slope) are available at
prediction time. No leakage.

## Audit Status

✓ Proceed to analysis plan.

---

_Student note: I didn't know what "ca" meant until Codex asked me to look it up.
It's the number of major vessels visible on fluoroscopy — a clinical measure of
coronary artery disease. The missing values might not be random (hard to visualize
→ more disease?), so the indicator column matters._
