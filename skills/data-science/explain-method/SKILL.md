---
name: explain-method
description: Zoom out and explain why a modeling method fits the current problem — assumptions, when it breaks, what the alternatives are, and why this one was chosen over them. Use in tutor mode when a student asks why a method is being used, when a data scientist needs to justify a choice in a model card, or when a method has been applied without documenting its rationale. Adapted from Matt Pocock's zoom-out pattern for data science method selection.
category: data-science
status: active
stage: modeling
role_compatibility:
  - student
  - data scientist
  - data science manager
inputs:
  - method name
  - current problem context (decision, target, metric)
  - what came before in the workflow (baseline, data audit findings)
outputs:
  - method rationale
  - key assumptions and when they break
  - comparison to the most relevant alternative
  - one-sentence model card justification
depends_on:
  - problem-framing
  - modeling
recommended_next:
  - model-evaluation
  - model-prototype
related_method_skills:
  - random-forest
  - linear-regression
  - lasso
  - gradient-boosting
---

# Skill: Explain Method

## Purpose

Explain why a method fits the current problem — not in the abstract, but in the context of this specific analysis.

The goal is not a textbook definition. It is a situated justification: given this decision, this data, and this baseline result, why does this method make sense as the next thing to try?

## When To Invoke

Use this skill when:

- a student sees a method being used and asks "why are we using this instead of X?"
- a practitioner needs to write the model card justification for a choice
- a method was applied without documenting the reasoning
- a manager asks why one model was chosen over another

## Structure

Answer these four questions for the method in context:

**1. What does this method do that the baseline cannot?**
The baseline exists — usually logistic regression or linear regression. This method is being tried because there's a specific limitation the baseline has. Name it concretely.

Example: "Logistic regression cannot capture the interaction between age and cholesterol level without manually engineering a feature for it. Random forest learns those interactions directly from the data."

**2. What does this method assume, and does the data satisfy those assumptions?**
Every method has assumptions. State the two or three most load-bearing ones and briefly check whether the current data violates them.

Example assumptions to address by method family:
- Linear models: linear relationship, no multicollinearity, homoskedastic residuals
- Tree ensembles: no assumptions about linearity, but sensitive to class imbalance and feature scale doesn't matter
- SVMs: assumes a separating hyperplane exists; sensitive to feature scale
- Neural networks: assumes enough data to generalize; sensitive to initialization

**3. What is the most relevant alternative, and why was it not chosen first?**
There is usually one obvious competitor. Name it and explain why this method ranks ahead of it for this problem.

This is not a comprehensive comparison — just the most useful contrast.

**4. What would cause this method to fail here?**
State the specific failure mode that would be visible in the evaluation results if the method is wrong for this problem.

## Output Format

Produce a brief explanation in plain prose (3–5 sentences per question). End with a one-sentence justification suitable for the model card:

> Method justification: [method] was chosen over [baseline/alternative] because [specific reason tied to this problem's data and decision context].

## Connecting To ISLR

If the method corresponds to an ISLR chapter, reference it for deeper reading:

| Method | ISLR Chapter |
|---|---|
| Linear/logistic regression | Chapter 3–4 |
| Cross-validation | Chapter 5 |
| Ridge / Lasso | Chapter 6 |
| Splines / GAMs | Chapter 7 |
| Trees / Random Forest / Boosting | Chapter 8 |
| SVM | Chapter 9 |
| PCA / Clustering | Chapter 12 |

See the [ISLR resource skill](../../resources/islr/SKILL.md) for chapter-level method explanations.
