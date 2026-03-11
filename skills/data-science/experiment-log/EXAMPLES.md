# Examples: Experiment Log

## Example 1

User request:

> Log the latest XGBoost run before we decide whether to keep iterating.

Expected behavior:

- record the full run context
- compare against baseline
- state a clear decision outcome

## Example 2

User request:

> We changed the split strategy and the metric moved. Create the experiment log entry.

Expected behavior:

- document the split change explicitly
- avoid direct comparison without caveats
- note implications for interpretation

## Example 3

User request:

> Record this failed experiment too.

Expected behavior:

- log the failed run fully
- preserve the hypothesis and result
- avoid selective reporting
