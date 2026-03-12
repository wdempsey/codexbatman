# Rubric: Modeling

## What Good Execution Looks Like

- Baseline model is explicit and justified.
- Candidate models are constrained and purposeful.
- Validation strategy is leakage-aware and reproducible.
- Feature/transform decisions are documented.
- Output supports clean handoff to evaluation.

## Minimum Acceptable Outputs

- baseline model specification
- candidate model set
- validation approach
- feature/transform notes
- training log or model summary

## Common Mistakes

- no baseline model
- tuning before validation design
- mixing split strategies across comparisons
- undocumented preprocessing changes
- selecting a winner without uncertainty checks

## Review Checklist

- Is baseline defined before candidate comparisons?
- Is validation protocol explicit and appropriate?
- Are model comparisons apples-to-apples?
- Are feature and transform decisions documented?
- Is the handoff to evaluation clear and complete?
