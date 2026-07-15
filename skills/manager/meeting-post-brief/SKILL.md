---
name: meeting-post-brief
description: Turn meeting notes or transcripts into project-memory updates and follow-up drafts. Use after a project meeting when a manager needs decisions, owners, deadlines, and Research Design and Progress updates captured; do not use for autonomous sending or scheduled filing.
category: manager
status: active
stage: manager-communication
role_compatibility:
  - data science manager
inputs:
  - meeting notes or transcript
  - project-specific config
  - Research Design and Progress document
  - latest project state
outputs:
  - post-meeting summary
  - decision and action capture
  - follow-up draft package
artifacts:
  - meeting summary
  - decision log update
  - action list update
depends_on:
  - project-setup
recommended_next:
  - project-manager-agent
  - weekly-review
  - stakeholder-update
human_review_required: true
---

# Skill: Meeting Post-Brief

## Purpose

Convert meeting notes or transcripts into durable project memory.

This skill is the reasoning and drafting side after a meeting. It extracts
decisions, owners, deadlines, open questions, and project-state changes, then
prepares updates for the configured project artifacts.

It may draft follow-up messages, but it must not send, schedule, or file
anything through live systems. n8n owns scheduled or credentialed execution, and
a human approves outbound actions.

## When to Use

Use this skill when:

- a project meeting just ended
- meeting notes or transcripts need to be turned into project memory
- decisions or action items need owners and deadlines
- follow-up drafts are needed before a human sends them
- the Research Design and Progress document may need an update

## Required Inputs

- Meeting notes, transcript, or human summary
- Project config or project folder
- Research Design and Progress document or equivalent project hub
- Team roster and decision-log rules
- Intended audience for any follow-up drafts

If project setup artifacts are missing, stop and recommend `project-setup`.

## Procedure

### Step 1: Check Meeting Eligibility

Do not convert sensitive meetings into shared project memory when they involve:

- personnel performance, hiring, firing, compensation, or health
- legal, disciplinary, or confidential institutional matters
- sensitive student feedback not intended for project artifacts
- private strategy that should remain outside shared records

If sensitive status is unclear, ask before summarizing.

### Step 2: Classify Meeting Content

Separate:

- decisions made
- proposed ideas not yet decided
- action items with owners and deadlines
- blockers and risks
- design or analysis changes
- follow-up communications needed
- items that require human review before recording broadly

### Step 3: Reconcile Against Project Artifacts

Compare the meeting content with:

- Research Design and Progress document
- decision log or change log
- latest weekly review
- project manager state
- existing action list or waiting-on list

Flag contradictions, stale state, or missing approvals.

### Step 4: Draft Artifact Updates

Prepare updates for the configured artifacts:

- decision log or change log
- Research Design and Progress document
- project state or next actions
- weekly-review input notes
- risk register or blocker list

If asked to write local files, make additive updates only. If the target is a
Google Doc, live system, or scheduled workflow, return a patch plan for the
integration layer or human operator.

### Step 5: Draft Human-Reviewed Follow-Ups

When useful, draft follow-up messages with:

- recipient
- purpose
- facts being communicated
- ask or decision needed
- sensitivity level

Mark all outbound drafts as requiring human approval. Do not send them.

## Output Format

Produce:

### 1. Meeting Source and Sensitivity Check

### 2. Decisions Made

### 3. Actions, Owners, and Deadlines

### 4. Project Artifact Updates

### 5. Risks, Blockers, and Open Questions

### 6. Follow-Up Drafts Requiring Human Approval

### 7. Handoff to Project Manager Agent or Weekly Review

## Guardrails

- Do not send messages, file emails, update calendars, or run scheduled workflows.
- Do not record sensitive personnel/legal material in shared project artifacts.
- Do not treat discussion as a decision without evidence.
- Do not overwrite existing project state without reconciling contradictions.
- Do not let meeting notes override required data-science workflow gates.

## Escalation Conditions

Stop and ask for direction if:

- the meeting appears sensitive
- decisions conflict with existing project artifacts
- owner or deadline is unclear for a critical action
- outbound communication could create external commitments
- the user asks for autonomous sending, filing, or scheduled automation
