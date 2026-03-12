# Examples: EDA Plan

## Example 1

User request:

> Build an EDA plan for a churn project using the approved framing and data audit artifacts.

Expected behavior:

- produce prioritized exploratory questions
- define plot list with analytical purpose
- include subgroup, confounder, and outlier checks

Expected artifacts:

- EDA plan
- prioritized questions
- plot list
- subgroup checks
- confounder/outlier checks

## Example 2

User request:

> Create a reproducible EDA protocol for this panel dataset before we choose model families.

Expected behavior:

- include temporal diagnostics and cohort slices
- specify logging structure for EDA outputs
- define criteria for revisiting framing assumptions

Expected artifacts:

- EDA plan with temporal checks
- visualization set specification
- logging and exit conditions

## Example 3 (Bad Invocation)

User request:

> Just make some plots and tell me what looks interesting.

Expected Codex response:

- refuse unscoped exploration
- request framing objective and audit context
- propose a structured EDA plan template before plotting

Expected artifacts after correction:

- scoped EDA plan
- prioritized exploratory questions
