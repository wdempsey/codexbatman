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
- `eda-hypothesis-journal`
- `plan-as-guidance`
- `reproducibility-capture`
- `result-communication`

## 5. Remaining Structural Tasks

- sync stale docs and config to current architecture
- tighten role entry pages into stronger operating lanes
- standardize metadata across folder-based skills
- expand manager examples and workflows
- mature student overlay behavior

The methods skill library is intentionally incremental. Its initial methods cover common supervised learning workflows, and additional method skills will be added gradually using trusted sources such as ISLP, ISLR-Python, and Hands-On Machine Learning (`handson-ml3`) as repo-native teaching adapters rather than chapter-summary imports.

## 6. Immediate Priority

stabilization and synchronization before major expansion. PR-1 adds the flow audit, `/ask-codexbatman` router, `site-voice` normalization, role-alias cleanup, and a lightweight eval scaffold. PR-2 defines the determinism boundary, adds the student skill-promotion lifecycle gate, and adds the project `.claude/CLAUDE.md` student-session config shim. PR-3 adds skill telemetry conventions, a runnable eval harness, held-out versus improvement eval splits, and the `/improve-skill` meta-skill. PR-4 records the skill admission/pruning policy and adds `/grill-the-student` as a narrow pre-answer alignment overlay. PR-5 adds class-notes ingestion for persistent `NOTATION.md` and `COURSE-CONTEXT.md` student context. PR-6 refines the existing `misconception-diagnosis` skill around the reproduce, localize, counterexample, repair-check loop and mastery evidence records. PR-7 adds worked case studies for students bringing class notes, including Survival RAG, problem-set alignment, seeded note errors, and simulation-design notes. PR-8 curates the Osmani import through the intake process. PR-9 adds `plan-as-guidance` for loop-contract planning. PR-10 adds data-science-native EDA journaling and reproducibility capture skills. PR-11 adapts the incumbent `project-setup` manager skill around project-specific config, team roster, source keywords, decision logging, and the living Research Design and Progress artifact. PR-12 adapts `weekly-review` around file-and-transcript synthesis, the three-page overview, weekly history updates, and per-person priorities. PR-13 adds the manager meeting loop and n8n integration boundary while keeping scheduled, audited, credentialed execution outside Codex skills. The PR-0 through PR-13 skill-system sequence is complete; the next separate roadmap item is PR 19 from the next-pass site sequence.
