---
name: core-ml
description: A lightweight skill pack for basic supervised ML workflows done with explicit artifacts, leakage checks, baseline models, evaluation discipline, and reproducibility expectations.
category: data-science
status: active
stage: modeling
role_compatibility:
  - student
  - data scientist
  - data science manager
inputs:
  - problem framing artifact
  - data card or data audit artifact
  - analysis plan
outputs:
  - workflow selection guidance
  - core checks
  - evaluation and model card scaffolds
artifacts:
  - regression workflow plan
  - classification workflow plan
  - leakage review notes
  - metric alignment notes
  - evaluation report
  - model card
depends_on:
  - problem-framing
  - data-audit
  - eda-plan
recommended_next:
  - modeling
  - model-evaluation
---

# Skill Pack: Core ML

## Purpose

`core-ml` is the first repo-native pack for common supervised learning workflows.

It is meant to support "basic ML, done right":

- reproducible
- scaffolded
- artifact-producing
- usable in both learning and execution modes

This pack is not a textbook replacement. It is a workflow-oriented adapter for common ML project decisions inside the Codex Batman backbone.

## What This Pack Contains

### Workflow Guides

- `workflows/regression.md`
- `workflows/binary-classification.md`
- `workflows/multiclass-classification.md`

### Checks

- `checks/leakage-check.md`
- `checks/split-validity-check.md`
- `checks/metric-alignment-check.md`

### Templates

- `templates/model-card.md`
- `templates/evaluation-report.md`

## When To Use This Pack

Use this pack when a project needs a lightweight, defensible supervised ML workflow with explicit checks around:

- target definition
- unit of analysis
- prediction time
- train/test design
- leakage
- baselines
- model comparison
- evaluation metrics
- calibration when relevant
- model card production

## Pack Rules

1. Start with the problem frame, not the algorithm.
2. Define the target and prediction time before choosing metrics.
3. Check split validity before comparing models.
4. Document leakage risks explicitly.
5. Fit a baseline model before advancing to more complex methods.
6. Record outcomes in reproducible artifacts.

## Relationship To Existing Skills

This pack does not replace:

- `problem-framing`
- `data-audit`
- `eda-plan`
- `modeling`
- `model-evaluation`
- `experiment-log`

It supports those skills by adding a reusable supervised-ML operating layer.
