# Data Audit

Data audit is the second analytical gate in the canonical workflow.

Its job is not to summarize a dataset casually.

Its job is to decide whether the available data is fit for downstream work.

## Why This Workflow Matters

Many analytical failures are data failures that were never named:

- the unit of analysis is unstable
- joins silently duplicate rows
- the target is built with future information
- missingness is systematic
- temporal validity is broken
- fairness risks are visible but undocumented

The audit phase exists to convert those hidden risks into an explicit proceed decision.

This workflow follows the gate logic in [Data Science Layer Blueprint](blueprint.md).

## Common Mistakes

- Auditing without a clear framing artifact.
- Skipping unit-of-analysis checks.
- Treating schema review as sufficient audit.
- Missing temporal leakage in panel or longitudinal data.
- Assuming missingness is random.
- Declaring the data ready without a documented `PROCEED`, `PROCEED WITH CONDITIONS`, or `HALT`.

## Step-by-Step Workflow

### 1. Confirm unit of analysis and time structure

Codex should identify:

- what one row represents
- what keys define uniqueness
- whether time is present
- whether the structure is cross-sectional, repeated cross-section, or panel

### 2. Review schema and types

Check that:

- columns have sensible types
- dates are parsed correctly
- numeric columns are not silently stored as strings
- mixed-type columns are surfaced explicitly

### 3. Review missingness and coverage

Look at:

- column-level missingness
- subgroup missingness
- time-slice missingness
- whether missingness tracks the target or treatment

### 4. Review ranges and distributions

Check for:

- impossible values
- sudden shifts over time
- rare or malformed categories
- suspicious sparsity

### 5. Review target construction

If there is a target, Codex should document:

- how it is defined
- when it becomes known
- whether any candidate features leak future information

### 6. Review leakage, bias, and joins

This phase must explicitly evaluate:

- direct leakage
- temporal leakage
- group leakage
- sampling bias
- proxy risk
- join explosions
- unmatched keys

### 7. Issue a proceed decision

The audit artifact must end with exactly one of:

- `PROCEED`
- `PROCEED WITH CONDITIONS`
- `HALT`

The conditions or blockers must be concrete.

## Expected Artifacts

- Audit summary
- Key findings list
- Data quality section
- Leakage assessment
- Bias and representativeness section
- Join and key integrity section
- Proceed decision
- Immediate next actions

## How Codex Should Use The Skill

Codex should use `skills/data-science/data-audit/SKILL.md` only after a framing artifact exists.

Codex should:

- inspect actual source structure
- write an explicit audit artifact
- avoid modifying raw data
- stop downstream modeling when the audit says `HALT`

Codex should not:

- collapse the audit into an informal data summary
- move directly from schema reading to modeling
- hide uncertainty in a generic “looks fine” statement

## Run With Codex

```text
Use the data-audit skill on this dataset and produce a canonical audit artifact with a proceed decision.
```

```text
Run data-audit on these merged tables. Focus on join integrity, missingness, and leakage risk.
```

```text
Apply the data-audit skill after the framing artifact. If the target window is not defensible, halt the workflow.
```
