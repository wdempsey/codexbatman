---
name: improve-skill
description: Review skill telemetry, trigger misses, user corrections, deviation logs, and improvement evals, then propose a safe skill improvement without editing the skill in place. Use when a maintainer wants a reflection pass over one skill, when evals show repeated failures, when users correct routing or behavior, or when a proposed skill change must be turned into a human-reviewable patch.
category: overlays
status: active
stage: overlay
role_compatibility:
  - student
  - data scientist
  - data science manager
inputs:
  - target skill folder
  - skill telemetry log excerpts
  - improvement eval results
  - user corrections or trigger misses
  - deviation log entries
outputs:
  - skill improvement proposal
  - proposed diff
  - eval follow-up list
artifacts:
  - skill improvement proposal
  - proposed patch text
recommended_next:
  - skill-promotion-gate
human_review_required: true
---

# Improve Skill

Reflect and propose. Do not edit `SKILL.md`, `EXAMPLES.md`, `RUBRIC.md`, eval files, or metadata in place.

This skill turns operational evidence into a maintainer-reviewable improvement proposal. It is intentionally one step before implementation.

## Use When

Use this skill when:

- telemetry shows repeated trigger misses or user corrections for one skill
- improvement evals fail in a consistent way
- a maintainer wants a compact diagnosis before opening a skill-change PR
- a student-flagged idea was recommended for promotion and needs a draft approach
- a skill has grown confusing and needs a smaller, evidence-backed patch

## Inputs

- target skill path
- `SKILL.md`, `EXAMPLES.md`, `RUBRIC.md`, and adjacent references for that skill
- relevant improvement eval cases from `evals/improvement/`
- telemetry records described in `SKILL-TELEMETRY.md`
- PR-2 lifecycle gate and human-review rules

## Outputs

Produce a proposal with:

- target skill and evidence sources
- observed failure pattern
- proposed behavior change
- proposed diff as fenced `diff` text
- evals to run before implementation
- lifecycle-gate notes
- human-review questions

## Stop Conditions

Stop and ask before continuing when:

- the target skill is unclear
- the proposed change would rewrite a skill rather than patch a specific failure
- the proposal depends on private student memory that should not be quoted
- the change would edit held-out evals to make the proposal pass
- the proposal combines `memory/students/**/flagged-skills.md` changes with shared skill changes

## Procedure

1. Identify one target skill.
   - Use `CAPABILITY-MATRIX.md` to confirm the skill's default cell.
   - If multiple skills are implicated, choose one primary skill and list the rest as related.

2. Gather evidence.
   - Read the target skill's `SKILL.md`, `EXAMPLES.md`, and `RUBRIC.md` when present.
   - Read only relevant telemetry excerpts.
   - Use improvement evals from `evals/improvement/`.
   - Do not inspect `evals/heldout/` while drafting the proposal.

3. Diagnose the smallest useful change.
   - Prefer trigger-description fixes before body rewrites.
   - Prefer examples or rubric adjustments when behavior is clear but evaluation is underspecified.
   - Prefer splitting references only when the skill body is genuinely too large.

4. Draft the proposal.
   - Include a proposed diff, but do not apply it.
   - Name any new improvement eval cases that should accompany the change.
   - If the proposal comes from a student flag, remind the maintainer to keep the student flag PR separate from the skill-change PR.

5. Route to review.
   - Ask the maintainer whether to implement the proposed diff in a separate PR.
   - If implementation is approved later, run `scripts/hooks/codexbatman_lifecycle_gate.py`, `scripts/evals/run_skill_evals.py --check`, and `mkdocs build --strict`.

## Held-Out Eval Rule

Held-out evals are for final regression checks, not idea generation.

When drafting a proposal:

- use telemetry, user corrections, deviation logs, and `evals/improvement/`
- leave `evals/heldout/` unread until after a proposal exists
- do not edit held-out evals in the same PR as a skill improvement

If a held-out eval exposes a real missing case, add a new improvement eval in a later PR and route the skill change through review.

## Output Template

````markdown
# Skill Improvement Proposal: {skill}

## Evidence

- Telemetry:
- Trigger misses:
- User corrections:
- Improvement evals:

## Diagnosis

{one concise failure pattern}

## Proposed Change

{smallest useful change}

## Proposed Diff

```diff
{diff text}
```

## Evals To Run

- `scripts/evals/run_skill_evals.py --check`
- relevant improvement evals:
- held-out evals after proposal:

## Review Notes

- Human review required:
- Lifecycle gate considerations:
- Open questions:
````
