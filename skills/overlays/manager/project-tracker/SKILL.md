---
name: project-tracker
description: Wrap workflow artifacts into a manager-facing project-state view. Use when a manager needs cross-artifact tracking of progress, blockers, owners, and upcoming checkpoints.
category: overlays
status: active
stage: overlay
role_compatibility:
  - data science manager
overlays:
  - project-bootstrap
  - data-audit
  - experiment-log
  - weekly-review
---

# Skill: Project Tracker

## Purpose

Translate workflow outputs into project-state memory.

This overlay helps a manager see:

- where the project is in the workflow
- what is blocked
- who owns the next move
- which artifact is current

## When to Use

Use this overlay when:

- the workflow state must be tracked over time
- multiple artifacts need to be combined into one project view
- a manager needs meeting prep or review context from workflow progress

## How It Wraps Existing Skills

This overlay wraps the outputs of canonical and manager workflow skills.

It does not rerun the workflow logic. It organizes the results into project memory.

## Procedure

### Step 1: Identify current workflow stage

State where the project sits:

- bootstrap
- framing
- audit
- experiment
- review

### Step 2: Identify the latest artifact for each stage

Determine what is current, what is missing, and what is stale.

### Step 3: Extract blockers and owners

Record:

- blockers
- dependencies
- owners
- next checkpoints

## Output Format

Produce:

### 1. Current Workflow Stage

### 2. Artifact Status

### 3. Open Blockers

### 4. Owners and Next Moves

### 5. Upcoming Review Points

## Guardrails

- Do not invent project state not supported by artifacts.
- Do not confuse stale artifacts with current status.
- Do not replace the underlying workflow artifact with tracker notes.

## Escalation Conditions

Escalate if key artifacts are missing or stale enough that project state cannot be stated confidently.

