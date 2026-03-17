---
name: linear-regression
description: Teach the intuition, baseline role, assumptions, and beginner tradeoffs of linear regression as the default starting point for continuous prediction.
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

# Skill: Linear Regression

## Purpose

Teach linear regression as the simplest serious baseline for predicting a continuous outcome.

This is a method-teaching skill, not a workflow step. Use it when a learner needs a compact explanation before modeling continues.

## When To Invoke

Invoke this skill when:

- the workflow proposes a baseline model for a numeric target
- the student does not understand coefficients or directionality
- the student asks why linear regression comes before more complex models
- the student needs help interpreting residuals or the idea of a fitted line

## What The Student Should Understand Before Moving On

Before returning to the workflow, the student should understand:

- linear regression is a baseline method for continuous prediction
- coefficients describe direction and size of association in model units
- linearity is an approximation, not a claim that the world is perfectly linear
- residuals are the errors left after the model makes its prediction
- this method is usually the default comparison point before trying more complex models

## Intuition

Linear regression draws the best straight-line summary of how predictors and an outcome move together.

For one predictor, the line slopes up or down depending on whether larger `x` tends to go with larger or smaller `y`. For several predictors, the model still behaves like a weighted sum, just in more than one dimension.

Residual thinking is central: the model is useful when its misses are small enough to be informative, and those misses tell you what the straight-line approximation does not capture.

Simplified math:

`y_hat = b0 + b1 x1 + b2 x2 + ... + bp xp`

`residual = observed - predicted`

The model chooses coefficients that make squared residuals as small as possible.

## Simplest Workflow Role For This Method

Use linear regression as the first defensible baseline when the workflow reaches modeling for a continuous target.

Its role is not to win every leaderboard. Its role is to give the student a transparent reference point before ridge, lasso, random forest, or gradient boosting are considered.

## Common Mistakes

- treating a coefficient as causal without a causal design
- assuming linearity means reality must be exactly straight-line
- forgetting that coefficient interpretation depends on units and coding
- ignoring residuals and looking only at `R^2`
- skipping the baseline and jumping straight to a more complex model

## Handoff Back To Workflow

Return to the workflow once the student can explain why linear regression is the baseline, what a coefficient means, and what residuals represent.

Suggested handoff:

- if the workflow is in `modeling`, fit linear regression first and record it as the baseline
- if the workflow is in `model-evaluation`, compare more complex models against this baseline
- if causal claims begin to appear, hand off to `causal-design-check` before interpreting coefficients as effects

## Canonical References

- ISLR: [An Introduction to Statistical Learning](https://www.statlearning.com/)
- ESL: [The Elements of Statistical Learning](https://web.stanford.edu/~hastie/ElemStatLearn/)
