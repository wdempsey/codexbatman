---
name: experiment-log
description: Record a modeling or evaluation run as a reproducible experiment artifact. Use after any training, feature change, split change, or evaluation change that could affect analytical conclusions.
category: data-science
role_compatibility:
  - student
  - data scientist
  - data science manager
stage: logging
order: 7
inputs:
  - model configuration
  - dataset version
  - split strategy
  - metrics
  - seed
outputs:
  - logged run record
  - iteration decision
artifacts:
  - experiment log entry
  - comparison table
  - decision notes
depends_on:
  - modeling
  - model-evaluation
recommended_next:
  - result-communication
overlays:
  - student/tutor-mode
  - practitioner/execution-mode
  - practitioner/artifact-enforcer
  - manager/project-tracker
status: canonical
---

# Skill: Experiment Log

## Purpose

Document each modeling iteration in a structured, reproducible way.

This skill prevents:

- Undocumented iteration
- Metric drift
- Forgotten parameter changes
- Narrative rewriting after results
- Selective reporting
- Loss of reproducibility

Every modeling attempt must generate an experiment log entry.

## When to Invoke

Invoke this skill:

- after any model training
- after hyperparameter changes
- after feature set modifications
- after split strategy changes
- after metric changes
- before deciding to iterate further

No model iteration is considered valid until logged.

## Required Inputs

- Model type
- Dataset version
- Feature set description
- Train/test split description
- Metrics computed
- Hyperparameters used
- Random seed (if applicable)

## Procedure

### Step 1 â€” Context

Record:

- Date
- Author
- Dataset version
- Unit of analysis
- Target definition
- Split strategy

---

### Step 2 â€” Hypothesis

Explicitly state:

- What change was made?
- Why was this change expected to improve results?
- What metric is expected to move?

---

### Step 3 â€” Configuration

Document:

- Model type
- Hyperparameters
- Feature set version
- Preprocessing steps
- Random seed
- Evaluation window

---

### Step 4 â€” Results

Report:

- Primary metric
- Secondary metrics
- Comparison to baseline
- Confidence intervals (if available)
- Error analysis summary

---

### Step 5 â€” Interpretation

Answer:

- Did the hypothesis hold?
- Is the improvement practically meaningful?
- Is there evidence of overfitting?
- Are subgroup results stable?

---

### Step 6 â€” Decision

Choose one:

- Continue iterating
- Revert to baseline
- Freeze model
- Escalate for review

Justify the decision clearly.

## Expected Outputs

Produce a structured experiment entry containing:

### 1. Context

### 2. Hypothesis

### 3. Configuration

### 4. Results

### 5. Interpretation

### 6. Decision

If a local template exists, follow it. Otherwise use the canonical sections above.

## Artifact Checklist

- Run date recorded
- Dataset version recorded
- Target definition recorded
- Split strategy recorded
- Model and hyperparameters recorded
- Feature set version recorded
- Seed recorded
- Metrics recorded
- Comparison to baseline recorded
- Decision and next step recorded

## Common Failure Modes

- logging only successful runs
- omitting split or seed information
- comparing against an undefined baseline
- changing metrics without documentation
- recording results without interpretation
- iterating again before the current run is logged

## Guardrails

- Do not omit failed experiments.
- Do not compare models trained on different splits without stating it clearly.
- Do not change metrics midstream without documenting the change.
- Do not reuse a random seed silently.
- Do not interpret noise as signal without evidence.

## Human Review Requirement

Require human review if:

- Metrics degrade unexpectedly
- Model instability appears across runs
- Large subgroup disparities appear
- Hyperparameter search significantly increases variance
- Baseline is unclear or undocumented

