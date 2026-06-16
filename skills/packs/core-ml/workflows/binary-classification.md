# Binary Classification Workflow

Use this workflow when the target has two classes and the project needs a reproducible classification pipeline.

## Focus

- define the positive class explicitly
- align metrics to the decision context
- check class balance and threshold consequences
- compare baseline and candidate models under the same protocol

## Minimum Workflow

1. Define the positive class and the operational question.
2. Confirm prediction time and leakage boundaries.
3. Validate train/test design.
4. Fit a simple baseline model first.
5. Compare candidate models using aligned metrics.
6. Consider threshold behavior and calibration when needed.
7. Produce evaluation and model-card artifacts.

## Minimum Checks

- positive class is explicit
- metric choice matches operational cost
- split design prevents leakage
- baseline exists
- threshold implications are documented

## Recommended Outputs

- binary classification comparison summary
- evaluation report
- model card
- experiment log entry
