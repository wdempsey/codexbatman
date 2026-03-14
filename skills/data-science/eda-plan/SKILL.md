---
name: eda-plan
description: Plan exploratory data analysis as a disciplined workflow phase before modeling. Use when a project needs explicit exploratory questions, plot priorities, subgroup checks, and outlier/confounder checks tied to the framing and audit artifacts.
category: data-science
status: canonical
stage: eda
order: 4
role_compatibility:
  - student
  - data scientist
  - data science manager
inputs:
  - problem framing artifact
  - data audit artifact
  - dataset summary
  - subgroup definitions
outputs:
  - eda protocol
  - modeling handoff recommendation
artifacts:
  - EDA plan
  - prioritized questions
  - plot list
  - subgroup checks
  - confounder and outlier checks
depends_on:
  - problem-framing
  - data-audit
recommended_next:
  - modeling
overlays:
  - tutor-mode
  - execution-mode
  - artifact-enforcer
halts_if_missing:
  - problem framing artifact
  - data audit artifact
produces_gate: modeling-ready
---

# Skill: EDA Plan

## Purpose

Design exploratory analysis as a structured plan instead of ad hoc plotting.

This skill converts problem framing and audit findings into a reproducible EDA protocol.

It prevents:

- random plotting without analytical intent
- untracked exploration scope creep
- subgroup blind spots
- unstructured outlier treatment
- confounder omissions before modeling

## When to Invoke

Invoke this skill:

- after `problem-framing`
- after `data-audit`
- before any model specification
- before creating feature transforms based on exploratory patterns

## Required Inputs

- Approved problem-framing artifact
- Approved data-audit artifact
- Dataset/schema summary used for exploration
- Unit of analysis and time structure
- Known subgroup definitions (if applicable)

If framing or audit artifacts are missing, halt and request them.

## Procedure

### Step 1 - Define Exploratory Questions

Specify prioritized questions tied to the analytical objective:

- primary pattern checks
- uncertainty checks
- subgroup behavior checks

---

### Step 2 - Define Variable Coverage

Map variables into:

- target(s)
- candidate predictors
- controls/confounders
- segmentation variables

Identify variables requiring transformations before plotting.

---

### Step 3 - Specify Plot and Diagnostic Set

Produce a prioritized plot list:

- distribution plots
- relationship plots
- temporal checks (if longitudinal)
- missingness visuals

Each plot must state its analytical purpose.

---

### Step 4 - Plan Subgroup and Slice Checks

Define subgroup checks by:

- demographic slices
- geography/team/product segments
- time windows/cohorts

Specify minimum sample thresholds for subgroup interpretation.

---

### Step 5 - Plan Confounder and Outlier Checks

Document:

- confounders to inspect and why
- outlier detection criteria
- outlier handling policy (inspect, winsorize, exclude, model robustly)

---

### Step 6 - Define Logging and Exit Conditions

Define:

- where EDA outputs will be stored
- how insights are logged
- what findings trigger revisions to framing/audit/modeling plan

## Expected Outputs

Produce an EDA planning artifact with:

### 1. EDA Plan

### 2. Prioritized Questions

### 3. Plot List

### 4. Subgroup Checks

### 5. Confounder and Outlier Checks

### 6. Logging and Exit Conditions

## Artifact Checklist

- EDA scope tied to framing objective
- Prioritized exploratory questions listed
- Plot list includes purpose for each plot
- Subgroup checks documented with thresholds
- Confounder checks explicitly listed
- Outlier policy documented
- Logging location and naming convention defined
- Proceed-to-modeling recommendation stated

## Common Failure Modes

- plotting without explicit questions
- exploring variables not tied to decision context
- missing subgroup checks
- treating outliers inconsistently
- inferring causal claims from exploratory patterns
- starting modeling before EDA outputs are documented

## Proceed / Halt Guidance

Proceed to modeling only if:

- EDA plan outputs are complete
- no critical unresolved audit issue remains
- outlier/confounder handling policy is explicit

Halt and escalate if:

- exploratory findings conflict with framing assumptions
- subgroup instability is severe and unexplained
- outlier influence dominates key patterns without resolution

