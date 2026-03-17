---
name: model-evaluation
description: Evaluate model behavior with performance interpretation, failure analysis, and robustness checks. Use after modeling to determine whether a model is ready to advance, needs revision, or should be rejected.
category: data-science
status: canonical
stage: evaluation
order: 6
role_compatibility:
  - student
  - data scientist
  - data science manager
inputs:
  - modeling summary
  - baseline and candidate metrics
  - validation design
  - subgroup definitions
  - decision thresholds
outputs:
  - evaluation recommendation
  - next-step conditions
artifacts:
  - evaluation report
  - metric summary
  - error analysis
  - robustness checks
  - recommendation note
depends_on:
  - modeling
recommended_next:
  - experiment-log
overlays:
  - tutor-mode
  - execution-mode
  - executive-summary
  - communication-workflows
method_prerequisites:
  - linear-regression
  - random-forest
  - gradient-boosting
method_default_path:
  - linear-regression
  - random-forest
  - gradient-boosting
method_escalation_rule: >
  If the learner cannot explain what model is being evaluated
  or why it was chosen, pause evaluation and route to the
  relevant method skill before interpreting results.
method_handoff_prompts:
  unfamiliar: "Pause evaluation and teach the method before interpreting metrics."
  compare: "Explain the tradeoff between the baseline and the stronger model."
  stronger-than-baseline: "Explain why the stronger model was proposed over the baseline."
human_review_required: true
halts_if_missing:
  - modeling summary
  - baseline and candidate metrics
  - validation design
produces_gate: evaluation-recommendation
---

# Skill: Model Evaluation

## Purpose

Interpret model performance in a decision-relevant way.

This skill emphasizes robustness, subgroup behavior, and failure analysis rather than single-metric reporting.

It prevents:

- leaderboard-only conclusions
- missing failure mode analysis
- untested robustness assumptions
- deployment recommendations without evidence

## When to Invoke

Invoke this skill:

- after `modeling`
- before finalizing any shared recommendation
- before model-card completion for final models

## Required Inputs

- Modeling summary artifact
- Baseline and candidate metrics
- Validation design and split details
- Subgroup definitions
- Business/decision thresholds from framing

If metrics or split details are incomplete, halt and request completion.

## Procedure

### Step 1 - Summarize Performance Metrics

Report primary and secondary metrics for baseline and candidate models.

Interpret relative differences in practical terms.

---

### Step 2 - Conduct Error Analysis

Analyze:

- false positive/false negative patterns
- high-error slices
- threshold sensitivity (if applicable)

---

### Step 3 - Run Bias and Fairness Checks

Assess subgroup performance differences and potential proxy effects.

Document material disparities and implications.

---

### Step 4 - Run Robustness Checks

Evaluate stability under:

- temporal shifts
- subgroup slices
- perturbation/stress tests
- alternate thresholds/assumptions

---

### Step 5 - Synthesize Findings and Recommendation

Produce a recommendation:

- proceed
- proceed with conditions
- halt/revise

Include concrete next-step actions.

## Expected Outputs

Produce an evaluation artifact with:

### 1. Evaluation Report

### 2. Metric Summary

### 3. Error Analysis

### 4. Robustness Checks

### 5. Recommendation and Next-Step Note

## Artifact Checklist

- Baseline versus candidate metrics summarized
- Error patterns documented
- Subgroup/bias checks documented
- Robustness checks documented
- Recommendation with conditions and actions stated

## Common Failure Modes

- relying on one aggregate metric
- skipping subgroup analysis
- ignoring instability across time or slices
- recommending deployment without failure analysis
- omitting next-step actions

## Proceed / Halt Guidance

Proceed only if:

- performance is decision-relevant
- failure modes are understood and acceptable
- robustness checks show acceptable stability

Proceed with conditions if:

- mitigation actions are required before deployment/use

Halt and revise if:

- critical subgroup disparities are unresolved
- robustness failures undermine conclusions
- recommendation cannot be justified from evidence

