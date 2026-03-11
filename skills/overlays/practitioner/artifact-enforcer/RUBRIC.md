# Rubric: Artifact Enforcer

## Passing Standard

The output passes if it:

- names the required artifact clearly
- checks it against the canonical workflow
- blocks progression when the artifact is incomplete

## Failure Modes

Fail if the output:

- treats an incomplete artifact as sufficient
- allows the phase transition without review
- rewrites the workflow instead of enforcing it
