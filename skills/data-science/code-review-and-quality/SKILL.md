---
name: code-review-and-quality
description: Review data-science software changes before merge for spec fit, tests, workflow gates, code quality, data risk, security, and maintainability. Use after a feature, bug fix, refactor, or agent-authored change is ready for review.
category: data-science
status: active
stage: evaluation
role_compatibility:
  - data scientist
  - data science manager
inputs:
  - diff or pull request
  - originating brief or spec
  - verification evidence
outputs:
  - ordered review findings
  - verification assessment
  - merge readiness recommendation
recommended_next:
  - incremental-implementation
  - handoff
source_attribution:
  - "Adapted from Addy Osmani's code-review-and-quality skill in addyosmani/agent-skills; rewritten for Codex Batman data-science software-team workflows."
---

# Code Review And Quality

## Purpose

Use this skill to decide whether a data-science software change is ready to merge.

The review standard is not perfection. The standard is that the change clearly improves the repo, satisfies the originating brief, preserves workflow discipline, and leaves a verification story a future maintainer can trust.

## Use When

- Reviewing a pull request, branch, or local diff before merge.
- Checking code produced by an agent or another collaborator.
- Reviewing a bug fix and its regression test.
- Reviewing data pipeline, feature engineering, inference, model-serving, documentation tooling, or workflow-code changes.

Do not use this as a substitute for `problem-framing`, `data-audit`, `model-evaluation`, or human sign-off where the workflow gates require them.

## Review Axes

Review in this order:

1. Brief fit: does the change do exactly what was requested?
2. Workflow gates: are problem framing, data audit, experiment log, model card, or human review requirements respected?
3. Correctness: do behavior, edge cases, and failure paths match the contract?
4. Tests and verification: would the checks catch a regression?
5. Data risk: leakage, split contamination, target timing, privacy, and schema assumptions.
6. Maintainability: naming, module boundaries, complexity, file size, and duplication.
7. Security and dependency risk: secrets, untrusted data, dependency need, license, and attack surface.
8. Performance: unbounded work, N+1 patterns, unnecessary recomputation, or expensive operations in hot paths.

## Procedure

### 1. Reconstruct The Contract

Read the brief, issue, PR body, or spec before reading the diff. State the expected behavior in one or two sentences. If the contract is missing, flag that before reviewing implementation details.

### 2. Review Tests First

Look at tests, evals, docs checks, and manual verification before implementation. Ask:

- Does a failing case exist for the bug or new behavior?
- Are tests behavioral rather than implementation-detail checks?
- Are data-science risks represented by checks or documented human review?
- Was the right local verification command run?

### 3. Review The Diff

Inspect changed files against the review axes. Prefer a few high-conviction findings over a long list of nits.

Use severity labels:

- Critical: security, data loss, broken workflow gate, or incorrect result.
- Required: must fix before merge.
- Optional: useful improvement that can be deferred.
- Nit: small style issue that does not block merge.
- FYI: context only.

### 4. Propose The Smaller Move

When flagging structure, propose the fix:

- collapse duplicate branches
- extract a focused helper
- move feature-specific logic out of shared code
- reuse the canonical helper
- make a boundary explicit instead of adding silent fallbacks
- split a large change into reviewable slices

### 5. State Merge Readiness

End with:

```text
Findings:
Verification reviewed:
Open questions:
Merge readiness: approve / request changes / blocked
```

If you identify orphaned code or files, list them and ask before deletion unless the user explicitly requested cleanup.
