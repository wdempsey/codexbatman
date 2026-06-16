# Methods / Code Project — Manager Lens

Use this lens when the goal is to review technical progress without reading the whole repository.

## What The Manager Sees

- current status of the technical objective
- major decisions that were made
- blockers in the code or experiment design
- what changed in the latest worker session
- what the next scoped task should be

## Risks

- technical drift without durable state
- repeated work because prior exploration was not recorded
- hidden blockers inside a complex repository

## Recommended Next Action

Require the project manager layer to keep:

- `PROJECT_STATE.md`
- `DECISIONS.md`
- `HANDOFF.md`

current before scheduling the next worker task.
