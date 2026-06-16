---
name: lab-manager-agent
description: Maintain portfolio-level visibility across projects, people, deadlines, handoffs, and waiting-on dependencies. Use when a manager needs a short action-oriented weekly brief, portfolio dashboard update, or cross-project coordination view.
category: manager
status: active
stage: manager-ops
role_compatibility:
  - data science manager
inputs:
  - lab dashboard
  - active projects
  - people map
  - deadlines
  - waiting-on list
  - project state files
  - recent handoffs
outputs:
  - portfolio weekly brief
  - dashboard update
  - next-actions summary
artifacts:
  - weekly brief
  - waiting-on list
  - stale-project list
  - Walter next actions
  - approaching deadlines summary
depends_on:
  - project-setup
  - weekly-review
recommended_next:
  - stakeholder-update
human_review_required: true
---

# Skill: Lab Manager Agent

## Purpose

Coordinate the portfolio above the project level.

This skill turns many project artifacts into a short action-oriented management view. It should help a lab or data science manager see what needs attention without rereading every project from scratch.

## Inputs To Read

This skill should read from durable portfolio and project artifacts such as:

- `LAB_DASHBOARD.md`
- `ACTIVE_PROJECTS.md`
- `PEOPLE.md`
- `DEADLINES.md`
- `WAITING_ON.md`
- project `PROJECT_STATE.md` files
- recent `HANDOFF.md` files
- meeting notes if available
- email summaries if available

## What This Skill Should Produce

Produce short operational outputs such as:

- weekly brief
- waiting-on list
- stale projects
- Walter next actions
- approaching deadlines
- recommended focus blocks
- draft agendas
- draft follow-up emails

## When To Use

Use this skill when:

- a portfolio-level weekly review is needed
- many projects need to be summarized together
- a manager needs a current waiting-on view
- student or collaborator meetings need preparation
- priorities must be surfaced across multiple active projects

## Procedure

### Step 1: Read Portfolio State

Read the highest-value portfolio files first:

- active projects
- dashboard
- deadlines
- waiting-on dependencies

Then pull project-level evidence only where needed.

### Step 2: Check Project Freshness

Identify:

- stale project states
- missing handoffs
- unclear ownership
- deadlines with weak evidence

Do not smooth over missing project memory.

### Step 3: Synthesize The Portfolio

Answer the core management questions:

- What needs Walter?
- Who is waiting on Walter?
- Who is Walter waiting on?
- Which projects are stale?
- Which deadlines are approaching?

### Step 4: Draft Action-Oriented Outputs

Prefer short, operational sections over long prose.

The goal is prioritization, not narrative completeness.

### Step 5: Draft, Do Not Send

The skill may draft agendas and follow-up emails, but external communication remains human-approved.

## Guardrails

- Do not replace project-level scientific review.
- Do not infer claims without project evidence.
- Do not send communication autonomously.
- Do not hide stale or missing project state behind generic summaries.

## Escalation Conditions

Stop and escalate if:

- portfolio priorities conflict and require explicit human choice
- deadlines or owners are unclear
- key project artifacts are stale enough to make the summary misleading
- a communication draft would carry material risk without review
