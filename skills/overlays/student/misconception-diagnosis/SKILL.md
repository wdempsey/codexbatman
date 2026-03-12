---
name: misconception-diagnosis
description: Diagnose why a student is stuck when working through an existing skill or workflow. Use when repeated errors suggest a conceptual misunderstanding rather than a missing hint.
category: overlays
role_compatibility:
  - student
stage: delivery-style
inputs:
  - student attempt
  - base skill standard
outputs:
  - conceptual diagnosis and repair prompt
artifacts:
  - misconception note
  - corrective contrast
  - revision prompt
overlays:
  - wraps base skills for conceptual error diagnosis
status: active
---

# Skill: Misconception Diagnosis

## Purpose

Identify the conceptual error blocking progress.

This overlay is for teaching moments where the studentâ€™s answer is wrong for a reason, and the reason matters more than the correction.

## When to Use

Use this overlay when:

- the student repeats the same type of error
- hinting has not worked
- the studentâ€™s reasoning reveals a conceptual misunderstanding
- the wrong answer would propagate through later workflow steps

## How It Wraps Existing Skills

Choose the relevant base skill, then inspect the studentâ€™s attempt against the logic of that workflow.

Focus on diagnosing:

- what they misunderstood
- why that misunderstanding is plausible
- what contrast or correction would repair it

## Procedure

### Step 1: Identify the Workflow Step

Name the specific step or artifact the student is failing on.

### Step 2: Compare Attempt to Expected Logic

Check the studentâ€™s reasoning against the workflowâ€™s actual standard.

### Step 3: Name the Misconception

State the misconception in plain language.

### Step 4: Contrast Correct vs Incorrect Reasoning

Show the difference without simply replacing the studentâ€™s work.

### Step 5: Give a Repair Prompt

Ask the student to revise one piece of reasoning or one artifact section.

## Output Format

Produce:

### 1. Underlying Skill or Workflow

### 2. Observed Student Reasoning

### 3. Likely Misconception

### 4. Why It Leads to Error

### 5. Corrective Contrast

### 6. Student Revision Prompt

## Guardrails

- Do not label the student as confused without naming the actual confusion.
- Do not give only the right answer; explain the conceptual gap.
- Do not over-diagnose when the issue is just incomplete effort.

## Escalation Conditions

If the student lacks prerequisite knowledge entirely, say so directly and recommend stepping back to `tutor-mode` or a simpler exercise.

