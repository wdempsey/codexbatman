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

## The Gates in Detail

Each gate has its own page explaining what Codex checks, why it matters, and what the common failure modes are — with interactive exercises using the cardiac risk dataset as a running example.

| Gate | What it enforces |
|---|---|
| [Problem Framing](problem-framing.md) | target, metric, decision context, prediction time, population scope |
| [Data Audit](data-audit.md) | missingness, leakage flags, schema review, stop conditions |
| [EDA Plan](eda-plan.md) | bounded exploration questions, stopping criterion, analysis plan |
| [Modeling](modeling.md) | baseline first, preprocessing inside the fold, cross-validation setup |
| [Evaluation](evaluation.md) | held-out performance, confusion matrix at threshold, subgroup analysis, limitations |
| [Experiment Log](experiment-log.md) | every run recorded with decision notes, not just the winner |

Project Bootstrap (folder structure and backbone files before any analysis) is covered in [Quickstart](../../quickstart.md).

## How Each Role Uses This

All three roles run the same sequence. What changes is the interaction style.

Students work through the gates with coaching — Codex asks for their reasoning before revealing the output, uses hints before full answers, and keeps the scaffolding visible. Practitioners move through the same gates with less hand-holding — Codex executes more directly and expects artifact-quality output. Managers use the gates as checkpoints: they verify that projects are ready to advance rather than running the steps themselves.

## Where To Go Next

If you haven't run a project yet, the [Basic Classification Example](../../examples/basic-classification/index.md) shows the full sequence on the Cleveland Heart Disease dataset — with student, practitioner, and manager lenses. That's the fastest way to see this workflow in practice.

If you want to understand the artifact system underneath the workflow, read [Backbone Protocol](../../backbone/index.md).
