# Examples: Model Evaluation

## Example 1

User request:

> Evaluate these two churn models against baseline and recommend whether we should proceed.

Expected behavior:

- summarize metrics in decision context
- perform error and subgroup analysis
- run robustness checks and issue recommendation

Expected artifacts:

- evaluation report
- metric summary
- error analysis
- recommendation note

## Example 2

User request:

> Produce an evaluation memo for leadership with risks and next actions.

Expected behavior:

- translate metrics into operational implications
- include robustness and failure analysis
- provide clear proceed/condition/halt recommendation

Expected artifacts:

- evaluation report
- robustness summary
- recommendation and next-step note

## Example 3 (Bad Invocation)

User request:

> Accuracy is highest for model B. Approve it.

Expected Codex response:

- reject single-metric approval
- require subgroup and robustness checks
- require error analysis before recommendation

Expected artifacts after correction:

- complete metric summary
- error breakdown
- robustness check summary
