---
title: First Session - Predict Housing Prices with Tutor Mode
description: A short warm-up exercise using the Kaggle Housing Prices dataset and tutor mode — for students who want a gentler intro before the full analytics repo example.
---

# First Session - Predict Housing Prices with Tutor Mode

**This is a warm-up exercise.** If you're brand new, you can start here to see what a single tutor-mode exchange feels like — but the main student starting point is [Analytics Repo Example — Student Path](../examples/analytics-repo/student.md), which takes you through the full eight-gate workflow.

This session covers just the first two steps: problem framing and data audit. It's useful if you want to get a feel for how Codex asks questions before you commit to the full sequence.

## What You'll Get Out of This

You'll see how tutor mode structures a coaching exchange — Codex asks for your reasoning before explaining, and the session ends with a problem brief artifact. That's it. The full project (split strategy, baseline model, feature handling, model comparison, evaluation, and workflow trace) is in the [Analytics Repo Example](../examples/analytics-repo/student.md).

## What To Do Right Now

1. copy the first prompt below
2. paste it into Codex
3. stay in tutor mode until you produce a problem brief
4. come back to this page for the next prompt

## Dataset

Use the Kaggle Housing dataset:

- [House Prices: Advanced Regression Techniques](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques)

This dataset predicts housing prices from structured tabular features such as lot size, neighborhood, quality measures, and house characteristics.

Your working objective is to predict `SalePrice` with low RMSE.

## First Codex Prompt

Paste this into Codex:

```text
Use tutor mode to guide me through the first steps of a housing price prediction project.

Dataset: Kaggle Housing Prices
Objective: predict SalePrice with low RMSE.

Start with the workflow skill problem-framing.

Ask me questions instead of giving the full answer immediately.

Guide me step-by-step until we produce a problem brief.
```

## Example Tutor Interaction

Student:

> I want to predict SalePrice from the housing dataset.

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
> - estimating house values
> - identifying underpriced homes
> - predicting price ranges
>
> Write 1-2 sentences.

## Resulting Artifact

Example artifact:

`problem_brief.md`

```md
# Problem Brief

- decision: predict house sale price
- target: SalePrice
- metric: RMSE
- predictors: housing attributes
- risks: missing values, categorical encoding

Next step: data-audit
```

## Continue the Workflow

Next prompt:

```text
Continue in tutor mode.

Switch to workflow skill data-audit.

Help me examine the housing dataset structure and identify potential issues before modeling.
```

## After This Session

Once you've done this warm-up, go to [Analytics Repo Example — Student Path](../examples/analytics-repo/student.md). That page continues from where this leaves off and takes you through all eight gates of the real project — with an interactive demo you can work through step by step before running it in Codex yourself.

When a modeling step introduces a method you don't know yet, tutor mode can pause the workflow, route to a method skill like `linear-regression` or `random-forest`, and then return you to the workflow step.
