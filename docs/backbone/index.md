---
description: Backbone Protocol v0.1 for AI-native, reproducible, artifact-first data science projects.
---

# Backbone Protocol

Backbone Protocol v0.1 is the minimal artifact system for AI-native reproducible data science projects.

It gives Codex Batman a shared structure for work that needs to survive beyond a single chat session. The protocol is intentionally small — enough to support disciplined execution, review, handoff, and improvement without turning every project into a heavy framework.

## Start Here If

Use this section when you want to answer one of these questions quickly:

- What durable files should every project keep?
- What workflow stages should leave artifacts behind?
- How does project memory survive beyond one chat session?
- What is the minimum structure before we add templates or skill packs?

## Why This Exists

AI can accelerate analysis, but acceleration without durable structure creates brittle work:

- key decisions disappear into chat history
- analysis plans drift without a record
- experiment comparisons become hard to trust
- collaborators inherit output without context

Backbone Protocol exists to keep project state legible to both humans and agents.

## Core Principle

The protocol is artifact-first. Important work should leave durable files that answer what problem this project is solving, what data is being used, what plan is being executed, what experiments were run, what decisions were made, what model or output is being shared, and what happened during the workflow.

## Minimum Artifact Set

Backbone Protocol v0.1 defines this minimum artifact set:

```text
PROJECT_STATE.md
problem_frame.md
data_card.md
analysis_plan.md
experiment_log.md
model_card.md
workflow_trace.md
decision_log.md
```

These files are explained in [Artifacts](artifacts.md).

## Lifecycle

The protocol supports this minimal lifecycle:

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

This lifecycle is documented in [Lifecycle](lifecycle.md).

## What The Protocol Is Not

This protocol is not:

- a CLI tool
- a web application
- a rigid schema system
- a substitute for human judgment
- a substitute for scientific review

It is a shared operating layer for reproducible project memory.

## Design Rules

- Keep the protocol minimal.
- Keep files human-readable and agent-readable.
- Prefer markdown over custom formats when possible.
- Preserve existing project layouts where possible.
- Use the protocol to support workflow gates, not to bypass them.

## Related Pages

- [Artifacts](artifacts.md)
- [Lifecycle](lifecycle.md)
- [Self-Improvement Loop](self-improvement.md)
- [Project Template](project-template.md)
- [Examples](../examples/index.md)
- [Tooling Stack](../tooling/index.md)
- [Core Data Science Workflow](../workflows/data-science/index.md)

## Return To Your Role Path

Once you have reviewed the protocol, return to the path that matches your role:

- [For Students](../students/index.md) — see how artifact discipline fits into guided learning
- [For Researchers & Data Scientists](../data-scientists/index.md) — apply the backbone to a real project
- [For Managers](../managers/index.md) — use the artifact list to verify project readiness before team advancement
