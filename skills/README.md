# Skills & Agents

## What This Directory Does

This directory contains the execution-layer workflows for this repository's Codex-native data science operating system.

Skills encode repeatable best practices. Overlays adapt those workflows by role and delivery style. Codex routes requests in the repository by role, then mode, then workflow skill.

## Skill Formats

Two skill formats currently coexist in this repository:

- command-style markdown skills
- folder-based Codex skills with `SKILL.md`

Folder-based skills are now the canonical format for this repo. They are the primary way the workflow backbone, manager workflows, and role overlays are expressed.

Command-style markdown skills remain only for compatibility and transition. They are not the primary authoring target for new repository-native workflow logic.

## Categories

- `data-science/` = canonical analytical workflow backbone
- `manager/` = project management, communication, and coordination workflows
- `overlays/` = role-aware wrappers for delivery style

## Recommended Usage

Normal use is repo-native.

Users clone the repository and open it in Codex. Folder-based skills are intended to be read and executed in local repository context, where adjacent docs, workflow pages, and project state are available.

Overlays modify delivery style without replacing canonical workflow logic. The shared workflow backbone remains the source of truth for analytical sequencing, gates, and artifacts.

## Legacy Compatibility

Legacy command-style usage remains optional.

If you need compatibility with a command-based setup, you can still copy a markdown skill into a user command directory. This is a secondary path, not the default operating model.

Example:

```bash
mkdir -p ~/.claude/commands
curl -o ~/.claude/commands/review-plan.md \
  https://raw.githubusercontent.com/wdempsey/codexbatman/main/skills/data-science/review-plan.md
```

## Additional References

- [Skill Library](../docs/setup/skill-reference.md)
- [System documentation](../docs/system/index.md)
