# For Students

**Use this path if you want to learn data science workflows through guided practice without losing the discipline of real project artifacts.**

## Start Here

If you are new to this system, begin with:

[**First Session - Predict Housing Prices with Tutor Mode**](first-session.md)

If you only open one page today, open [First Session](first-session.md).

## This Path Is For You If

- you are learning data science workflows for the first time
- you want Codex to coach your reasoning instead of just giving answers
- you need hints, checks for understanding, and structured practice
- you still want to produce real project artifacts while learning

## Role Summary

Students use the same canonical data science workflow as practitioners, but with a scaffolded delivery style.

The workflow logic does not change by role. What changes is how Codex helps you move through it: more prompting, more hints, more checks for understanding, and more attempt-before-answer behavior.

You do not need to learn the whole architecture first.

Start with the guided session, then come back to the workflow pages after you have seen one concrete example.

## What Changes In Student Mode

Student mode changes how Codex teaches, not the standards of the work.

- Codex asks for your attempt before giving the full answer.
- Hints usually come before worked solutions.
- Feedback focuses on reasoning quality, not just correctness.
- Workflow artifacts still matter, because learning includes learning disciplined process.

Under the hood, this uses student overlays on top of the shared workflow skills. You do not need to memorize that structure before starting.

## Recommended First Three Steps

1. Start with [First Session](first-session.md) if you want a concrete guided walkthrough.
2. Read [Core Data Science Workflow](../workflows/data-science/index.md) to see the full shared backbone.
3. Use the [Skill Library](../setup/skill-reference.md) when you want to understand which student overlays wrap that backbone.

## Recommended Sequence

Follow this path in order if you are new:

1. [First Session](first-session.md)
2. [Core Data Science Workflow](../workflows/data-science/index.md)
3. [Skill Library](../setup/skill-reference.md)

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

## What To Ignore For Now

If you are brand new, you can safely ignore these until after the first guided session:

- the full skill catalog
- most build/customization pages
- advanced manager workflow pages
- older companion/reference sections

## Student-Focused Skills

- `tutor-mode`
- `hint-ladder`
- `misconception-diagnosis`
- `exercise-generator`
- `repo-bootstrap-student`
- `problem-framing`
- `data-audit`
- `eda-plan`
- `experiment-log`
- `causal-design-check`

## If You Want A Real Repo Example

Open [Analytics Repo Example - Student Path](../examples/analytics-repo/student.md).

That page shows how the student path should build a real Kaggle-style housing analysis repo without Codex simply giving the solution away.

## Where To Go Next

- Go straight to [First Session](first-session.md) if you have not done it yet.
- Use [Choose Your Role](../roles/index.md) if you want to compare this path with the researcher/data scientist or manager paths.
- Read [Core Data Science Workflow](../workflows/data-science/index.md) after the first session if you want to see the full shared sequence.
- Use the [Skill Library](../setup/skill-reference.md) after the first session if you want the shared catalog of workflow skills, overlays, and manager tools.
- Review [Examples](../examples/index.md) after the first session to see how the same backbone looks in learning, execution, and manager modes.
- Use [How Skills Work](../system/skills-explained.md) if you want the mental model for how workflow skills, tutor overlays, and method skills fit together.
