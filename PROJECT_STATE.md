# Project State — Codex-Native Data Science Operating System

This document summarizes the current architectural state of the project.

It is intended to provide context for future AI collaboration and prevent drift.

---

# 1. Core Identity

This repository is no longer a Claude-first tutorial site.

It is evolving into:

A Codex-native workflow system for structured, reproducible data science.

It now integrates:

- Structured skills
- Role-aware overlays
- Explicit workflow gates
- Reproducibility enforcement
- Human-in-the-loop
- Workflow documentation on the site

The goal is to teach data science through a constrained operating system.

---

# 2. Data Science Layer — Current State

## Architectural Documents

- Data Science Layer Blueprint
- Data Science Layer Goals
- Canonical workflow skill pages
- Cross-references between Blueprint and Goals
- DS workflow gates enforced in AGENTS.md

## Canonical Backbone Skills

- project-bootstrap
- problem-framing
- data-audit (Proceed / Halt protocol)
- experiment-log

## Role-Aware Overlay Layers

- student
- practitioner
- manager

## Templates

- workflow-driven artifacts (framing, audit, experiment log)
- project instruction patterns

## Enforcement

Root AGENTS.md now requires:

- Problem Framing before modeling
- Data Audit before EDA/modeling
- Experiment Log for each modeling iteration
- Model Card before final model freeze

Reproducibility is non-negotiable.

---

# 3. Project Logging

Current state:

- `planning.md` is the active repository log for current work and follow-up tasks.
- `PROJECT_STATE.md` is a durable architecture snapshot.
- `AGENTS.md` still references a future `devlog/` template, but that directory does not currently exist in the repository.

Implication:

- A real devlog system still needs to be added or the stale references removed.

---

# 4. Digital Garden Plan (Separate Repo)

Planned separate repository.

Purpose:

- Public thinking space
- Essays (long form)
- Notes (atomic)
- Patterns (structured ideas)
- Maps (concept linking)

The garden reflects on applying the system.
It is not the system itself.

Graph view enabled but not designed around.

---

# 5. Remaining Structural Tasks

## Identity & Differentiation

- Completed: repository identity rewritten around Codex-native data science
- Completed: role-aware MkDocs navigation
- Completed: first-wave canonical skill and overlay architecture
- Review for duplicate or conflicting workflow pages and stale branding

## Garden System

- Create separate garden repo
- Decide whether devlog-to-garden distillation remains in scope for this repository
- Add actual devlog infrastructure if retained
- Cross-link tutorial and garden repos if the separate garden remains active

## Future Work

- Build end-to-end worked example
- Evaluate two candidate example projects
- Pressure-test DS workflow
- Add later-phase canonical skills beyond the first wave

---

# 6. Design Principles

This system is:

- Thinking-first
- Audit-driven
- Artifact-producing
- Documentation-enforced
- Reproducibility-centered
- Human-in-the-loop

Speed is secondary to discipline.

---

# 7. Immediate Priority

Stabilize the new architecture by reviewing for duplication, stale pages, and conflicting site language before expanding the worked examples.

Architecture before application.
