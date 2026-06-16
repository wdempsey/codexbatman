---
description: Minimum artifact definitions for Backbone Protocol v0.1.
---

# Backbone Artifacts

Backbone Protocol v0.1 defines a minimal set of shared artifacts for reproducible, AI-native data science work.

Each artifact should be lightweight, readable, and useful to both humans and agents.

## Artifact Summary

| Artifact | Purpose | Usually created during |
|----------|---------|------------------------|
| `PROJECT_STATE.md` | High-level project memory and current state | bootstrap |
| `problem_frame.md` | Analytical question, target decision, and constraints | frame |
| `data_card.md` | Data description, limitations, and readiness notes | audit |
| `analysis_plan.md` | Planned workflow before open-ended execution | plan |
| `experiment_log.md` | Structured record of modeling or analysis runs | execute / evaluate |
| `model_card.md` | Final shared description of model purpose, limits, and performance | communicate |
| `workflow_trace.md` | What happened during the workflow and what should be reusable | trace |
| `decision_log.md` | Record of material decisions and rationale | across the lifecycle |

## PROJECT_STATE.md

Purpose:
- Maintain the durable project snapshot.

When created:
- During bootstrap, before major analytical work begins.

Who reads it:
- project contributors
- manager workflows
- handoff or review sessions
- agents entering the project later

Who updates it:
- the primary project owner
- a project manager agent
- Codex during structured workflow updates

Minimum contents:
- project goal
- current phase
- key open questions
- current risks or blockers
- active artifacts and their status

How it supports agents:
- gives a new session immediate orientation
- reduces repeated rediscovery of project context

## problem_frame.md

Purpose:
- Capture the analytical problem before execution begins.

When created:
- During framing, before modeling or broad EDA.

Who reads it:
- analysts
- reviewers
- managers
- agents deciding next steps

Who updates it:
- analyst and supervisor
- Codex during framing refinement

Minimum contents:
- decision context
- question being answered
- target or estimand
- success criteria
- constraints and risks

How it supports agents:
- keeps the session anchored to the real problem instead of drifting into generic analysis

## data_card.md

Purpose:
- Describe the dataset, its boundaries, and its readiness.

When created:
- During data audit.

Who reads it:
- analysts
- model reviewers
- managers checking readiness
- future contributors

Who updates it:
- analyst
- Codex during audit updates

Minimum contents:
- data source
- unit of analysis
- important fields
- known quality issues
- leakage or access risks
- readiness judgment

How it supports agents:
- helps future sessions understand what the data can and cannot support

## analysis_plan.md

Purpose:
- Define the bounded plan before execution becomes open-ended.

When created:
- After framing and audit, before heavy analysis.

Who reads it:
- analyst
- project lead
- review sessions
- manager workflows when checking whether work is on track

Who updates it:
- analyst
- Codex in planning mode

Minimum contents:
- planned steps
- evaluation approach
- baseline comparison plan
- reproducibility expectations
- stop conditions

How it supports agents:
- creates a durable contract for what should happen next

## experiment_log.md

Purpose:
- Record runs, comparisons, and conclusions.

When created:
- Before the first substantial modeling or analysis run.

Who reads it:
- analyst
- reviewer
- manager checking progress
- future contributors comparing past attempts

Who updates it:
- analyst
- Codex after each substantive run

Minimum contents:
- run identifier or date
- inputs or dataset version
- parameters or specification
- metrics or outcomes
- conclusion
- next recommended action

How it supports agents:
- prevents repeated experiments and makes iteration auditable

## model_card.md

Purpose:
- Describe the final shared model or analytical output.

When created:
- Before a result is handed off or shared.

Who reads it:
- managers
- collaborators
- downstream users
- reviewers

Who updates it:
- analyst
- Codex drafting with human approval

Minimum contents:
- intended use
- training or input context
- evaluation summary
- limitations
- risks
- recommended interpretation

How it supports agents:
- helps future sessions avoid overclaiming what the model can do

## workflow_trace.md

Purpose:
- Capture what happened during the workflow and what should become reusable.

When created:
- After a meaningful work session or workflow cycle.

Who reads it:
- future contributors
- distillation or improvement workflows
- lab or project manager agents

Who updates it:
- Codex
- analyst
- handoff-oriented workflows

Minimum contents:
- goal
- context used
- steps taken
- files touched
- decisions made
- outcome
- reusable pattern or lesson

How it supports agents:
- turns one-off sessions into reusable operating memory

## decision_log.md

Purpose:
- Record the important decisions and why they were made.

When created:
- As soon as material choices begin affecting the project.

Who reads it:
- collaborators
- reviewers
- manager workflows
- future sessions trying to understand why the project looks the way it does

Who updates it:
- analyst
- project lead
- Codex when instructed to preserve rationale

Minimum contents:
- decision
- date or session context
- rationale
- alternatives considered
- downstream implications

How it supports agents:
- prevents later sessions from undoing deliberate choices because the reasoning was lost

## Related Pages

- [Backbone Protocol](index.md)
- [Lifecycle](lifecycle.md)
- [Self-Improvement Loop](self-improvement.md)
