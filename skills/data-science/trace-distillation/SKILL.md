---
name: trace-distillation
description: Distill workflow traces into reusable lessons, checklist updates, prompt refinements, evaluation ideas, or skill and template improvements.
category: data-science
status: active
stage: evaluation
role_compatibility:
  - student
  - data scientist
  - data science manager
inputs:
  - workflow trace
  - outcomes
  - failure modes
outputs:
  - distillation summary
  - reusable improvement candidates
artifacts:
  - lessons learned
  - checklist update candidates
  - skill or template update candidates
depends_on:
  - workflow-trace
recommended_next:
  - project-bootstrap
  - problem-framing
  - modeling
---

# Skill: Trace Distillation

## Purpose

Turn workflow traces into reusable infrastructure candidates.

This skill exists to answer:

- What did we learn?
- What failed in a repeatable way?
- What should be promoted into a checklist, prompt, template, eval, or skill?

## When to Invoke

Invoke this skill:

- after a workflow trace is recorded
- after a recurring failure mode appears
- after a session reveals a reusable improvement opportunity
- before updating a skill, template, or process rule

## Required Inputs

- one or more workflow traces
- session outcome
- failure modes or friction points
- any relevant existing skill or template context

## Procedure

### Step 1: Extract Lessons Learned

State the practical lessons revealed by the trace.

### Step 2: Identify Failure Modes

Record recurring or avoidable errors such as:

- unclear gates
- missing artifacts
- weak prompts
- ambiguous decisions
- missing review checks

### Step 3: Propose Reusable Updates

Generate candidate improvements for:

- checklist updates
- prompt updates
- evaluation updates
- skill updates
- template updates

### Step 4: Keep Improvements Small

Prefer the smallest change that would prevent the problem or preserve the lesson.

## Expected Outputs

Produce a distillation summary containing:

### 1. Lessons Learned

### 2. Failure Modes

### 3. Candidate Checklist Updates

### 4. Candidate Prompt Updates

### 5. Candidate Eval Updates

### 6. Candidate Skill Or Template Updates

## Common Failure Modes

- turning one trace into an overgeneralized system rewrite
- recording vague lessons with no reusable implication
- proposing changes without linking them to a real failure mode

## Guardrails

- Prefer principles over narrative.
- Keep each lesson atomic and testable.
- Do not implement broad workflow changes unless the evidence supports them.
