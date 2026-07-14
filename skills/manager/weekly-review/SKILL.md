---
name: weekly-review
description: Produce a file-and-transcript-based weekly review for a research or data science project. Use after project-setup when a manager needs project docs and meeting transcripts synthesized into a three-page overview with strategic reminder, near-term imperatives, per-person priorities, and a weekly history update.
category: manager
status: active
stage: manager-ops
role_compatibility:
  - data science manager
inputs:
  - project-specific config
  - Research Design and Progress document
  - project docs
  - meeting transcripts
  - experiment logs
outputs:
  - three-page project overview
  - weekly history entry
  - per-person priorities
artifacts:
  - project overview update
  - weekly history tab update
  - risk register update
  - owner action list
depends_on:
  - project-setup
source_attribution:
  - "Adapted from Chris Blattman's /weekly-review pattern; rewritten as a Codex Batman manager workflow skill."
recommended_next:
  - project-manager-agent
  - stakeholder-update
human_review_required: true
---

# Skill: Weekly Review

## Purpose

Generate a project-centered weekly synthesis from project files and meeting
transcripts.

This skill uses the `project-setup` operating layer to turn the latest project
docs, Research Design and Progress document, meeting transcripts, and local
status artifacts into:

- a manager-ready three-page overview
- a strategic reminder grounded in the project north star
- near-term imperatives, blockers, and decisions
- per-person priorities
- a weekly history entry appended to the project history tab or section
- a durable weekly record

This is a recurring manager workflow. It does not replace data-science workflow
gates or approve analysis to advance.

## When to Use

Use this skill when:

- a project needs a weekly status review
- a manager needs meeting prep from the last review period
- the project overview or history tab needs an update
- the user wants a synthesis across project docs and meeting transcripts
- the team needs person-by-person priorities for the coming week

## Required Inputs

- Project instruction file or equivalent project config
- Research Design and Progress document or equivalent project hub
- Review period
- Access to relevant project docs and meeting transcript files
- Team roster and source keywords from project setup
- Current overview, dashboard, or weekly history baseline

At minimum, identify:

- project objectives
- source locations
- transcript location
- prior review or current dashboard baseline

## Procedure

### Step 1: Read Project Context and Preconditions

Read the project configuration, Research Design and Progress document, and
current overview/history baseline. Identify:

- project name
- strategic north star or current objectives
- team roster and roles
- source keywords and source map
- output destinations
- weekly history convention
- sensitive-content constraints

If the project lacks a usable configuration, Research Design and Progress
document, source map, or team roster, stop and recommend `project-setup`.

### Step 2: Define the Review Window

Use the most recent weekly history entry if present. Otherwise choose a
reasonable default window and state it explicitly.

If the user provides a review period, use it.

### Step 3: Gather File and Transcript Sources

Collect only sources relevant to the review window and source keywords:

- Research Design and Progress document
- current project overview, dashboard, or prior weekly history
- project docs changed during the review window
- meeting transcripts or notes
- experiment logs, workflow traces, or decision logs if they exist
- local email, chat, or calendar summaries only if already available

Do not require live email, WhatsApp, or calendar integrations for this PR-12
workflow. Record any unavailable or skipped sources.

### Step 4: Verify Important Claims and Filter Sensitive Material

Before writing the review:

- check quantitative claims against the strongest available source
- distinguish decisions from discussion, proposals, and unresolved questions
- flag claims that are unsupported, stale, or contradictory
- exclude sensitive personnel, compensation, hiring, or private performance material from broadly shared outputs
- preserve data-science workflow gates as gates, not manager impressions

If a claim cannot be verified, label it as uncertain rather than asserting it.

### Step 5: Draft the Three-Page Overview

Produce a concise manager-ready overview. Aim for the equivalent of three pages,
not a transcript dump.

Use these sections:

1. **Strategic Reminder**
   - north star or project purpose
   - current phase and major progress since the last review
   - research/design or analysis-plan changes
   - workflow-gate status and any human-review needs

2. **Near-Term Imperatives**
   - decisions due soon
   - blockers and risks
   - deadlines and milestones
   - items needing escalation

3. **Per-Person Priorities**
   - each owner
   - actions due before the next review
   - dependency or decision needed
   - evidence source or confidence note

Organize around strategic priorities and owners, not chronology alone.

### Step 6: Draft the Weekly History Entry

Append a weekly summary to the project history tab or section. If the existing
project uses newest-first history, preserve that convention while making the
update explicit.

Include:

- review window
- sources read and sources missing
- concise activity summary
- decisions made, with owner and source
- design or analysis changes to reflect in Research Design and Progress
- owner actions and deadlines
- unresolved questions, blockers, and confidence notes

### Step 7: Update Project Artifacts or Return a Patch Plan

If asked to write files, update only the configured project artifacts. Preserve
existing sections unless new evidence supersedes them.

Preferred update targets:

- project overview/dashboard
- weekly history tab or section
- Research Design and Progress change log for design or decision changes
- risk register or owner action list if configured

If the destination is a Google Doc, live external system, or missing required
markers/sections, stop and return the exact update text plus the manual or
integration step needed. PR-13 owns scheduled/live integration behavior.

### Step 8: Extract Handoffs

Identify:

- decisions made
- owners
- deadlines or next checkpoints
- blockers
- items needing escalation
- follow-up work for `project-manager-agent` or `stakeholder-update`

## Output Format

Produce:

### 1. Review Window

### 2. Source Coverage

### 3. Three-Page Overview

#### Strategic Reminder

#### Near-Term Imperatives

#### Per-Person Priorities

### 4. Weekly History Entry

### 5. Artifact Updates or Patch Plan

### 6. Decisions, Risks, and Blockers

### 7. Handoff to Project Manager or Stakeholder Update

### 8. Missing Data or Confidence Notes

## Guardrails

- Do not overwrite the prior dashboard blindly; treat it as a living baseline.
- Do not include sensitive personnel commentary in a broadly shared review.
- Do not rely on one source when higher-quality evidence is available.
- Do not use generic status language without project-specific facts.
- Do not produce a raw chronological transcript summary as the final review.
- Do not imply full source coverage when sources were missing.
- Do not use live scheduled integrations or outbound actions in this skill; route those to PR-13 integration work.
- Do not let manager summaries override `problem-framing`, `data-audit`, `experiment-log`, or model-card requirements.

## Escalation Conditions

Stop and ask for direction if:

- the project config is missing
- the Research Design and Progress document or weekly history destination is missing
- source coverage is too weak for a credible review
- sensitive content may be inappropriate for the intended audience
- there are conflicting facts across key sources
- the user asks for scheduled filing, live email/calendar pulls, or outbound actions
