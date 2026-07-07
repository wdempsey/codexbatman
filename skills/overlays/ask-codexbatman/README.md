# ask-codexbatman Attribution

`ask-codexbatman` is modeled on Matt Pocock's `/ask-matt` router pattern:

- Source: https://github.com/mattpocock/skills/tree/main/skills/engineering/ask-matt
- License: MIT License, Copyright (c) 2026 Matt Pocock

The borrowed idea is the router shape: a skill that does not do the work itself, but places the user's situation on the right flow and hands off to the skill that should act next.

This version is distinct because Codex Batman routes by role and data science workflow gates. It covers student identity loading, tutoring overlays, data science gate order, method handoffs, manager operations, and repository-maintenance skills. It does not import Matt's engineering idea-to-ship flow or its issue-tracker assumptions.
