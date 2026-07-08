# Skill Telemetry

Date: 2026-07-07

This file defines the logging conventions for PR-3. It does not require every session to write logs yet; it defines the event vocabulary that `/improve-skill` and future automation should expect.

## Event Format

Use newline-delimited JSON when logs are written to disk.

Suggested local path:

```text
logs/skill-telemetry.ndjson
```

Do not commit runtime telemetry logs. Summarize durable lessons in PR descriptions, `planning.md`, or future devlog artifacts.

Required fields:

| Field | Meaning |
| --- | --- |
| `timestamp` | ISO 8601 timestamp with timezone when available |
| `event` | One of the event types below |
| `skill` | Primary skill involved |
| `role` | `student`, `data scientist`, `data science manager`, or `repository maintainer` |
| `summary` | One sentence describing what happened |
| `evidence` | Short artifact reference, command, eval id, or user correction |
| `next_action` | `none`, `add-improvement-eval`, `propose-skill-diff`, `route-to-pr-2-gate`, or `human-review` |

Optional fields:

- `session_ref`
- `related_skills`
- `eval_id`
- `deviation_ref`
- `privacy_note`

## Event Types

| Event | Use when |
| --- | --- |
| `skill_invocation` | A skill is intentionally selected for a task. |
| `trigger_miss` | A skill should have triggered but did not, or the wrong skill was selected first. |
| `user_correction` | The user corrects routing, scope, role, terminology, or output shape. |
| `deviation` | Implementation departs from a planned PR or skill instruction for a documented reason. |
| `eval_result` | A skill eval case passes, fails, or is updated. |
| `improvement_proposal` | `/improve-skill` produces a proposed change. |

## Privacy Rules

- Do not log raw student work, private data, credentials, or personally identifying details.
- For student sessions, refer to the student folder path or a redacted session id instead of quoting memory contents.
- Prefer artifact references over pasted content.
- If an event depends on sensitive context, log the category of evidence and keep the details out of telemetry.

## Deviation Logs As Improvement Signals

Deviation logs double as improvement signals. A deviation should become a telemetry event when it suggests that a skill, eval, hook, or docs page needs to change.

Examples:

```json
{"timestamp":"2026-07-07T13:10:00-04:00","event":"trigger_miss","skill":"site-voice","role":"repository maintainer","summary":"Site copy request initially routed as page-structure review.","evidence":"PR comment on role page copy","next_action":"add-improvement-eval"}
{"timestamp":"2026-07-07T13:20:00-04:00","event":"deviation","skill":"ask-codexbatman","role":"repository maintainer","summary":"Identity-loader enforcement deferred from PR-1 to PR-2 because prose cannot enforce startup reads.","evidence":"FLOW-AUDIT.md#identity-loader-boundary","next_action":"human-review"}
```

## `/improve-skill` Contract

`/improve-skill` may read telemetry, improvement evals, and target skill files. It proposes diffs; it does not apply them.

Held-out evals are regression checks. Do not use held-out failures as direct training examples in the same PR. If a held-out failure reveals a real missing case, add a new improvement eval in a later PR.
