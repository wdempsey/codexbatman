# Analytics Repo Example - Student Path

Use this page when the learner should build the project step by step without Codex simply revealing the final answer.

## Student Goal

Learn how to build a real analytics repo while still doing the reasoning yourself.

The student path should feel scaffolded, but not fake.

You are still building:

- a real repo
- real workflow artifacts
- a real baseline modeling sequence

## What Codex Should Do

Codex should:

- ask for short attempts before full answers
- explain why each artifact exists
- keep the learner inside the workflow order
- pause to teach unfamiliar methods before continuing

Codex should not:

- silently write the whole solution end to end
- skip straight from dataset to tuned model
- collapse the repo structure into one notebook and one chat

## Suggested Student Sequence

1. Start with `repo-bootstrap-student` so the learner creates the repository and understands the folder structure.
2. Switch to `problem-framing` in tutor mode and ask the learner to define the target, decision, metric, and risks.
3. Switch to `data-audit` and have the learner inspect missingness, feature types, and likely leakage risks.
4. Ask the learner to propose a train/test split before any model is fit.
5. Have the learner describe a baseline model choice before Codex suggests alternatives.
6. Record the run in `experiment_log.md`.
7. Help the learner draft a short `model_card.md`.
8. End by updating `workflow_trace.md` with what was learned and what comes next.

## Example Tutor Prompt

```text
Use tutor mode to help me build a housing-price analytics repository step by step.

Project type: Kaggle-style tabular regression
Dataset: House Prices: Advanced Regression Techniques
Goal: predict SalePrice

Use the shared Codex Batman workflow backbone.

Do not give me the full solution immediately.
Ask for my attempt first whenever the next step is still learnable.
Start with repo-bootstrap-student, then move into problem-framing.
```

## Minimum Student Artifacts

By the end of the first serious pass, the learner should have:

- `PROJECT_STATE.md`
- `analysis/problem_frame.md`
- `data/data_card.md`
- `analysis/analysis_plan.md`
- `runs/experiment_log.md`
- `reports/model_card.md`
- `memory/workflow_trace.md`

## What Success Looks Like

Success is not "the student got a great leaderboard score."

Success is:

- the learner can explain the problem
- the learner can explain the split
- the learner knows why leakage matters
- the repo has durable artifacts
- the next session can continue from project state instead of chat memory

## What To Open Next

- [Analytics Repo Example](index.md)
- [First Session - Predict Housing Prices with Tutor Mode](../../students/first-session.md)
- [For Students](../../students/index.md)
