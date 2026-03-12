---
name: data-audit
description: Audit data sources and derived datasets before EDA or modeling. Use when the project needs a documented quality, leakage, bias, and temporal-validity assessment with an explicit proceed decision.
category: data-science
role_compatibility:
  - student
  - data scientist
  - data science manager
stage: audit
order: 3
inputs:
  - dataset sources
  - schema or dictionary
  - target definition
  - time index
  - unit of analysis
outputs:
  - audit decision
  - remediation actions
artifacts:
  - data audit report
  - schema summary
  - quality flags
  - proceed/halt decision
depends_on:
  - problem-framing
recommended_next:
  - eda-plan
overlays:
  - student/tutor-mode
  - practitioner/execution-mode
  - practitioner/artifact-enforcer
  - manager/project-tracker
status: canonical
---

# Skill: Data Audit (Proceed / Halt Protocol)

## Purpose

Perform a structured audit of a dataset (or data sources) before EDA, feature engineering, or modeling.

This skill aims to surface:
- data quality issues
- target construction errors
- leakage risks
- temporal validity problems
- sampling and measurement biases
- join and key integrity risks

The output includes an explicit **Proceed / Halt** recommendation.

## When to Invoke

Invoke this skill:

- immediately after `problem-framing`
- before EDA, feature engineering, or modeling
- before finalizing split strategy
- after any major data refresh or pipeline change

## Required Inputs

Minimum required:
- Dataset location and format (files/db tables/API)
- Data dictionary or schema (if available)
- Candidate target definition (if applicable)
- Time index definition (if applicable)
- Unit of analysis definition (e.g., person-day, firm-quarter)

Optional but helpful:
- Known join keys and intended joins
- Known filters applied (time range, population)
- Prior baselines or historical versions of the data

If essential inputs are missing, request them before completing the audit.

## Procedure

### Step 1 â€” Confirm Unit of Analysis and Time Structure

Document:
- Unit of analysis (what one row represents)
- Unique identifier(s)
- Time index (if any): timestamp/date, period granularity, panel structure
- Whether data is cross-sectional, repeated cross-section, or panel/longitudinal

Checks:
- Are IDs unique at the claimed unit of analysis?
- If panel: are there duplicate (id, time) rows?

---

### Step 2 â€” Schema & Type Validation

Check:
- Column names and types match expectations
- Categorical vs numeric types are sensible
- Obvious parsing issues (dates as strings, numeric fields with commas, etc.)

Flag:
- Unexpected null-heavy columns
- Mixed-type columns
- Silent coercions that could break modeling

---

### Step 3 â€” Missingness & Coverage

Assess:
- Overall missingness rate per column
- Missingness by key slices (time, group, region, etc.)
- Whether missingness correlates with target or treatment

Flag:
- Columns with extreme missingness
- Systematic missingness (entire groups/time periods)
- â€œMissing not at randomâ€ signals (strong correlation with outcomes)

---

### Step 4 â€” Distribution & Range Sanity Checks

For numeric variables:
- Range, percentiles, outliers, invalid values (negative ages, impossible counts)

For categorical variables:
- Cardinality
- Rare categories
- Unexpected category values (typos, casing)

Flag:
- Implausible ranges
- Sudden distribution shifts across time
- Highly sparse high-cardinality categoricals

---

### Step 5 â€” Target Construction Review (if applicable)

Document:
- Exact target definition and window
- Whether target is available at prediction time

Leakage checks:
- Any feature derived from future information relative to prediction time?
- Any post-outcome variables included?
- Any data processing step using labels to compute features?

If target is time-dependent:
- Confirm the cutoff point for feature availability
- Confirm the target window occurs strictly after feature window

---

### Step 6 â€” Leakage Risk Scan (Predictive + Longitudinal)

Systematically identify:
- Direct leakage: target itself or proxies
- Temporal leakage: future values used as features
- Group leakage: aggregated labels by group that include the same row
- Train/test contamination: same entity appears in both sets when it should not

Flag:
- Any variable that would not exist at prediction time
- Any join that could pull future information (e.g., â€œlatest statusâ€ tables)

---

### Step 7 â€” Bias and Representativeness Checks

Assess:
- Sampling frame (who is included/excluded)
- Label availability bias (missing outcomes)
- Measurement bias (different instruments across groups)
- Proxy risk (sensitive attributes inferred)

Flag:
- Large coverage differences across groups/time
- Strong outcome missingness differences by subgroup
- Potential fairness risks requiring explicit handling

---

### Step 8 â€” Join and Key Integrity (if multiple sources)

If multiple tables/sources:
- Validate join keys
- Check for one-to-many explosions
- Check for unmatched keys and dropped rows
- Confirm join direction aligns with unit of analysis

Flag:
- Silent row multiplication
- Large drop rates on join
- Many-to-many joins without explicit intent

---

### Step 9 â€” Split Validity (Preview Only)

Do not finalize splits here, but assess plausibility:
- For longitudinal: time-based split or blocked split may be required
- For panel: entity-level split may be required to avoid leakage

Flag:
- Any split strategy that would contaminate evaluation
- Any scenario where the same entity appears across train/test improperly

## Expected Outputs

Produce an audit artifact with:

### 1. Summary

- data sources reviewed
- unit of analysis
- time structure

### 2. Key Findings

### 3. Data Quality

### 4. Leakage Assessment

### 5. Bias and Representativeness

### 6. Join and Key Integrity

### 7. Proceed Decision

Choose one:

- `PROCEED`
- `PROCEED WITH CONDITIONS`
- `HALT`

### 8. Next Actions

## Artifact Checklist

- Data sources listed
- Unit of analysis documented
- Time structure documented or explicitly absent
- Missingness review completed
- Schema and type issues checked
- Leakage review completed
- Bias and sampling risks recorded
- Join integrity reviewed if relevant
- Proceed decision stated with conditions

## Common Failure Modes

- auditing a dataset without a clear unit of analysis
- ignoring the target construction window
- missing temporal leakage in longitudinal data
- assuming missingness is random
- skipping join explosion checks
- issuing `PROCEED` without documented conditions

## Guardrails

- Do not proceed to modeling if leakage risks are unresolved.
- Do not assume missingness is random.
- Do not assume cross-sectional methods apply to longitudinal data.
- Do not modify raw data; propose transformations in a processed layer.
- Do not finalize train/test splits without explicit rationale.

## Human Review Requirement

Human review is mandatory before any modeling if the audit returns `PROCEED WITH CONDITIONS` or `HALT`.

## Escalation Conditions

Require human confirmation if:
- Proceed/Halt decision is not clearly PROCEED
- Target definition is ambiguous or likely leaking
- Time ordering is unclear for longitudinal data
- Join integrity suggests row explosion or major drop
- Fairness or proxy risks are detected
- Dataset appears non-representative relative to intended use

