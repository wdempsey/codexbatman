---
name: execution-mode
description: Wrap a canonical workflow skill for practitioner execution. Use when a data scientist needs direct progress, artifact production, and minimal pedagogical or managerial framing.
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

# Skill: Execution Mode

## Purpose

Deliver the canonical workflow directly.

This overlay keeps the shared workflow logic intact but changes delivery toward:

- direct execution
- concise assumptions
- explicit outputs
- immediate artifact production

## When to Use

Use this overlay when:

- the user is acting as a data scientist or analyst
- the goal is to move the workflow forward now
- the user wants the artifact, not tutoring
- the workflow gate is understood and should be executed directly

## How It Wraps Existing Skills

This overlay:

1. identifies the relevant canonical skill
2. preserves that skillâ€™s workflow and guardrails
3. executes the workflow with minimal instructional overhead

Common wrapped skills:

- `project-bootstrap`
- `problem-framing`
- `data-audit`
- `experiment-log`

## Procedure

### Step 1: Identify the workflow skill

State the canonical skill being used.

### Step 2: Execute directly

Run the shared workflow with:

- explicit assumptions
- artifact-first output
- no pedagogical scaffolding

### Step 3: Surface blockers only when material

Do not interrupt for minor uncertainty. Make reasonable assumptions and keep the workflow moving.

## Output Format

Produce:

### 1. Workflow Skill

### 2. Assumptions

### 3. Artifact or Artifact Draft

### 4. Remaining Blockers

## Guardrails

- Do not bypass canonical workflow gates.
- Do not replace the artifact with a casual summary.
- Do not add tutoring steps unless explicitly requested.

## Escalation Conditions

Escalate when:

- required inputs are materially missing
- a workflow gate requires human approval
- the canonical skill would return halt conditions

