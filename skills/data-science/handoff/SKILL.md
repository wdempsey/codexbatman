---
name: handoff
description: Produce a short structured handoff after a work session so the next human or agent can continue without reconstructing context from scratch.
category: data-science
status: active
stage: evaluation
role_compatibility:
  - student
  - data scientist
  - data science manager
inputs:
  - work completed
  - commands or evidence
  - open questions
  - recommended next step
outputs:
  - handoff summary
artifacts:
  - handoff note
depends_on:
  - workflow-trace
recommended_next:
  - workflow-trace
  - result-communication
overlays:
  - execution-mode
  - project-tracker
  - executive-summary
human_review_required: true
---

# Skill: Handoff

## Purpose

Create a concise handoff note after a work session so the next person or agent can continue without rebuilding the full context.

This skill should produce the smallest useful handoff that still preserves momentum.

## When to Invoke

Invoke this skill:

- after a meaningful coding or analysis session
- before pausing work
- before routing the work to another agent
- when a manager or collaborator needs a quick project-state transfer

## Required Inputs

- what changed
- evidence or commands run
- open questions
- recommended next action

## Procedure

### Step 1: Summarize What Changed

List the meaningful work completed, not every minor action.

### Step 2: Record Evidence

Capture the commands run, build checks, or other evidence that supports the current state.

### Step 3: Record Open Questions

State anything unresolved that could block or redirect the next session.

### Step 4: Recommend The Next Action

Tell the next person or agent what should happen next.

## Expected Output

Produce a handoff in this structure:

```markdown
## What I changed

## Evidence / commands run

## Open questions

## Recommended next action
```

## Common Failure Modes

- writing a changelog instead of a handoff
- omitting unresolved blockers
- giving no next action
- assuming the next session remembers the context

## Guardrails

- Keep it short and actionable.
- Prefer clarity over exhaustiveness.
- Record uncertainty honestly.
