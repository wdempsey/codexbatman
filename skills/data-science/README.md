# Data Science Skills

This category contains the canonical data science workflow backbone.

The backbone is artifact-first and Codex-native.

- `project-bootstrap` establishes the workspace and artifact locations.
- `problem-framing` defines the analytical objective before data work begins.
- `data-audit` tests whether the available data is fit for downstream work.
- `experiment-log` records every modeling iteration as a durable artifact.

These skills are designed to compose in order:

1. `project-bootstrap`
2. `problem-framing`
3. `data-audit`
4. `experiment-log`

This is the minimal canonical chain, not the full eventual system. It aligns with the blueprint in [docs/workflows/data-science/blueprint.md](/Users/wdem/Documents/github/codexbatman/docs/workflows/data-science/blueprint.md):

- explicit workflow phases
- explicit artifacts
- reproducibility discipline
- human review at workflow gates

Each canonical skill defines:

- purpose
- invocation boundary
- required inputs
- expected outputs
- artifact checklist
- common failure modes

The goal is to make workflow state legible to Codex and to humans. These skills are not generic prompts. They are operating procedures for disciplined data science work.
