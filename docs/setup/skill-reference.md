# Skill Library

The Skill Library is the shared catalog hub for this repository's skills.

Use it to understand what exists, how the skills are grouped, and where to find the source folders. Role pages summarize which skills matter most for each audience; this page is the shared reference point.

## Core Data Science Workflow

These are the canonical shared workflow skills.

- [`project-bootstrap`](https://github.com/wdempsey/codexbatman/tree/main/skills/data-science/project-bootstrap): establish the minimum artifact and workspace backbone before analysis begins
- [`problem-framing`](https://github.com/wdempsey/codexbatman/tree/main/skills/data-science/problem-framing): define the analytical question, constraints, and success criteria
- [`data-audit`](https://github.com/wdempsey/codexbatman/tree/main/skills/data-science/data-audit): assess data readiness, risk, and stop conditions
- [`eda-plan`](https://github.com/wdempsey/codexbatman/tree/main/skills/data-science/eda-plan): design bounded exploration before open-ended analysis
- [`modeling`](https://github.com/wdempsey/codexbatman/tree/main/skills/data-science/modeling): structure model-building work after workflow gates are satisfied
- [`model-evaluation`](https://github.com/wdempsey/codexbatman/tree/main/skills/data-science/model-evaluation): evaluate performance, limitations, and fit for purpose
- [`experiment-log`](https://github.com/wdempsey/codexbatman/tree/main/skills/data-science/experiment-log): document each modeling run and next step

See [Core Data Science Workflow](../workflows/data-science/index.md) for the narrative workflow pages that explain when these skills should run.

## Role Overlays

These overlays change delivery style without replacing canonical workflow logic.

- Router: [`ask-codexbatman`](https://github.com/wdempsey/codexbatman/tree/main/skills/overlays/ask-codexbatman) chooses the role, overlay, and workflow when the next step is ambiguous
- Skill maintenance: [`improve-skill`](https://github.com/wdempsey/codexbatman/tree/main/skills/overlays/improve-skill) turns telemetry, corrections, and eval results into a proposed skill patch without editing in place
- Student overlays: [`class-notes-ingestion`](https://github.com/wdempsey/codexbatman/tree/main/skills/overlays/student/class-notes-ingestion), [`grill-the-student`](https://github.com/wdempsey/codexbatman/tree/main/skills/overlays/student/grill-the-student), [`tutor-mode`](https://github.com/wdempsey/codexbatman/tree/main/skills/overlays/student/tutor-mode), [`hint-ladder`](https://github.com/wdempsey/codexbatman/tree/main/skills/overlays/student/hint-ladder), [`misconception-diagnosis`](https://github.com/wdempsey/codexbatman/tree/main/skills/overlays/student/misconception-diagnosis), [`exercise-generator`](https://github.com/wdempsey/codexbatman/tree/main/skills/overlays/student/exercise-generator)
- Practitioner overlays: [`execution-mode`](https://github.com/wdempsey/codexbatman/tree/main/skills/overlays/practitioner/execution-mode), [`artifact-enforcer`](https://github.com/wdempsey/codexbatman/tree/main/skills/overlays/practitioner/artifact-enforcer)
- Manager overlays: [`executive-summary`](https://github.com/wdempsey/codexbatman/tree/main/skills/overlays/manager/executive-summary), [`project-tracker`](https://github.com/wdempsey/codexbatman/tree/main/skills/overlays/manager/project-tracker), [`communication-workflows`](https://github.com/wdempsey/codexbatman/tree/main/skills/overlays/manager/communication-workflows)

Role guides:

- [For Students](../students/index.md)
- [For Data Scientists](../data-scientists/index.md)
- [For Data Science Managers](../managers/index.md)

## Manager Workflow Skills

These support coordination, planning, and communication around analytical work.

- [`lab-manager-agent`](https://github.com/wdempsey/codexbatman/tree/main/skills/manager/lab-manager-agent): maintain portfolio visibility across projects, deadlines, handoffs, and waiting-on dependencies
- [`project-setup`](https://github.com/wdempsey/codexbatman/tree/main/skills/manager/project-setup): initialize project operations and coordination structure
- [`project-manager-agent`](https://github.com/wdempsey/codexbatman/tree/main/skills/manager/project-manager-agent): maintain one project's state, actions, decisions, and handoffs
- [`weekly-review`](https://github.com/wdempsey/codexbatman/tree/main/skills/manager/weekly-review): summarize progress, blockers, and open questions
- [`stakeholder-update`](https://github.com/wdempsey/codexbatman/tree/main/skills/manager/stakeholder-update): turn project state into clear communication
- [`inbox-triage`](https://github.com/wdempsey/codexbatman/tree/main/skills/manager/inbox-triage): manage operational intake and prioritize follow-up

See [Project Management](../workflows/project-management.md), [Managing Data Science](../workflows/managing-data-science/index.md), and [Lab Manager Agent](../workflows/manager/lab-manager-agent.md) for the manager workflow layer.

## Additional Shared Skills

The repository also contains additional reusable data science skills that can plug into specific projects:

- [`causal-design-check`](https://github.com/wdempsey/codexbatman/tree/main/skills/data-science/causal-design-check)
- [`debug-analysis-notebook`](https://github.com/wdempsey/codexbatman/tree/main/skills/data-science/debug-analysis-notebook): diagnose notebook execution errors without destructive rewrites
- [`debug-model-failure`](https://github.com/wdempsey/codexbatman/tree/main/skills/data-science/debug-model-failure): systematic loop for semantic model failures — code runs but results are wrong; reproduce → minimise → hypothesise → fix
- [`grill-problem-frame`](https://github.com/wdempsey/codexbatman/tree/main/skills/data-science/grill-problem-frame): challenge a problem statement before any data is touched — decision context, metric, prediction time, leakage risks, population scope
- [`explain-method`](https://github.com/wdempsey/codexbatman/tree/main/skills/data-science/explain-method): zoom out and explain why a method fits the current problem — assumptions, alternatives, model card justification
- [`handoff`](https://github.com/wdempsey/codexbatman/tree/main/skills/data-science/handoff): produce a short structured session handoff so the next person or agent can continue without rebuilding context
- [`model-prototype`](https://github.com/wdempsey/codexbatman/tree/main/skills/data-science/model-prototype): quick throwaway model to test a specific hypothesis before committing to the full workflow
- [`paper-to-replication`](https://github.com/wdempsey/codexbatman/tree/main/skills/data-science/paper-to-replication)
- [`repo-bootstrap-student`](https://github.com/wdempsey/codexbatman/tree/main/skills/data-science/repo-bootstrap-student): teach a student how to create a GitHub-backed data science repository with a minimal artifact-first structure and first commit
- [`result-communication`](https://github.com/wdempsey/codexbatman/tree/main/skills/data-science/result-communication)
- [`trace-distillation`](https://github.com/wdempsey/codexbatman/tree/main/skills/data-science/trace-distillation)
- [`workflow-trace`](https://github.com/wdempsey/codexbatman/tree/main/skills/data-science/workflow-trace)

## Software Team Skills

These skills are for data scientists working as part of a software engineering team — writing production code, collaborating with engineers, and shipping ML features through a standard development workflow. Adapted from [Matt Pocock's engineering skills](https://github.com/mattpocock/skills).

- [`tdd-data-pipeline`](https://github.com/wdempsey/codexbatman/tree/main/skills/data-science/tdd-data-pipeline): test-driven development for data pipelines, feature transforms, and model inference wrappers — red-green-refactor loop, behavioral contracts not implementation details
- [`zoom-out`](https://github.com/wdempsey/codexbatman/tree/main/skills/data-science/zoom-out): map an unfamiliar section of code — callers, data flow, downstream dependencies, backbone artifact references — before modifying anything
- [`grill-with-codebase`](https://github.com/wdempsey/codexbatman/tree/main/skills/data-science/grill-with-codebase): build a shared domain language with the engineering team before writing production data science code — resolves naming conflicts, documents conventions, creates `DATA_CONTEXT.md` and ADRs
- [`ml-feature-spec`](https://github.com/wdempsey/codexbatman/tree/main/skills/data-science/ml-feature-spec): write a machine learning feature spec (PRD) and break it into vertical-slice GitHub issues — input/output contracts, validation criteria, user stories, monitoring requirements

## Methods Skills

Method skills teach a specific ML technique in context — they pause the workflow, explain the method, and hand back to the gate where the method will be applied. Each references the relevant ISLR chapter.

- [`linear-regression`](https://github.com/wdempsey/codexbatman/tree/main/skills/methods/linear-regression): ISLR Ch. 3
- [`ridge-regression`](https://github.com/wdempsey/codexbatman/tree/main/skills/methods/ridge-regression): ISLR Ch. 6
- [`lasso`](https://github.com/wdempsey/codexbatman/tree/main/skills/methods/lasso): ISLR Ch. 6
- [`cross-validation`](https://github.com/wdempsey/codexbatman/tree/main/skills/methods/cross-validation): ISLR Ch. 5 — k-fold CV, LOOCV, the preprocessing-inside-the-fold rule
- [`random-forest`](https://github.com/wdempsey/codexbatman/tree/main/skills/methods/random-forest): ISLR Ch. 8 — bagging, variable importance, when to use vs. linear baseline
- [`gradient-boosting`](https://github.com/wdempsey/codexbatman/tree/main/skills/methods/gradient-boosting): ISLR Ch. 8 — sequential improvement on residuals, tuning parameters

## Textbook Resources

Resource skills map canonical textbooks to the method and workflow skills that use them. Install a resource skill to give Codex access to chapter-level explanations when a method is introduced in tutor mode.

- [`islr-resource`](https://github.com/wdempsey/codexbatman/tree/main/skills/resources/islr): chapter index for *An Introduction to Statistical Learning* (James et al.) — routes students to the right chapter for any method in the curriculum

## Skill Packs

Skill packs group a workflow family with reusable checks and templates.

- [`core-ml`](https://github.com/wdempsey/codexbatman/tree/main/skills/packs/core-ml): basic supervised ML workflows with explicit leakage checks, split-validity checks, metric alignment checks, evaluation scaffolds, and model-card scaffolds

See [Core ML Pack](core-ml-pack.md) for the repository-facing overview.

## Site Review Skills

These skills help future Codex sessions improve the documentation site without overbuilding it.

- [`site-voice`](https://github.com/wdempsey/codexbatman/tree/main/skills/site-voice): apply the repository's direct, warm, technically precise site voice to docs pages and navigation copy
- [`ui-ux-review`](https://github.com/wdempsey/codexbatman/tree/main/skills/site/ui-ux-review): review one page at a time for page purpose, audience, hierarchy, copy density, and next-action clarity
- [`navigation-review`](https://github.com/wdempsey/codexbatman/tree/main/skills/site/navigation-review): review `mkdocs.yml`, section naming, orphan pages, and cross-links among major site sections
- [`visual-polish-pass`](https://github.com/wdempsey/codexbatman/tree/main/skills/site/visual-polish-pass): apply restrained Material-native polish after structure and content are already in place

See [Site Review](../site/index.md) and [UI/UX Standards](../site/ui-ux-standards.md) for the repo-local guidance these skills should follow.

## Build And Extend

Use [Build Your Own](../system/index.md) for the meta-layer: how to design skills, when to use agents, and how to improve the system over time. Use [Downloads & Reference Library](../downloads/index.md) for longer-form guides and templates.

## Legacy References

These compatibility anchors preserve older internal links while the shared catalog is simplified.

### External And Inherited References

<a id="done-session-capture"></a>
<a id="morning-brief-daily-briefing"></a>
<a id="checkin-daily-check-in-session"></a>
<a id="schedule-query-calendar-availability"></a>
<a id="todo-add-add-to-do-item"></a>
<a id="todo-review-to-do-review"></a>
<a id="todo-queue-todo-queue"></a>
<a id="goals-review-goals-review"></a>
<a id="tips-curate-tip-curation"></a>
<a id="proposal-write-proposal-drafting"></a>
<a id="proposal-revise-proposal-revision"></a>
<a id="review-writing"></a>
<a id="review-methodology"></a>

These links point to entries that were part of the inherited long-form reference library. They are not part of the current repository skill catalog, but pages that still mention them can continue to land here while the surrounding docs are cleaned up.

### Current Repository Equivalents

<a id="triage-inbox-smart-inbox-triage"></a>
<a id="setup-project-management-project-setup"></a>
<a id="weekly-review-weekly-project-review"></a>

Current closest matches in this repository:

- `triage-inbox` -> [`inbox-triage`](https://github.com/wdempsey/codexbatman/tree/main/skills/manager/inbox-triage)
- `setup-project-management` -> [`project-setup`](https://github.com/wdempsey/codexbatman/tree/main/skills/manager/project-setup)
- `weekly-review` -> [`weekly-review`](https://github.com/wdempsey/codexbatman/tree/main/skills/manager/weekly-review)
