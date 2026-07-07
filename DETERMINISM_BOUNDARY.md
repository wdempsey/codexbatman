# Determinism Boundary

Date: 2026-07-07

Scope: PR-2 boundary after the PR-1 flow audit. This document classifies current Codex Batman behaviors as suggested skill guidance, deterministic enforcement, or explicit follow-up.

## Boundary Rule

Skills can suggest behavior. Hooks, scripts, config reads, CI checks, and branch protections enforce behavior.

Do not claim a behavior "must always happen" unless it has a deterministic enforcement surface.

## Current Classification

| Behavior | Source | Classification | PR-2 state |
| --- | --- | --- | --- |
| Data science workflow gates: problem framing before EDA, data audit before modeling, experiment log for modeling runs | `AGENTS.md`, workflow skills, `ask-codexbatman` | Suggested | Still skill/prose guidance; future hooks would need project artifact detection before enforcement. |
| Student identity loading before student overlays | `AGENTS.md`, `identity-loader`, `.claude/CLAUDE.md` | Config-read required, not fully hook-enforced | PR-2 adds a project `.claude/CLAUDE.md` shim so Claude sessions read the student identity rule at startup. |
| Student memory updates require confirmation | `identity-loader`, `session-wrap` | Suggested | Still prose guidance; no script can detect conversational confirmation yet. |
| Skill promotion pipeline: student flags first, auditor verdict next, maintainer opens draft skill PR only after recommendation | `AGENTS.md`, `session-wrap`, `memory/students/README.md` | Enforced for file-level promotion shape | PR-2 adds `scripts/hooks/codexbatman_lifecycle_gate.py` and a GitHub Actions workflow. |
| Student flag PR must not also promote shared skills | lifecycle gate script | Enforced | The script fails if `memory/students/**/flagged-skills.md` changes in the same PR as `skills/**`, `evals/**`, `SKILL-STYLE.md`, `CAPABILITY-MATRIX.md`, or `skills/METADATA.md`. |
| Student memory files must not be deleted accidentally | lifecycle gate script | Enforced | The script fails on deletes under `memory/students/**`. |
| Skill intake metadata, matrix placement, and eval examples | `SKILL-STYLE.md`, `CAPABILITY-MATRIX.md` | Suggested | PR-3 should add a runnable eval/metadata harness before treating this as enforced. |
| Git safety for general repo edits | `AGENTS.md` | Suggested | No broad git hook yet; PR-2 only adds student-facing memory and promotion guardrails. |
| MkDocs site build | local command and deploy workflow | Enforced in deploy path only | `mkdocs build --strict` remains the local verification command for PRs. |

## Lifecycle Gate

Run locally against staged changes:

```bash
./.venv/bin/python scripts/hooks/codexbatman_lifecycle_gate.py
```

Run against a branch diff:

```bash
./.venv/bin/python scripts/hooks/codexbatman_lifecycle_gate.py --base main --head HEAD
```

The GitHub Actions workflow runs the same script on pull requests that touch student memory, skills, evals, or the skill-intake files.

## What PR-2 Does Not Enforce

PR-2 does not try to enforce conversational facts that a script cannot observe, such as whether a student confirmed a mastery update or whether an agent actually asked a Socratic question.

PR-2 also does not enforce every data science workflow gate. That would require project-local artifact detection across multiple possible repository layouts. Until that exists, gate order remains skill guidance and review responsibility.

## Follow-Ups

- PR-3 should turn `evals/` into a runnable harness and decide what metadata checks become deterministic.
- A future student-session hook could record an identity-loaded marker, but only after the session runtime has a stable place to write that state.
- A future project-artifact hook could enforce data science gates when a project template has stable artifact paths.
