---
name: interview-me
description: Clarify an underspecified user intent before planning, problem framing, or software implementation begins. Use when a data scientist or collaborator asks for a conventional artifact without saying who it serves, why it is needed now, what success means, or what is out of scope.
category: data-science
status: active
stage: problem-framing
role_compatibility:
  - data scientist
  - data science manager
inputs:
  - underspecified request
  - available stakeholder or project context
outputs:
  - confirmed intent restatement
  - downstream skill recommendation
recommended_next:
  - problem-framing
  - grill-problem-frame
  - ml-feature-spec
source_attribution:
  - "Adapted from Addy Osmani's interview-me skill in addyosmani/agent-skills; rewritten for Codex Batman data-science software-team workflows."
---

# Interview Me

## Purpose

Use this skill to find out what the user actually wants before Codex turns a vague request into a plan or code.

This is an intent-extraction skill, not a data-science gate. It sits before `problem-framing`, `grill-problem-frame`, or `ml-feature-spec` when the request is too ambiguous to route safely.

## Use When

- The ask names an artifact but not the underlying need: "build a dashboard", "make a tracker", "write a spec".
- The user has not named the beneficiary, decision, success criterion, binding constraint, or non-goal.
- A data scientist is about to ask an engineering team for work and the request is still conventional rather than specific.
- You are silently filling gaps before any plan, spec, or code exists.

Do not use this for typo fixes, mechanical edits, direct information requests, or already-approved implementation tasks.

## Procedure

### 1. State The Current Hypothesis

Start with one sentence and a confidence number.

```text
Hypothesis: You want <artifact> because <underlying outcome>.
Confidence: 35% - missing user, success criterion, and out-of-scope boundary.
```

If confidence is below 70%, name what is missing so the user can help close the gap.

### 2. Ask One Question At A Time

Ask a single focused question. Attach your best guess so the user can react to a concrete hypothesis.

```text
Question: Who needs this output to make a decision?
Guess: The experiment owner, because the request sounds like a personal tracking gap rather than a team reporting gap.
```

Wait for the answer before asking the next question. Do not batch questions.

### 3. Probe Convention Language

When the user says something like "best practice", "clean", "scalable", "standard", or "whatever you think", ask what they would choose if they did not have to justify it.

The goal is not to reject best practice. The goal is to separate the user's actual need from a conventional answer.

### 4. Restate The Intent

When confidence is high enough to predict how the user would answer the next few questions, restate:

```text
Outcome:
User:
Why now:
Success:
Constraint:
Out of scope:
Recommended next skill:
```

The out-of-scope line is required. Silent disagreement about non-goals is a common source of rework.

### 5. Require Explicit Confirmation

Proceed only after the user explicitly confirms the restatement. If the answer is "whatever you think", turn the uncertainty into two concrete choices and ask again.

## Boundaries

- Use `grill-problem-frame` when the intent is known but the analytical frame needs pressure-testing.
- Use `grill-with-codebase` when the issue is terminology or architecture alignment inside an existing engineering codebase.
- Use `ml-feature-spec` when the intent is confirmed and the output should be a software-team ML feature spec.
- Use `problem-framing` when the confirmed intent is an analytical project that must enter the workflow backbone.
