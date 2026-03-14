---
name: executive-summary
description: Wrap a workflow skill for manager-facing summary delivery. Use when canonical or operational artifacts need to be translated into concise status, risk, and decision summaries for leaders or stakeholders.
category: overlays
status: active
stage: overlay
role_compatibility:
  - data science manager
overlays:
  - problem-framing
  - data-audit
  - model-evaluation
  - weekly-review
  - stakeholder-update
  - result-communication
---

# Skill: Executive Summary

## Purpose

Convert workflow artifacts into decision-ready summaries.

This overlay changes delivery toward:

- status
- risk
- key decisions
- next actions

It does not replace the underlying workflow.

## When to Use

Use this overlay when:

- the user is acting as a data science manager
- the main need is synthesis, not raw artifact generation
- leaders or stakeholders need a short summary of workflow state

## How It Wraps Existing Skills

This overlay:

1. selects the relevant workflow skill or artifact
2. preserves the original workflow conclusions
3. compresses them into manager-facing output

Common wrapped skills:

- `problem-framing`
- `data-audit`
- `experiment-log`
- `weekly-review`
- `stakeholder-update`

## Procedure

### Step 1: Identify the source artifact

State which workflow artifact is being summarized.

### Step 2: Extract the management signal

Focus on:

- current status
- risks
- decisions required
- next checkpoints

### Step 3: Keep technical detail subordinate

Preserve the underlying logic, but do not lead with low-level workflow mechanics unless they affect decisions.

## Output Format

Produce:

### 1. Source Workflow or Artifact

### 2. Current Status

### 3. Key Risks

### 4. Decision or Ask

### 5. Next Steps

## Guardrails

- Do not change the underlying artifactâ€™s meaning.
- Do not bury halt conditions or risk flags.
- Do not substitute summary for the required artifact itself when the artifact is still needed.

## Escalation Conditions

Escalate if the underlying artifact is incomplete or too stale to summarize credibly.

