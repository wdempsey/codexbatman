---
name: modeling
description: Specify and compare models in a controlled, reproducible way. Use when EDA is complete and the project needs a baseline, candidate model set, validation approach, and training record before evaluation.
category: data-science
status: canonical
stage: modeling
order: 5
role_compatibility:
  - student
  - data scientist
  - data science manager
inputs:
  - problem framing artifact
  - data audit artifact
  - EDA plan
  - dataset version
  - split strategy
  - metrics
outputs:
  - model comparison summary
  - evaluation handoff recommendation
artifacts:
  - baseline model spec
  - candidate model set
  - validation approach
  - feature and transform notes
  - training log or model summary
depends_on:
  - problem-framing
  - data-audit
  - eda-plan
recommended_next:
  - model-evaluation
overlays:
  - tutor-mode
  - execution-mode
  - artifact-enforcer
method_prerequisites:
  - linear-regression
  - ridge-regression
  - lasso
  - random-forest
  - gradient-boosting
method_default_path:
  - linear-regression
  - ridge-regression
  - lasso
  - random-forest
  - gradient-boosting
method_escalation_rule: >
  Start with the simplest method the learner can understand and defend.
  If a new method is proposed and the learner is unfamiliar with it,
  pause the workflow, route to the relevant method skill,
  then resume modeling.
method_handoff_prompts:
  unfamiliar: "Pause modeling and teach the method before continuing."
  compare: "Explain why this method is being compared to the baseline."
  baseline-first: "Teach or fit the simplest defensible baseline before advanced models."
  why-this-method: "Explain why this method is appropriate for the current modeling step."
halts_if_missing:
  - problem framing artifact
  - data audit artifact
  - EDA plan
  - split strategy
  - metrics
---

# Skill: Modeling

## Purpose

Define and execute model specification and comparison without collapsing into blind auto-optimization.

This skill enforces explicit baselines, controlled candidate comparisons, and documented configuration choices.

It prevents:

- model shopping without rationale
- untracked feature/transform changes
- invalid comparisons across split strategies
- tuning-first workflows with no baseline anchor

## When to Invoke

Invoke this skill:

- after `problem-framing`
- after `data-audit`
- after `eda-plan`
- before `model-evaluation`

## Required Inputs

- Approved framing artifact
- Approved data-audit artifact
- Approved EDA plan artifact
- Dataset version and split strategy
- Candidate feature set and transform notes
- Primary/secondary metrics

If split strategy or metric definitions are unclear, halt and request clarification.

## Procedure

### Step 1 - Define Baseline Model

Specify a baseline model that is:

- simple
- reproducible
- aligned with objective type

Document expected baseline behavior.

---

### Step 2 - Define Candidate Model Set

List candidate models and rationale for inclusion.

Limit candidates to a justified set rather than exhaustive search.

---

### Step 3 - Define Validation Approach

Specify:

- split or resampling strategy
- leakage controls
- subgroup or temporal validation checks
- comparison rules against baseline

---

### Step 4 - Document Feature and Transform Decisions

Record:

- included/excluded feature groups
- transformations and encodings
- handling of missingness/outliers
- assumptions introduced by preprocessing

---

### Step 5 - Run Controlled Training

Train baseline and candidate models under the same protocol where comparable.

Capture run metadata for experiment logging.

---

### Step 6 - Produce Modeling Summary

Summarize:

- candidate performance against baseline
- parameter choices
- stability indicators
- recommended models for evaluation stage

## Expected Outputs

Produce a modeling artifact with:

### 1. Baseline Model Specification

### 2. Candidate Model Set

### 3. Validation Approach

### 4. Feature and Transform Notes

### 5. Training Log or Model Summary

### 6. Recommendation for Evaluation

## Artifact Checklist

- Baseline model documented
- Candidate set documented with rationale
- Validation strategy documented
- Feature/transform decisions documented
- Comparable training conditions stated
- Training log or summary recorded
- Handoff recommendation to evaluation provided

## Common Failure Modes

- skipping baseline model
- comparing models across non-comparable splits
- indiscriminate hyperparameter search
- undocumented feature engineering
- choosing top metric without stability checks

## Proceed / Halt Guidance

Proceed to `model-evaluation` only if:

- baseline and candidate comparisons are documented
- validation design is explicit and leakage-aware
- training summary is reproducible

Halt and escalate if:

- model ranking depends on non-comparable setups
- leakage concerns appear during training
- metric gains are unstable or uninterpretable

