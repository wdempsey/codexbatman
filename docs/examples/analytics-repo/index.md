---
description: Linear regression on California Housing data — continuous target, regularization, residual analysis, and the policy stakes of getting predictions wrong.
---

# Linear Regression — California Housing

This example runs the full workflow on a regression problem: predicting median house values across California census tracts, using 1990 census data.

The dataset ships with sklearn. The target is continuous. The stakes are concrete — this is the kind of model a housing agency might use to identify where housing cost burden is highest relative to income, to prioritize assistance program deployment. Getting predictions systematically wrong for one region means directing assistance away from people who need it.

---

## What this example teaches

The basic-classification example covers binary targets, ROC-AUC, and leakage from prediction time. This example builds on those concepts and introduces what's different when the target is continuous:

**RMSE vs MAE** — two metrics that measure prediction error differently. RMSE penalizes large errors more heavily (squares them before averaging). If your model produces a few very bad predictions for specific tracts, RMSE catches that; MAE treats a $200K error the same as ten $20K errors. Which one you optimize for depends on whether large individual errors are worse than distributed small errors.

**Log-transforming a skewed target** — house values are right-skewed: most tracts cluster below $200K, but some go much higher. Linear regression assumes residuals are approximately normal. Fitting on the raw target produces a model that struggles with high-value tracts and violates that assumption. Log-transforming the target before modeling — then exponentiating predictions back — is the standard fix.

**Geographic features** — latitude and longitude carry real signal: California housing prices vary strongly by location. But treating lat/lon as linear predictors is wrong (the relationship isn't linear — it's spatial). This example explores how to handle them and what the residual map looks like when you don't.

**Ridge and lasso regularization** — when features are correlated (as they are here: AveRooms and AveBedrms are highly correlated), standard linear regression coefficients become unstable. Ridge shrinks them; lasso zeroes some out entirely. This connects directly to ISLR Ch. 6.

**Residual analysis** — for regression, the evaluation gate includes residual plots. Systematic patterns in residuals (errors that correlate with geography, income level, or tract size) reveal model failures that RMSE alone doesn't surface.

**The $500K ceiling** — the dataset caps MedHouseVal at $500K ($5.0 in the scaled target). This creates a visible spike in the data — a censoring artifact. Your model won't know the true values above the ceiling; the residuals will show a systematic underestimate for high-value tracts. This is a limitation that belongs in the model card.

---

## The dataset

**California Housing** (sklearn.datasets.fetch_california_housing)

20,640 census tracts from the 1990 California census. Each row is one census tract.

| Feature | Description |
|---|---|
| MedInc | Median household income (tens of thousands) |
| HouseAge | Median age of housing units in the tract |
| AveRooms | Average number of rooms per household |
| AveBedrms | Average number of bedrooms per household |
| Population | Census tract population |
| AveOccup | Average number of household members |
| Latitude | Tract centroid latitude |
| Longitude | Tract centroid longitude |
| **MedHouseVal** | **Target — median house value ($100,000s), capped at 5.0** |

No missing values. One censoring artifact (the $500K cap). 20,640 rows — large enough that an 80/20 split gives a stable test set.

---

## Choose your path

- [Learning Lens →](learning.md) — attempt-before-answer coaching through all 7 gates, with California Housing as the running example
- [Execution Lens →](execution.md) — direct practitioner walkthrough, artifacts and decisions without scaffolding
- [Manager Lens →](manager.md) — what a program director reviews before approving model use for policy allocation

---

## How this compares to the classification example

| | Basic Classification | Linear Regression |
|---|---|---|
| Dataset | Cleveland Heart Disease (303 rows) | California Housing (20,640 rows) |
| Target | Binary (disease present/absent) | Continuous (median house value) |
| Primary metric | ROC-AUC | RMSE (log-scale) |
| Key data issue | Prediction time (post-test features) | Target ceiling ($500K cap) |
| Regularization | — | Ridge / Lasso (ISLR Ch. 6) |
| Evaluation add-on | Confusion matrix at threshold | Residual plots, geographic error |
| Manager concern | False-negative rate (missed disease) | Systematic underprediction by region |

---

*Related: [Basic Classification](../basic-classification/index.md) · [Core Data Science Workflow](../../workflows/data-science/index.md) · [ISLR Ch. 6 — Ridge & Lasso](../../system/textbook-resources.md)*
