# Model Card

_Gate 6 — Evaluation_
_Produced: tutor mode, evaluation skill_

---

## Model

Ridge Regression, alpha=1.0, sklearn defaults
StandardScaler applied to all 8 features

## Intended Use

Estimate median house value per California census tract to support housing policy
decisions — prioritizing investment in undervalued neighborhoods, flagging tracts
for further analysis, or benchmarking local housing markets.

**Not intended for**: individual property appraisal, real-time pricing, investment advice,
or any high-stakes automated decision without human review.

## Population

California census tracts, 1990 US Census. Generalization to other states, other years,
or other countries unvalidated. The $500K ceiling artifact is specific to this dataset.

## Performance (held-out test set, n=4,128 tracts)

| Metric | Value | Interpretation |
|--------|-------|----------------|
| RMSE (all tracts) | 0.724 | Typical error ≈ $72,400 |
| R² (all tracts) | 0.609 | Model explains ~61% of variance |
| RMSE (non-ceiling tracts, n=3,926) | 0.666 | Typical error ≈ $66,600 |
| RMSE (ceiling tracts, n=202) | 1.097 | Typical error ≈ $109,700 |

## Key Coefficients (standardized)

| Feature | Coefficient | Interpretation |
|---------|-------------|----------------|
| MedInc | +0.816 | Income is the dominant driver |
| Latitude | -0.308 | Further north → lower predicted values |
| Longitude | -0.231 | Further east (inland) → lower predicted values |
| AveRooms | +0.189 | More rooms → higher value |
| AveOccup | -0.130 | Higher occupancy → lower value |
| HouseAge | +0.082 | Older housing slightly higher |
| AveBedrms | -0.061 | Small residual after ridge shrinkage; do not interpret literally |
| Population | -0.046 | Very small effect |

## Known Limitations

1. **$500K ceiling artifact**: 4.7% of tracts are capped at $500K. The model
   systematically underpredicts coastal high-value neighborhoods (RMSE +65% vs. non-ceiling).
   Report model outputs with this caveat for any LA / Bay Area / San Diego analysis.

2. **Lat/Lon as linear predictors**: geographic signal is captured partially. The model
   cannot represent the nonlinear relationship between coastal proximity and value.
   Residuals show clear geographic patterns (coastal underprediction).

3. **Multicollinearity (AveRooms/AveBedrms)**: ridge shrinks the artifact but does not
   eliminate it. Coefficient magnitudes for these two features should not be compared.

4. **1990 Census**: housing market has changed dramatically since 1990. This model
   describes 1990 relationships; do not apply to current pricing without retraining.

---

_Student note: I wanted to skip the "Known Limitations" section. Codex asked: "If a policy
analyst uses this model to rank tracts in the Bay Area, what happens?" I realized they'd get
systematically underestimated values for coastal tracts — exactly where the ceiling artifact
is worst. Writing the limitations wasn't just documentation hygiene; it would prevent a real
downstream error._
