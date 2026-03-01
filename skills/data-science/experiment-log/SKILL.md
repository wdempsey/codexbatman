---
name: experiment-log
description: Structured logging protocol for documenting modeling experiments, decisions, and outcomes to enforce reproducibility and analytical discipline.
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

---

## When to Use

Use this skill:

- After any model training
- After hyperparameter changes
- After feature set modifications
- After split strategy changes
- After metric changes
- Before deciding to iterate further

No model iteration is considered valid until logged.

---

## Required Inputs

- Model type
- Dataset version
- Feature set description
- Train/test split description
- Metrics computed
- Hyperparameters used
- Random seed (if applicable)

---

## Procedure

### Step 1 — Context

Record:

- Date
- Author
- Dataset version
- Unit of analysis
- Target definition
- Split strategy

---

### Step 2 — Hypothesis

Explicitly state:

- What change was made?
- Why was this change expected to improve results?
- What metric is expected to move?

---

### Step 3 — Configuration

Document:

- Model type
- Hyperparameters
- Feature set version
- Preprocessing steps
- Random seed
- Evaluation window

---

### Step 4 — Results

Report:

- Primary metric
- Secondary metrics
- Comparison to baseline
- Confidence intervals (if available)
- Error analysis summary

---

### Step 5 — Interpretation

Answer:

- Did the hypothesis hold?
- Is the improvement practically meaningful?
- Is there evidence of overfitting?
- Are subgroup results stable?

---

### Step 6 — Decision

Choose one:

- Continue iterating
- Revert to baseline
- Freeze model
- Escalate for review

Justify the decision clearly.

---

## Output Format

Each experiment must produce a structured entry following the template in:

templates/ds/experiment-log-template.md

---

## Guardrails

- Do not omit failed experiments.
- Do not compare models trained on different splits without stating it clearly.
- Do not change metrics midstream without documenting the change.
- Do not reuse a random seed silently.
- Do not interpret noise as signal without evidence.

---

## Escalation Conditions

Require human review if:

- Metrics degrade unexpectedly
- Model instability appears across runs
- Large subgroup disparities appear
- Hyperparameter search significantly increases variance
- Baseline is unclear or undocumented
