# Skill Metadata Schema

## Schema

All folder-based `SKILL.md` files should begin with YAML front matter.

### Core fields

- `name`
- `description`
- `category`
- `status`

### Canonical workflow fields

Use when applicable:

- `stage`
- `order`
- `inputs`
- `outputs`
- `artifacts`
- `depends_on`
- `recommended_next`
- `overlays`

### Routing and policy fields

Use when clearly supported by the skill:

- `role_compatibility`
- `human_review_required`
- `halts_if_missing`
- `produces_gate`

## Allowed Values

### `category`

- `data-science`
- `manager`
- `overlays`

### `status`

- `canonical`
- `active`
- `experimental`
- `planned`

### `stage`

Use concise stable names such as:

- `bootstrap`
- `framing`
- `audit`
- `eda`
- `modeling`
- `evaluation`
- `logging`
- `manager-ops`
- `overlay`

### `role_compatibility`

Use only these role strings:

- `student`
- `data scientist`
- `data science manager`

## Examples

### Canonical Data-Science Skill

```yaml
---
name: data-audit
description: Audit data sources and derived datasets before EDA or modeling.
category: data-science
status: canonical
stage: audit
order: 3
role_compatibility:
  - student
  - data scientist
  - data science manager
inputs:
  - dataset sources
  - schema or dictionary
  - target definition
  - time index
  - unit of analysis
outputs:
  - audit decision
  - remediation actions
artifacts:
  - data audit report
  - schema summary
  - quality flags
  - proceed/halt decision
depends_on:
  - problem-framing
recommended_next:
  - eda-plan
overlays:
  - tutor-mode
  - execution-mode
  - artifact-enforcer
  - project-tracker
human_review_required: true
halts_if_missing:
  - dataset sources
  - target definition
  - unit of analysis
produces_gate: audit-decision
---
```

### Manager Skill

```yaml
---
name: weekly-review
description: Produce a project-centered weekly review for a data science or research project.
category: manager
status: active
stage: manager-ops
role_compatibility:
  - data science manager
inputs:
  - project artifacts
  - experiment logs
  - team updates
  - open risks
outputs:
  - weekly synthesis and actions
artifacts:
  - weekly review report
  - risk register update
  - owner action list
depends_on:
  - project-setup
recommended_next:
  - stakeholder-update
---
```

### Overlay Skill

```yaml
---
name: tutor-mode
description: Wrap an existing skill in student tutoring mode.
category: overlays
status: active
stage: overlay
role_compatibility:
  - student
overlays:
  - project-bootstrap
  - problem-framing
  - data-audit
  - eda-plan
  - modeling
  - model-evaluation
  - experiment-log
---
```

## Routing Guidance

Codex should use metadata as the first routing layer for folder-based skills.

1. Filter by `category` and `role_compatibility`.
2. Prefer `stage`, `order`, `depends_on`, and `recommended_next` when selecting among canonical workflow skills.
3. Use `status` to avoid routing to `planned` skills by default.
4. Read prose after metadata to confirm fit, execution details, and stop conditions.
5. Treat overlays as delivery-style wrappers, not canonical workflow steps.
