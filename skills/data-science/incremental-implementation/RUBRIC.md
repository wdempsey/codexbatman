# Incremental Implementation Rubric

Score a use of this skill against these checks:

- Confirms the contract before editing.
- Chooses a vertical, contract-first, risk-first, or cleanup-first slice deliberately.
- States what is out of scope for the current slice.
- Keeps the repository buildable or clearly reports a verification blocker.
- Runs the least expensive meaningful check after each slice.
- Stops implementation when verification fails and routes to debugging.
- Keeps refactors separate unless required by the slice.
- Ends with completed slices, verification evidence, open risks, and next step.

Failure modes:

- Building scaffolding across many files with no working behavior.
- Mixing unrelated cleanup into the feature.
- Saving all verification for the end.
- Using this skill to skip data-science workflow gates.
- Treating TDD and implementation slicing as the same job.
