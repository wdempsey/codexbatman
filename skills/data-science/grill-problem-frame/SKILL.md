---
name: grill-problem-frame
description: Interrogate a problem definition before any data is touched. Challenge the decision context, metric, prediction time, population scope, leakage risks, and failure modes. Use this before running problem-framing whenever a problem statement feels underspecified, when a student or practitioner has jumped to a model before clarifying the question, or when a manager wants to pressure-test a framing before approving the project. Adapted from Matt Pocock's grill-me pattern for data science.
category: data-science
status: active
stage: problem-framing
role_compatibility:
  - student
  - data scientist
  - data science manager
inputs:
  - problem statement or initial description
  - dataset name or description
  - stated goal or metric
outputs:
  - resolved problem frame
  - list of open decisions
  - ready-to-write problem_frame.md brief
depends_on: []
recommended_next:
  - problem-framing
  - data-audit
---

# Skill: Grill Problem Frame

## Purpose

Challenge a problem statement until every load-bearing decision is explicit.

The most common failure in data science isn't a modeling error — it's a framing error that goes unnoticed until evaluation. This skill surfaces those errors before any data is loaded.

## When To Invoke

Use this skill when:

- a student or practitioner has described a problem but hasn't answered: what decision does the model support?
- the metric is stated but not justified (e.g., "we'll use accuracy" without checking class balance)
- the prediction time is undefined — is the model deployed before or after a key event?
- leakage risks haven't been listed
- "good performance" hasn't been defined in terms of the actual decision

## The Grilling Sequence

Work through these in order. Do not accept vague answers — ask follow-up questions until each is concrete.

**1. Decision context**
> What specific decision does this model support?
> Who makes that decision, when, and with what alternatives?

A model that "predicts churn" is not yet a decision. "Flags accounts for a retention call from the customer success team" is a decision.

**2. Target definition**
> What exactly is being predicted?
> If it's a category, what are the class boundaries and who decided them?
> If it's a number, what precision matters?

**3. Metric alignment**
> Why is this metric right for this decision?
> What kind of errors cost more — false positives or false negatives?
> Is the metric sensitive to class imbalance?

Common traps: using accuracy on imbalanced data, using RMSE when direction of error matters asymmetrically, using AUC when a specific operating threshold is what actually matters.

**4. Prediction time**
> At what point in time will this model run in deployment?
> What information is available at that moment?
> Are any features only knowable after the event being predicted?

This is the leakage check. If any feature could only be observed after the target event, it cannot be used.

**5. Population scope**
> Who is in the training data?
> Who will the model be applied to in deployment?
> Are those populations the same?

A model trained on clinic patients from 1988 should not be deployed to a general screening population without revalidation.

**6. Success criteria**
> What performance is "good enough" to deploy?
> Is there a baseline to beat (human judgment, rule-based system, prior model)?
> What would cause the project to stop?

**7. Failure modes**
> What happens if the model gets it wrong in the worst direction?
> Is there a downstream system or human that catches those errors?

## Output Format

After grilling is complete, produce a brief summary:

```
Decision: [one sentence]
Target: [variable name and type]
Metric: [metric and justification]
Prediction time: [when the model runs]
Population: [who it applies to]
Leakage risks: [list any features that need checking]
Success threshold: [what good enough looks like]
Open decisions: [anything still unresolved]
```

Hand this to `problem-framing` to write `problem_frame.md`.

## What Counts As Done

The grilling is done when you can answer every question above in one sentence each, with no placeholders like "TBD" or "depends on the data."

If the person cannot answer a question, that is useful — it means the framing isn't ready. Document the gap explicitly and agree on how to resolve it before the project proceeds.
