---
name: problem-framing
description: Define the analytical problem before any audit, exploration, or modeling begins. Use when a project needs an explicit problem statement, success metrics, constraints, and a documented risk register.
---

# Skill: Problem Framing

## Purpose

Clarify and formalize the analytical objective before data audit, exploration, or modeling begins.

This skill converts an informal request into explicit analytical artifacts.

It exists to prevent:

- metric confusion
- ill-defined targets
- implicit assumptions
- causal misclassification
- premature modeling
- silent stakeholder conflicts

No downstream modeling work should proceed until this artifact is reviewed.

## When to Invoke

Invoke this skill before:

- any data audit
- any exploratory data analysis
- any feature engineering
- any model training
- any evaluation design
- any database or pipeline design tied to modeling assumptions

## Required Inputs

- Problem description (free text)
- Stakeholder context (if applicable)
- Known constraints (business, ethical, regulatory, computational)
- Known data sources (if available)

If inputs are incomplete, request clarification before proceeding.

## Procedure

### Step 1 — Clarify Objective Type

Determine whether the task is:

- Predictive
- Descriptive
- Causal
- Policy evaluation
- Exploratory research

Explicitly state which type applies.

If unclear, ask for clarification.

---

### Step 2 — Define the Decision Context

Document:

- Who will use the output?
- What decision will be made?
- What action follows the model output?
- What are the costs of false positives and false negatives?

---

### Step 3 — Define Success Metrics

Specify:

- Primary metric
- Secondary metrics
- Operational definition of each metric
- Measurement window
- Thresholds (if applicable)

Avoid vague metric descriptions.

---

### Step 4 — Define Constraints

Identify:

- Time horizon
- Latency requirements
- Interpretability requirements
- Fairness constraints
- Deployment environment
- Resource constraints

---

### Step 5 — Identify Risks

Create a structured risk register:

- Target leakage risks
- Proxy bias risks
- Temporal misalignment risks
- Feedback loop risks
- Intervention effects (if causal)
- Ethical concerns

---

### Step 6 — Define Data Requirements

List:

- Required variables
- Temporal structure requirements
- Minimum sample size assumptions
- Required external data
- Identification assumptions (if causal)

## Expected Outputs

Produce a framing artifact with:

- problem statement
- objective type
- decision context
- success metrics
- constraints
- risk register
- data requirements

Use this structure:

### 1. Problem Statement

### 2. Objective Type

### 3. Decision Context

### 4. Success Metrics

### 5. Constraints

### 6. Risk Register

### 7. Data Requirements

## Artifact Checklist

- Objective type explicitly named
- Decision user and action path stated
- Primary metric defined operationally
- Secondary metrics defined if needed
- Constraints documented
- Risk register populated
- Data requirements listed
- Proceed-to-audit recommendation stated

## Common Failure Modes

- treating every problem as predictive
- naming metrics without operational definitions
- skipping stakeholder or decision context
- ignoring causal implications
- listing data requirements too vaguely to audit
- allowing modeling to begin without review

## Guardrails

- Do not assume the task is predictive.
- Do not assume available data is sufficient.
- Do not proceed to modeling automatically.
- Do not invent metrics without definitions.
- Do not ignore causal implications.

## Human Review Requirement

Human review is mandatory before moving to `data-audit`.

Escalate if:

- The objective is ambiguous.
- Metrics conflict.
- Causal inference is implied but assumptions are unclear.
- Ethical risks are detected.
- Stakeholder goals conflict.
