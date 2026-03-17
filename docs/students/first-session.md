---
title: First Session - Predict Housing Prices with Tutor Mode
description: A worked student example using the Kaggle Housing Prices dataset and tutor mode across the canonical workflow.
---

# First Session - Predict Housing Prices with Tutor Mode

## What You Will Learn

This first session shows how to run Codex inside this repository, how workflow skills structure a data science project, and how tutor mode helps you learn the workflow instead of skipping straight to answers.

You will move through the canonical sequence:

problem framing  
data audit  
EDA  
baseline modeling  
evaluation  
experiment log

The point is not to finish the whole project in one sitting. The point is to learn how the workflow, tutor overlay, and method skills work together on a real dataset.

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

## What Comes Next

The next workflow skills are:

- [problem-framing](../workflows/data-science/problem-framing.md)
- [data-audit](../workflows/data-science/data-audit.md)
- [eda-plan](../workflows/data-science/eda-plan.md)
- [modeling](../workflows/data-science/modeling.md)
- [model-evaluation](../workflows/data-science/evaluation.md)
- [experiment-log](../workflows/data-science/experiment-log.md)

These pages correspond to the canonical workflow backbone.

When a modeling step introduces a method you do not know yet, tutor mode can pause the workflow, route to a method skill such as `linear-regression` or `random-forest`, and then return you to the workflow step.
