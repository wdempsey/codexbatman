---
name: communication-workflows
description: Wrap workflow artifacts into manager-facing email, meeting, and stakeholder communication workflows. Use when a data science manager needs communication support grounded in existing project and analysis artifacts.
category: overlays
status: active
stage: overlay
role_compatibility:
  - data science manager
overlays:
  - weekly-review
  - stakeholder-update
  - result-communication
  - model-evaluation
---

# Skill: Communication Workflows

## Purpose

Connect workflow artifacts to managerial communication work.

This overlay is for:

- meeting preparation
- recap notes
- stakeholder updates
- project-linked email workflows

## When to Use

Use this overlay when:

- meetings or email need to reflect the latest workflow state
- a manager needs communication support without redoing the analysis
- project artifacts need to be translated into operational communication

## How It Wraps Existing Skills

This overlay wraps:

- canonical workflow artifacts
- `inbox-triage`
- `weekly-review`
- `stakeholder-update`

It preserves their logic and turns them into communication-ready outputs.

## Procedure

### Step 1: Identify the communication task

Determine whether the task is:

- meeting prep
- follow-up note
- stakeholder email
- project update

### Step 2: Pull the relevant artifact state

Use the latest available artifacts rather than conversational memory.

### Step 3: Produce communication outputs

Focus on:

- recent changes
- decisions
- open questions
- owners
- timing

## Output Format

Produce:

### 1. Communication Task

### 2. Source Artifacts

### 3. Key Points

### 4. Draft or Structured Notes

### 5. Open Questions or Follow-Ups

## Guardrails

- Do not draft communications detached from current artifacts.
- Do not expose sensitive internal detail to the wrong audience.
- Do not confuse meeting prep with full project review.

## Escalation Conditions

Escalate if the communication task requires artifact state that is missing, stale, or audience-sensitive.

