---
name: meeting-pre-brief
description: Prepare a manager for a project meeting from existing project artifacts. Use after project-setup when a manager needs agenda context, open decisions, risks, and owner-specific prompts before a meeting; do not use for live calendar pulls or scheduled automation.
category: manager
status: active
stage: manager-communication
role_compatibility:
  - data science manager
inputs:
  - project-specific config
  - Research Design and Progress document
  - latest weekly review
  - meeting agenda or calendar summary
outputs:
  - meeting pre-brief
  - agenda risks
  - decision prompts
artifacts:
  - meeting prep note
depends_on:
  - project-setup
recommended_next:
  - meeting-post-brief
human_review_required: true
---

# Skill: Meeting Pre-Brief

## Purpose

Prepare a manager for a project meeting from durable project artifacts.

This skill is the reasoning side of the meeting loop. It turns the latest
project state, Research Design and Progress document, weekly review, and agenda
or calendar summary into a short meeting prep note.

It does not fetch live calendar data, send invitations, file emails, or schedule
automation. Those belong to the n8n integration layer.

## When to Use

Use this skill when:

- a manager has an upcoming project meeting
- the meeting needs agenda context grounded in project artifacts
- the manager needs open decisions, blockers, and owner-specific questions
- a calendar digest has already been prepared by a human or integration layer

## Required Inputs

- Project config or project folder
- Research Design and Progress document or equivalent project hub
- Latest weekly review or project manager state
- Meeting title, date, attendees, and agenda if available
- Sensitive-meeting flag or audience constraints

If the project setup artifacts are missing, stop and recommend `project-setup`.

## Procedure

### Step 1: Check Meeting Eligibility

Do not prepare a broad pre-brief for meetings involving:

- personnel performance, hiring, firing, compensation, or health
- legal, disciplinary, or confidential institutional matters
- sensitive student feedback not intended for project artifacts
- private strategy that should not enter shared project memory

If sensitive status is unclear, ask before proceeding.

### Step 2: Read Authoritative Context

Read the strongest available project artifacts first:

- project config and team roster
- Research Design and Progress document
- latest weekly review
- project manager state, decisions, and next actions
- relevant handoffs, experiment logs, or stakeholder updates

Do not rely on chat memory if current artifacts exist.

### Step 3: Build the Meeting Frame

Identify:

- meeting purpose
- current project phase
- strategic north star or decision context
- decisions that may be needed in the meeting
- blockers, stale items, and unresolved risks
- owner-specific questions or follow-ups

### Step 4: Draft the Pre-Brief

Keep the pre-brief short and operational.

Include:

- why the meeting matters
- current project status
- decisions or tradeoffs to surface
- questions by person or role
- risks, blockers, or sensitive topics to avoid
- artifacts to update after the meeting

### Step 5: Leave a Post-Meeting Capture Plan

Name what should be captured after the meeting:

- decisions made
- changed owners or deadlines
- design or analysis changes
- items for the Research Design and Progress document
- items for `meeting-post-brief`, `project-manager-agent`, or `weekly-review`

## Output Format

Produce:

### 1. Meeting Context

### 2. Strategic Reminder

### 3. Decisions and Tradeoffs to Surface

### 4. Questions by Person or Role

### 5. Risks, Blockers, and Sensitive Topics

### 6. Post-Meeting Capture Plan

## Guardrails

- Do not pull live calendar, email, or transcript data in this skill.
- Do not prepare sensitive personnel or legal meetings for broad project memory.
- Do not invent attendee commitments from stale artifacts.
- Do not treat meeting prep as a weekly review.
- Do not send messages or invitations.

## Escalation Conditions

Stop and ask for direction if:

- the meeting appears sensitive
- attendee list or meeting purpose is unclear
- project artifacts are missing or stale enough to mislead
- the manager needs live calendar/email access or scheduled automation
