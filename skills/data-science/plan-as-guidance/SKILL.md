---
name: plan-as-guidance
description: Draft a flexible outcome-oriented plan for data-science or implementation work. Use after intent, problem frame, or spec is clear when the work needs sequencing but discovery may require reordering, merging, splitting, or revising steps mid-flight.
category: data-science
status: active
stage: framing
role_compatibility:
  - data scientist
inputs:
  - confirmed intent, problem frame, or approved spec
  - constraints and known risks
  - expected verification commands or artifacts
outputs:
  - loop contract
  - guidance plan
  - revision triggers
  - deviation log template
recommended_next:
  - incremental-implementation
  - workflow-trace
source_attribution:
  - "Adapted from Addy Osmani's planning-and-task-breakdown skill in addyosmani/agent-skills; rewritten for Codex Batman loop-contract planning."
---

# Plan As Guidance

## Purpose

Use this skill to produce plans that guide work without pretending discovery will follow a fixed script.

A plan is a contract on outcomes, evidence, and decision points. It is not a promise to execute a sequence exactly as written.

## Use When

- The goal is clear enough to plan, but the order may change as data, code, or constraints are discovered.
- Exploratory analysis needs bounded intent, acceptance criteria, and revision triggers.
- A data scientist needs a plan before handing work to `incremental-implementation`.
- A prior plan is no longer accurate and should be revised without treating revision as failure.

Do not use this for a one-line mechanical change, an ML feature spec that belongs in `ml-feature-spec`, or a data-science project that still lacks `problem-framing`.

## Procedure

### 1. Confirm The Planning Anchor

Name the anchor before writing steps:

- outcome
- intended user or decision
- acceptance evidence
- constraints
- non-goals
- known uncertainty

If the anchor is missing, route to `interview-me` or `problem-framing` first.

### 2. Write The Loop Contract

Create a short contract:

```markdown
## Loop Contract

Outcome:
Acceptance evidence:
Non-goals:
Allowed revisions:
Must ask before:
Stop conditions:
```

Allowed revisions should name when the plan may be reordered, merged, split, or paused.

### 3. Draft Guidance Steps

Each step should carry intent, not just an action:

```markdown
### Step N: [verb-led title]

Intent:
Acceptance criteria:
Verification:
Dependencies:
Permitted revision:
Notes:
```

Keep steps small enough for one focused session. If a step has more than three acceptance criteria, split it unless those criteria are inseparable.

### 4. Add Revision Triggers

Explicitly list what should change the plan:

- data quality issue discovered
- leakage or target definition risk appears
- verification fails for a reason not covered by the plan
- dependency order is wrong
- two steps are better merged after reading the code
- a step becomes too large and should be split
- human review changes the acceptance target

### 5. Keep A Deviation Log

A deviation is not automatically a mistake. Hidden deviation is the problem.

Use this format:

```markdown
## Deviation Log

- Planned:
  Changed:
  Evidence:
  Reason:
  Next action:
```

Record deviations when the plan changes because reality taught you something.

## Boundaries

- Use `ml-feature-spec` when the missing artifact is an engineering-facing ML feature spec.
- Use `incremental-implementation` after a guidance step is ready to execute.
- Use `workflow-trace` after meaningful work changes the plan or completes a loop.
- Use `code-review-and-quality` when reviewing a finished diff against the plan and brief.
- Use `data-audit`, `eda-plan`, or `modeling` when workflow gates, not planning mechanics, are the next required step.
