---
name: inbox-triage
description: Triage project-relevant inbox activity into project memory, actions, waiting-fors, and meeting-prep inputs. Use when a manager needs email processed in project context rather than as isolated messages.
category: manager
status: active
stage: manager-ops
role_compatibility:
  - data science manager
inputs:
  - inbox sources
  - project context
  - triage policy
outputs:
  - triage decisions
  - priority queue
artifacts:
  - triage log
  - priority labels
  - follow-up queue
recommended_next:
  - project-setup
  - weekly-review
---

# Skill: Inbox Triage

## Purpose

Convert inbox activity into project management signals.

This skill treats email as an input to project memory, not the operating system itself.

## When to Use

Use this skill when:

- a user needs project-relevant email summarized
- inbox activity should be converted into actions or waiting-fors
- meeting preparation depends on recent email movement
- email threads need to be linked to project state

## Required Inputs

- Access to the relevant inbox or exported thread set
- Project names, aliases, or keywords
- Team roster or collaborator list when available
- Current project context or dashboard baseline

## Procedure

### Step 1: Frame the Triage Scope

Determine:

- which project or projects matter
- the date window
- whether the goal is full triage, meeting prep, or action extraction

### Step 2: Identify Project-Relevant Threads

Classify email using project context:

- direct project correspondence
- decisions or approvals
- blockers
- scheduling and logistics
- FYI or low-signal traffic

Ignore bulk mail and non-project noise unless the user asked for broad inbox processing.

### Step 3: Summarize by Thread, Not by Message

Preserve conversation context. Extract:

- what changed
- who owns the next move
- deadlines or timing cues
- unresolved questions

### Step 4: Route Outputs

Convert findings into:

- project memory updates
- action items
- waiting-for items
- candidate meeting prep notes
- draft reply prompts where useful

### Step 5: Flag Importance

Separate:

- urgent and decision-relevant items
- operational follow-ups
- background context

## Output Format

Produce:

### 1. Scope

### 2. Priority Threads

### 3. Actions

### 4. Waiting-Fors

### 5. Meeting Prep Inputs

### 6. Draft Reply Needs

### 7. Low-Signal or Deferred Items

## Guardrails

- Do not summarize each email independently when thread context matters.
- Do not confuse FYI messages with action items.
- Do not lose ownership or due-date information.
- Do not treat inbox processing as complete project review.

## Escalation Conditions

Stop and ask for clarification if:

- project assignment is ambiguous
- thread intent is unclear
- an email includes sensitive personnel or legal content
- the userâ€™s goal is unclear between triage, meeting prep, and drafting

