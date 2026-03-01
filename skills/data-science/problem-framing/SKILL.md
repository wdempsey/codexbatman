---
name: problem-framing
description: Structured clarification of analytical objectives before any data analysis or modeling begins. Prevents metric confusion, leakage, and causal misinterpretation.
---

# Skill: Problem Framing

## Purpose

Clarify and formalize the analytical objective before any data access, exploration, or modeling begins.

This skill prevents:

- Metric confusion
- Ill-defined targets
- Implicit assumptions
- Causal misinterpretation
- Premature modeling
- Hidden stakeholder conflicts

No modeling or EDA should begin before this phase is completed and reviewed.

---

## When to Use

Use this skill before:

- Any exploratory data analysis
- Any feature engineering
- Any model training
- Any database schema design tied to modeling
- Any metric evaluation

---

## Required Inputs

- Problem description (free text)
- Stakeholder context (if applicable)
- Known constraints (business, ethical, regulatory, computational)
- Known data sources (if available)

If inputs are incomplete, request clarification before proceeding.

---

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

---

## Output Format

Produce a structured summary in this format:

### 1. Problem Statement
(Concise paragraph)

### 2. Objective Type
(Predictive / Causal / etc.)

### 3. Decision Context
(Bulleted list)

### 4. Success Metrics
(Bulleted list with definitions)

### 5. Constraints
(Bulleted list)

### 6. Risk Register
(Bulleted list)

### 7. Data Requirements
(Bulleted list)

---

## Guardrails

- Do not assume the task is predictive.
- Do not assume available data is sufficient.
- Do not proceed to modeling automatically.
- Do not invent metrics without definitions.
- Do not ignore causal implications.

---

## Escalation Conditions

Stop and require human confirmation if:

- The objective is ambiguous.
- Metrics conflict.
- Causal inference is implied but assumptions are unclear.
- Ethical risks are detected.
- Stakeholder goals conflict.

Human review is mandatory before moving to Data Audit or EDA.
