# Skill Style And Intake Guide

This guide defines how new or adapted folder-based skills enter this repository.
It complements `skills/METADATA.md` and `CAPABILITY-MATRIX.md`; it does not
replace them.

- `skills/METADATA.md` owns field names and allowed metadata values.
- `SKILL-STYLE.md` owns how a skill should be written and verified.
- `CAPABILITY-MATRIX.md` owns routing placement, collision checks, and dedupe.

New repository-native skills should use the folder-based Codex format:

```text
skills/<category>/<skill-slug>/SKILL.md
skills/<category>/<skill-slug>/EXAMPLES.md
skills/<category>/<skill-slug>/RUBRIC.md
```

Command-style markdown skills may remain for compatibility, but they are not the
default authoring target for new workflow logic.

## Intake Rule

Every skill proposal goes through the same sequence:

1. Normalize it to this style guide.
2. Place it in exactly one default cell in `CAPABILITY-MATRIX.md`.
3. If that cell already has an incumbent skill, evaluate both skills on shared
   tasks that represent the cell.
4. Keep the winner, merge the useful parts, or reject the proposal.
5. Record the outcome and any deviations in the PR description.

Dedupe by function through evaluation. Do not dedupe by reading descriptions
side by side and guessing.

## Admission And Pruning Rule

New skills must reduce routing uncertainty, not add to it.

Admit a new skill only when it satisfies at least one condition:

- owns a distinct job that no incumbent skill should own
- replaces an incumbent after eval comparison
- exposes a reusable workflow that would be too large or fragile as a section of an existing skill

Do not admit a new skill when the idea is better represented as:

- an example in `EXAMPLES.md`
- a rubric item
- a short section inside an incumbent skill
- an eval case that sharpens existing behavior

If a proposal overlaps an occupied matrix cell, compare it against the incumbent skill on shared eval tasks. The PR must record the keep, merge, replace, or reject decision.

## Frontmatter

Every `SKILL.md` starts with YAML frontmatter. Required fields are defined in
`skills/METADATA.md`; at minimum, new folder-based skills need:

```yaml
---
name: skill-slug
description: One or two trigger-oriented sentences.
category: data-science
status: active
stage: modeling
role_compatibility:
  - data scientist
---
```

### Description Style

Descriptions are routing text, not marketing copy.

Use this shape:

```text
Do the concrete thing. Use when <trigger condition>, <trigger condition>, or
<boundary condition>.
```

Prefer:

- specific verbs: audit, diagnose, draft, evaluate, route, teach, summarize
- explicit triggers: "Use when the project needs..." or "Use after modeling..."
- role boundaries when they matter: "student only", "manager-facing", "data
  scientist working in a software codebase"
- exclusions when a nearby skill exists

Avoid:

- broad verbs such as "help with", "support", or "assist"
- descriptions that could trigger across multiple roles without saying why
- duplicating another skill's trigger phrase with only wording changes
- claiming deterministic enforcement in prose

### Source Attribution

Adapted skills must be rewritten in this repository's voice and vocabulary.
Never paste upstream content as the skill.

If a skill is adapted from an external source, add a short attribution note in
frontmatter when the metadata schema supports it, or in the first body section
when it does not:

```yaml
source_attribution:
  - "Adapted from Matt Pocock's grill-me pattern; rewritten for Codex Batman."
```

Attribution is not a license to copy structure wholesale. Adapt the mechanism,
then express it as a repo-native teaching or workflow adapter.

## Progressive Disclosure

The first screen of a skill should be enough for Codex to route and begin
safely. Long guidance belongs after the quick-start section or in adjacent
`EXAMPLES.md` and `RUBRIC.md` files.

Recommended structure:

1. Frontmatter.
2. One-paragraph purpose and boundary.
3. "Use When" with 3-5 concrete triggers.
4. "Inputs" and "Outputs".
5. "Stop Conditions" or "Ask Before Continuing" when relevant.
6. Short procedure.
7. Detailed guide, examples, rubrics, or appendices.

Do not front-load a full essay before the user can tell what the skill is for.

## Suggested Vs Enforced Behavior

Skills are probabilistic guidance. Hooks and scripts are deterministic
enforcement.

Use skill prose for:

- how to think through a workflow
- what artifact to draft
- what questions to ask
- how to teach or summarize
- what risks to notice

Use deterministic hooks or scripts for behavior that must always happen:

- promotion gates
- required config reads
- git safety checks
- protected-file restrictions
- audit logging that cannot be skipped

If the proposed behavior would be unsafe or invalid when skipped, do not rely on
skill prose alone. Route it to a hook-oriented PR.

See `DETERMINISM_BOUNDARY.md` for the current suggested-vs-enforced inventory
and `scripts/hooks/codexbatman_lifecycle_gate.py` for the PR-2 student-memory
and skill-promotion gate.

## Verification

Every skill PR should include verification appropriate to its blast radius.

Minimum checks:

- frontmatter conforms to `skills/METADATA.md`
- the skill has one default `CAPABILITY-MATRIX.md` cell
- nearby skills in the same cell were considered
- examples or eval tasks exist when the skill changes behavior
- `./.venv/bin/mkdocs build --strict` passes when docs are touched

Skill PRs that add or change user-facing behavior should include 3-5 eval tasks:

```text
Input:
Expected behavior:
Scoring rubric:
Failure modes:
```

When a frozen held-out eval set exists, do not modify it during improvement PRs.
Add improvement examples separately.

Run the eval harness for skill PRs:

```bash
./.venv/bin/python scripts/evals/run_skill_evals.py
```

## Deviation Log

Plans are guidance, not rails. If implementation departs from the plan, record
the deviation in the PR description.

Use this format:

```text
DEVIATIONS
- Planned: <what the plan said>
  Changed: <what happened>
  Reason: <why the change improved correctness, scope, or reviewability>
```

Do not hide deviations by rewriting the plan after the fact.

## Reviewer Checklist

Before approving a new or adapted skill, check:

- The trigger description is specific enough to route.
- The skill has one default matrix cell.
- Any cell collision was evaluated through shared tasks.
- The skill adds a capability or improves an incumbent.
- The skill passes the admission and pruning rule: distinct job, replacement, or necessary reusable workflow.
- The first screen is short enough to load before the full guide.
- Enforcement requirements are not buried in prose.
- Source inspiration is attributed without copying.
- Verification and eval notes are in the PR description.
