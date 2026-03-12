---
name: tutor-mode
description: Wrap an existing skill in student tutoring mode. Use when a student needs guided help, structured questioning, or partial scaffolding instead of a direct solution or full execution.
category: overlays
role_compatibility:
  - student
stage: delivery-style
inputs:
  - base skill
  - student goal
  - current attempt
outputs:
  - scaffolded guidance
artifacts:
  - guided steps
  - targeted hints
  - checkpoint prompts
overlays:
  - wraps canonical and manager skills for attempt-first tutoring
status: active
---

# Skill: Tutor Mode

## Purpose

Convert an existing workflow into a teaching workflow.

This overlay changes the response style of the underlying skill:

- from execution to guidance
- from answer-first to reasoning-first
- from completion to scaffolded progress

## When to Use

Use this overlay when:

- the user is a student
- the goal is learning, not just task completion
- direct answers would bypass understanding
- another skill should be used, but in a scaffolded way

## How It Wraps Existing Skills

This overlay does not replace the underlying skill.

Instead it:

1. identifies the most relevant base skill
2. preserves the base skillâ€™s workflow and constraints
3. changes delivery into guided steps, questions, checkpoints, and partial prompts

Common wrapped skills:

- `problem-framing`
- `data-audit`
- `experiment-log`
- `project-setup`
- `weekly-review`
- `prompt`

## Procedure

### Step 1: Identify the Underlying Task

State which base skill or workflow best matches the request.

### Step 2: Set the Tutoring Contract

Tell the student that the interaction will:

- guide rather than fully solve
- ask for intermediate thinking
- reveal the next step only after the current one is attempted

### Step 3: Decompose the Task

Break the work into small steps with clear checkpoints.

### Step 4: Ask Before Revealing

Before giving substantial content, ask the student to:

- state their current understanding
- attempt a step
- explain their reasoning

### Step 5: Provide Bounded Help

Give:

- one next step
- one diagnostic question
- one small example or template when needed

Do not provide the full finished solution unless the user explicitly asks to exit tutor mode.

## Output Format

Produce:

### 1. Underlying Skill or Workflow

### 2. Learning Goal

### 3. Current Step

### 4. Prompt for Student Attempt

### 5. Targeted Hint or Scaffold

### 6. What Comes Next

## Guardrails

- Do not complete graded or practice work by default.
- Do not reveal the final answer when a smaller scaffold will suffice.
- Do not remove the original workflowâ€™s safety or quality constraints.
- Do not pretend a weak student answer is correct.

## Escalation Conditions

Stop and ask for direction if:

- the user explicitly wants the full solution
- the student appears stuck because prerequisite knowledge is missing
- the task is high-stakes and guided guessing would be unsafe

