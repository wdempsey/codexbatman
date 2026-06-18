---
name: debug-model-failure
description: Systematic diagnostic loop for unexpected model behavior — metric degrades, results flip between sessions, or performance looks implausibly good or bad. Reproduce the failure, minimise it, hypothesise a cause, instrument to test the hypothesis, fix the smallest thing, verify it held. Use when a model produces surprising output and the cause is unclear. Distinct from debug-analysis-notebook (which handles notebook execution errors) — this skill handles semantic failures where code runs but the results are wrong.
category: data-science
status: active
stage: modeling
role_compatibility:
  - student
  - data scientist
inputs:
  - model or evaluation output showing unexpected behavior
  - description of what was expected vs observed
  - recent changes to the pipeline
outputs:
  - root cause statement
  - minimal fix
  - regression test or check to prevent recurrence
depends_on:
  - data-audit
  - modeling
recommended_next:
  - experiment-log
  - model-evaluation
---

# Skill: Debug Model Failure

## Purpose

Diagnose semantic model failures — cases where the code runs but the output is wrong or surprising.

This is different from fixing a Python error. The pipeline executes. The numbers come out. But something is off: performance dropped, results look too good, the metric flipped, or a feature importance changed dramatically with no obvious cause.

Adapted from Matt Pocock's `diagnose` pattern for data science analysis.

## The Loop

Run these stages in order. Do not jump to fixing before you've reproduced and minimised.

**1. Reproduce**
Can you make the failure happen again from scratch? Run the pipeline end to end with a fixed seed and confirm the problem is consistent. If it isn't reproducible, you're chasing a fluke — document it as noise and move on.

**2. Minimise**
What is the smallest version of the pipeline that still shows the problem? Strip out features, reduce to a single model, shrink to a small data subset. The goal is to isolate the failure to one component or transformation.

**3. Hypothesise**
Given the minimal reproduction, what are the two or three most likely causes? Write them down before testing any of them. Common candidates for data science failures:

- **Leakage**: a feature computed from the test set is visible during training
- **Split contamination**: preprocessing ran before the split, not after
- **Target shift**: the label distribution in train and test is different from what was expected
- **Evaluation mismatch**: the metric is computed on the wrong subset (e.g., predicted on train, not test)
- **Scale/encoding error**: a transformation applied inconsistently across splits
- **Seed dependency**: results are unstable across seeds, indicating the model is fitting noise

**4. Instrument**
Add a minimal diagnostic to test the top hypothesis. A shape check, a distribution plot, a print of train vs test label rates. Do not refactor the pipeline while diagnosing.

**5. Fix**
Change the smallest thing that resolves the hypothesis. One fix at a time. If fixing one thing reveals another problem, document it and loop back to step 1.

**6. Verify**
Confirm the failure is gone with the same minimal reproduction from step 2. Then run the full pipeline and confirm the fix held. Log the root cause in `experiment_log.md` so a future session knows what happened.

## Common Root Causes In Order Of Frequency

1. Preprocessing happened before the train/test split — target encoding, imputation fitted on full dataset
2. A feature column contains post-target information — a timestamp, an outcome proxy, a derived field
3. The evaluation metric is applied to the training set by mistake
4. Class weights or sample weights applied inconsistently between train and evaluation
5. The feature importance or coefficient changed because the scale of a feature changed (check normalization)

## Output

After completing the loop, write a brief root cause statement:

```
Failure: [what went wrong]
Root cause: [what caused it]
Fix applied: [what was changed]
Verification: [how it was confirmed fixed]
Added to experiment_log: [yes/no, entry number]
```

## What This Skill Does Not Cover

Code-level notebook execution errors (import failures, shape mismatches, index errors) are handled by `debug-analysis-notebook`. Use this skill when the code runs cleanly but the model behavior is wrong.
