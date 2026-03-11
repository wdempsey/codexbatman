# Examples: Artifact Enforcer

## Example 1

User request:

> Use artifact enforcement on problem framing. I do not want to move to audit until the artifact is complete.

Expected behavior:

- wrap `problem-framing`
- check the canonical checklist
- block the next phase if the artifact is incomplete

## Example 2

User request:

> Enforce the experiment log before we run another model.

Expected behavior:

- wrap `experiment-log`
- require the full entry
- refuse silent iteration
