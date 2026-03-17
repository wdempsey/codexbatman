---
name: gradient-boosting
description: Teach gradient boosting as a sequential tree ensemble for strong tabular prediction, with emphasis on tuning sensitivity and workflow order after simpler baselines.
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

# Skill: Gradient Boosting

## Purpose

Teach gradient boosting when a student needs a beginner-safe explanation of sequential error correction, strong tabular prediction, and why this method usually comes after simpler baselines.

This is a method-teaching skill, not a workflow step.

## When To Invoke

Invoke this skill when:

- the workflow proposes a boosted tree model for tabular prediction
- the student confuses boosting with bagging or random forest
- the student asks why gradient boosting usually comes after a baseline
- the student needs help understanding tuning sensitivity and overfitting risk

## What The Student Should Understand Before Moving On

Before returning to the workflow, the student should understand:

- gradient boosting builds models sequentially by correcting earlier errors
- it can perform very strongly on tabular data
- it is more sensitive to tuning and overfitting than a simple baseline
- in a beginner workflow, it usually comes after a baseline and often after random forest

## Intuition

Start with a rough model. Look at where it is wrong. Add a small tree that tries to correct part of that error. Repeat.

Instead of averaging many independent trees, boosting builds a chain of corrections. That is why it can become very accurate, but also why careless tuning can let it chase noise.

Simplified math:

`f(x) = first_tree + learning_rate * second_tree + learning_rate * third_tree + ...`

## Simplest Workflow Role For This Method

Use gradient boosting later in the beginner modeling sequence as a high-performance comparison model for tabular data.

Its simplest role is not "start here." It is "compare this stronger but more tuning-sensitive method after understanding the baseline and, often, after trying random forest."

## Common Mistakes

- confusing boosting with bagging
- thinking each tree is a full standalone model
- ignoring the role of learning rate and depth
- assuming more trees always means better performance
- using boosting before understanding the baseline workflow role

## Handoff Back To Workflow

Return to the workflow once the student can explain sequential error correction, name one tuning risk, and say why boosting typically comes after the baseline and often after random forest in a beginner sequence.

Suggested handoff:

- in `modeling`, evaluate gradient boosting only after establishing a simpler baseline
- in `model-evaluation`, compare gains against added tuning burden and overfitting risk
- if feature importance or partial effects are treated causally, hand off to `causal-design-check`

## Canonical References

- ISLR: [An Introduction to Statistical Learning](https://www.statlearning.com/)
- ESL: [The Elements of Statistical Learning](https://web.stanford.edu/~hastie/ElemStatLearn/)
