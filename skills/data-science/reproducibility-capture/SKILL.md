---
name: reproducibility-capture
description: Capture the seed, data version, code version, environment, commands, and randomness controls needed to reproduce data-science results. Use before sharing EDA, modeling, evaluation, or handoff claims whose evidence must be rerunnable.
category: data-science
status: active
stage: logging
role_compatibility:
  - data scientist
inputs:
  - result or claim to reproduce
  - code location
  - dataset source or version
  - command or notebook path
outputs:
  - reproducibility capsule
  - missing reproducibility gaps
  - experiment-log or workflow-trace handoff
recommended_next:
  - experiment-log
  - workflow-trace
  - model-evaluation
---

# Reproducibility Capture

## Purpose

Use this skill to turn a result into something another data scientist can rerun or audit.

This skill captures reproducibility metadata. It does not replace `experiment-log`, which records modeling run interpretation and decisions.

## Use When

- Before reporting EDA, modeling, or evaluation results.
- Before handing a project to another human or agent.
- After changing dependencies, data extracts, split logic, seeds, or runtime environment.
- When a notebook result cannot be reproduced from the current artifacts.

Do not use this to interpret model performance. Use `experiment-log` and `model-evaluation` for interpretation and decisions.

## Stop Conditions

Do not present a result as reproducible if any of these are unknown:

- dataset version or extract definition
- code version or changed-file state
- command, notebook, or script that produced the result
- seed or randomness policy for stochastic steps
- package/environment source

If a field is missing, record the gap and the action needed to close it.

## Procedure

### 1. Name The Claim Or Result

State the result being made reproducible and the artifact it belongs to: EDA journal entry, experiment log entry, model card, evaluation report, or handoff.

### 2. Capture Data Version

Record:

- source path, table, query, or artifact name
- extract date or snapshot identifier
- filters and inclusion/exclusion rules
- row count and key schema summary
- checksum or version pointer when available

### 3. Capture Code Version

Record:

- git branch and commit
- whether the worktree was clean or dirty
- changed files relevant to the result
- script, notebook, or entrypoint path
- exact command or notebook execution order when known

Do not require a clean worktree for exploration, but never hide a dirty worktree from the record.

### 4. Capture Environment

Record:

- language versions such as Python or R
- package manager and lockfile source
- key package versions
- operating system or runtime notes when relevant
- hardware/accelerator notes if nondeterminism or performance matters

### 5. Capture Randomness Controls

Record:

- global seed
- data split seed
- cross-validation or bootstrap seed
- model-specific seed
- known nondeterministic operations
- whether repeated runs are expected to match exactly or within tolerance

### 6. Write The Reproducibility Capsule

Use this template:

```markdown
## Reproducibility Capsule

Result:
Data version:
Code version:
Command or notebook path:
Environment:
Seed strategy:
Randomness caveats:
Known gaps:
Handoff:
```

If the result is a modeling run, copy or link the capsule into the `experiment-log` entry. If it is a broader session result, include it in `workflow-trace`.
