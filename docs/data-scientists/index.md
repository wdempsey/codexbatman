# For Researchers & Data Scientists

**This is for you if you're running real analysis and want Codex to enforce artifacts, workflow gates, and reproducible forward progress — not just chat along while you work.**

## Start Here

Begin with [**Core Data Science Workflow**](../workflows/data-science/index.md).

Researchers and data scientists use Codex as a workflow executor — not a chat assistant. The emphasis is direct execution, artifact quality, and forward progress. Use this page to find the practitioner overlays and skills that matter most during execution.

## What Changes In Practitioner Mode

Practitioner overlays keep the shared workflow strict and execution-oriented. Codex executes workflow steps directly rather than asking for your attempt first. Artifacts are produced with minimal scaffolding — the emphasis is output quality and forward progress, not step-by-step coaching. Workflow gates still apply, but Codex moves through them faster and expects you to direct the exceptions.

The underlying backbone and standards are identical to the student path. What changes is speed, delegation, and the assumption that you already know what you're trying to produce.

If you're not sure where to open first: workflow, then backbone, then examples, then skill catalog.

## Here's Why This Order Matters

Start with [Core Data Science Workflow](../workflows/data-science/index.md) to learn the execution sequence and the gates that separate each stage. Then read [Backbone Protocol](../backbone/index.md) — it tells you which durable artifacts your project should keep, so nothing lives only in the chat. Open [Examples](../examples/index.md) before adapting the system to your own project, and use the [Skill Library](../setup/skill-reference.md) once you understand how workflow and backbone fit together.

## If You Only Have Ten Minutes

Scan [Core Data Science Workflow](../workflows/data-science/index.md), open [Backbone Protocol](../backbone/index.md), and bookmark [Examples](../examples/index.md) for when you start your first real project. That's enough to get moving without reading everything first.

## Typical Practitioner Outputs

- framing artifacts
- data audit reports
- bounded EDA plans
- modeling outputs
- evaluation summaries
- experiment logs

## Example Practitioner Artifact

This is the kind of artifact the practitioner path should leave behind during execution:

```md
# experiment_log.md

- run_id: 2026-06-17-baseline-001
- baseline: linear regression
- comparison candidate: random forest
- split: fixed validation set
- metric: RMSE
- result: baseline remains the reference
- next action: inspect feature leakage and missingness handling
```

The point is that another analyst can see what has already been tried and what should happen next without reopening the whole chat history.

## If You Want A Real Repo Example

Open [Analytics Repo Example - Practitioner Path](../examples/analytics-repo/practitioner.md).

That page shows the intended shorter practitioner sequence for the same housing-price project backbone used in the student path.

## Researcher And Data Scientist Skills

- `project-bootstrap`
- `execution-mode`
- `artifact-enforcer`
- `problem-framing`
- `data-audit`
- `eda-plan`
- `modeling`
- `model-evaluation`
- `experiment-log`
- `result-communication`

## Where To Go Next

Start with [Core Data Science Workflow](../workflows/data-science/index.md) if you haven't already. After your first session, use the [Skill Library](../setup/skill-reference.md) to find practitioner skills and packs, and open [Core ML Pack](../setup/core-ml-pack.md) when you want a concrete supervised ML starter. [How Skills Work](../system/skills-explained.md) is worth reading once you want to understand the operating model beneath the surface.
