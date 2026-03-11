# Experiment Log

Experiment logging is the canonical record of analytical iteration.

It exists to make model development reproducible, reviewable, and harder to narrate backward.

## Why This Workflow Matters

Unlogged experimentation produces familiar problems:

- model changes are remembered incorrectly
- split changes are omitted from comparisons
- failed runs disappear from memory
- metrics drift without explanation
- seeds, parameters, and dataset versions go undocumented

The experiment log exists to make each run a durable artifact rather than a disposable event.

This phase aligns with the reproducibility commitments in [Goals of the Data Science Layer](goals.md) and [Data Science Layer Blueprint](blueprint.md).

## Common Mistakes

- Logging only successful runs.
- Omitting dataset version, seed, or split strategy.
- Comparing runs that are not actually comparable.
- Recording results without stating the hypothesis.
- Continuing iteration before the current run is logged.
- Treating the experiment log as an afterthought at the end of a project.

## Step-by-Step Workflow

### 1. Record context

Capture:

- date
- author
- dataset version
- unit of analysis
- target definition
- split strategy

### 2. Record the hypothesis

State:

- what changed
- why the change was made
- what result was expected

### 3. Record configuration

Document:

- model type
- hyperparameters
- preprocessing
- feature set version
- evaluation window
- random seed

### 4. Record results

Report:

- primary metric
- secondary metrics
- comparison to baseline
- any subgroup or error analysis notes

### 5. Record interpretation

Codex should answer:

- did the hypothesis hold
- is the change meaningful
- is there evidence of instability or overfitting
- what should happen next

### 6. Record decision outcome

End the entry with a decision such as:

- continue iterating
- revert
- freeze
- escalate for review

## Expected Artifacts

- Structured experiment log entry
- Explicit hypothesis section
- Configuration record
- Results section
- Interpretation section
- Decision outcome

## How Codex Should Use The Skill

Codex should use `skills/data-science/experiment-log/SKILL.md` after every meaningful modeling or evaluation change.

Codex should:

- insist on enough detail to reproduce the run
- preserve failed runs
- compare against a stated baseline
- stop unsupported interpretation

Codex should not:

- accept undocumented metric changes
- silently reuse the same seed or split
- let a run disappear because the result was weak

## Run With Codex

```text
Use the experiment-log skill on the latest training run and write the canonical entry before we discuss next steps.
```

```text
Run experiment-log for this model comparison. Include the split strategy, seed, baseline, and interpretation.
```

```text
Apply the experiment-log skill to this failed run too. I want the full artifact, not just the metrics.
```
