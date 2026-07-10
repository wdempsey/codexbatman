---
name: eda-hypothesis-journal
description: Execute bounded exploratory data analysis with a hypothesis journal, sanity checks, and leakage audit. Use after problem framing, data audit, and EDA plan are approved when a data scientist needs to explore patterns without drifting into modeling.
category: data-science
status: active
stage: eda
role_compatibility:
  - data scientist
inputs:
  - problem framing artifact
  - data audit decision
  - EDA plan
  - dataset version
  - unit of analysis and time structure
outputs:
  - EDA hypothesis journal
  - sanity check notes
  - leakage audit update
  - modeling handoff recommendation
depends_on:
  - problem-framing
  - data-audit
  - eda-plan
recommended_next:
  - modeling
  - plan-as-guidance
  - workflow-trace
halts_if_missing:
  - problem framing artifact
  - data audit decision
  - EDA plan
---

# EDA Hypothesis Journal

## Purpose

Use this skill to run exploratory analysis as a disciplined investigation: each check starts from a hypothesis, records evidence, and either supports modeling readiness or sends the project back to the right gate.

This skill executes an approved EDA plan. It does not replace `eda-plan`, `data-audit`, or `modeling`.

## Use When

- Problem framing, data audit, and EDA plan are already approved.
- You need to explore distributions, relationships, missingness, subgroups, or time structure before modeling.
- EDA findings may change the analysis plan and need an evidence trail.
- You need a final proceed/revise/halt recommendation before `modeling`.

Do not use this to start open-ended plotting, define the analytical question, audit data readiness, or train models.

## Stop Conditions

Stop and route back before continuing if:

- no approved data-audit decision exists
- target definition or prediction time is ambiguous
- EDA reveals leakage, split contamination, or impossible ranges
- subgroup counts are too small to support the planned claim
- exploration suggests a different objective than the problem frame

## Procedure

### 1. Confirm Gates And Journal Location

Name the framing artifact, data-audit decision, EDA plan, dataset version, and where the journal will be written. If the data audit is `PROCEED WITH CONDITIONS`, list the conditions before running EDA.

### 2. Start The Hypothesis Journal

Use one entry per question:

```markdown
## Hypothesis Entry

Question:
Prior expectation:
Check performed:
Evidence:
Interpretation:
Action:
```

Do not record only interesting findings. Record failed or null hypotheses when they affected the next step.

### 3. Run Sanity Checks First

Before interpreting any plot, check:

- row count and unit-of-analysis uniqueness
- duplicate IDs or duplicate `(id, time)` rows
- missingness by key slices
- impossible numeric ranges and invalid categories
- target prevalence or outcome coverage
- date ordering and feature/target windows
- join cardinality and row loss if multiple tables are involved

Any failing sanity check gets an entry and a proceed/revise/halt note.

### 4. Execute The Planned EDA Checks

Work through the EDA plan one question at a time. For each table, plot, or diagnostic, state what decision it informs. Avoid adding new exploratory branches unless they are triggered by evidence and logged as a plan revision.

### 5. Run The EDA Leakage Audit

For candidate predictors and transformations observed during EDA, ask:

- Would this value exist at prediction time?
- Is it a post-outcome field, direct target proxy, or manually corrected label?
- Did any summary, imputation, encoding, or scaling use future or full-dataset information?
- Could entity overlap or repeated observations contaminate a future split?
- Did EDA suggest feature engineering that must be constrained inside folds later?

If any answer creates leakage risk, update the data-audit artifact or hand off to `plan-as-guidance` for revision before modeling.

### 6. Produce The Modeling Handoff

End with:

```markdown
## EDA Handoff

Proceed decision: proceed / revise / halt
Supported hypotheses:
Rejected or inconclusive hypotheses:
Sanity check issues:
Leakage audit findings:
Feature or transform notes:
Required plan revisions:
Recommended next skill:
```

Proceed to `modeling` only when the EDA evidence supports the existing problem frame, data-audit conditions are satisfied, and leakage risks have an explicit mitigation.
