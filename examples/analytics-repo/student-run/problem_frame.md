# Problem Frame

_Gate 1 — Problem Framing_
_Produced: tutor mode, problem-framing skill_

---

## Decision

A housing policy agency wants to estimate median house values for California census tracts
to prioritize investment in undervalued neighborhoods.

This is a **policy support tool** — the model output informs budget allocation decisions
across tracts, not individual property appraisals.

## Modeling Objective

- **Task**: regression (continuous target)
- **Target**: `MedHouseVal` — median house value per census tract, in units of $100,000
- **Metric**: RMSE (in $100K units; multiply by 100,000 for dollar interpretation)
- **Secondary metric**: R² to understand explained variance

## Target Distribution Note

`MedHouseVal` is capped at 5.0 ($500,000). Any tract with true median ≥ $500K records
exactly 5.0. This creates an **artificial ceiling artifact** — the model will underpredict
high-value tracts and RMSE will be higher in that region. Document this; do not attempt
to fix it without more data.

## Prediction Time

All 8 features come from the same census survey. No temporal leakage. Prediction time = any
time the census data is available. Features: MedInc, HouseAge, AveRooms, AveBedrms,
Population, AveOccup, Latitude, Longitude.

## Scope and Constraints

- Unit of analysis: census tract (not individual house)
- Population: California census tracts from the 1990 US Census
- Model is descriptive/predictive; causal claims not supported without further work
- No deployment constraint given — treat as offline batch scoring

## First-Pass Risk Register

| Risk | Severity | Notes |
|------|----------|-------|
| $500K ceiling artifact | High | 965 tracts (~4.7%) are capped at 5.0 — model will underestimate these |
| Multicollinearity (AveRooms/AveBedrms) | Medium | Both measure room density; may inflate OLS coefficient variance |
| Geographic signal (Lat/Lon as linear predictors) | Medium | Linear terms miss nonlinear coastal/valley patterns |
| No missing values | None | sklearn dataset is clean |

---

_Student note: I almost said the metric was R². Codex asked me: "If your RMSE is 0.7,
what does that mean for a policy decision?" I couldn't answer. RMSE in $100K units is
interpretable — 0.7 means typical prediction error of $70,000. R² is relative, not
actionable. Switched to RMSE as primary._

Next step: `data-audit`
