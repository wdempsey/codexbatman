# EDA Hypothesis Journal Examples

## Bounded Churn Exploration

Input:

```text
The EDA plan asks whether churn differs by tenure band and whether missing contract fields are concentrated in recent cohorts.
```

Good journal entry:

```markdown
## Hypothesis Entry

Question: Does churn rate increase in the first 90 days?
Prior expectation: Higher churn in early tenure because onboarding failures are plausible.
Check performed: Churn rate by tenure band with minimum n=100 per band.
Evidence: 0-30 day churn is 18%, 31-90 day churn is 14%, 90+ day churn is 8%.
Interpretation: Early tenure is a candidate risk segment, but the first band is small enough to require caution.
Action: Keep tenure band in feature review; add subgroup stability check before modeling.
```

## Leakage Found During EDA

Good response:

```markdown
Sanity check issue: `last_support_resolution` is populated after the churn decision window.
Leakage audit finding: Post-outcome field; cannot be used as a predictor.
Proceed decision: revise.
Recommended next skill: update `data-audit`, then revise the plan with `plan-as-guidance`.
```

Do not continue to modeling until the feature set and audit artifact are corrected.
