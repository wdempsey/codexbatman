---
name: project-bootstrap
description: Initialize the artifact backbone for a Codex-native data science project before analysis begins. Use when a repository or workspace needs the core files, directories, and workflow anchors required for framing, audit, and experiment logging.
category: data-science
role_compatibility:
  - student
  - data scientist
  - data science manager
stage: bootstrap
order: 1
inputs:
  - project scope
  - repository context
  - tooling constraints
outputs:
  - bootstrap plan
  - workspace setup artifact
artifacts:
  - project bootstrap artifact
  - workspace conventions
recommended_next:
  - problem-framing
overlays:
  - student/tutor-mode
  - practitioner/execution-mode
  - practitioner/artifact-enforcer
status: canonical
---

# Skill: Project Bootstrap

## Purpose

Create the minimum viable artifact structure for a Codex-native data science workflow.

This skill establishes:

- a project root with explicit analysis boundaries
- locations for framing, audit, and experiment artifacts
- a clear distinction between raw inputs and derived work
- a repository state that later skills can rely on

This is a foundation skill. It does not perform analysis.

## When to Invoke

Invoke this skill when:

- a new analysis workspace is being created
- an existing repository lacks a coherent artifact structure
- later skills cannot run because required files or directories do not exist
- a project needs to be normalized to the repositoryâ€™s canonical workflow

## Required Inputs

- Project root or target workspace
- Project name or working title
- Known data sources or access methods
- Known constraints on storage, privacy, or reproducibility
- Existing repository conventions that must be preserved

If these are incomplete, inspect the workspace first and then surface only the blocking gaps.

## Procedure

### Step 1: Inspect Current State

Identify:

- existing directories and naming conventions
- existing analysis artifacts
- current handling of raw, processed, and derived outputs
- any conflicts with the canonical workflow backbone

### Step 2: Define the Minimum Backbone

Specify the smallest structure needed to support:

- problem framing
- data inventory and audit
- experiment logging
- reproducibility notes

Preserve working project conventions where possible.

### Step 3: Create or Propose Artifacts

Create or propose canonical placeholders for:

- project brief or instruction anchor
- framing artifact location
- audit artifact location
- experiment log location
- outputs directory for derived analysis artifacts

Do not create unnecessary scaffolding.

### Step 4: Record Workflow Assumptions

State:

- what counts as raw data
- what counts as processed data
- where analysis code should live
- where logs and reports should be written

### Step 5: Verify Readiness

Confirm the workspace is ready for `problem-framing`.

## Expected Outputs

- A bootstrap plan or implemented bootstrap structure
- A defined location for each canonical artifact
- A short readiness summary for downstream skills

## Artifact Checklist

- Project root identified
- Raw vs processed boundary documented
- Framing artifact path defined
- Audit artifact path defined
- Experiment log path defined
- Reproducibility notes path defined or reserved

## Common Failure Modes

- Creating a generic folder tree without inspecting the actual project
- Mixing raw and derived data paths
- Treating bootstrap as analysis
- Overwriting existing conventions without approval
- Leaving downstream artifact locations implicit

## Guardrails

- Do not move or rename user files without approval.
- Do not modify raw data.
- Do not invent infrastructure the repository does not use.
- Do not mark the workspace ready if canonical artifact paths are still ambiguous.

## Human Review Requirement

Human confirmation is required before any restructuring that changes existing project organization.

