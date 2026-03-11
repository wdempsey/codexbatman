---
name: hint-ladder
description: Provide progressive hints for a student task by wrapping an existing skill or workflow. Use when the student should receive the smallest helpful hint first, with stronger hints only if needed.
---

# Skill: Hint Ladder

## Purpose

Deliver help in increasing levels of specificity.

This overlay prevents premature answer disclosure by using staged hints.

## When to Use

Use this overlay when:

- a student is stuck on a defined task
- the goal is guided progress
- one-shot answers would short-circuit learning

## How It Wraps Existing Skills

Choose the relevant base skill, then translate its next required step into a hint ladder.

The underlying workflow stays the same. Only the disclosure policy changes.

## Hint Levels

### Level 1

Orientation:

- restate the goal
- identify the relevant concept or subproblem

### Level 2

Strategic hint:

- suggest the next reasoning move
- narrow the search space

### Level 3

Structural hint:

- provide a template, outline, or partial setup

### Level 4

Near-solution hint:

- show the key inference or missing bridge without fully finishing

Only give the next level after the student responds or explicitly asks.

## Procedure

1. Identify the underlying task and base skill.
2. Determine the student’s current blockage.
3. Start at the lowest useful hint level.
4. Escalate only as needed.
5. After each hint, ask the student to attempt the next move.

## Output Format

Produce:

### 1. Underlying Skill or Workflow

### 2. Student Block

### 3. Current Hint Level

### 4. Hint

### 5. Student Next Move

## Guardrails

- Do not jump to Level 4 unless lower levels failed.
- Do not give a hidden full solution disguised as a hint.
- Do not keep escalating if the real issue is a misconception.

## Escalation Conditions

Switch to `misconception-diagnosis` if the student’s attempts show conceptual confusion rather than simple blockage.
