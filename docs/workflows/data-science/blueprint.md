# Data Science Layer Blueprint
## A Codex-Native, Reproducible Analyst Assistant System

---

# 1. Purpose

This Data Science (DS) layer defines a structured, reproducible analyst assistant model embedded within this repository.

It is designed to:

- Teach best practices through a working system
- Guide both analytical reasoning and code generation
- Support tabular ML, causal inference, and longitudinal data
- Integrate light but explicit data engineering practices
- Enforce reproducibility and documentation discipline
- Keep humans firmly in the loop

This is not a collection of prompts.

It is a layered operating model.

---

# 2. Scope

## In Scope

- Tabular machine learning workflows
- Causal inference (design-aware, assumption-explicit)
- Longitudinal and panel data analysis
- Data audit and leakage detection
- Structured EDA planning
- Reproducible experiment design
- Experiment logging
- Model documentation (model cards)
- Data documentation (data cards)
- Database scoping and schema design
- Ingestion and transformation planning
- Analytics system boundaries (batch, API, dashboard)

## Out of Scope (for now)

- NLP workflows
- Computer vision workflows
- Large-scale distributed training infrastructure
- Feature store infrastructure

These may be added later as extensions.

---

# 3. Design Philosophy

The DS assistant must be:

- Structured
- Skeptical
- Reproducibility-first
- Bias-aware
- Leakage-aware
- Documentation-driven
- Human-in-the-loop

It must not:

- Over-optimize prematurely
- Skip problem framing
- Hide assumptions
- Modify raw data
- Replace statistical reasoning with blind model tuning
- Proceed without explicit evaluation criteria

The assistant supports analytical thinking.
It does not replace analytical judgment.

---

# 4. Workflow Phases (State Machine)

The DS layer operates as a structured workflow engine.

Each phase produces explicit artifacts.
For intent and rationale behind these workflow gates, see [Goals of the Data Science Layer](goals.md).

---

## Phase 1 — Problem Framing

Outputs:

- Clear problem definition
- Stakeholder context
- Success metric definition
- Operational constraints
- Risk register
- Causal vs predictive clarification
- Data requirements checklist

No modeling may begin before this phase is approved.

---

## Phase 2 — Data Inventory & Access

Outputs:

- Data sources list
- Access method (database, files, API)
- Schema overview
- Lineage notes
- Raw vs processed distinction
- Temporal structure identification

This phase enforces clarity around what data exists and how it flows.

---

## Phase 3 — Data Audit & Risk Check

Outputs:

- Missingness analysis
- Distribution summaries
- Target construction review
- Leakage risk assessment
- Proxy bias risks
- Sampling bias risks
- Temporal validity checks (for longitudinal data)
- “Proceed / Halt” recommendation

This phase prevents downstream modeling errors.

---

## Phase 4 — EDA Plan & Baseline

Outputs:

- Structured EDA plan
- Feature sanity checks
- Hypothesis checklist
- Baseline model specification
- Initial evaluation plan

EDA must follow a plan, not random exploration.

---

## Phase 5 — Modeling & Evaluation

Outputs:

- Reproducible training script
- Deterministic seed usage
- Explicit metric alignment with problem definition
- Error analysis
- Sensitivity checks
- Validation strategy justification

For causal settings:

- Explicit identification strategy
- Assumptions stated clearly
- Threats to validity documented
- Robustness checks described

---

## Phase 6 — Experiment Logging

Outputs:

- Structured experiment log entry
- Parameter changes
- Performance results
- Interpretation
- Decision outcome
- Next-step recommendation

All experiments must be logged before iteration.

---

## Phase 7 — Documentation & Packaging

Outputs:

- Model card
- Data card (if appropriate)
- Reproducibility instructions
- Deployment boundary notes
- Monitoring considerations (if relevant)

Documentation is not optional.
It is part of the workflow.

---

# 5. Skill Architecture

Skills are modular and follow a strict structure.

Each skill lives in: skills/data-science/<skill-name>/

Each skill contains:

- `SKILL.md`
- `references/`
- `assets/`
- `scripts/` (optional, for deterministic tasks)

Each skill has:

- Single responsibility
- Clear inputs
- Clear outputs
- Guardrails
- Escalation conditions
- Human review requirement

---

## Initial Keystone Skills

1. problem-framing
2. data-audit
3. experiment-log
4. model-card
5. causal-design-check
6. db-scope-and-setup (data engineering)

These anchor the system.

---

# 6. Reproducibility Standards

All DS workflows must:

- Use pinned environments
- Use deterministic seeds
- Avoid modifying raw data
- Separate exploratory notebooks from production scripts
- Provide a runnable pipeline entry point
- Document data dependencies
- Log all experiments
- Version outputs appropriately

Reproducibility is non-negotiable.

---

# 7. Data Engineering Layer

This DS system includes light but explicit data engineering practices.

The assistant must guide:

- Database selection reasoning
- Schema design principles
- Ingestion planning
- Transform vs raw separation
- Backend vs analytics boundary decisions
- Versioning awareness
- Migration considerations

The goal is to grow data scientists toward responsible system design.

---

# 8. Tutorial Integration

The tutorial site will:

- Explain the DS operating model
- Walk through a full end-to-end example
- Show how skills compose
- Teach why guardrails exist
- Contrast strong vs weak workflows
- Demonstrate reproducibility in practice

The tutorial teaches through usage of the system.

---

# 9. Relationship to AGENTS.md

The root AGENTS.md enforces:

- Reproducibility discipline
- No raw data modification
- Small PR changes
- Human-in-the-loop decision making
- Experiment documentation requirements

The DS layer and AGENTS.md are intentionally aligned.

---

# 10. Garden Integration

Devlog entries that surface reusable insights will become:

- Atomic notes
- Structured patterns
- Long-form essays

The DS layer feeds the digital garden.
The garden reflects on lessons learned from applying the system.

---

# 11. Long-Term Extensions

Possible future modules:

- Production ML monitoring
- Data validation frameworks
- Feature store design
- ML governance frameworks
- Simulation workflows
- Advanced experimental design libraries

These will be added once the tabular foundation is stable.
