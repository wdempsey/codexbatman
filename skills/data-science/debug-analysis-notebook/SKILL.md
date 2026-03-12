---
name: debug-analysis-notebook
description: Debug analytical notebooks without uncontrolled rewrites. Use when analysis outputs are inconsistent or broken and the team needs a structured diagnosis of logic, leakage, shape, split, and metric issues.
category: data-science
role_compatibility:
  - data scientist
  - data science manager
stage: debugging
inputs:
  - notebook path
  - error traces
  - expected behavior
  - dataset and split assumptions
  - recent changes
outputs:
  - debug diagnosis
  - minimal fix plan
artifacts:
  - symptom summary
  - reproduction steps
  - root cause analysis
  - minimal fix list
  - verification plan
depends_on:
  - data-audit
  - modeling
recommended_next:
  - experiment-log
  - model-evaluation
overlays:
  - practitioner/execution-mode
  - practitioner/artifact-enforcer
status: near-canonical
---

# Skill: Debug Analysis Notebook

## Purpose

Diagnose notebook failures systematically without silently rewriting the full analysis.

This skill isolates and documents root causes across logic, data pipeline, and evaluation layers.

It prevents:

- destructive notebook rewrites
- silent leakage introduction during fixes
- train/test contamination
- shape and indexing errors hidden by quick patches
- metric/plot inconsistencies going undocumented

## When to Invoke

Invoke this skill:

- when notebook results are inconsistent or failing
- when metrics change unexpectedly after edits
- when data-shape or merge issues appear
- before accepting a major notebook rewrite

## Required Inputs

- Notebook path or equivalent script
- Error messages or anomalous outputs
- Expected behavior/target result
- Dataset version and split assumptions
- Recent change summary (if available)

If failure context is missing, request minimal reproducible context first.

## Expected Outputs

Produce a debugging artifact with:

### 1. Symptom Summary

### 2. Reproduction Steps

### 3. Root Cause Analysis

### 4. Proposed Minimal Fixes

### 5. Leakage/Contamination Checks

### 6. Verification Plan

## Artifact Checklist

- Symptoms and failure conditions documented
- Reproduction path documented
- Root cause hypothesis tied to evidence
- Minimal patch strategy proposed
- Leakage and split integrity checked
- Metric/plot consistency checks included
- Post-fix verification plan listed

## Common Failure Modes

- rewriting entire notebook instead of isolating fault
- fixing syntax but missing logic error
- patching data shapes without checking join semantics
- ignoring split contamination during debug
- accepting metric shifts without explanation

## Proceed / Halt Guidance

Proceed with fix if:

- root cause is evidenced
- minimal change resolves targeted failure
- leakage/split checks remain valid

Halt and escalate if:

- root cause is ambiguous after reasonable isolation
- fix requires architectural changes beyond notebook scope
- contamination/leakage risk remains unresolved

