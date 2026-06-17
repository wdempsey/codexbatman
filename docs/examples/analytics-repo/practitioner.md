# Analytics Repo Example - Practitioner Path

Use this page when the analyst wants the same standards, but a shorter and more execution-oriented path.

## Practitioner Goal

Set up and advance a real analytics repository with durable artifacts and fast forward progress.

The practitioner path assumes the analyst already knows the basics of:

- target definition
- validation logic
- baseline-first modeling
- experiment tracking

## What Codex Should Do

Codex should:

- move directly through the workflow gates
- draft artifacts quickly for review
- enforce prediction-time and leakage discipline
- keep the repo memory current after each working block

Codex should not:

- skip problem framing
- begin modeling before the audit is acceptable
- optimize prematurely without a recorded baseline

## Suggested Practitioner Sequence

1. Initialize the project with `project-bootstrap`.
2. Draft `problem_frame.md` with target, metric, decision context, and stop conditions.
3. Run `data-audit` and document missingness, feature classes, and leakage risks.
4. Define the split strategy and baseline model in `analysis_plan.md`.
5. Fit the baseline and one or two justified candidate models.
6. Record every run in `experiment_log.md`.
7. Draft `model_card.md` for the best current model.
8. Update `workflow_trace.md` and `PROJECT_STATE.md` before ending the session.

## Example Practitioner Prompt

```text
Set up and execute a housing-price analytics repository using the Codex Batman backbone.

Dataset: House Prices: Advanced Regression Techniques
Goal: predict SalePrice

Work in practitioner mode.
Be direct and artifact-oriented.
Do not skip workflow gates.
Start with project-bootstrap, then move to problem-framing and data-audit.
```

## Minimum Practitioner Outputs

- a clean repo scaffold
- a framed problem with metric and prediction target
- a data audit with leakage notes
- a baseline model result
- a logged comparison against at least one candidate
- a model card
- an updated project state and workflow trace

## What Success Looks Like

Success means the repo is handoff-ready.

Another analyst should be able to open the folder and answer:

- what problem is being solved
- what data is in scope
- what has been tried
- what model currently leads
- what should happen next

## What To Open Next

- [Analytics Repo Example](index.md)
- [For Researchers & Data Scientists](../../data-scientists/index.md)
- [Core Data Science Workflow](../../workflows/data-science/index.md)
