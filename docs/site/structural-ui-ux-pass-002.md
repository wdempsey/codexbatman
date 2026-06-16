# Structural UI/UX Pass 002

**Purpose:** propose structural site and navigation changes that make Codex Batman easier to enter for students, researchers/data scientists, and data science managers.

This is a proposal pass, not an implementation pass. It uses the existing site skills as checklists:

- `ui-ux-review`: purpose, audience, first screenful, hierarchy, and next action
- `navigation-review`: top-level clarity, duplicate labels, orphan pages, and cross-link strength
- `visual-polish-pass`: restrained MkDocs Material-native polish after structure is clear

## Executive Recommendation

Use the existing site skills directly. Do not add a new generic `skills.md` for UI/UX yet.

The current problem is not missing generic design rules. The site already has adequate rules in [UI/UX Standards](ui-ux-standards.md). The higher-value work is structural:

1. reduce top-level navigation decisions
2. make role-based entry obvious
3. make the researcher/data scientist path recognizable
4. separate usage paths from build/customization paths
5. replace homepage placeholders with proof of utility
6. verify mobile and tablet behavior after the structure is simplified

## Current Navigation Finding

The current top-level nav treats many concepts as equal first-run decisions:

- Start Here
- Core Data Science Workflow
- Students
- Data Scientists
- Managers
- Skill Library
- Tooling Stack
- Backbone Protocol
- Examples
- Build Your Own

Each section is defensible on its own, but together they create too many choices for a first-time visitor. A new user must understand the difference between workflow, skills, tooling, backbone, examples, and role pages before knowing where to click.

That violates the local UI/UX standard that navigation should reduce decisions rather than create more of them.

## Proposed Top-Level Navigation

Recommended top-level tabs:

1. Start Here
2. Roles
3. Workflow
4. Examples
5. Skills
6. Build
7. About

This keeps the core architecture visible while making the first decision simpler:

- "I am new" -> Start Here
- "I know my role" -> Roles
- "I want the process" -> Workflow
- "I want to see it in action" -> Examples
- "I need reusable commands/packs" -> Skills
- "I want to extend the system" -> Build
- "I need trust/context" -> About

## Proposed Navigation Shape

```yaml
nav:
  - Start Here:
    - Home: index.md
    - Quickstart: quickstart.md
    - Setup Overview: setup/index.md
    - Install:
      - Mac: toolkit/install-mac.md
      - Windows: toolkit/install-windows.md
      - VS Code: setup/vscode-setup.md
      - MCP Setup: toolkit/mcp-setup.md

  - Roles:
    - Choose Your Role: roles/index.md
    - Students: students/index.md
    - Researchers & Data Scientists: data-scientists/index.md
    - Managers: managers/index.md

  - Workflow:
    - Overview: workflows/data-science/index.md
    - Project Bootstrap: workflows/data-science/project-bootstrap.md
    - Problem Framing: workflows/data-science/problem-framing.md
    - Data Audit: workflows/data-science/data-audit.md
    - Exploratory Analysis: workflows/data-science/eda-plan.md
    - Modeling: workflows/data-science/modeling.md
    - Evaluation: workflows/data-science/evaluation.md
    - Experiment Logging: workflows/data-science/experiment-log.md
    - Backbone Protocol: backbone/index.md

  - Examples:
    - Overview: examples/index.md
    - Basic Classification:
      - Overview: examples/basic-classification/index.md
      - Learning Lens: examples/basic-classification/learning.md
      - Execution Lens: examples/basic-classification/execution.md
      - Manager Lens: examples/basic-classification/manager.md
    - Grant Project:
      - Overview: examples/grant-project/index.md
      - Learning Lens: examples/grant-project/learning.md
      - Execution Lens: examples/grant-project/execution.md
      - Manager Lens: examples/grant-project/manager.md
    - Methods / Code Project:
      - Overview: examples/methods-code-project/index.md
      - Learning Lens: examples/methods-code-project/learning.md
      - Execution Lens: examples/methods-code-project/execution.md
      - Manager Lens: examples/methods-code-project/manager.md

  - Skills:
    - Skill Library: setup/skill-reference.md
    - Core ML Pack: setup/core-ml-pack.md
    - How Skills Work: system/skills-explained.md

  - Build:
    - Overview: system/index.md
    - Tooling Stack: tooling/index.md
    - Ponytail: tooling/ponytail.md
    - codebase-memory-mcp: tooling/codebase-memory.md
    - Building Skills: system/building-skills.md
    - Agents vs Skills: system/agents-vs-skills.md
    - Continuous Improvement: system/continuous-improvement.md
    - Patterns: system/patterns.md
    - Site Review: site/index.md
    - Downloads & Reference Library: downloads/index.md

  - About:
    - About: about.md
    - Resources: resources.md
    - Privacy: privacy.md
```

This proposal intentionally does not create top-level tabs for `Tooling Stack` or `Backbone Protocol`. They are important, but they are not first-run audience choices. Tooling belongs under `Build`; Backbone belongs under `Workflow`.

## Role Path Recommendation

### Students

Primary question:

- "How do I learn the workflow without getting lost?"

Best first destination:

- [Student First Session](../students/first-session.md)

Needed structural change:

- Keep students under `Roles`, not as a top-level tab.
- Preserve the concrete first-session link above the abstract workflow explanation.
- On the student page, make the first action a prominent Material card or callout.

### Researchers And Data Scientists

Primary question:

- "How do I run trustworthy analysis with Codex?"

Best first destination:

- [Core Data Science Workflow](../workflows/data-science/index.md)

Needed structural change:

- Rename the nav label from `Data Scientists` to `Researchers & Data Scientists`.
- Keep the page path as `data-scientists/index.md` for link stability.
- Update the page title or opening line to acknowledge researchers explicitly.

Rationale:

The repository mission says `data scientist`, but many likely users will self-identify as researchers. The navigation can welcome both without changing the underlying role architecture.

### Managers

Primary question:

- "How do I track project health, blockers, handoffs, and next actions?"

Best first destination:

- [Lab Manager Agent](../workflows/manager/lab-manager-agent.md)

Needed structural change:

- Keep managers under `Roles`, with manager workflows nested or cross-linked from the manager page.
- Avoid making managers choose between `Project Management`, `Managing Data Science`, `Lab Manager Agent`, and `Research OS Template` at the top level.
- Make the manager page the routing hub for those workflow pages.

## Homepage Structural Recommendation

The homepage should route users before it explains the full architecture.

Recommended homepage sequence:

1. concise promise
2. three role cards: student, researcher/data scientist, manager
3. one "see it in action" proof section with a real artifact or example snapshot
4. workflow backbone summary
5. setup/build links for advanced users

Current homepage friction:

- the hero explains the system before showing enough concrete payoff
- placeholder media blocks still make the page feel unfinished
- role lanes are present, but they arrive after a conceptual section
- the final section points to site standards rather than a user-centered next action

Minimal fix:

- Move role selection earlier.
- Replace placeholder media blocks with either real screenshots, artifact previews, or no media block.
- Make `Quickstart`, `Examples`, and the three role paths the dominant actions.

## Role Page Template

Use one shared structure for all three role pages:

1. role promise
2. "Start here" action
3. "This path is for you if..." bullets
4. what changes in this mode
5. first three steps
6. typical outputs
7. key skills
8. where to go next

This is mostly already present, but the order differs. The next pass should standardize the order so users can compare paths quickly.

Recommended visual pattern:

- one top callout for the first action
- one compact card grid for first three steps
- one simple table for skills and outputs
- no custom JavaScript
- no new dependency

## Orphan And Legacy Content Policy

Before adding more nav links, decide whether the site is using a `narrow` or `layered` structure.

Recommended: `layered`, with a clearly labeled reference layer.

- Primary paths: start, roles, workflow, examples, skills
- Builder paths: tooling, backbone details, skill creation, system improvement
- Reference/archive paths: downloads, essentials, tax workflow, inherited Claude-focused material

This avoids deleting useful material while preventing it from confusing first-time users.

## Implementation Sequence

### Phase 1: Navigation Reshape

- Create `docs/roles/index.md` as a role chooser page.
- Collapse `Students`, `Data Scientists`, and `Managers` under `Roles`.
- Rename `Data Scientists` nav label to `Researchers & Data Scientists`.
- Move `Backbone Protocol` under `Workflow`.
- Move `Tooling Stack` under `Build`.
- Move `Resources` and `Privacy` under `About`.

### Phase 2: Role Entry Pages

- Standardize the three role pages around the shared role page template.
- Give each role page a visible first action.
- Cross-link examples by lens from each role page.

### Phase 3: Homepage Routing

- Move role selection closer to the top.
- Replace placeholder visuals with real artifacts or remove the empty media slots.
- Make the final section point to user next actions, not internal site standards.

### Phase 4: Legacy Layer

- Decide which orphan pages are primary, reference, or archive.
- Keep useful legacy material discoverable through a Reference Library rather than top-level tabs.
- Remove or update stale inherited links as a separate content cleanup pass.

### Phase 5: Visual QA

- Run `mkdocs build`.
- Inspect homepage, role chooser, role pages, workflow overview, and examples at desktop, tablet, and mobile widths.
- Fix layout issues before adding further polish.

## Changes To Avoid

- Do not introduce a new generic UI/UX `skills.md` before using the existing site skills.
- Do not add a design system dependency.
- Do not add more custom JavaScript.
- Do not use visual polish to compensate for navigation ambiguity.
- Do not expand top-level navigation to expose every useful page.

## Success Criteria

This pass succeeds when:

- a student can find the first guided session from the homepage or nav in one click
- a researcher can recognize that the `Data Scientists` path applies to them
- a manager can find lab/project coordination workflows without reading the full data science workflow first
- top-level nav has fewer concept-heavy decisions
- homepage placeholders are gone
- mobile role routing remains readable
