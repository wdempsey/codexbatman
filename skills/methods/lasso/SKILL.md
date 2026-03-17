---
name: lasso
description: Teach lasso as a sparse regularized regression method that can shrink coefficients and remove some predictors entirely.
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

# Skill: Lasso

## Purpose

Teach lasso when a student needs to understand sparsity, feature selection intuition, and how lasso differs from ridge.

This is a method-teaching skill, not a workflow step.

## When To Invoke

Invoke this skill when:

- the workflow proposes a sparse regularized model
- the student asks why some coefficients become exactly zero
- the student wants a beginner comparison of lasso versus ridge
- the student is overinterpreting selected variables as proof of importance

## What The Student Should Understand Before Moving On

Before returning to the workflow, the student should understand:

- lasso encourages sparsity, which means a simpler model with some coefficients set to zero
- lasso can act like feature selection, but that selection is data-dependent
- lasso differs from ridge because ridge shrinks coefficients without usually removing predictors
- correlated predictors can make lasso selection unstable

## Intuition

Lasso tells the model: fit the outcome, but pay a price for keeping too many nontrivial coefficients.

That pressure can make weaker predictors drop out. The result is often easier to read than ridge, but it can also be less stable when several predictors carry similar information.

Simplified math:

`sum(observed - predicted)^2 + lambda * sum(abs(bj))`

The `abs(bj)` penalty is what pushes some coefficients exactly to zero.

## Simplest Workflow Role For This Method

Use lasso after the plain linear baseline when the workflow wants a selective regularized comparison for a continuous target.

Its simplest role is to test whether a sparse model performs well enough to justify a simpler feature set. It should not replace understanding the baseline.

## Common Mistakes

- saying lasso discovers the truly important variables
- ignoring instability when predictors are strongly correlated
- treating zero coefficients as proof of causal irrelevance
- skipping the linear baseline and moving directly to selection
- forgetting that tuning `lambda` changes the selected model

## Handoff Back To Workflow

Return to the workflow once the student can explain sparsity, compare lasso with ridge, and name one risk of using lasso with correlated predictors.

Suggested handoff:

- in `modeling`, fit lasso as a sparse regularized comparison after linear regression
- in `model-evaluation`, compare performance and note whether sparsity materially helps
- if variable selection starts being interpreted causally, hand off to `causal-design-check`

## Canonical References

- ISLR: [An Introduction to Statistical Learning](https://www.statlearning.com/)
- ESL: [The Elements of Statistical Learning](https://web.stanford.edu/~hastie/ElemStatLearn/)
