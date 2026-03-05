---
hide:
  - navigation
description: Codex-native data science workflow system with structured workflow gates, reproducibility enforcement, and devlog-to-garden distillation.
social:
  cards_layout_options:
    title: Codex-Native Data Science Workflow System
    description: Structured, reproducible workflow for disciplined applied data science.
---

# Codex-Native Data Science Workflow System

<p class="hero-pitch">A structured operating system for applied data science: clear gates, reproducible execution, and documented decisions from framing through model handoff.</p>

<div class="hero-buttons">
<a href="quickstart.md" class="md-button md-button--primary">Get started</a>
<a href="workflows/data-science/blueprint.md" class="md-button">See the workflow</a>
<a href="workflows/data-science/goals.md" class="md-button">Set project goals</a>
<a href="https://github.com/wdempsey/codexbatman" class="md-button social-btn">GitHub</a>
</div>

<div class="credibility-strip" markdown>
This repository began as a fork of the original Claude Blattman site and evolved into a Codex-native data science system. The focus is methodological discipline: explicit stop conditions, reproducible runs, and human-reviewed conclusions.
</div>

## What Is This?

This project defines a practical workflow for applied data science teams and solo practitioners who want rigor without process theater. It combines workflow gates, experiment logging, and model documentation so work stays auditable and reusable.

The objective is not faster modeling. The objective is better analytical discipline.

## Where to Start

<div class="grid cards" markdown>

-   **:material-rocket-launch-outline: Quickstart**

    ---

    Install Codex, run the first workflow loop, and verify your setup with a concrete end-to-end check.

    [:octicons-arrow-right-24: Open Quickstart](quickstart.md)

-   **:material-target: Problem Framing + Goals**

    ---

    Define scope, constraints, and success criteria before touching data. This enforces decision quality from day one.

    [:octicons-arrow-right-24: Goals](workflows/data-science/goals.md)

-   **:material-file-chart-outline: Data Science Blueprint**

    ---

    Follow the full gate-based sequence: framing, data audit, planned EDA, logged experiments, and model card output.

    [:octicons-arrow-right-24: Blueprint](workflows/data-science/blueprint.md)

-   **:material-shield-check-outline: Reproducibility Standards**

    ---

    Deterministic seeds, pinned environments, and strict raw/processed separation are required, not optional.

    [:octicons-arrow-right-24: Process Rules](workflows/first-session-skills.md)

-   **:material-cog-outline: System Design Orientation**

    ---

    Build with database boundaries, join integrity, and downstream consumers in mind so analysis survives real deployment.

    [:octicons-arrow-right-24: System Patterns](system/index.md)

-   **:material-notebook-multiple-outline: Devlog and Distillation**

    ---

    Capture implementation decisions in devlogs, then distill transferable learnings into reusable operating knowledge.

    [:octicons-arrow-right-24: Downloads and References](downloads/index.md)

</div>

!!! tip "Stay in the loop"
    Iterate in small, reversible diffs. Verify locally with `mkdocs build`, then promote only changes that preserve correctness, safety, and link integrity.
