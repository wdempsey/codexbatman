# Evals

This directory is a lightweight scaffold for PR-3. It is not a runnable harness yet.

Use these files to capture skill-routing examples in a stable, reviewable format before the telemetry and eval runner exist.

Each eval task should include:

- `Input`
- `Expected route`
- `Must include`
- `Must not`
- `Notes for PR-3`

PR-3 should decide the runnable format, split frozen held-out tasks from improvement tasks, and connect telemetry or trigger-miss logs to this directory.
