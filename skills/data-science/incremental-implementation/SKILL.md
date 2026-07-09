---
name: incremental-implementation
description: Implement data-science software changes in small verified slices. Use after intent and spec are clear when a change touches multiple files, spans pipeline layers, or is at risk of becoming one large unreviewable commit.
category: data-science
status: active
stage: modeling
role_compatibility:
  - data scientist
inputs:
  - confirmed intent or spec
  - target files or task list
  - verification commands
outputs:
  - slice plan
  - verified increments
  - handoff or commit-ready summary
depends_on:
  - problem-framing
recommended_next:
  - code-review-and-quality
  - handoff
source_attribution:
  - "Adapted from Addy Osmani's incremental-implementation skill in addyosmani/agent-skills; rewritten for Codex Batman data-science software-team workflows."
---

# Incremental Implementation

## Purpose

Use this skill to keep implementation reviewable while a data scientist changes production-adjacent code: feature pipelines, inference wrappers, project templates, docs-backed workflow code, or model-serving glue.

This skill is distinct from `tdd-data-pipeline`. TDD owns the red-green-refactor loop for behavioral contracts. Incremental implementation owns the slicing discipline for multi-file or multi-layer delivery, whether or not tests are being written first.

## Use When

- A change touches more than one file or layer.
- A task list exists and needs to be implemented safely one piece at a time.
- You are tempted to write a large batch of code before running a check.
- A feature can be hidden, stubbed, or sliced without exposing incomplete behavior.

Do not use this to avoid required workflow gates. Modeling or analysis code still needs the repo's problem-framing, data-audit, and experiment-log discipline when those gates apply.

## Procedure

### 1. Confirm The Contract

Before editing, name:

- the user-visible or collaborator-visible outcome
- the verification command or manual check for the whole task
- files or layers expected to change
- what is explicitly out of scope

If the request is still ambiguous, use `interview-me` before slicing.

### 2. Choose A Slice Strategy

Prefer the first strategy that makes the next increment independently reviewable:

- Vertical slice: one narrow path through data, model, API, UI, or docs surfaces.
- Contract-first slice: define interface/schema/spec before consumers.
- Risk-first slice: prove the most uncertain dependency or behavior first.
- Cleanup-first slice: remove a blocker only when it is necessary for the requested work.

Avoid horizontal slices that create all scaffolding first and defer working behavior until the end.

### 3. Execute One Slice

For each slice:

1. State the slice and non-goals.
2. Edit only the files needed for that slice.
3. Run the least expensive meaningful verification.
4. Record the result and remaining risk.
5. Commit or hand off when the slice is coherent.

If verification fails, stop feature work and route to the appropriate debug skill before continuing.

### 4. Keep The Diff Reversible

- Prefer additive changes until the replacement is proven.
- Do not mix refactors with new behavior unless the refactor is required for the slice.
- Do not modernize nearby code just because it is visible.
- Ask before deleting unclear orphaned code or artifacts.

### 5. Close With Evidence

End with:

```text
Slices completed:
Verification run:
Open risks:
Recommended next step:
```

## Boundary With Nearby Skills

- Use `ml-feature-spec` before this skill when the team needs a reviewable ML feature PRD and issue breakdown.
- Use `tdd-data-pipeline` inside a slice when the next change is a data transform or inference contract that should be test-first.
- Use `zoom-out` before slicing unfamiliar code.
- Use `code-review-and-quality` after the implementation is ready for merge.
