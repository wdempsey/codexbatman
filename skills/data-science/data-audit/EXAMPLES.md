# Examples: Data Audit

## Example 1

User request:

> Audit this panel dataset before we start feature engineering.

Expected behavior:

- identify unit of analysis and panel structure
- check leakage and temporal validity
- issue a proceed decision with conditions if needed

## Example 2

User request:

> We merged three sources into one training table. Run the canonical data audit.

Expected behavior:

- inspect joins and key integrity
- check missingness and type issues
- document audit findings in the canonical sections

## Example 3

User request:

> Tell me whether this data is ready for modeling.

Expected behavior:

- avoid a casual answer
- produce an explicit audit artifact
- issue `PROCEED`, `PROCEED WITH CONDITIONS`, or `HALT`
