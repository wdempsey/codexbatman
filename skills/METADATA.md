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

### Method handoff fields for workflow skills

Use when a workflow step may need to pause and teach a method before continuing:

- `method_prerequisites`
- `method_default_path`
- `method_escalation_rule`
- `method_handoff_prompts`

### Method skill fields

Use for `category: methods` skills:

- `method_family`
- `prerequisites`
- `related_workflow_skills`

## Allowed Values

### `category`

- `data-science`
- `manager`
- `methods`
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
- `methods`
- `overlay`

### `role_compatibility`

Use only these role strings:

- `student`
- `data scientist`
- `data science manager`

### Method metadata conventions

For method skills:

- prefer `status` values `active`, `experimental`, or `planned`
- use a stable `method_family` such as `supervised-learning`
- use `prerequisites` to name workflow context that should already exist
- use `related_workflow_skills` to name likely handoff destinations such as `modeling`, `model-evaluation`, or `causal-design-check`

### Workflow method-handoff conventions

For workflow skills:

- use `method_prerequisites` for methods a learner may need to understand to execute the workflow step well
- use `method_default_path` for the preferred instructional order, usually baseline first, simpler before more complex, and interpretable before black-box when reasonable
- use `method_escalation_rule` as a short plain-language routing rule for unfamiliar-method cases
- use `method_handoff_prompts` as a keyed map from short cue strings such as `unfamiliar`, `compare`, or `baseline-first` to concise routing prompts

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

### Workflow Skill With Method Handoff

```yaml
---
name: modeling
description: Specify and compare models in a controlled, reproducible way.
category: data-science
status: canonical
stage: modeling
role_compatibility:
  - student
  - data scientist
  - data science manager
depends_on:
  - problem-framing
  - data-audit
  - eda-plan
recommended_next:
  - model-evaluation
method_prerequisites:
  - linear-regression
  - ridge-regression
  - lasso
  - random-forest
  - gradient-boosting
method_default_path:
  - linear-regression
  - ridge-regression
  - lasso
  - random-forest
  - gradient-boosting
method_escalation_rule: >
  Start with the simplest method the learner can understand and defend.
  If a new method is proposed and the learner is unfamiliar with it,
  pause the workflow, route to the relevant method skill,
  then resume modeling.
method_handoff_prompts:
  unfamiliar: "Pause modeling and teach the method before continuing."
  compare: "Explain why this method is being compared to the baseline."
  baseline-first: "Teach or fit the simplest defensible baseline before advanced models."
---
```

### Method Skill

```yaml
---
name: linear-regression
description: Teach the intuition, baseline role, assumptions, and beginner tradeoffs of linear regression as the default starting point for continuous prediction.
category: methods
status: active
role_compatibility:
  - student
  - data scientist
  - data science manager
method_family: supervised-learning
prerequisites:
  - problem-framing
  - data-audit
  - eda-plan
related_workflow_skills:
  - modeling
  - model-evaluation
  - causal-design-check
---
```

## Routing Guidance

Codex should use metadata as the first routing layer for folder-based skills.

1. Filter by `category` and `role_compatibility`.
2. Prefer `stage`, `order`, `depends_on`, and `recommended_next` when selecting among canonical workflow skills.
3. Use `status` to avoid routing to `planned` skills by default.
4. If a workflow skill includes method-handoff metadata, prefer that routing guidance over ad hoc method suggestions.
5. For student flows, route to the relevant method skill when the learner is unfamiliar with a proposed method, then return to the workflow skill.
6. Read prose after metadata to confirm fit, execution details, and stop conditions.
7. Treat overlays as delivery-style wrappers, not canonical workflow steps.
