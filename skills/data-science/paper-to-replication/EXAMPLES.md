# Examples: Paper to Replication

## Example 1

User request:

> Convert this RCT paper into a replication plan we can execute next week.

Expected behavior:

- extract estimand, sample rules, and variable definitions
- produce data requirements and implementation checklist
- list unresolved details explicitly

Expected artifacts:

- structured paper summary
- data requirements table
- replication plan
- implementation checklist

## Example 2

User request:

> Create a partial replication plan for the main table and one robustness check.

Expected behavior:

- constrain scope to selected outputs
- map dependencies for selected outputs only
- identify what is intentionally out of scope

Expected artifacts:

- scoped replication plan
- implementation checklist for target outputs
- risks/unknowns note

## Example 3 (Bad Invocation)

User request:

> Replicate this paper quickly.

Expected Codex response:

- request explicit replication scope
- require paper/method inputs
- produce planning artifacts before coding

Expected artifacts after correction:

- structured summary
- scoped data requirements
- executable checklist
