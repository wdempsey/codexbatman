---
title: How Skills Work
description: Explain how workflow skills, tutor overlays, and method skills interact in the Codex-native data science operating system.
---

# How Skills Work

## Workflow Skills

Workflow skills define the structure of a data science project.

Examples:

- `problem-framing`
- `data-audit`
- `eda-plan`
- `modeling`
- `model-evaluation`
- `experiment-log`

These skills define what step of the project you are in.

## Tutor Overlay

Tutor mode changes how Codex delivers workflow guidance.

Instead of giving answers immediately, it:

- asks questions
- prompts the student to think
- reveals the next step gradually

Tutor mode wraps workflow skills.

Example:

`tutor-mode + problem-framing`

## Method Skills

Method skills teach specific algorithms.

Examples:

- `linear-regression`
- `ridge-regression`
- `lasso`
- `random-forest`
- `gradient-boosting`

Method skills are invoked when a student encounters an unfamiliar method.

Workflow -> method explanation -> workflow resumes.

## Example Interaction

```text
Workflow skill
  |
  v
Tutor overlay
  |
  v
Method explanation (if needed)
  |
  v
Return to workflow
```
