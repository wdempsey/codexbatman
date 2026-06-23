# Experiment Log

_Gates 4–5 — Baseline + Model Comparison_
_Produced: tutor mode, modeling skill_

---

## Run 001 — OLS Baseline

**Model**: LinearRegression() (sklearn defaults)
**Split**: 80/20 random, seed=42
**Preprocessing**: StandardScaler on all 8 features

### Results

| Metric | Value |
|--------|-------|
| RMSE (test) | 0.728 ($72,800 typical error) |
| R² (test) | 0.606 |
| RMSE (non-ceiling tracts) | 0.669 |
| RMSE (ceiling tracts, n=202) | 1.113 |

### Standardized Coefficients (top contributors)

| Feature | Coeff | Interpretation |
|---------|-------|----------------|
| MedInc | +0.821 | Strongest predictor — income drives value |
| Latitude | -0.311 | Further north → lower values (coastal south is expensive) |
| Longitude | -0.234 | Further east → lower values |
| AveOccup | -0.127 | More occupants → lower value |
| HouseAge | +0.083 | Older neighborhoods → slightly higher value (urban density?) |
| AveRooms | +0.286 | More rooms → higher value |
| AveBedrms | -0.198 | **Negative coefficient** — suppression artifact from multicollinearity with AveRooms |
| Population | -0.048 | Small effect |

Note: AveBedrms negative coefficient is a multicollinearity artifact (r=0.847 with AveRooms).
Do not interpret this coefficient as "more bedrooms → lower value."

**Decision**: reasonable baseline. Ceiling RMSE much worse than non-ceiling (expected).
Proceed to regularized models to address multicollinearity.

---

## Run 002 — Ridge Regression

**Model**: Ridge(alpha=1.0) — default alpha, will tune if promising
**Same split and preprocessing as 001**

### Results

| Metric | Value |
|--------|-------|
| RMSE (test) | 0.724 ($72,400) |
| R² (test) | 0.609 |
| RMSE (non-ceiling) | 0.666 |
| RMSE (ceiling) | 1.097 |

### Coefficient Changes vs. OLS

- AveBedrms coefficient: -0.198 → -0.061 (ridge shrinks the suppression artifact)
- AveRooms: +0.286 → +0.189 (shrunk toward zero, less inflated)
- All other coefficients similar magnitude

**Decision**: marginal improvement. RMSE -0.004, R² +0.003. Ridge is preferable to OLS
because it handles the multicollinearity more honestly — coefficients are more interpretable.

---

## Run 003 — Lasso Regression

**Model**: Lasso(alpha=0.001) — small alpha to avoid aggressive shrinkage
**Same split and preprocessing**

### Results

| Metric | Value |
|--------|-------|
| RMSE (test) | 0.726 ($72,600) |
| R² (test) | 0.607 |

### Coefficient Changes

- AveBedrms: zeroed out (Lasso selected AveRooms over AveBedrms)
- All other features retained

**Decision**: Lasso auto-selected between the correlated pair — AveBedrms dropped.
RMSE similar to ridge (+0.002). Ridge preferred: lasso zeroed a feature we want to
keep for interpretability, with no meaningful performance gain.

---

## Summary

| Run | Model | RMSE | R² |
|-----|-------|------|----|
| 001 | OLS | 0.728 | 0.606 |
| 002 | Ridge (α=1.0) | 0.724 | 0.609 |
| 003 | Lasso (α=0.001) | 0.726 | 0.607 |

**Selected**: Ridge regression (Run 002).
Reason: best RMSE, best R², more honest coefficient estimates on the correlated pair,
no features dropped unnecessarily.

---

_Student note: I expected ridge to massively outperform OLS. It didn't. Codex asked me
why I thought it would. I had assumed multicollinearity hurts predictions — it doesn't,
it hurts coefficient interpretation. Ridge fixes the interpretation problem; OLS predictions
were already reasonable. The big remaining issue (ceiling artifact) can't be fixed with
regularization — it's a data problem._
