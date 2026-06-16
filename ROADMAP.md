# Codex Batman Roadmap

Last updated: 2026-06-16

## Goal

Turn `codexbatman` into a reference implementation for an AI-native data science ecosystem that remains:

- markdown-first
- repo-first
- artifact-first
- Codex-native
- model-agnostic
- minimal and reversible
- useful for learning, execution, and management

The shared backbone should support three lenses:

1. Learning lens
2. Execution lens
3. Manager lens

## North Star

Codex Batman should teach users to stop treating AI as isolated chat sessions.

- Every project has living memory.
- Every meeting updates that memory.
- Every coding or writing session leaves a handoff.
- Every week the lab manager agent turns distributed project state into a short, actionable brief.

## Guiding Architecture

Codex Batman should contain two connected systems inside one repo:

```text
Data Science Backbone
  teaches and executes reproducible data science projects

Research OS / Lab Manager Layer
  coordinates many projects, people, deadlines, and handoffs
```

Shared artifacts connecting these layers:

```text
PROJECT_STATE.md
problem_frame.md
data_card.md
analysis_plan.md
experiment_log.md
model_card.md
workflow_trace.md
decision_log.md
HANDOFF.md
NEXT_ACTIONS.md
```

Optional external tooling stack:

```text
Codex Batman
  = workflow backbone and operating rules

Ponytail
  = optional minimal-change behavior guardrail

codebase-memory-mcp
  = optional repo graph / structural code memory

Codex / Cursor / Claude
  = execution agents

PROJECT_STATE.md / workflow traces / handoffs
  = durable project memory
```

## Scope-Control Rules

1. Do not build CLI tooling yet.
2. Do not add a web app.
3. Do not vendor external tools.
4. Do not fork Ponytail or `codebase-memory-mcp`.
5. Do not add heavy CSS, custom JavaScript, or new dependencies for UI work.
6. Prefer MkDocs Material-native patterns.
7. Keep each PR additive, focused, and reversible.
8. Use skills and templates before automation.
9. Keep the backbone minimal but concrete.
10. Every added section should have a clear user-facing purpose.

## PR Sequence

### PR 1: Add Tooling Stack Registry

Goal:
- Add concise docs for optional external tools used alongside Codex Batman.

Outputs:
- `docs/tooling/index.md`
- `docs/tooling/ponytail.md`
- `docs/tooling/codebase-memory.md`
- `mkdocs.yml` nav updates

Key positioning:
- Codex Batman is the workflow backbone.
- Ponytail is an optional minimal-change behavior guardrail.
- `codebase-memory-mcp` is an optional repo graph / code memory layer.
- External tools are optional plugins, not core dependencies.

### PR 2: Add Backbone Protocol v0.1 Docs

Goal:
- Define the shared Data Science Backbone Protocol.

Outputs:
- `docs/backbone/index.md`
- `docs/backbone/artifacts.md`
- `docs/backbone/lifecycle.md`
- `docs/backbone/self-improvement.md`
- nav updates

Minimum artifacts:

```text
PROJECT_STATE.md
problem_frame.md
data_card.md
analysis_plan.md
experiment_log.md
model_card.md
workflow_trace.md
decision_log.md
```

Lifecycle:

```text
bootstrap
frame
audit
plan
execute
evaluate
communicate
trace
distill
improve
```

### PR 3: Add Minimal Data Science Project Template

Goal:
- Add a minimal project template implementing Backbone Protocol v0.1.

Outputs:
- `templates/ds-project/`
- `docs/backbone/project-template.md`
- Backbone and Tooling links

### PR 4: Add Core ML Skill Pack

Goal:
- Add the first concrete skill pack for basic ML workflows.

Outputs:
- `skills/packs/core-ml/`
- workflow/check/template files
- skills index/docs links

Emphasis:
- reproducibility
- target definition
- unit of analysis
- prediction timing
- leakage checks
- split validity
- baseline comparison
- metric alignment
- model card

### PR 5: Add Workflow Trace, Distillation, and Handoff Skills

Goal:
- Support the self-improving workflow loop.

Outputs:
- `skills/data-science/workflow-trace/SKILL.md`
- `skills/data-science/trace-distillation/SKILL.md`
- `skills/data-science/handoff/SKILL.md`
- updated references

### PR 6: Add Lab Manager Workflow Docs

Goal:
- Add the research management layer as an extension of the Data Science Manager lane.

Outputs:
- `docs/workflows/manager/lab-manager-agent.md`
- manager-doc cross-links

Hierarchy:

```text
Lab Manager Agent
  -> Project Manager Agents
      -> Worker Agents
          -> Codex / Cursor / Claude in local folders
```

### PR 7: Add Research OS Templates

Goal:
- Add templates for lab-level and project-level research management.

Outputs:
- `templates/research-os/`
- `templates/research-os/project/`
- `docs/workflows/manager/research-os-template.md`

### PR 8: Add Lab Manager and Project Manager Skills

Goal:
- Add manager skills for portfolio and project coordination.

Outputs:
- `skills/manager/lab-manager-agent/SKILL.md`
- `skills/manager/project-manager-agent/SKILL.md`
- updated manager references

### PR 9: Add Worked Examples Across Three Lenses

Goal:
- Add examples showing the same backbone through learning, execution, and manager lenses.

Outputs:
- `docs/examples/index.md`
- `docs/examples/basic-classification/`
- `docs/examples/grant-project/`
- `docs/examples/methods-code-project/`
- nav updates

Each example should include:
- `index.md`
- `learning.md`
- `execution.md`
- `manager.md`

### PR 10: Add UI/UX Standards and Site Review Skills

Goal:
- Add lightweight UI/UX guidance and repo-local site review skills.

Outputs:
- `docs/site/ui-ux-standards.md`
- `skills/site/ui-ux-review/SKILL.md`
- `skills/site/navigation-review/SKILL.md`
- `skills/site/visual-polish-pass/SKILL.md`
- skill index updates

UI constraints:
- no external dependencies
- no custom JavaScript
- no heavy CSS
- prefer MkDocs Material-native patterns
- keep changes minimal and reversible

Use [UI_REDESIGN_BRIEF.md](/Users/wdem/Documents/github/codexbatman/UI_REDESIGN_BRIEF.md:1) and [SITE_STRUCTURE_REVIEW.md](/Users/wdem/Documents/github/codexbatman/SITE_STRUCTURE_REVIEW.md:1) as planning inputs for this PR.

### PR 11: Run First UI/UX Pass Over the Site

Goal:
- Apply a light UI/UX pass using repo-local site-review skills.

Review targets:

```text
home page
quickstart
student role page
data scientist role page
manager role page
Backbone Protocol landing page
Tooling Stack landing page
Lab Manager workflow page
Examples landing page
```

Outputs:
- minimal site polish
- nav refinements if justified
- `docs/site/ui-pass-001.md`
- build verification summary

Use:

```text
skills/site/ui-ux-review/SKILL.md
skills/site/navigation-review/SKILL.md
skills/site/visual-polish-pass/SKILL.md
```

## Final Expected State

After PR 11, the repo should include:

```text
1. Tooling Stack docs
2. Ponytail page
3. codebase-memory page
4. Backbone Protocol v0.1
5. Minimal DS project template
6. Core ML skill pack
7. Workflow trace skill
8. Trace distillation skill
9. Worker handoff skill
10. Lab Manager workflow docs
11. Research OS templates
12. Lab Manager skill
13. Project Manager skill
14. Three worked examples
15. Three lenses per example
16. UI/UX standards
17. Site review skills
18. First UI pass report
```

## Mature Workflow Model

Portfolio workflow:

```text
Lab Manager Agent identifies priority
  -> Project Manager Agent scopes task
      -> Worker Agent executes in folder
          -> Worker Agent updates handoff
      -> Project Manager Agent updates project state
  -> Lab Manager Agent updates portfolio dashboard
```

Data science workflow:

```text
bootstrap
  -> frame
  -> audit
  -> plan
  -> execute
  -> evaluate
  -> communicate
  -> trace
  -> distill
  -> improve
```

Ecosystem principle:

> Every project has living memory. Every analysis leaves artifacts. Every agent session leaves a handoff. Every week produces a portfolio brief. Every useful lesson becomes a reusable skill, checklist, prompt, template, or eval.
