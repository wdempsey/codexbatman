# Code Review And Quality Examples

## Inference Wrapper PR

Review focus:

```text
Brief: Add a prediction wrapper for the approved churn model.
Diff: model loading, input schema validation, predict() wrapper, tests.
Verification: pytest tests/test_inference_wrapper.py
```

Good findings:

```text
Required: The wrapper accepts a DataFrame with extra columns but does not reject missing approved features. This violates the model-card input contract and can silently reorder features.

Optional: The fixture name could be more domain-specific; `valid_churn_features` would read better than `df`.

Verification reviewed: targeted wrapper tests ran, but no negative schema test covers missing required features.
Merge readiness: request changes.
```

## Notebook Fix PR

Review focus:

```text
Brief: Fix implausibly high validation AUC in the notebook.
Diff: train/test split moved before preprocessing, experiment log entry updated.
```

Good findings:

```text
Required: The fix moves imputation after the split, but target encoding still fits on the full dataset. This leaves a leakage path.

Verification reviewed: notebook rerun and metric drop documented; add a leakage check or note why target encoding is not in scope.
Merge readiness: request changes.
```
