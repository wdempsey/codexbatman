# Codex Batman Project Config

Read `AGENTS.md` as the source of truth for repository routing, scope, and safety rules.

Student-session startup is the only rule repeated here because this file is loaded as project config:

- If the session is student-facing, read `skills/overlays/student/identity-loader/SKILL.md` before role overlays or workflow skills.
- Resolve `memory/students/{name}/profile.md` and `memory/students/{name}/mastery.json` when a student identity is known.
- If no student subfolder exists, offer registration using `memory/students/_template/`.
- If the session is not student-facing, skip identity loading.

Skill promotion and student-memory guardrails are enforced by `scripts/hooks/codexbatman_lifecycle_gate.py` and `.github/workflows/skill-promotion-gate.yml`; do not rely on this file for that gate.
