---
name: weekly-review
description: Produce a project-centered weekly review for a data science or research project by synthesizing transcripts, email, documents, and prior status artifacts into a dashboard, log, and action summary.
---

# Skill: Weekly Review

## Purpose

Generate a project-centered weekly synthesis.

This skill turns scattered operational signals into:

- current project status
- progress against strategic objectives
- open risks and blockers
- team actions
- a durable weekly record

## When to Use

Use this skill when:

- a project needs a weekly status review
- a manager needs meeting prep from the last review period
- the team needs a shared dashboard or log update
- the user wants a synthesis across transcripts, email, and documents

## Required Inputs

- Project instruction file or equivalent project config
- Review period
- Access to the relevant local artifacts
- Known source systems if they contribute context

At minimum, identify:

- project objectives
- source locations
- prior review or current dashboard baseline

## Procedure

### Step 1: Read Project Context

Read the project configuration and identify:

- project name
- core objectives
- collaborators
- relevant sources
- output destinations

If the project lacks a usable configuration, stop and recommend `project-setup`.

### Step 2: Define the Review Window

Use the most recent review if present. Otherwise choose a reasonable default window and state it explicitly.

### Step 3: Gather Source Material

Collect only sources relevant to the review window:

- meeting transcripts or notes
- project email threads
- working documents
- prior dashboard or status notes
- messaging summaries if available

Record any missing or unavailable sources.

### Step 4: Verify Important Claims

Before writing the review, check quantitative claims against the strongest available source.

If a claim cannot be verified, label it as uncertain rather than asserting it.

### Step 5: Synthesize at Two Levels

Produce:

- a high-level dashboard view
- a detailed weekly log

Organize around strategic priorities, not chronology alone.

### Step 6: Extract Actions and Risks

Identify:

- decisions made
- owners
- deadlines or next checkpoints
- blockers
- items needing escalation

### Step 7: Save or Update Outputs

If asked to write files, update the project’s designated review artifacts. Otherwise return the review in a structured draft.

## Output Format

Produce:

### 1. Review Window

### 2. Source Coverage

### 3. Dashboard Summary

### 4. Progress by Objective

### 5. Decisions and Changes

### 6. Team Actions

### 7. Risks and Blockers

### 8. Detailed Weekly Log

### 9. Missing Data or Confidence Notes

## Guardrails

- Do not overwrite the prior dashboard blindly; treat it as a living baseline.
- Do not include sensitive personnel commentary in a broadly shared review.
- Do not rely on one source when higher-quality evidence is available.
- Do not use generic status language without project-specific facts.

## Escalation Conditions

Stop and ask for direction if:

- the project config is missing
- source coverage is too weak for a credible review
- sensitive content may be inappropriate for the intended audience
- there are conflicting facts across key sources
