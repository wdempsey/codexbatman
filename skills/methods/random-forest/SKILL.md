---
name: random-forest
description: Teach random forests as tree ensembles for nonlinear prediction, with emphasis on comparison against simpler baselines and interpretability tradeoffs.
category: methods
status: active
role_compatibility:
  - student
  - data scientist
  - data science manager
method_family: supervised-learning
prerequisites:
  - problem-framing
  - data-audit
  - eda-plan
related_workflow_skills:
  - modeling
  - model-evaluation
  - causal-design-check
---

# Skill: Random Forest

## Purpose

Teach random forests when a student needs a practical explanation of tree ensembles, nonlinearity, interactions, and why flexible models should still be compared to simpler baselines.

This is a method-teaching skill, not a workflow step.

## When To Invoke

Invoke this skill when:

- the student does not understand why many trees can outperform one tree
- the workflow proposes a nonlinear model after a linear baseline
- the student needs help understanding interactions and nonlinear structure
- the student assumes random forest should be the automatic default for every tabular problem

## What The Student Should Understand Before Moving On

Before returning to the workflow, the student should understand:

- random forests are ensembles of many decision trees
- they can capture nonlinearities and interactions without manual specification
- they are usually less interpretable than linear models
- they should be used as a comparison to a baseline, not as an automatic replacement for one

## Intuition

A single tree can change a lot if the training sample changes. A random forest reduces that instability by averaging many trees built on slightly different data and feature views.

That makes the model flexible enough to learn bends and interactions, but the final prediction is no longer as easy to narrate coefficient by coefficient.

Simplified math for regression:

`prediction = (tree1 + tree2 + ... + treeB) / B`

Each tree sees a slightly different sample and a random subset of features at each split, which helps the ensemble capture nonlinearities and interactions without making every tree identical.

## Simplest Workflow Role For This Method

Use random forest after a simple baseline when the workflow wants a flexible nonlinear comparison model.

Its beginner role is comparative, not automatic: test whether the extra flexibility materially improves results enough to justify lower interpretability.

## Common Mistakes

- saying a forest is just one large tree
- assuming random forests are as interpretable as linear regression
- treating random forest as the automatic default before a baseline is tried
- forgetting that forests can still overfit or hide important workflow errors
- treating feature importance scores as causal evidence

## Handoff Back To Workflow

Return to the workflow once the student can explain what the ensemble is doing, when nonlinear flexibility is useful, and why random forest should be compared against the baseline rather than assumed to be best.

Suggested handoff:

- in `modeling`, fit random forest after a simpler baseline such as linear regression
- in `model-evaluation`, compare predictive gains against the loss in interpretability
- if feature importance is being treated causally, hand off to `causal-design-check`

## Canonical References

- ISLR: [An Introduction to Statistical Learning](https://www.statlearning.com/)
- ESL: [The Elements of Statistical Learning](https://web.stanford.edu/~hastie/ElemStatLearn/)
