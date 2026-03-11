# Examples: Project Bootstrap

## Example 1

User request:

> Bootstrap this repository for the canonical data science workflow before we start analysis.

Expected behavior:

- inspect the current workspace
- define the canonical artifact locations
- create only the minimum missing structure

## Example 2

User request:

> This project already has code and data folders. Normalize it to the Codex-native workflow without reorganizing everything.

Expected behavior:

- preserve the current layout where possible
- document the artifact backbone
- avoid broad restructuring

## Example 3

User request:

> Tell me what is missing before this workspace can support problem framing, audit, and experiment logging.

Expected behavior:

- perform assessment only
- produce a readiness checklist
- avoid creating files unless asked
