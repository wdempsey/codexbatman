# ask-codexbatman Examples

## Student Method Confusion

Input:

> I am in my first ML class and do not understand why we are using ridge instead of linear regression.

Expected route:

- Role/lane: student
- Start with: `identity-loader`
- Then: `tutor-mode` plus `socratic-tutor`, then `ridge-regression` or `explain-method`
- Stop or ask before: assuming ridge familiarity

## Data Scientist Gate Check

Input:

> Fit a random forest on this dataset and tell me if it beats logistic regression.

Expected route:

- Role/lane: data scientist
- Start with: `problem-framing` or `data-audit` if missing
- Then: `modeling`, `model-evaluation`, and `experiment-log`
- Stop or ask before: modeling before the framing and audit gates

## Manager Status Review

Input:

> Pull together the weekly status for this research project and highlight blocker decisions.

Expected route:

- Role/lane: data science manager
- Start with: `weekly-review`
- Then: `project-tracker` if project state is stale
- Stop or ask before: inventing status not present in artifacts

## Site Copy Pass

Input:

> This role page feels stiff. Make it sound like the rest of the site.

Expected route:

- Role/lane: repository maintainer
- Start with: `site-voice`
- Then: `ui-ux-review` only if page structure is also in scope
- Stop or ask before: broad rewrites unrelated to voice

## New Skill Intake

Input:

> Add a new skill for reviewing messy class notes.

Expected route:

- Role/lane: repository maintainer
- Start with: `SKILL-STYLE.md` and `CAPABILITY-MATRIX.md`
- Then: compare against existing student overlays and PR-sequence briefs
- Stop or ask before: creating a duplicate of a planned or existing skill
