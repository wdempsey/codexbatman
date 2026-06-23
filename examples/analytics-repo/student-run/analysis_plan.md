# Analysis Plan

_Gate 3 — Analysis Plan_
_Produced: tutor mode, eda-plan + experiment-design skills_

---

## Objective

Regression: predict MedHouseVal (census tract median house value, $100K units).
Primary metric: RMSE. Secondary: R².

## Split Strategy

- **Method**: random 80/20 train/test, random_state=42
- **Train**: 16,512 rows | **Test**: 4,128 rows
- No stratification needed (continuous target; large n)
- No validation set for OLS baseline — add if regularized models are close

## Preprocessing Pipeline

1. No missing value imputation needed
2. Scale all features: StandardScaler (OLS doesn't require it, but ridge/lasso do — apply
   to all models for comparability)
3. No categorical encoding — all features are numeric
4. Leave outliers (AveOccup) in place for baseline; flag if they show high leverage

## Baseline Model

OLS linear regression (sklearn LinearRegression).
Rationale: interpretable coefficients, fast, establishes the floor for more complex models.

## Model Candidates

| Model | Why consider it |
|-------|----------------|
| OLS linear regression | Baseline; interpretable |
| Ridge regression | L2 regularization; handles AveRooms/AveBedrms multicollinearity |
| Lasso regression | L1 regularization; may zero out one of the correlated pair |

We stop after ridge/lasso unless RMSE gap vs. OLS > 0.05 ($5,000) and we have a clear
reason to go nonlinear.

## EDA Hypotheses to Test Before Modeling

1. MedInc vs. MedHouseVal — expected strong positive correlation (primary driver)
2. Latitude vs. MedHouseVal — does coastal California show higher values? (nonlinear?)
3. AveRooms vs. AveBedrms scatter — visualize the multicollinearity
4. Ceiling tracts on a map — where are the $500K+ neighborhoods?

## Evaluation Plan

- Report RMSE and R² on full test set
- Report RMSE separately: ceiling tracts (MedHouseVal == 5.0) vs. non-ceiling
- Residual plot: predicted vs. actual, colored by Latitude to check geographic bias
- Feature importances (OLS: standardized coefficients; ridge/lasso: coefficient magnitudes)

---

_Student note: Codex asked me whether the same preprocessing should apply to OLS and ridge.
I said "yes" without thinking. It then asked: "Why?" I realized I'd said it by habit —
scaling doesn't affect OLS predictions (only coefficient interpretation), but it's
required for ridge/lasso for the regularization penalty to be fair. We apply scaling
to everything for consistency._
