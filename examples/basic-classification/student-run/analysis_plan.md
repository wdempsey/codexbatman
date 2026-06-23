# Analysis Plan

_Gate 3 — Analysis Plan_
_Produced: tutor mode, eda-plan + experiment-design skills_

---

## Objective

Binary classification of cardiac disease presence. Metric: ROC-AUC.
Secondary: sensitivity at the threshold we'll set after baseline.

## Split Strategy

- **Method**: stratified 80/20 train/test, random_state=42
- **Train**: 242 rows | **Test**: 61 rows
- **Stratify on**: binarized target (to preserve 54.5% positive rate in both splits)
- No validation set for baseline — add 5-fold CV if model comparison gets close

## Preprocessing Pipeline

1. Binarize target: `(target > 0).astype(int)`
2. Missing values:
   - `ca`: mode impute (0) + add `ca_missing` binary indicator
   - `thal`: mode impute (3)
3. Encode categoricals: `cp`, `restecg`, `slope`, `thal` → one-hot (drop_first=True)
4. Scale numerics: StandardScaler on `age`, `trestbps`, `chol`, `thalach`, `oldpeak`
5. Binary columns (`sex`, `fbs`, `exang`, `ca_missing`) — no scaling needed

## Baseline Model

Logistic regression (sklearn defaults, max_iter=1000, C=1.0).
Rationale: interpretable, strong baseline for tabular clinical data, fast to iterate on.

## Model Candidates

| Model | Why consider it |
|-------|----------------|
| Logistic regression | Baseline; interpretable coefficients |
| Random forest | Handles nonlinear interactions; feature importance |
| Gradient boosting (XGBoost) | Strong tabular performance; try if RF underperforms |

We'll compare by ROC-AUC on the held-out test set. Stop at 2 models unless AUC gap < 0.02.

## EDA Hypotheses to Test Before Modeling

1. `cp` type distribution by target — is asymptomatic chest pain actually riskier?
2. `thalach` vs `target` — higher max heart rate → lower disease risk?
3. `ca` count vs `target` — more visible vessels → more disease?
4. Age × sex interaction — does the age-disease relationship differ by sex?

## Threshold Decision

Set threshold post-baseline based on sensitivity/specificity tradeoff.
Clinical default: prefer sensitivity ≥ 0.85 (fewer missed disease cases).
Report precision-recall curve alongside ROC.

---

_Student note: Codex asked me which metric I'd use to pick between models — I said accuracy,
and it pushed back. Accuracy assumes equal cost of FP and FN. For a cardiac referral tool,
missing disease is much worse than over-referring, so ROC-AUC + sensitivity at threshold is
the right framing. I'll carry that forward._
