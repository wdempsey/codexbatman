---
name: cross-validation
description: Teach cross-validation as the canonical answer to overfitting evaluation — why training error is misleading, how k-fold CV works, how to choose k, and how to use CV correctly without leaking preprocessing steps. Use when a student uses training error to judge a model, when a student asks how to choose between models, or when the analysis plan needs a validation strategy beyond a single holdout split. ISLR Chapter 5.
category: methods
status: active
method_family: resampling
prerequisites:
  - problem-framing
  - data-audit
related_workflow_skills:
  - modeling
  - model-evaluation
  - analysis-plan (split strategy)
role_compatibility:
  - student
  - data scientist
---

# Skill: Cross-Validation

## Purpose

Teach cross-validation when a student uses training error to judge a model or needs a principled way to compare models without touching the test set.

This is a method-teaching skill, not a workflow execution step. After this skill, the student should be able to apply CV correctly within the `modeling` and `model-evaluation` gates.

## ISLR Reference

Chapter 5: Resampling Methods  
[statlearning.com](https://www.statlearning.com/) — freely available.

## The Core Problem CV Solves

Training error is optimistic. A model evaluated on the same data it was trained on will almost always look better than it actually performs on new data. The more flexible the model, the worse this overestimation gets.

The validation set approach — holding out a fixed fraction of data — reduces that optimism, but it's noisy: the performance estimate depends heavily on which observations happened to land in the holdout set.

Cross-validation repeats the evaluation across multiple holdout partitions and averages, reducing that noise while keeping the test set clean.

## Intuition

Imagine grading 30 students on a multiple-choice exam. If you let each student check their own work, every answer looks correct. If you shuffle papers and have a neighbor grade each one, you get a more honest picture.

K-fold CV does this for the model: the dataset is split into k groups. The model trains on k–1 groups and is evaluated on the remaining one. This repeats k times, with a different group held out each time. The final CV estimate is the average across k folds.

## The Three Variants (ISLR Ch. 5)

**Validation set approach**: one random split into train and validation. Fast, but high variance — the result depends heavily on which observations ended up where.

**k-fold CV**: split into k equal groups. Usual choices: k = 5 or k = 10. Lower k = higher bias, lower variance. Higher k = lower bias, higher variance (and more computation). k = 5 is the standard starting point for tabular data.

**Leave-one-out CV (LOOCV)**: k = n. Each observation is its own test set. Very low bias but high variance and computationally expensive. Rarely used in practice except for small datasets or when a single observation is high-leverage.

## The Critical Rule: Preprocessing Inside The Fold

This is the most common mistake in student implementations.

**Wrong**: impute missing values on the full dataset, then run CV.  
**Right**: run CV, and inside each fold, impute on the training fold only.

If preprocessing (imputation, scaling, encoding, feature selection) is fitted on the full dataset before CV, test-fold information leaks into training. The CV estimate will be optimistic.

The fix: treat preprocessing as part of the model. In scikit-learn, use `Pipeline` to chain preprocessing and the model — then pass the pipeline to `cross_val_score`. The pipeline is fitted fresh on each fold's training data.

```python
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

pipe = Pipeline([
    ('impute', SimpleImputer(strategy='median')),
    ('model', LogisticRegression())
])

cv_scores = cross_val_score(pipe, X_train, y_train, cv=5, scoring='roc_auc')
print(f"CV ROC-AUC: {cv_scores.mean():.3f} ± {cv_scores.std():.3f}")
```

The test set is never touched during this process.

## Common Student Mistakes

- Evaluating on training data and calling it CV
- Fitting a scaler on the full dataset, then running CV
- Using CV scores to select features, then re-evaluating on the same folds (another leak)
- Confusing CV with the final test evaluation — CV guides model selection; the held-out test set provides the final honest estimate

## Connection To The Workflow

**In `analysis_plan.md`**: document whether you're using a single holdout split or k-fold CV, and why. For small datasets (< 500 rows), CV is usually preferable because a single split wastes too much data.

**In `modeling`**: use CV inside the training set to compare candidate models. Never use it on the test set.

**In `model-evaluation`**: the final reported performance is the held-out test set estimate, not the CV score. CV guides which model to evaluate; the test set provides the honest estimate.

## What The Student Should Understand Before Moving On

- Why training error is an optimistic estimate
- How k-fold CV reduces variance compared to a single validation split
- Why preprocessing must happen inside the fold, not before it
- That CV is for model selection — the final evaluation uses the held-out test set

## Handoff Back To Workflow

Return to `modeling` once the student can implement CV correctly using a pipeline and can explain why preprocessing must be inside the fold.

If they're choosing between candidate models using CV, hand off to `model-evaluation` once a model is selected.
