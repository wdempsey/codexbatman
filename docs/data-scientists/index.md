# For Data Scientists

## AI-Native Data Science

This system treats Codex as a workflow executor, not a generic chat interface.

Workflows encode best practices directly into operational steps. Each step produces explicit artifacts so analysis decisions are inspectable, reproducible, and reviewable.

Typical outputs include:

- analysis notebooks
- data audits
- experiment logs
- model cards
- decision memos

## The Canonical Workflow

The shared workflow backbone is:

- problem framing
- data audit
- EDA plan
- modeling
- evaluation
- experiment logging
- documentation

These stages are encoded as skills. The skill system standardizes execution while preserving project-specific choices.

## Using Skills

Skills are invoked directly in Codex, for example:

- `/problem-framing`
- `/data-audit`
- `/experiment-log`

Each skill:

- defines required inputs
- produces structured artifacts
- enforces workflow guardrails

## Example Workflow

problem-framing  
↓  
data-audit  
↓  
eda-plan  
↓  
modeling  
↓  
experiment-log

## Key Skills for Practitioners

- `project-bootstrap`
- `problem-framing`
- `data-audit`
- `eda-plan`
- `modeling-plan`
- `evaluation-plan`
- `experiment-log`
- `model-card`
- `decision-memo`

## Skill Links

- [skills/data-science/problem-framing](https://github.com/wdempsey/codexbatman/tree/main/skills/data-science/problem-framing)
- [skills/data-science/data-audit](https://github.com/wdempsey/codexbatman/tree/main/skills/data-science/data-audit)
- [skills/data-science/experiment-log](https://github.com/wdempsey/codexbatman/tree/main/skills/data-science/experiment-log)
- [skills/overlays/practitioner](https://github.com/wdempsey/codexbatman/tree/main/skills/overlays/practitioner)
