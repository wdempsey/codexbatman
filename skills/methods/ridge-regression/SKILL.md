---
name: ridge-regression
description: Teach ridge regression as a regularized linear baseline for continuous prediction when coefficient shrinkage and multicollinearity stabilization matter.
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

# Skill: Ridge Regression

## Purpose

Teach ridge regression as the first regularized extension of linear regression when a student needs to understand shrinkage, stability, and the bias-variance tradeoff.

This is a method-teaching skill, not a workflow step.

## When To Invoke

Invoke this skill when:

- the student asks what regularization is
- linear regression feels unstable because predictors overlap heavily
- the workflow proposes ridge as a baseline upgrade for multicollinearity
- the student confuses shrinkage with feature selection

## What The Student Should Understand Before Moving On

Before returning to the workflow, the student should understand:

- ridge adds a penalty that shrinks coefficients toward zero
- shrinkage can improve stability on new data even if it adds some bias
- ridge is useful when predictors are correlated and ordinary regression is unstable
- ridge usually keeps predictors in the model rather than selecting a small subset

## Intuition

Ridge regression tells the model: fit the data, but do not rely on extreme coefficient values unless the evidence is strong.

That extra restraint helps when many predictors are telling similar stories. Instead of letting coefficients swing wildly, ridge spreads weight more smoothly across them.

Simplified math:

`sum(observed - predicted)^2 + lambda * sum(bj^2)`

Larger `lambda` means more shrinkage. The bias-variance tradeoff is the key idea: accept a little more bias to get lower variance and steadier predictions.

## Simplest Workflow Role For This Method

Use ridge after plain linear regression when the workflow needs a regularized comparison model for a continuous target.

Its simplest role is not feature discovery. It is stability: a defensible next step when the baseline is too wobbly because predictors are correlated.

## Common Mistakes

- saying ridge selects variables by setting coefficients to zero
- ignoring the bias-variance tradeoff and treating shrinkage as automatically bad
- forgetting that standardization is usually important
- treating `lambda` as a model coefficient
- choosing ridge before first understanding the linear baseline

## Handoff Back To Workflow

Return to the workflow once the student can explain why ridge helps with multicollinearity, what shrinkage means, and why ridge usually does not perform feature selection.

Suggested handoff:

- in `modeling`, fit ridge after linear regression as a stabilized comparison
- in `model-evaluation`, compare predictive performance and calibration against the unregularized baseline
- if the student begins making causal claims from shrunken coefficients, hand off to `causal-design-check`

## Canonical References

- ISLR: [An Introduction to Statistical Learning](https://www.statlearning.com/)
- ESL: [The Elements of Statistical Learning](https://web.stanford.edu/~hastie/ElemStatLearn/)
