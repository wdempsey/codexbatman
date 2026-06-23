# Data Card

_Gate 2 — Data Audit_
_Produced: tutor mode, data-audit skill_

---

## Source

California Housing Dataset — 1990 US Census
Available via: `from sklearn.datasets import fetch_california_housing`
Download: see `examples/analytics-repo/learning.md` Try It section

## Shape

- **Rows**: 20,640 census tracts
- **Columns**: 9 (8 features + 1 target)
- **Missing values**: 0

## Features

| Column | Type | Range | Interpretation |
|--------|------|-------|----------------|
| MedInc | numeric | 0.5–15.0 | Median income in tract ($10,000 units) |
| HouseAge | numeric | 1–52 | Median house age in tract (years) |
| AveRooms | numeric | 0.8–141.9 | Average rooms per household |
| AveBedrms | numeric | 0.3–34.1 | Average bedrooms per household |
| Population | numeric | 3–35,682 | Tract population |
| AveOccup | numeric | 0.7–1,243 | Average occupants per household |
| Latitude | numeric | 32.5–42.0 | Tract centroid latitude |
| Longitude | numeric | -124.4–-114.3 | Tract centroid longitude |
| **MedHouseVal** | **numeric (target)** | **0.15–5.0** | **Median house value ($100K, capped at $500K)** |

## Distribution Notes

- `AveRooms` and `AveBedrms`: heavy right skew; outliers likely from small tracts with
  unusual occupancy (e.g., a student dorm or assisted living facility inflating rooms/people)
- `AveOccup`: outliers present (up to 1,243 — clearly erroneous or an edge case tract)
- `Population`: wide range; some very small tracts
- `MedHouseVal`: bimodal-ish distribution with a spike at 5.0 (the $500K ceiling)

## Ceiling Artifact Detail

```
Tracts at ceiling (MedHouseVal == 5.0): 965 / 20,640 = 4.68%
Geographic concentration: primarily coastal California (LA, Bay Area, San Diego)
```

These tracts are NOT missing — they have a real value that was censored. The model will
underpredict them. We'll report RMSE on ceiling vs. non-ceiling tracts separately.

## Multicollinearity Check

Correlation between AveRooms and AveBedrms: r = 0.847

This is high. Both measure housing density per household. OLS will still produce valid
predictions, but coefficient interpretation for these two variables will be unreliable.
Note in model card.

## Audit Status

✓ No missing values. Ceiling artifact documented. Multicollinearity flagged.
Proceed to analysis plan.

---

_Student note: Codex asked me to describe what AveOccup means before we moved on. I said
"average number of people per house." It then asked: what does AveOccup = 1,243 mean?
That made me realize there must be weird tracts in the data. We checked — it's a real
(but extreme) outlier. We decided not to remove it; we'll watch whether it's influential._
