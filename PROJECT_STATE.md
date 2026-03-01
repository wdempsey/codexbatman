# Project State — Codex-Native Data Science Workflow System

This document summarizes the current architectural state of the project.

It is intended to provide context for future AI collaboration and prevent drift.

---

# 1. Core Identity

This repository is no longer a Claude-first tutorial site.

It is evolving into:

A Codex-native workflow system for structured, reproducible data science.

It integrates:

- Structured skills
- Explicit workflow gates
- Reproducibility enforcement
- Human-in-the-loop
- Devlog → Digital Garden distillation loop

The goal is to teach data science through a constrained operating system.

---

# 2. Data Science Layer — Current State

## Architectural Documents

- Data Science Layer Blueprint
- Data Science Layer Goals
- Cross-references between Blueprint and Goals
- DS workflow gates enforced in AGENTS.md

## Implemented Skills

- problem-framing
- data-audit (Proceed / Halt protocol)
- experiment-log

## Templates

- experiment-log template
- model-card template

## Enforcement

Root AGENTS.md now requires:

- Problem Framing before modeling
- Data Audit before EDA/modeling
- Experiment Log for each modeling iteration
- Model Card before final model freeze

Reproducibility is non-negotiable.

---

# 3. Devlog System

The repository includes:

- devlog/
- Devlog template
- Weekly distillation ritual

Devlogs are raw.
Digital Garden entries are distilled.

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

- Completed: Project Direction page added at docs/about/project-direction.md
- Rewrite homepage messaging
- Remove Claude-first framing
- Tighten mkdocs navigation

## Garden System

- Create separate garden repo
- Add AGENTS.md (strict voice preservation)
- Add folder structure
- Add note/pattern/essay templates
- Add distillation protocol page
- Cross-link tutorial and garden repos

## Future Work

- Add “How to Use This Layer” page
- Build end-to-end worked example
- Evaluate two candidate example projects
- Pressure-test DS workflow
- Generate garden essays from real use

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

Clarify repository direction and restructure navigation before starting example projects.

Architecture before application.
