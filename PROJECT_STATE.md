# Project State - Codex-Native Data Science Operating System

## 1. Core Identity

This repository is a Codex-native data science operating system organized around:

- one shared workflow backbone
- three roles
- role-aware overlays
- explicit workflow gates
- reproducibility controls

## 2. Design Principles

The system is:

- thinking-first
- audit-driven
- artifact-producing
- documentation-enforced
- reproducibility-centered
- human-in-the-loop

## 3. Logging Status

- `planning.md` is the active operational log for current tasks and follow-ups
- `PROJECT_STATE.md` is the durable architecture snapshot
- `devlog/` is deferred unless explicitly implemented

## 3.5 Skill Intake Status

The skill library now has two intake-level sources of truth:

- `SKILL-STYLE.md` defines authoring style, trigger phrasing, progressive disclosure, verification, and deviation-log expectations.
- `CAPABILITY-MATRIX.md` assigns each current folder-based `SKILL.md` file to one default role x task-type cell and records overlap risks for future audits.

`skills/METADATA.md` remains the schema source of truth for frontmatter fields and allowed values.

## 4. Current Backbone Status

The canonical data-science backbone currently includes:

- `project-bootstrap`
- `problem-framing`
- `data-audit`
- `eda-plan`
- `modeling`
- `model-evaluation`
- `experiment-log`

The next layer of advanced AI-native skills is also present or emerging:

- `causal-design-check`
- `paper-to-replication`
- `debug-analysis-notebook`
- `result-communication`

## 5. Remaining Structural Tasks

- sync stale docs and config to current architecture
- tighten role entry pages into stronger operating lanes
- standardize metadata across folder-based skills
- expand manager examples and workflows
- mature student overlay behavior

The methods skill library is intentionally incremental. Its initial methods cover common supervised learning workflows, and additional method skills will be added gradually using trusted sources such as ISLP, ISLR-Python, and Hands-On Machine Learning (`handson-ml3`) as repo-native teaching adapters rather than chapter-summary imports.

## 6. Immediate Priority

stabilization and synchronization before major expansion. PR-1 adds the flow audit, `/ask-codexbatman` router, `site-voice` normalization, role-alias cleanup, and a lightweight eval scaffold. PR-2 defines the determinism boundary, adds the student skill-promotion lifecycle gate, and adds the project `.claude/CLAUDE.md` student-session config shim. PR-3 adds skill telemetry conventions, a runnable eval harness, held-out versus improvement eval splits, and the `/improve-skill` meta-skill. The next skill-system step is PR-4: `/grill-the-student`.
