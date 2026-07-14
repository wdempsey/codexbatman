---
name: project-setup
description: Set up the manager operating layer for a research or data science project. Use when a project needs a project-specific config with team roster, source keywords, decision log rules, and a living Research Design and Progress document before weekly reviews, project-manager updates, or stakeholder communication.
category: manager
status: active
stage: manager-ops
role_compatibility:
  - data science manager
inputs:
  - project charter
  - team context
  - source systems and keywords
  - timeline constraints
outputs:
  - project operating setup
  - project-specific config
  - Research Design and Progress document outline
artifacts:
  - project setup plan
  - roles and owners map
  - decision log protocol
  - cadence and checkpoints
source_attribution:
  - "Adapted from Chris Blattman's /setup-project-management pattern; rewritten as a Codex Batman manager workflow skill."
recommended_next:
  - weekly-review
  - project-manager-agent
  - stakeholder-update
human_review_required: true
---

# Skill: Project Setup

## Purpose

Create the foundation for project-centered management work.

This skill owns the manager operating layer around a research or data science
project. It formalizes:

- project-specific configuration
- team roster, owners, and review cadence
- source aliases, keywords, and system map
- decision log rules
- the living Research Design and Progress document
- external system links
- readiness for weekly review and downstream reporting

Use this before recurring review or coordination workflows. It does not replace
`project-bootstrap`, `problem-framing`, `data-audit`, `experiment-log`, or other
data-science workflow gates.

## When to Use

Use this skill when:

- a project has no coherent operating structure
- context is scattered across email, docs, drives, and notes
- decisions are being made in chat but not preserved in project artifacts
- a user wants a project hub or dashboard foundation
- weekly review, project-manager, or stakeholder-update cannot run because
  inputs are not organized

## Required Inputs

- Project root or intended workspace
- Project name and type
- Known collaborators and roles
- Core systems in use: docs, email, storage, chat, transcripts
- Project aliases, search terms, and source-specific keywords
- Existing source-of-truth docs, if any
- Constraints on sensitive data or access

If the user has not provided these, inspect the workspace first and then ask only for missing critical facts.

## Procedure

### Step 1: Assess Current State

Inspect the existing project structure before proposing changes.

Capture:

- current folders and naming conventions
- existing project instructions or config
- current source-of-truth documents
- current transcript, meeting note, and reporting habits
- known team members, owners, and decision makers
- known project aliases and source keywords
- potential conflicts with a new structure

### Step 2: Define the Minimum Operating Layer

Propose the smallest viable setup that enables:

- project memory
- meeting capture
- weekly synthesis
- stakeholder communication

Preserve working structures. Add only what is missing.

### Step 3: Draft the Project-Specific Config

Define a config that later manager skills can read before acting.

Include:

- project name, aliases, and short description
- team roster with roles, ownership, decision authority, and contact channels
- source map: docs, folders, inboxes, calendars, transcript tools, data locations
- source keywords: include terms, exclude terms, sender/channel hints, and ambiguous aliases
- decision log rules: where decisions live, what fields to record, who approves them
- update cadence and output destinations
- sensitive-data and access constraints

The config can be a project instruction file, a section in the project hub, or a
small local markdown file. Prefer the form that fits the existing project.

### Step 4: Establish the Research Design and Progress Document

Make the living Research Design and Progress document the core manager artifact
for research projects. For non-research data science projects, adapt the title
while preserving the function: one durable document that holds design context,
progress, decisions, and open questions.

At minimum, define sections for:

- project state and last-updated metadata
- strategic orientation or north star
- current research/design or analysis plan
- data, measurement, and workflow-gate status
- team roster and responsibilities
- decision log or change log with date, source, owner, and impact
- blockers, risks, open questions, and next checkpoints

Decisions discovered during setup must be recorded in this document or in the
linked decision log. Do not leave them only in chat.

### Step 5: Specify Core Artifacts

Define the artifacts the project needs. Usually:

- project instruction file
- project index or hub
- Research Design and Progress document
- transcript location
- weekly review output location
- decision log or change log
- dashboard or status document

For each artifact, state:

- purpose
- location
- owner
- update cadence

### Step 6: Map External Systems

Document how the project connects to:

- email
- calendar
- shared docs
- storage
- messaging platforms
- transcript tools

Do not assume every system is required. Only map the systems the project actually uses.

### Step 7: Produce an Implementation Plan

Give a concrete setup plan with:

- folders to create
- files to create
- files to leave unchanged
- manual dependencies
- blockers or open questions

If asked to implement, make additive changes only after the user confirms the
plan. If implementation reveals new decisions, record them in the Research
Design and Progress document or decision log.

## Output Format

Produce:

### 1. Current State

### 2. Gaps

### 3. Proposed Operating Layer

### 4. Project-Specific Config

### 5. Research Design and Progress Document

### 6. Core Artifacts

### 7. External System Map

### 8. Implementation Plan

### 9. Risks and Open Questions

### 10. Handoff to Weekly Review or Project Manager Agent

## Guardrails

- Do not reorganize existing folders without approval.
- Do not invent integrations the user does not have.
- Do not treat setup as complete if source-of-truth documents are undefined.
- Do not let manager summaries replace required data-science workflow gates.
- Do not leave decisions only in chat when a project artifact exists.
- Do not move sensitive files unless explicitly instructed.

## Escalation Conditions

Stop and require confirmation if:

- multiple competing folder structures exist
- sensitive data handling is unclear
- the proposed structure would overwrite existing project conventions
- required external systems are missing or inaccessible
- decision authority or project ownership is unclear
- the user asks to advance analysis before required workflow gates exist
