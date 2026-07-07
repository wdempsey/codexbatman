# ask-codexbatman Eval Tasks

## Eval 1: Student Start

Input:

> I am a student and I want help starting my first classification project.

Expected route:

- `identity-loader`
- `tutor-mode` plus `socratic-tutor`
- `project-bootstrap` or `problem-framing`

Must include:

- student lane
- identity resolution before workflow routing
- student overlay wrapping the canonical workflow

Must not:

- skip directly to modeling

Notes for PR-3:

- Score whether identity loading is treated as a stop-before-work step.

## Eval 2: Premature Modeling

Input:

> Train a gradient boosting model and compare it to random forest. We have not written the data audit yet.

Expected route:

- data scientist lane
- `data-audit` before `modeling`
- `experiment-log` once modeling starts

Must include:

- a halt or condition before modeling

Must not:

- accept the requested model comparison as the immediate first step

Notes for PR-3:

- Score gate safety.

## Eval 3: Manager Blocker Review

Input:

> I need a manager-facing summary of blockers and decisions for this week's lab meeting.

Expected route:

- data science manager lane
- `weekly-review`
- `project-tracker` if project state is missing or stale

Must include:

- manager-facing outputs

Must not:

- route to a technical model-evaluation gate unless the user asks for model quality review

Notes for PR-3:

- Score distinction between management synthesis and technical workflow execution.

## Eval 4: Site Voice

Input:

> Rewrite the homepage intro so it sounds less robotic but keep the structure.

Expected route:

- repository-maintainer lane
- `site-voice`

Must include:

- keep structure in scope unless user broadens it

Must not:

- route to `navigation-review` or `visual-polish-pass` as the primary skill

Notes for PR-3:

- Score site-maintenance subrouting.

## Eval 5: New Skill Proposal

Input:

> Add a skill that teaches students how to debug misconceptions in logistic regression.

Expected route:

- repository-maintainer lane
- `SKILL-STYLE.md`
- `CAPABILITY-MATRIX.md`
- compare against `misconception-diagnosis`, `tutor-mode`, and method skills

Must include:

- duplicate-risk check

Must not:

- create a new skill before checking the incumbent student-help cell

Notes for PR-3:

- Score intake discipline and overlap handling.
