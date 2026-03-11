# Codex Batman

**A Codex-native Data Science Operating System for disciplined workflow design, execution, and review.**

Documentation site: [wdempsey.github.io/codexbatman](https://wdempsey.github.io/codexbatman/)

---

## What This Is

This repository defines a Codex-native operating system for applied data science.

It has three connected layers:

1. **Skills encode best practices** for recurring work such as framing, audits, experiment logging, planning, review, and writing.
2. **The website explains workflows** so users can understand the system architecture, adoption sequence, and operating rules.
3. **Codex executes workflows** against local files, project context, and reusable skill instructions.

The result is a practical system for moving from question framing to execution, review, and handoff with explicit gates and reusable documentation.

## Who It's For

The repository is organized around three roles:

- **Student**: learn structured problem framing, reproducible execution, and disciplined use of AI as a tutor and collaborator.
- **Data scientist**: use skills, templates, and workflow documentation to execute analysis and modeling work with stronger process controls.
- **Data science manager**: run project-centered planning, review, and coordination workflows across teams and stakeholders.

The materials are markdown-first, workflow-driven, and designed to be understandable without heavy software engineering overhead.

## Quick Start

1. Read the local quickstart: [`docs/quickstart.md`](docs/quickstart.md).
2. Or use the deployed page: [Quickstart](https://wdempsey.github.io/codexbatman/quickstart/).
3. Then choose your role lane in the workflow docs and skill library.

## Architecture

- Canonical workflow skills live under `skills/data-science/`.
- Manager workflows live under `skills/manager/`.
- Role overlays live under `skills/overlays/`.

## Roles

- Student -> scaffolded learning overlay
- Data Scientist -> direct execution overlay
- Data Science Manager -> planning, review, and communication overlay

## Skills

This repository includes:

- downloadable command-style skills for recurring workflows
- Codex skill folders for data science operating procedures
- agents and templates that support review, writing, and project setup

See `skills/README.md` for the current inventory and installation patterns.

## Repo Structure

```
codexbatman/
|- docs/               # Website source (MkDocs Material)
|- skills/             # Downloadable skills and Codex skill folders
|- agents/             # Downloadable agent files
|- templates/          # Starter templates (CLAUDE.md, goals.yaml)
|- mkdocs.yml          # Site configuration
|- CONTRIBUTING.md     # Maintenance guide
`- LICENSE             # MIT
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to edit content, add skills, and maintain the site.

## License

MIT - use anything here however you want.
