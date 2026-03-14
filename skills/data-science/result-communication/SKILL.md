---
name: result-communication
description: Convert technical outputs into decision-facing communication artifacts. Use when analysis results need memo, update, or slide-ready summaries with uncertainty, caveats, and recommended actions.
category: data-science
status: active
stage: evaluation
role_compatibility:
  - data scientist
  - data science manager
inputs:
  - evaluation or experiment artifacts
  - audience
  - decision context
  - uncertainties
  - format target
outputs:
  - decision-facing summary
artifacts:
  - memo
  - project update
  - slide-ready summary
  - caveat section
  - recommendation and next steps
depends_on:
  - model-evaluation
  - experiment-log
recommended_next:
  - stakeholder-update
overlays:
  - executive-summary
  - communication-workflows
human_review_required: true
---

# Skill: Result Communication

## Purpose

Translate analytical outputs into decision-ready communication without losing uncertainty or caveats.

This skill bridges technical artifacts and manager/stakeholder interpretation.

It prevents:

- overconfident claims
- metric-only reporting with no decision context
- omission of uncertainty and limits
- inconsistent messaging across audiences

## When to Invoke

Invoke this skill:

- after evaluation or experiment-log updates
- when preparing leadership updates
- when drafting project memos or status summaries
- before sharing externally visible conclusions

## Required Inputs

- Latest evaluation and/or experiment artifacts
- Target audience (technical, mixed, executive)
- Decision context and required action
- Key uncertainties and caveats
- Preferred output format (memo/update/slide summary)

If audience or decision objective is unclear, request clarification before drafting.

## Expected Outputs

Produce communication artifacts with:

### 1. Core Finding Summary

### 2. Manager-Facing Interpretation

### 3. Uncertainty and Caveats

### 4. Recommendation and Next Steps

### 5. Format-Specific Output

At least one of:

- memo draft
- project update draft
- slide-ready summary

## Artifact Checklist

- Findings tied to validated metrics
- Audience-appropriate interpretation included
- Uncertainty explicitly stated
- Caveats and limits documented
- Recommendation and next actions stated
- Claims constrained to evidence

## Common Failure Modes

- overstating evidence strength
- omitting caveats for non-technical audiences
- confusing predictive and causal claims
- no action recommendation
- verbose technical detail with no executive summary

## Proceed / Halt Guidance

Proceed if:

- claims are evidence-aligned
- uncertainty/caveats are explicit
- recommendation is actionable

Halt and escalate if:

- evidence is contradictory or unstable
- requested claim exceeds evaluation support
- communication objective conflicts with documented limits

