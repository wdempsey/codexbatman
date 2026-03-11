# Examples: Execution Mode

## Example 1

User request:

> Run problem framing on this project and give me the artifact.

Expected behavior:

- wrap `problem-framing`
- execute directly
- return the artifact without tutor-style scaffolding

## Example 2

User request:

> Apply the canonical data audit to this dataset and tell me if we can proceed.

Expected behavior:

- wrap `data-audit`
- produce the audit artifact
- state the proceed decision clearly
