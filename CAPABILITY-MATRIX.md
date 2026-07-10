# Capability Matrix

This matrix is the intake map for folder-based Codex skills in this repository.
It answers one question: when a new skill is proposed, what existing capability
does it compete with?

The matrix classifies the current folder-based `SKILL.md` inventory. Each skill
occupies exactly one default cell, even when its frontmatter lists multiple
compatible roles. That default cell is the dedupe and evaluation owner.

Current coverage: 63 folder-based `SKILL.md` files.

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

Admission policy lives in `SKILL-STYLE.md`. In this matrix, every new skill must
either own a distinct default cell/job, replace an incumbent after eval
comparison, or be rejected/folded into an incumbent as examples, rubric, or
reference material.

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
| `router` | Cross-lane orientation that chooses the role, overlay, and workflow without doing the downstream work |
| `skill-maintenance` | Skill telemetry, evals, improvement proposals, and intake-system upkeep |
| `site-maintenance` | Repository documentation, navigation, style, and visual review |
| `skill-pack` | Bundled checks, templates, or sub-workflows |

## Current Matrix

### Student

| Task type | Default skills |
| --- | --- |
| `student-overlay` | `identity-loader`, `repo-bootstrap-student`, `session-wrap`, `class-notes-ingestion`, `grill-the-student`, `tutor-mode`, `socratic-tutor`, `hint-ladder`, `exercise-generator`, `misconception-diagnosis` |
| `method-teaching` | `linear-regression`, `ridge-regression`, `lasso`, `cross-validation`, `random-forest`, `gradient-boosting`, `islr-resource`, `explain-method` |

### Data Scientist

| Task type | Default skills |
| --- | --- |
| `workflow-gate` | `project-bootstrap`, `problem-framing`, `data-audit`, `eda-plan`, `modeling`, `model-evaluation`, `experiment-log` |
| `workflow-support` | `causal-design-check`, `grill-problem-frame`, `eda-hypothesis-journal`, `plan-as-guidance`, `paper-to-replication`, `reproducibility-capture`, `result-communication`, `workflow-trace`, `handoff`, `trace-distillation` |
| `diagnostics` | `debug-analysis-notebook`, `debug-model-failure`, `model-prototype` |
| `software-team` | `interview-me`, `grill-with-codebase`, `zoom-out`, `ml-feature-spec`, `incremental-implementation`, `tdd-data-pipeline`, `code-review-and-quality` |
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
| `router` | `ask-codexbatman` |
| `skill-maintenance` | `improve-skill` |
| `site-maintenance` | `site-voice`, `ui-ux-review`, `navigation-review`, `visual-polish-pass` |

## Overlap Watchlist

These are not automatic conflicts. They are cells or neighboring cells where a
future intake PR should run comparative evals before admitting another skill.

| Area | Skills to compare | Review question |
| --- | --- | --- |
| Problem definition | `problem-framing`, `grill-problem-frame`, `causal-design-check` | Is the new skill framing the project, pressure-testing the frame, or validating causal claims? |
| Planning and revision | `plan-as-guidance`, `ml-feature-spec`, `incremental-implementation`, `workflow-trace` | Is the new skill writing the spec, guiding a flexible plan, executing a slice, or recording what changed? |
| EDA execution and reproducibility | `eda-plan`, `eda-hypothesis-journal`, `data-audit`, `reproducibility-capture`, `experiment-log` | Is the new skill planning EDA, executing logged EDA checks, gating data readiness, capturing rerun metadata, or recording a modeling run? |
| Modeling and method rationale | `modeling`, `model-prototype`, `core-ml`, `explain-method`, method skills | Is the new skill executing a gate, running a throwaway probe, bundling checks, or teaching a method? |
| Debugging | `debug-analysis-notebook`, `debug-model-failure`, `model-prototype` | Is the failure execution-level, semantic/model-level, or a quick learnability probe? |
| Software-team delivery | `interview-me`, `ml-feature-spec`, `incremental-implementation`, `tdd-data-pipeline`, `code-review-and-quality` | Is the new skill clarifying intent, writing the spec, slicing implementation, writing tests first, or reviewing the finished change? |
| Session closure | `workflow-trace`, `handoff`, `trace-distillation`, `session-wrap` | Is the output a session record, a handoff, a reusable lesson, or student memory? |
| Student help | `tutor-mode`, `socratic-tutor`, `hint-ladder`, `misconception-diagnosis`, `exercise-generator` | Is the student asking for guided workflow help, a hint, diagnosis, or practice? |
| Student context intake | `identity-loader`, `class-notes-ingestion`, `grill-the-student`, `tutor-mode`, `misconception-diagnosis` | Is the missing piece student identity, persistent class-note context, pre-answer context alignment, ordinary tutoring, or misconception repair? |
| Manager operations | `project-setup`, `project-manager-agent`, `lab-manager-agent`, `weekly-review`, `project-tracker` | Is the scope one project, a portfolio, a recurring review, or a manager-facing overlay? |
| Manager communication | `stakeholder-update`, `communication-workflows`, `executive-summary` | Is the output an external update, a communication workflow, or a summary wrapper? |
| Routing | `ask-codexbatman`, role overlays, workflow gates | Is the proposed skill only choosing a route, or is it executing a workflow step? |
| Skill improvement | `improve-skill`, `SKILL-STYLE.md`, eval runner | Is the work diagnosing an existing skill, proposing a patch, or implementing an approved skill change? |
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
- `skills/site-voice/SKILL.md` was normalized in PR-1.
- Software-team skills were normalized from the legacy `practitioner` role alias
  to `data scientist` in PR-1.
