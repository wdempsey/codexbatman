# Skills & Agents

Execution-layer skills and agents for this repository's Codex-native Data Science Operating System.

## What This Directory Does

This directory contains reusable workflow instructions and role overlays that Codex executes in-repo.

- Skills encode repeatable best practices.
- Agents provide specialized review or drafting behavior.
- The docs explain when to use each workflow.
- Codex routes by role, mode, then workflow skill.

Two formats currently coexist:

- command-style markdown skills
- folder-based Codex skills with `SKILL.md`

## Categories

- `data-science/` = canonical analytical workflow backbone.
- `manager/` = operational and coordination workflows.
- `overlays/` = role-aware delivery wrappers.

## Quick Install

### Repo-native (recommended)

Folder-based Codex skills are intended to stay in this repository and be executed in local context. In normal use, no extra install step is required beyond cloning the repo and opening it in Codex.

### Legacy command-style compatibility

Command-style markdown skills can still be copied into a user tool directory if you need compatibility with command-based setups.

Legacy Claude-compatible install example:

```bash
mkdir -p ~/.claude/commands
curl -o ~/.claude/commands/review-plan.md \
  https://raw.githubusercontent.com/wdempsey/codexbatman/main/skills/data-science/review-plan.md
```

## Recommended Usage

- Use repo-native skill folders for canonical workflows.
- Use overlays to adapt behavior by role.
- Treat command-style skills as transitional compatibility tools.

## Additional References

- Skill library docs: `docs/setup/skill-reference.md`
- System architecture docs: `docs/system/`
