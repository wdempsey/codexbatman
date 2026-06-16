# AGENTS.md

## Purpose

This project template supports project-manager and worker-agent coordination.

## Rules

1. Keep `PROJECT_STATE.md` current.
2. Keep `NEXT_ACTIONS.md` action-oriented.
3. Record material decisions in `DECISIONS.md`.
4. Leave a `HANDOFF.md` after meaningful sessions.
5. Escalate if project evidence is insufficient for a claim.

## Default Workflow

```text
project manager updates state
  -> worker executes scoped task
  -> worker leaves handoff
  -> project manager updates next actions and decisions
```
