# Regression Workflow

Use this workflow when the target is continuous and the project needs a defensible prediction or explanation pipeline.

## Focus

- define the continuous target clearly
- confirm unit of analysis
- confirm prediction time
- choose a simple baseline first
- compare candidate models under the same split strategy

## Minimum Workflow

1. Confirm the target and whether it is measured at the right level.
2. Confirm a valid split strategy and leakage boundaries.
3. Fit a simple baseline such as linear regression.
4. Compare justified candidate models only.
5. Record metrics, diagnostics, and interpretation notes.
6. Produce a model card and update the experiment log.

## Minimum Checks

- target definition is stable
- unit of analysis is correct
- leakage review is complete
- split strategy is defensible
- metric choice matches the actual decision problem

## Recommended Outputs

- regression comparison summary
- evaluation report
- model card
- experiment log entry
