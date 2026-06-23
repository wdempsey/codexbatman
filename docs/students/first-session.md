---
title: First Session - Predict Housing Prices with Tutor Mode
description: A short warm-up exercise using California Housing data and tutor mode — introduces problem framing and data audit before the full linear regression learning lens.
---

# First Session - Predict Housing Prices with Tutor Mode

**This is a warm-up for the [Linear Regression — Learning Lens](../examples/analytics-repo/learning.md).** It covers just the first two steps — problem framing and data audit — so you can see how Codex asks questions before you commit to the full 7-gate sequence. Same dataset, same topic, much shorter.

If you'd rather start with classification instead, go directly to [Basic Classification — Learning Lens](../examples/basic-classification/learning.md).

## What You'll Get Out of This

You'll see how tutor mode structures a coaching exchange: Codex asks for your reasoning before explaining, and the session ends with a `problem_frame.md` artifact. The full regression project — split strategy, baseline OLS, multicollinearity handling, ridge/lasso comparison, evaluation, and workflow trace — is in [Linear Regression — Learning Lens](../examples/analytics-repo/learning.md).

## What To Do Right Now

1. Copy the first prompt below
2. Paste it into Codex
3. Stay in tutor mode until you produce a problem brief
4. Come back for the next prompt

## Dataset

California Housing ships with scikit-learn — no download or login needed:

```python
from sklearn.datasets import fetch_california_housing
data = fetch_california_housing(as_frame=True)
df = data.frame
df.to_csv("california_housing.csv", index=False)
```

20,640 census tracts, 8 features, target is median house value per tract (in units of $100,000, capped at $500K).

## First Codex Prompt

```text
Use tutor mode to guide me through the first steps of a housing price prediction project.

Dataset: California Housing (sklearn fetch_california_housing, saved to california_housing.csv)
Target: MedHouseVal — median house value per census tract (units: $100,000, capped at $500K)
Objective: predict median house value with low RMSE.

Start with the workflow skill problem-framing.

Ask me questions instead of giving the full answer immediately.

Guide me step-by-step until we produce a problem brief.
```

## Example Tutor Interaction

Student:

> I want to predict median house value from California census data.

Codex:

> Underlying skill: problem-framing
>
> Goal: define the decision and modeling objective.
>
> Question:
>
> What decision would this model support?
>
> Examples:
> - estimating property values for a housing agency
> - identifying undervalued census tracts for investment
> - predicting price ranges for policy modeling
>
> Write 1-2 sentences.

## Resulting Artifact

Example artifact:

`problem_frame.md`

```md
# Problem Frame

- decision: predict median house value per census tract
- target: MedHouseVal ($100K units, $500K ceiling)
- metric: RMSE
- predictors: income, house age, rooms, bedrooms, population, occupancy, lat/lon
- risks: ceiling artifact at $500K distorts high-end predictions, geographic multicollinearity (lat/lon correlated with income)

Next step: data-audit
```

## Continue the Workflow

Next prompt:

```text
Continue in tutor mode.

Switch to workflow skill data-audit.

Help me examine the California Housing dataset structure and identify potential issues before modeling.
```

## After This Session

Go to [Linear Regression — Learning Lens](../examples/analytics-repo/learning.md). That page takes you through all 7 gates of the full California Housing regression project — with an interactive demo at each step and real artifact examples.

After linear regression, the natural next step is [Basic Classification — Learning Lens](../examples/basic-classification/learning.md) — same 7-gate backbone, different problem type (binary outcome, ROC-AUC metric).

When a modeling step introduces a method you don't know, tutor mode can pause the workflow, route to a method skill like `linear-regression` or `ridge-regression`, and return you to the workflow step.
