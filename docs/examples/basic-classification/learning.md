# Basic Classification — Learning Lens

Use this lens when the goal is to teach how to reason through the workflow.

## What The Learner Should Understand

- why the target must be defined before the model
- why leakage matters even in a simple student-risk example
- why a baseline model comes first
- why the experiment log exists
- why the model card matters even for a small project

## Reflection Questions

1. What is the actual decision this classifier supports?
2. What information would be unavailable at prediction time?
3. Why is a simple baseline useful before trying more complex models?
4. What could go wrong if the team skips the data card?

## Artifact Purpose

- `problem_frame.md` keeps the task tied to the advising decision.
- `data_card.md` records what fields exist and whether attendance history could leak future information.
- `analysis_plan.md` bounds the workflow before random experimentation.
- `experiment_log.md` records each attempted classifier.
- `model_card.md` explains how the classifier should and should not be used.

## Tutor-Style Takeaway

The main lesson is that "small ML task" is not an excuse to skip workflow discipline.
