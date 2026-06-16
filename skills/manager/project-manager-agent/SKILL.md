---
name: project-manager-agent
description: Maintain one project's state, next actions, decisions, and handoffs. Use when a manager or coordinating agent needs a project-level operating layer above worker execution.
category: manager
status: active
stage: manager-ops
role_compatibility:
  - data science manager
inputs:
  - project brief
  - project state
  - next actions
  - decisions
  - handoffs
  - meeting notes
outputs:
  - updated project operating state
  - scoped coordination summary
artifacts:
  - project state update
  - next actions update
  - decisions update
  - handoff update
depends_on:
  - project-setup
recommended_next:
  - weekly-review
  - stakeholder-update
human_review_required: true
---

# Skill: Project Manager Agent

## Purpose

Maintain one project's operating memory so worker sessions and manager reviews stay coordinated.

This skill sits between portfolio-level coordination and task execution.

## Core Files To Maintain

This skill should maintain:

- `PROJECT_STATE.md`
- `NEXT_ACTIONS.md`
- `DECISIONS.md`
- `HANDOFF.md`

## Responsibilities

The Project Manager Agent should:

- maintain one project's state
- record decisions
- summarize meetings and emails into project memory
- identify blockers
- create scoped tasks for worker agents
- update handoffs after work sessions

## When To Use

Use this skill when:

- one project needs a reliable operating layer
- a worker finished a task and the project state must be updated
- a manager needs a clean project snapshot
- decisions and next actions are drifting out of sync

## Procedure

### Step 1: Read Current Project Memory

Read the current project brief, project state, next actions, decisions, and latest handoff.

### Step 2: Reconcile New Evidence

Pull in new information from:

- recent work sessions
- meeting notes
- email summaries
- updated analytical artifacts

### Step 3: Update Operating State

Update the project memory so it reflects:

- current phase
- what is complete
- what is in progress
- what is blocked
- what matters next

### Step 4: Scope Work For Workers

Break the next step into bounded work items that a worker agent could complete without owning the whole project.

### Step 5: Preserve Handoff Continuity

After meaningful work, leave the next session with:

- current state
- open questions
- recommended next action

## Guardrails

- Do not replace backbone artifacts with manager summaries.
- Do not let `NEXT_ACTIONS.md` become a stale backlog.
- Do not treat handoff notes as optional after meaningful work.
- Do not draft external commitments as if they are already approved.

## Escalation Conditions

Stop and escalate if:

- project evidence is too weak to maintain a credible state summary
- decisions conflict across sources
- a blocker requires scientific or strategic judgment beyond coordination
- the next action depends on unresolved ownership
