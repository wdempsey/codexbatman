# improve-skill Examples

## Trigger Miss

Input:

> Users keep asking for site copy edits and Codex routes to `ui-ux-review` instead of `site-voice`.

Expected proposal:

- target skill: `site-voice` or `ask-codexbatman`
- evidence: trigger-miss telemetry plus improvement evals
- proposed change: sharpen trigger wording or add an eval case
- no direct edit to the skill

## Eval Regression

Input:

> `ask-codexbatman` fails the premature-modeling eval because it jumps straight to `modeling`.

Expected proposal:

- target skill: `ask-codexbatman`
- diagnosis: gate-safety routing weakness
- proposed diff: reinforce data-audit-before-modeling route
- evals: improvement eval first, held-out after the proposal exists

## Student Flag Promotion

Input:

> A student flagged a useful explanation pattern for logistic regression. The auditor recommended promotion.

Expected proposal:

- target skill: likely a method skill or student overlay
- lifecycle note: keep the student `flagged-skills.md` PR separate from the maintainer skill PR
- proposed diff only after checking existing overlap in `CAPABILITY-MATRIX.md`
