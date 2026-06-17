# For Students

**This is for you if you're learning data science workflows for the first time and want Codex to coach your reasoning rather than just hand you answers — while still producing real project artifacts.**

## Start Here

Begin with [**Analytics Repo Example - Student Path**](../examples/analytics-repo/student.md). It walks you through a real Kaggle-style housing project step by step, with Codex coaching your reasoning instead of giving away the answer.

You use the same canonical data science workflow as practitioners. What changes is how Codex helps you move through it — more prompting, more hints, more checks for understanding, and more attempt-before-answer behavior. You don't need to learn the whole architecture first. Start with the guided session, then come back to the workflow pages after you've seen one concrete example.

If you want a shorter warm-up first, open [First Session - Predict Housing Prices with Tutor Mode](first-session.md) and then return to the analytics repo example.

## What Changes In Student Mode

Student mode changes how Codex teaches, not the standards of the work. Codex asks for your attempt before giving a full answer, leads with hints before solutions, and focuses feedback on your reasoning rather than just whether the output is correct. Workflow artifacts still matter — learning includes learning disciplined process. Under the hood this uses student overlays on top of the shared workflow skills, but you don't need to memorize that structure before starting.

## Typical Student Outputs

- problem frames
- data audit notes
- bounded exploration plans
- experiment logs
- reflection on what changed and why

## Example Student Artifact

This is the kind of artifact the student path should leave behind early:

```md
# problem_frame.md

- target: SalePrice
- metric: RMSE
- decision context: estimate likely sale price from structured housing features
- first risks: missing values, leakage, overfitting to leaderboard habits
```

The point is not polished prose. The point is durable project memory that proves the learner framed the task before modeling.

## Don't Worry About These Yet

If you're brand new, skip the full skill catalog, the build and customization pages, the manager workflow pages, and any companion or reference sections. None of those are for your first session — come back to them once you've seen the workflow in action.

## Student-Focused Skills

The four skills that matter most when you're starting out:

- `tutor-mode` — activates attempt-before-answer coaching; Codex asks what you think before explaining
- `hint-ladder` — gives you progressive hints instead of jumping straight to the solution
- `problem-framing` — guides you through defining target, metric, and risk before touching the data
- `repo-bootstrap-student` — scaffolds the repository structure so you're not starting from a blank folder

The full skill catalog (`misconception-diagnosis`, `exercise-generator`, `data-audit`, `eda-plan`, `experiment-log`, `causal-design-check`) is in the [Skill Library](../setup/skill-reference.md) when you're ready.

## Where To Go Next

If you haven't started yet, go to [Analytics Repo Example - Student Path](../examples/analytics-repo/student.md) — that's the right first move.

After your first session, read [Core Data Science Workflow](../workflows/data-science/index.md) to see the full shared sequence, then browse [Examples](../examples/index.md) to see how the same backbone looks across learning, execution, and manager modes.
