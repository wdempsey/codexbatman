# Metric Alignment Check

Use this check before deciding that a model is "better."

## Questions

- Does the primary metric reflect the real decision problem?
- Are secondary metrics needed to reveal tradeoffs?
- For classification, are threshold-sensitive costs visible?
- For imbalanced settings, is plain accuracy misleading?
- Are calibration or subgroup metrics needed?

## Minimum Output

- primary metric rationale
- secondary metric rationale
- known blind spots in the metric set
