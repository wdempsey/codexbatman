---
hide:
  - navigation
description: Codex-native data science workflow system with structured workflow gates, reproducibility enforcement, and devlog-to-garden distillation.
social:
  cards_layout_options:
    title: Codex-Native Data Science Workflow System
    description: Structured, reproducible workflow for disciplined applied data science.
---

# Codex-Native Data Science Workflow System

This repository defines a structured, reproducible workflow for applied data science.

It originated as a fork of the claudeblattman site and has evolved into a Codex-native operating system for disciplined analytical work.

---

## Scope

The project integrates:

- A structured Data Science layer  
- Explicit workflow gates  
- Skill-based modular architecture  
- Reproducibility enforcement  
- Human-in-the-loop supervision  
- Devlog → Digital Garden separation  

The objective is not faster modeling.
The objective is better analytical discipline.

---

## Data Science Layer

The Data Science layer formalizes a sequence:

1. Problem Framing  
2. Data Audit (Proceed / Halt protocol)  
3. Structured EDA planning  
4. Logged modeling experiments  
5. Model Card documentation  

These stages are encoded in `AGENTS.md` and implemented as modular skills.

No model is considered complete without documentation.
No analysis proceeds without explicit framing and audit.

---

## Reproducibility Standards

All workflows require:

- Deterministic seeds  
- Versioned datasets  
- Logged configurations  
- Explicit evaluation strategy  
- Separation of raw and processed data  

Reproducibility is treated as a methodological requirement, not a technical afterthought.

---

## System Design Orientation

This repository assumes that modern data scientists operate within systems.

Accordingly, the workflow includes:

- Database scoping and schema reasoning  
- Join integrity checks  
- Boundary awareness (batch, API, dashboard)  
- Documentation suitable for collaborative environments  

The emphasis is on applied rigor.

---

## Devlog and Digital Garden

Implementation work is recorded in structured devlogs.

Distilled insights are moved into a separate Digital Garden repository, where ideas are organized as:

- Essays  
- Notes  
- Patterns  
- Concept maps  

The workflow produces artifacts.
The garden produces reflection.

---

## Intended Audience

This project is intended for:

- Data scientists seeking stronger methodological discipline  
- Practitioners working at the boundary of research and engineering  
- Instructors interested in teaching through constrained systems  

The repository continues to evolve as a structured operating system for applied data science.
