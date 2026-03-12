---
name: causal-design-check
description: Validate causal design logic before causal claims are made. Use when analysis includes treatment effects, policy effects, or intervention impacts that require explicit estimands, assumptions, and threat assessment.
category: data-science
role_compatibility:
  - student
  - data scientist
  - data science manager
stage: causal-design
inputs:
  - problem framing artifact
  - treatment definition
  - outcome definition
  - timing structure
  - design assumptions
outputs:
  - causal design assessment
  - proceed/halt recommendation
artifacts:
  - estimand definition
  - identification assumptions
  - threat register
  - overlap and interference notes
  - interpretation limits
depends_on:
  - problem-framing
  - data-audit
recommended_next:
  - modeling
  - model-evaluation
overlays:
  - student/tutor-mode
  - manager/executive-summary
status: near-canonical
---

# Skill: Causal Design Check

## Purpose

Force explicit causal reasoning before estimation or interpretation.

This skill validates the causal question, identification assumptions, and interpretation limits.

It prevents:

- causal language without estimand definition
- hidden identification assumptions
- unexamined overlap and interference risks
- over-interpretation of weak designs

## When to Invoke

Invoke this skill:

- after `problem-framing` for causal or policy questions
- before causal model specification
- before sharing causal conclusions
- when identification assumptions change

## Required Inputs

- Problem-framing artifact
- Unit of analysis and timing structure
- Treatment/exposure definition
- Outcome definition
- Data-audit summary relevant to causal variables
- Proposed design (if already drafted)

If treatment timing, estimand, or outcome window is unclear, halt and request clarification.

## Expected Outputs

Produce a structured causal-design artifact with:

### 1. Estimand Definition

### 2. Identification Assumptions

### 3. Threats to Identification

### 4. Overlap/Support Assessment Plan

### 5. Interference and Spillover Risks

### 6. Interpretation Limits

### 7. Proceed / Halt Recommendation

## Artifact Checklist

- Estimand explicitly defined
- Treatment, outcome, and timing windows aligned
- Identification assumptions listed and test strategy noted
- Major threats documented
- Overlap/support checks specified
- Interference risks considered
- Interpretation limits stated
- Proceed/Halt recommendation stated

## Common Failure Modes

- writing "causal" without estimand
- assuming ignorability without argument
- ignoring positivity/overlap problems
- ignoring spillovers/interference
- claiming policy effects beyond design support
- mixing predictive and causal objectives

## Proceed / Halt Guidance

Proceed if:

- estimand is explicit
- assumptions are documented and plausible
- key threats have mitigation or sensitivity plan

Halt and escalate if:

- estimand is ambiguous
- identification depends on unsupported assumptions
- overlap/interference risks are severe and unresolved
- interpretation limits are too narrow for intended claim

