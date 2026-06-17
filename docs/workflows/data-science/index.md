# Core Data Science Workflow

AI makes analysis faster. Workflow discipline makes it trustworthy. This page explains the seven-stage sequence that all three roles use — and why the order matters.

## The Canonical Sequence

Every project moves through these stages in order. The gates between them are not bureaucratic checkpoints — they exist because skipping them creates specific, recurring problems.

**1. Project Bootstrap** — set up the folder structure and backbone files before anything else. If you skip this, artifacts end up scattered and the next session starts from chaos.

**2. Problem Framing** — define the target, metric, decision context, and first risks before touching the data. If you skip this, you'll model the wrong thing and only notice after evaluation.

**3. Data Audit** — document what's in the dataset: missingness, leakage risks, column types, temporal structure. If you skip this, you'll find data quality problems at the worst possible moment — inside the model.

**4. Exploratory Analysis** — run a bounded EDA focused on the questions the framing raised. The key word is *bounded*: EDA without a plan tends to drift and never end.

**5. Modeling** — fit a baseline first, then one or two justified candidates. Never skip the baseline — it's the only way to know if complexity is helping.

**6. Evaluation** — interpret results against the framing, check for failure modes and edge cases, and decide whether the model is ready to advance or needs revision.

**7. Experiment Logging** — record every run so the next session can start from real project state, not a reconstruction of what you think you tried.

## Skills That Run Each Stage

Each phase is a Codex skill you can invoke directly. The skill enforces the gate — it won't let you skip to modeling before the audit is in reasonable shape.

| Stage | Skill | What it enforces |
|---|---|---|
| Project Bootstrap | [`project-bootstrap`](https://github.com/wdempsey/codexbatman/tree/main/skills/data-science/project-bootstrap) | backbone folder structure and initial files |
| Problem Framing | [`problem-framing`](https://github.com/wdempsey/codexbatman/tree/main/skills/data-science/problem-framing) | target, metric, decision context, risk register |
| Data Audit | [`data-audit`](https://github.com/wdempsey/codexbatman/tree/main/skills/data-science/data-audit) | missingness, leakage flags, schema review |
| Exploratory Analysis | [`eda-plan`](https://github.com/wdempsey/codexbatman/tree/main/skills/data-science/eda-plan) | bounded exploration questions and plot priorities |
| Modeling | [`modeling`](https://github.com/wdempsey/codexbatman/tree/main/skills/data-science/modeling) | baseline + candidate models, validation approach |
| Evaluation | [`model-evaluation`](https://github.com/wdempsey/codexbatman/tree/main/skills/data-science/model-evaluation) | performance interpretation, failure analysis, advance decision |
| Experiment Logging | [`experiment-log`](https://github.com/wdempsey/codexbatman/tree/main/skills/data-science/experiment-log) | reproducible run record with next action |

## How Each Role Uses This

All three roles run the same sequence. What changes is the interaction style.

Students work through the gates with coaching — Codex asks for their reasoning before revealing the output, uses hints before full answers, and keeps the scaffolding visible. Practitioners move through the same gates with less hand-holding — Codex executes more directly and expects artifact-quality output. Managers use the gates as checkpoints: they verify that projects are ready to advance rather than running the steps themselves.

## Where To Go Next

If you haven't run a project yet, the [Analytics Repo Example](../../examples/analytics-repo/index.md) shows the full sequence on a concrete housing-price dataset — with student and practitioner lenses. That's the fastest way to see this workflow in practice.

If you want to understand the artifact system underneath the workflow, read [Backbone Protocol](../../backbone/index.md).
