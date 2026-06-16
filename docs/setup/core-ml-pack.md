---
description: Overview of the core-ml skill pack for basic supervised ML workflows inside the Codex Batman backbone.
---

# Core ML Pack

The `core-ml` pack is the first repo-native skill pack for common supervised learning workflows.

It is designed to make basic ML more disciplined without making the repository heavier.

## What It Covers

The pack currently includes:

- workflow guides for regression, binary classification, and multiclass classification
- checks for leakage, split validity, and metric alignment
- lightweight templates for evaluation reports and model cards

## What It Emphasizes

- defining the target clearly
- confirming unit of analysis
- confirming prediction time
- validating train/test design
- checking leakage risks
- fitting a baseline first
- comparing models under the same protocol
- selecting metrics that match the decision context
- documenting outputs in reproducible artifacts

## Pack Location

- [`skills/packs/core-ml`](https://github.com/wdempsey/codexbatman/tree/main/skills/packs/core-ml)

## How It Fits The Backbone

This pack is a support layer, not a replacement for the canonical workflow.

Use it after:

- problem framing
- data audit
- bounded exploratory planning

Then combine it with:

- `modeling`
- `model-evaluation`
- `experiment-log`

## Related Pages

- [Skill Library](skill-reference.md)
- [Backbone Protocol](../backbone/index.md)
- [Core Data Science Workflow](../workflows/data-science/index.md)
