---
description: Optional external tools that can complement Codex Batman without becoming core dependencies.
---

# Tooling Stack

Codex Batman is the workflow backbone.

It defines the operating rules, artifact expectations, and reusable skill structure for AI-native data science and research-management work. The tools in this section are optional companions, not required dependencies.

## Start Here If

Use this section when you are asking whether an external helper should be added to your workflow at all.

The default answer should still be to start with the backbone first and add tools only when they solve a specific recurring problem.

## What This Section Covers

These pages explain external tools that can be useful alongside Codex Batman when you need:

- tighter behavior guardrails for small edits
- structural memory for large or unfamiliar repositories
- additional execution agents in local folders

None of these tools replaces the backbone itself.

## Core Principle

Use external tools to support the workflow, not to redefine it.

Codex Batman should remain the source of truth for:

- workflow gates
- artifact expectations
- reproducibility rules
- handoff discipline
- project memory conventions

External tools may help with execution quality or navigation speed, but they should not become substitutes for scientific judgment or workflow protocol.

## Current Optional Tools

| Tool | Best for | Not a substitute for |
|------|----------|----------------------|
| [Ponytail](ponytail.md) | Minimal diffs, cleanup tasks, small implementation work, reducing overbuilding | Workflow gates, architecture decisions, scientific review |
| [codebase-memory-mcp](codebase-memory.md) | Repo graphing, codebase exploration, impact analysis, call-chain questions | Reproducibility checks, statistical correctness, human judgment |

## How To Use This Section

Read these pages when you want to decide whether a supporting tool is worth adding to your workflow.

Recommended stance:

1. Start with the Codex Batman backbone.
2. Add optional tools only when they solve a specific recurring problem.
3. Keep the project workflow artifact-first and repo-first even when external helpers are present.

## Related Pages

- [Examples](../examples/index.md)
- [Backbone Protocol](../backbone/index.md)
- [Core Data Science Workflow](../workflows/data-science/index.md)
- [Backbone Project Template](../backbone/project-template.md)
- [Skill Library](../setup/skill-reference.md)
- [Build Your Own](../system/index.md)
