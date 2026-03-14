---
name: paper-to-replication
description: Convert a paper or empirical design into executable replication artifacts. Use when teams need a structured summary, data requirements map, replication plan, and implementation checklist.
category: data-science
status: active
stage: bootstrap
role_compatibility:
  - student
  - data scientist
inputs:
  - paper or methods text
  - appendices
  - code or data links
  - replication scope
outputs:
  - replication plan package
artifacts:
  - structured summary
  - data requirements
  - replication plan
  - implementation checklist
  - risks and unknowns
recommended_next:
  - project-bootstrap
  - problem-framing
  - data-audit
overlays:
  - tutor-mode
  - execution-mode
---

# Skill: Paper to Replication

## Purpose

Translate published empirical work into a reproducible implementation plan.

This skill converts narrative methods into explicit artifacts required for replication.

It prevents:

- ambiguous replication scope
- missing data dependencies
- hidden implementation assumptions
- premature coding without plan

## When to Invoke

Invoke this skill:

- when starting replication of a published paper
- when onboarding a new team member to an existing empirical design
- before writing replication code
- when preparing preregistered replication tasks

## Required Inputs

- Paper or method document
- Any appendices/supplemental methods
- Available code/data links (if any)
- Replication objective (exact, partial, extension)

If design details are missing, identify unknowns and stop short of false precision.

## Expected Outputs

Produce a replication package artifact with:

### 1. Structured Paper Summary

### 2. Data Requirements

### 3. Replication Plan

### 4. Implementation Checklist

### 5. Risks and Unknowns

## Artifact Checklist

- Research question and estimand extracted
- Sample construction and timing rules extracted
- Variables and transformations listed
- Data dependency map created
- Replication scope defined (exact/partial/extension)
- Stepwise implementation checklist created
- Unknowns and blockers explicitly listed

## Common Failure Modes

- summarizing paper without operational steps
- ignoring sample construction details
- omitting transformation definitions
- pretending missing details are known
- starting code before dependency map is complete

## Proceed / Halt Guidance

Proceed if:

- replication scope is defined
- data requirements and plan are actionable
- unknowns are bounded and tracked

Halt and escalate if:

- key design elements are underspecified
- required data access is unavailable
- estimand cannot be mapped to implementable steps

