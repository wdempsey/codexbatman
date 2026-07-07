# Capability Matrix

This matrix is the intake map for folder-based Codex skills in this repository.
It answers one question: when a new skill is proposed, what existing capability
does it compete with?

The matrix classifies the current folder-based `SKILL.md` inventory. Each skill
occupies exactly one default cell, even when its frontmatter lists multiple
compatible roles. That default cell is the dedupe and evaluation owner.

Current coverage: 53 folder-based `SKILL.md` files.

## Intake Rule

1. Normalize the proposed skill to `SKILL-STYLE.md`.
2. Place it in exactly one default role x task-type cell below.
3. If the cell is empty, add the skill and update this matrix.
4. If the cell is occupied, run the proposal and incumbent skill(s) against the
   same task set.
5. Keep the winner, merge the useful parts, or reject the proposal.
6. Record the decision in the PR description.

Dedupe by function through eval. Do not dedupe by reading descriptions side by
side.

## Role Lanes

The repository's product roles remain:

- student
- data scientist
- data science manager

This matrix adds one repository-maintainer lane for skills whose default user is
the person maintaining the operating system itself rather than one of the three
product roles. This lane is intentional: some skills are foundation capabilities
that support all three product lanes by keeping the repository, site, and skill
system coherent.

## Task-Type Vocabulary

The matrix deliberately mixes stage-based and role-based task types.

| Task type | Use for |
| --- | --- |
| `workflow-gate` | Canonical data science backbone gates |
| `workflow-support` | Adjacent artifacts, handoff, trace, communication, or distillation |
| `method-teaching` | Teaching or reference material for statistical and ML methods |
| `student-overlay` | Student delivery, hints, memory, exercises, or misconception repair |
| `practitioner-overlay` | Direct execution and artifact enforcement for working analysts |
| `software-team` | Data scientists collaborating with engineering systems |
| `diagnostics` | Debugging, prototypes, or failure localization |
| `manager-ops` | Project operations and recurring coordination |
| `manager-communication` | Manager-facing summaries, updates, and project communication |
| `site-maintenance` | Repository documentation, navigation, style, and visual review |
| `skill-pack` | Bundled checks, templates, or sub-workflows |

## Current Matrix

### Student

| Task type | Default skills |
| --- | --- |
| `student-overlay` | `identity-loader`, `repo-bootstrap-student`, `session-wrap`, `tutor-mode`, `socratic-tutor`, `hint-ladder`, `exercise-generator`, `misconception-diagnosis` |
| `method-teaching` | `linear-regression`, `ridge-regression`, `lasso`, `cross-validation`, `random-forest`, `gradient-boosting`, `islr-resource`, `explain-method` |

### Data Scientist

| Task type | Default skills |
| --- | --- |
| `workflow-gate` | `project-bootstrap`, `problem-framing`, `data-audit`, `eda-plan`, `modeling`, `model-evaluation`, `experiment-log` |
| `workflow-support` | `causal-design-check`, `grill-problem-frame`, `paper-to-replication`, `result-communication`, `workflow-trace`, `handoff`, `trace-distillation` |
| `diagnostics` | `debug-analysis-notebook`, `debug-model-failure`, `model-prototype` |
| `software-team` | `grill-with-codebase`, `zoom-out`, `tdd-data-pipeline`, `ml-feature-spec` |
| `practitioner-overlay` | `execution-mode`, `artifact-enforcer` |
| `skill-pack` | `core-ml` |

### Data Science Manager

| Task type | Default skills |
| --- | --- |
| `manager-ops` | `project-setup`, `project-manager-agent`, `lab-manager-agent`, `weekly-review`, `inbox-triage` |
| `manager-communication` | `stakeholder-update`, `communication-workflows`, `executive-summary`, `project-tracker` |

### Repository Maintainer

| Task type | Default skills |
| --- | --- |
| `site-maintenance` | `site-voice`, `ui-ux-review`, `navigation-review`, `visual-polish-pass` |

## Overlap Watchlist

These are not automatic conflicts. They are cells or neighboring cells where a
future intake PR should run comparative evals before admitting another skill.

| Area | Skills to compare | Review question |
| --- | --- | --- |
| Problem definition | `problem-framing`, `grill-problem-frame`, `causal-design-check` | Is the new skill framing the project, pressure-testing the frame, or validating causal claims? |
| Modeling and method rationale | `modeling`, `model-prototype`, `core-ml`, `explain-method`, method skills | Is the new skill executing a gate, running a throwaway probe, bundling checks, or teaching a method? |
| Debugging | `debug-analysis-notebook`, `debug-model-failure`, `model-prototype` | Is the failure execution-level, semantic/model-level, or a quick learnability probe? |
| Session closure | `workflow-trace`, `handoff`, `trace-distillation`, `session-wrap` | Is the output a session record, a handoff, a reusable lesson, or student memory? |
| Student help | `tutor-mode`, `socratic-tutor`, `hint-ladder`, `misconception-diagnosis`, `exercise-generator` | Is the student asking for guided workflow help, a hint, diagnosis, or practice? |
| Manager operations | `project-setup`, `project-manager-agent`, `lab-manager-agent`, `weekly-review`, `project-tracker` | Is the scope one project, a portfolio, a recurring review, or a manager-facing overlay? |
| Manager communication | `stakeholder-update`, `communication-workflows`, `executive-summary` | Is the output an external update, a communication workflow, or a summary wrapper? |
| Site work | `site-voice`, `ui-ux-review`, `navigation-review`, `visual-polish-pass` | Is the change about copy voice, page hierarchy, navigation, or visual finishing? |

## Legacy And Duplicate Surfaces

The matrix covers folder-based `SKILL.md` files only. The repository still
contains command-style markdown skills and support files. They remain for
compatibility while migration happens gradually. Each migration, archive, or
keep decision should be tracked in `planning.md` or the relevant PR summary so
legacy surface area does not become invisible.

Legacy review candidates:

- `skills/data-science/proposal-write.md`
- `skills/data-science/proposal-revise.md`
- `skills/data-science/review-plan.md`
- `skills/data-science/tax-guide.md`
- `skills/manager/*.md` command-style workflows such as `weekly-review.md`,
  `triage-inbox.md`, `setup-project-management.md`, and `checkin.md`
- `skills/overlays/*.md` command-style prompt and tips workflows

Support files that should not be admitted as standalone skills unless promoted:

- `skills/packs/core-ml/checks/*.md`
- `skills/packs/core-ml/workflows/*.md`
- `skills/packs/core-ml/templates/*.md`
- `skills/overlays/*-references/*.md`

## Metadata Normalization Follow-Ups

The current inventory predates this matrix. Future cleanup PRs should normalize:

- `skills/resources/islr/SKILL.md` uses `category: resources`; this category
  should remain explicit in `skills/METADATA.md`.
- PR-1 should normalize `skills/site-voice/SKILL.md`; it has frontmatter but
  lacks `category`, `status`, `stage`, and `role_compatibility`.
- Some software-team skills list `practitioner` as a role alias. New skills
  should use `data scientist`; cleanup can normalize aliases later.
