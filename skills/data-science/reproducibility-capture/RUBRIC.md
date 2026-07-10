# Reproducibility Capture Rubric

Score a use of this skill against these checks:

- Names the result or claim being made reproducible.
- Captures data source, extract/version, filters, row count, and schema/key summary.
- Captures git commit, branch, dirty state, changed files, and command or notebook path.
- Captures language/runtime and package environment source.
- Captures global, split, resampling, and model seeds where applicable.
- Records nondeterminism caveats and expected rerun tolerance.
- Lists missing fields as gaps rather than papering over them.
- Hands modeling runs to `experiment-log` and broader session records to `workflow-trace`.

Failure modes:

- Treating a result as reproducible with unknown data version.
- Omitting dirty worktree state.
- Recording a seed without saying where it was applied.
- Replacing experiment interpretation with metadata capture.
- Requiring a clean worktree for exploratory work instead of recording the state honestly.
