---
name: workflow-trace
description: Capture what happened during a work session or workflow cycle so the outcome, decisions, changed files, and reusable lessons do not disappear into chat history.
category: data-science
status: active
stage: logging
role_compatibility:
  - student
  - data scientist
  - data science manager
inputs:
  - session goal
  - files read or changed
  - decisions made
  - outcome
outputs:
  - workflow trace entry
artifacts:
  - workflow trace
  - reusable pattern note
depends_on:
  - problem-framing
recommended_next:
  - trace-distillation
overlays:
  - tutor-mode
  - execution-mode
  - project-tracker
---

# Skill: Workflow Trace

## Purpose

Capture what happened during a meaningful work session so the work becomes durable project memory rather than disappearing into chat history.

This skill is for recording:

- goal
- context used
- steps taken
- decisions made
- files changed
- outcome
- reusable pattern

## When to Invoke

Invoke this skill:

- after a meaningful work session
- after a modeling or evaluation cycle
- before handing work to another person or agent
- when a session uncovered a reusable lesson

## Required Inputs

- session goal
- important context used
- summary of steps taken
- material decisions
- files changed or reviewed
- outcome

If the session produced no meaningful change, keep the trace minimal rather than inventing detail.

## Procedure

### Step 1: Record Goal

State the session goal in one or two lines.

### Step 2: Record Context Used

List the important files, artifacts, or prior decisions used during the session.

### Step 3: Record Steps Taken

Summarize the actual workflow steps taken rather than idealized steps.

### Step 4: Record Decisions

Capture the decisions that materially shaped the session outcome.

### Step 5: Record Files Changed

List files that were created, updated, or used as key evidence.

### Step 6: Record Outcome And Reusable Pattern

State:

- what the session achieved
- what remains open
- what reusable pattern, warning, or lesson should persist

## Expected Outputs

Produce a trace entry containing:

### 1. Goal

### 2. Context Used

### 3. Steps Taken

### 4. Decisions Made

### 5. Files Changed

### 6. Outcome

### 7. Reusable Pattern

## Common Failure Modes

- writing a vague narrative with no concrete decisions
- omitting files touched
- recording only successful work
- confusing a workflow trace with a polished report

## Guardrails

- Keep the trace factual.
- Record failures and dead ends when they matter.
- Do not rewrite history to make the workflow look cleaner than it was.
