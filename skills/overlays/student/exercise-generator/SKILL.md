---
name: exercise-generator
description: Generate practice exercises around an existing workflow or skill without solving the exercise. Use when a student needs targeted practice on framing, auditing, review, or project-structure reasoning.
category: overlays
role_compatibility:
  - student
stage: delivery-style
inputs:
  - base skill
  - learning objective
outputs:
  - practice exercises
artifacts:
  - exercise prompt
  - expected artifact type
  - self-check questions
overlays:
  - wraps workflows into bounded practice drills
status: active
---

# Skill: Exercise Generator

## Purpose

Create practice tasks that reinforce the logic of existing skills.

This overlay uses current workflows as teaching material and turns them into exercises.

## When to Use

Use this overlay when:

- a student wants practice before doing the real task
- an instructor or learner wants drills tied to repository workflows
- repeated exposure is needed without using the live project directly

## How It Wraps Existing Skills

Select an existing skill or workflow and generate exercises that rehearse:

- recognition
- decomposition
- judgment
- error detection
- structured output

Do not generate answer keys unless explicitly requested.

## Procedure

### Step 1: Select the Base Workflow

Choose the skill or phase being practiced.

### Step 2: Select the Learning Objective

Examples:

- identify objective type
- spot data leakage risk
- turn email into actions
- structure a stakeholder update

### Step 3: Generate Bounded Practice

Prefer short exercises with explicit constraints and deliverables.

### Step 4: Separate Prompt from Solution

If feedback is requested, provide evaluation criteria first, not the answer.

## Output Format

Produce:

### 1. Base Skill or Workflow

### 2. Learning Objective

### 3. Exercise Prompt

### 4. Expected Artifact Type

### 5. Self-Check Questions

### 6. Optional Instructor Rubric

## Guardrails

- Do not leak the full worked solution into the exercise prompt.
- Do not generate unrealistic exercises detached from the base workflow.
- Do not confuse practice generation with tutoring on the studentâ€™s live assignment.

## Escalation Conditions

If the student repeatedly fails the exercises for the same reason, switch to `misconception-diagnosis`.

