# For Students

**This is for you if you're learning data science workflows for the first time and want Codex to coach your reasoning rather than just hand you answers — while still producing real project artifacts.**

## Start Here

Begin with [**Basic Classification — Learning Lens**](../examples/basic-classification/learning.md). It walks you through predicting cardiac risk from clinical data — 303 patients, 7 workflow gates, one binary question: should this patient be referred for further cardiac evaluation? Codex asks for your reasoning at each step before revealing its output.

You use the same canonical data science workflow as practitioners. What changes is how Codex helps you move through it — more prompting, more hints, more checks for understanding, and attempt-before-answer at every gate. You don't need to learn the whole architecture first. Start with the guided session, then come back to the workflow pages after you've seen one concrete example.

If you'd rather start with linear regression, open [First Session — Predict Housing Prices with Tutor Mode](first-session.md) — a two-gate warm-up on California Housing that feeds directly into [Linear Regression — Learning Lens](../examples/analytics-repo/learning.md).

## What You Should Already Know

The guided sessions assume you can read and run basic Python — variables, functions, and a rough idea of what a pandas DataFrame is. No statistics background is required; that's what tutor mode teaches.

If the Python itself is the blocker, spend an evening with the free [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/) (chapters 2–3: NumPy and pandas) or [Kaggle Learn](https://www.kaggle.com/learn)'s short Python and pandas courses, then come back.

## What Changes In Student Mode

Student mode changes how Codex teaches, not the standards of the work. Codex asks for your attempt before giving a full answer, leads with hints before solutions, and focuses feedback on your reasoning rather than just whether the output is correct. Workflow artifacts still matter — learning includes learning disciplined process. Under the hood this uses student overlays on top of the shared workflow skills, but you don't need to memorize that structure before starting.

## Session Lifecycle

Each student session has three phases. You don't need to set anything up — Codex handles it.

**Start of session:** Codex asks your name and checks for a student profile in `memory/students/{name}/`. If you're new, it walks you through a quick registration (name, role, background, learning goals). If you're returning, it surfaces your last session topic, any open questions you left unresolved, and your current mastery levels for the topic you're about to work on.

**During the session:** Socratic mode is on by default — expect questions before answers. At each workflow gate, Codex asks what you think before explaining. If you're stuck, it offers hints rather than solutions. When you can explain a concept in your own words (the Feynman check), it marks that topic as mastered.

**End of session:** Type `/wrap` to close. Codex drafts a session summary — what you covered, one win, any misconception corrected, open questions carried forward — and proposes mastery level updates. You confirm before anything is written. Type `/flag-skill` at any point to flag a technique that seemed broadly useful; it gets logged to your `flagged-skills.md` for auditor review.

## Typical Student Outputs

- problem frames
- data audit notes
- bounded exploration plans
- experiment logs
- session summaries with open questions

## Example Student Artifact

This is the kind of artifact the student path should leave behind early:

```md
# problem_frame.md

- target: heart disease present (binary: 0 / 1+)
- metric: ROC-AUC
- decision context: cardiac referral triage — should this patient proceed to further evaluation?
- first risks: leakage (stress-test features run after referral), missingness (thal, ca), threshold choice
```

The point is not polished prose. The point is durable project memory that proves the learner framed the task before touching the data.

## Don't Worry About These Yet

If you're brand new, skip the full skill catalog, the build and customization pages, the manager workflow pages, and any companion or reference sections. None of those are for your first session — come back to them once you've seen the workflow in action.

## Student-Focused Skills

The skills that matter most when you're starting out:

- `socratic-tutor` — default interaction style; three-layer system (question ladder, RHRS session arc, self-check every 3 turns)
- `identity-loader` — pre-session; loads your profile and mastery, registers new students, surfaces open questions from last time
- `tutor-mode` — structural decomposition of workflow skills into student-paced steps
- `hint-ladder` — progressive hints when you're stuck, escalating from nudge to reveal
- `session-wrap` — triggered by `/wrap`; writes the session summary and confirmed mastery updates to your student folder

The full skill catalog (`misconception-diagnosis`, `exercise-generator`, `data-audit`, `eda-plan`, `experiment-log`) is in the [Skill Library](../setup/skill-reference.md) when you're ready.

## Where To Go Next

If you haven't started yet, go to [Basic Classification — Learning Lens](../examples/basic-classification/learning.md) — that's the right first move.

After your first full project, work through the other examples in order of complexity:

- [Linear Regression — Learning Lens](../examples/analytics-repo/learning.md) — California Housing, 20K census tracts, continuous prediction
- [Survival RAG](../examples/survival-rag/index.md) — bring your own textbook, local vector search, Socratic responses grounded in retrieved passages

Then read [Core Data Science Workflow](../workflows/data-science/index.md) to see the full shared sequence, and browse [Examples](../examples/index.md) to see how the same backbone looks through learning, execution, and manager lenses.
