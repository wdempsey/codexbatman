# Examples: Debug Analysis Notebook

## Example 1

User request:

> This notebook's AUC jumped from 0.71 to 0.93 after a refactor. Debug it without rewriting the notebook.

Expected behavior:

- compare pre/post split and feature pipeline
- test leakage and contamination hypotheses
- propose minimal targeted fixes

Expected artifacts:

- symptom summary
- root-cause analysis
- minimal fix plan
- verification checks

## Example 2

User request:

> Plot outputs and metric tables disagree across cells. Diagnose and patch only what is necessary.

Expected behavior:

- trace dependency and execution-order issues
- identify stale variables or state carryover
- recommend deterministic rerun strategy

Expected artifacts:

- reproduction steps
- root-cause notes
- patch list and verification plan

## Example 3 (Bad Invocation)

User request:

> Just clean up and rewrite this notebook.

Expected Codex response:

- refuse broad rewrite-first request
- require symptom-led debug scope
- propose diagnosis-first workflow with minimal edits

Expected artifacts after correction:

- scoped debug plan
- root-cause evidence table
- minimal patch set
