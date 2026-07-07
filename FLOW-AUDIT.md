# Flow Audit

Date: 2026-07-07

Scope: PR-1 flow audit after the PR-0 intake process. This audit covers folder-based `SKILL.md` routing metadata, high-confidence trigger collisions, progressive-disclosure gaps, the student identity-loader boundary, and the minimal eval handoff needed for PR-3.

## Summary

PR-1 makes four focused fixes:

- adds `skills/overlays/ask-codexbatman/` as a router skill modeled on Matt Pocock's `/ask-matt` pattern, rewritten for Codex Batman's role-first data science operating system
- normalizes `skills/site-voice/SKILL.md` frontmatter and adds a short quick-start block before the full voice guide
- removes the legacy `practitioner` role alias from four software-team skills and normalizes frontmatter descriptions that still used `practitioner` as trigger language
- adds a lightweight `evals/` scaffold and `evals/skills/ask-codexbatman.md` so PR-3 can turn examples into a runnable harness

## Trigger Collision Findings

The folder-based skill inventory now has 54 `SKILL.md` files after adding `ask-codexbatman`.

| Area | Finding | PR-1 action |
| --- | --- | --- |
| Role routing | No single skill answered "which role, overlay, or workflow should I use?" without doing the work. | Added `ask-codexbatman` in the repository-maintainer `router` matrix cell. |
| Software-team skills | Four data science skills used the old `practitioner` role alias in frontmatter, and five descriptions still used `practitioner` as trigger language. | Normalized those role values and descriptions to `data scientist`. |
| Site voice | `site-voice` had a strong body but missing schema fields, which made it weaker as a routable site skill. | Added `category`, `status`, `stage`, `role_compatibility`, inputs, outputs, artifacts, recommended next skills, and attribution. |
| Student help | `tutor-mode`, `socratic-tutor`, `hint-ladder`, `exercise-generator`, and `misconception-diagnosis` are related but not duplicates. | Left behavior unchanged; listed the cell in the overlap watchlist for eval-based intake. |
| Manager operations | Manager command-style files still overlap conceptually with folder-based manager skills. | Left migration gradual; track archive/keep decisions in `planning.md` and future PR summaries. |

## Progressive Disclosure Findings

High-confidence PR-1 fix:

- `site-voice` now starts with a quick-start boundary before the full guide, so an agent can route and begin safely without first reading the entire voice essay.

No broad rewrite was done. Several older skills remain long because they encode full procedures, but changing them all in one PR would make review noisy. Future cleanup should split long, multi-variant skills only when the added reference files reduce real context load.

Follow-up candidates:

- review command-style manager skills such as `skills/manager/checkin.md`, `skills/manager/morning-brief.md`, and `skills/manager/triage-inbox.md` for gradual migration or archive decisions
- compare the student-help cell before adding future student diagnostics skills, especially because `misconception-diagnosis` already exists
- consider moving long procedural appendices into adjacent reference files when a folder-based skill approaches the limits described in `SKILL-STYLE.md`

## Identity-Loader Boundary

The repository does not currently contain a project-level `.claude/CLAUDE.md` file. PR-1 therefore documents the desired config-read boundary rather than adding deterministic enforcement.

Current routing rule:

- for student sessions, `identity-loader` is the first overlay and must run before `tutor-mode`, workflow skills, or method skills
- if no `memory/students/{name}/` subfolder exists, the skill offers registration and proceeds without re-offering mid-session if the student declines

PR-2 should decide the deterministic hook or config-read mechanism. The open enforcement question is how to ensure session-start reads of the student identity folder without relying only on skill prose.

## Evals Handoff

PR-1 adds a non-runnable scaffold:

- `evals/README.md`
- `evals/skills/ask-codexbatman.md`

PR-3 should decide:

- the runnable eval file format
- where frozen held-out tasks live
- how trigger misses, user corrections, and deviation logs feed improvement examples
- how `/improve-skill` proposes diffs without editing skills in place

## Source Attribution

`ask-codexbatman` is modeled on:

- https://github.com/mattpocock/skills/tree/main/skills/engineering/ask-matt
- MIT License, Copyright (c) 2026 Matt Pocock

The imported mechanism is the router role: answer "which flow fits?" and hand off. The Codex Batman implementation is distinct because it routes through product roles, data science workflow gates, tutoring overlays, manager operations, and repository-maintenance skills.
