---
description: Lifecycle phases for Backbone Protocol v0.1.
---

# Backbone Lifecycle

Backbone Protocol v0.1 uses a lightweight lifecycle that connects the existing data science workflow to durable project memory.

The goal is not bureaucracy. The goal is keeping work reproducible, reviewable, and reusable.

## Lifecycle

```text
bootstrap
frame
audit
plan
execute
evaluate
communicate
trace
distill
improve
```

## bootstrap

Purpose:
- Create the minimum project memory and workspace backbone.

Typical outputs:
- `PROJECT_STATE.md`
- initial artifact locations
- raw vs processed boundary notes

Related workflow:
- [Project Bootstrap](../workflows/data-science/project-bootstrap.md)

## frame

Purpose:
- Define the problem before execution drifts.

Typical outputs:
- `problem_frame.md`
- initial entries in `decision_log.md`

Related workflow:
- [Problem Framing](../workflows/data-science/problem-framing.md)

## audit

Purpose:
- Decide whether the data can support the framed question.

Typical outputs:
- `data_card.md`
- readiness and risk notes

Related workflow:
- [Data Audit](../workflows/data-science/data-audit.md)

## plan

Purpose:
- Define the bounded execution plan.

Typical outputs:
- `analysis_plan.md`
- updated `PROJECT_STATE.md`

## execute

Purpose:
- Run the planned analysis or modeling work.

Typical outputs:
- working files
- intermediate outputs
- updated `experiment_log.md`

## evaluate

Purpose:
- Assess whether the work is good enough, trustworthy enough, and aligned to the question.

Typical outputs:
- evaluation notes
- comparison conclusions
- updated `experiment_log.md`
- decision entries

## communicate

Purpose:
- Turn the output into something another human can responsibly consume.

Typical outputs:
- `model_card.md`
- decision summary
- handoff-ready notes

## trace

Purpose:
- Capture what actually happened in the workflow.

Typical outputs:
- `workflow_trace.md`

This phase matters because valuable lessons often appear in execution details rather than in final outputs.

## distill

Purpose:
- Extract reusable lessons from traces, errors, and improvements.

Typical outputs:
- candidate checklist updates
- candidate prompt updates
- candidate template or skill updates

## improve

Purpose:
- Promote durable improvements back into the system.

Typical outputs:
- updated skills
- updated templates
- updated docs
- updated evaluation or review checklists

## Why The Final Three Phases Matter

Many teams stop at communication. Backbone Protocol does not.

The last three phases exist because:

- useful lessons should not disappear into chat history
- repeated problems should become reusable infrastructure
- agents improve most when workflows produce durable memory

## Related Pages

- [Backbone Protocol](index.md)
- [Artifacts](artifacts.md)
- [Self-Improvement Loop](self-improvement.md)
