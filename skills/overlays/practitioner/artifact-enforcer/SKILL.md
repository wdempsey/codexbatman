---
name: artifact-enforcer
description: Wrap a canonical skill with strict artifact enforcement. Use when a data scientist needs Codex to refuse workflow drift and require the canonical output before proceeding.
category: overlays
status: active
stage: overlay
role_compatibility:
  - data scientist
overlays:
  - project-bootstrap
  - problem-framing
  - data-audit
  - eda-plan
  - modeling
  - model-evaluation
  - experiment-log
---

# Skill: Artifact Enforcer

## Purpose

Prevent workflow drift by enforcing artifact completion.

This overlay is strict about output requirements. It does not change the underlying workflow logic. It changes how strongly Codex insists on durable artifacts.

## When to Use

Use this overlay when:

- the workflow is at risk of becoming conversational and undocumented
- the user wants a hard requirement for the canonical artifact
- downstream work should not proceed without a completed artifact

## How It Wraps Existing Skills

This overlay:

1. selects the canonical skill
2. restates the required artifact
3. refuses to mark the phase complete without that artifact

## Procedure

### Step 1: State the required artifact

Name the artifact the canonical skill must produce.

### Step 2: Check completeness

Use the underlying skillâ€™s checklist to verify that the artifact is complete enough to support the next phase.

### Step 3: Block premature progression

If the artifact is incomplete, state exactly what is missing and stop the transition.

## Output Format

Produce:

### 1. Workflow Skill

### 2. Required Artifact

### 3. Completeness Check

### 4. Missing Elements or Approval Status

## Guardrails

- Do not accept partial artifacts silently.
- Do not let later phases start without required documentation.
- Do not invent completeness when review is still required.

## Escalation Conditions

Escalate whenever the canonical skill requires human approval before the workflow can continue.

