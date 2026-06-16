---
description: Minimal data science project template for Backbone Protocol v0.1.
---

# Project Template

This project template is the preferred starting point for a new Backbone Protocol v0.1 project.

It is intentionally simple:

- markdown-first
- human-readable
- agent-readable
- additive
- easy to adapt to an existing repository

## Template Location

Template root:

[`templates/ds-project/`](https://github.com/wdempsey/codexbatman/tree/main/templates/ds-project)

## Template Structure

```text
templates/ds-project/
  AGENTS.md
  PROJECT_STATE.md
  project.yaml
  analysis/
    problem_frame.md
    analysis_plan.md
    decision_log.md
  data/
    data_card.md
  runs/
    experiment_log.md
  reports/
    model_card.md
  memory/
    workflow_trace.md
```

## Why This Template Exists

The Backbone Protocol defines the minimum artifact system. This template turns that protocol into a concrete starting layout.

The template is useful when you want:

- a clean starting point for a new project
- a canonical place for backbone artifacts
- a folder structure that future agents can understand quickly
- a project memory layer that survives beyond one session

## What `project.yaml` Does

`project.yaml` is a light metadata file for the project.

It defines:

- workflow identity
- default role mode
- skill pack expectations
- required artifacts
- core workflow gates

It is not a full schema system. It is a small declaration file that helps keep the backbone legible.

## How To Use The Template

Recommended approach:

1. Copy the template into a new project folder.
2. Fill in `PROJECT_STATE.md` and `analysis/problem_frame.md` first.
3. Adapt folder names only if the local repository already has strong conventions.
4. Keep the artifacts even if you embed them into an existing repository structure.

## Adaptation Rule

Do not treat this template as permission to reorganize an existing project aggressively.

Preferred behavior:

- map the backbone onto the existing repository when possible
- preserve working conventions
- add missing artifacts without broad structural churn

## Related Pages

- [Backbone Protocol](index.md)
- [Artifacts](artifacts.md)
- [Tooling Stack](../tooling/index.md)
