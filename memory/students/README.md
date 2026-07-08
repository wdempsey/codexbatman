# Student Identity System

The `memory/students/` directory persists learner identity and progress across sessions. Each student gets one subfolder. The tutor reads it at session start to greet returning students and calibrate depth. The student owns this data — the tutor only suggests; it never writes without confirmation.

---

## Subfolder schema

```
memory/students/{name}/
├── profile.md          — who you are, your goals, your preferred explanation style
├── mastery.json        — topic-by-topic mastery levels, open questions, resolved misconceptions
├── NOTATION.md         — confirmed professor/course notation for future tutoring
├── COURSE-CONTEXT.md   — confirmed course coverage, constraints, and note issues
├── session-log.md      — append-only log of every session summary
└── flagged-skills.md   — techniques worth promoting to the shared skill library
```

---

## How to register

1. Copy `_template/` to `memory/students/{your-name}/`
2. Fill in `profile.md` — the commented prompts explain each field
3. Leave `mastery.json` as-is — the tutor populates it as you work

That's it. Start a session and the tutor will find you.

---

## How to start a returning session

The tutor reads `profile.md` and `mastery.json` at the start of every student session. It surfaces:
- Your last session topic and date
- Any open questions you left unresolved
- Your current mastery levels for the topic you're about to work on
- Any confirmed `NOTATION.md` / `COURSE-CONTEXT.md` details that should shape tutoring

If no subfolder exists for your name, the tutor will offer to register you on the spot.

---

## How to start fresh

Archive your subfolder (e.g., rename to `{name}-archived-2026-06/`) or delete it. The next session treats you as a new student.

---

## Multiple students, one repo

Each student has their own subfolder. There is no collision. Mastery files are student-scoped — not shared, not merged.

---

## What the tutor can and cannot do

**The tutor can:**
- Read `profile.md` and `mastery.json` at session start
- Read `NOTATION.md` and `COURSE-CONTEXT.md` at session start when present
- Suggest updates to `NOTATION.md` and `COURSE-CONTEXT.md` after you confirm class-note ingestion
- Suggest mastery level updates at the end of a session (via `/wrap`)
- Append a session summary to `session-log.md` after the student confirms
- Append confirmed misconception-diagnosis evidence records to `mastery.json` via `/wrap`
- Add a flagged technique to `flagged-skills.md` when the student says `/flag-skill`

**The tutor cannot:**
- Write to `mastery.json` without explicit student confirmation
- Silently rewrite your professor's notation or silently correct possible note errors
- Merge, delete, or restructure the student folder
- Promote a flagged skill to the shared library — that requires human review via the skill-auditor agent

---

## Skill promotion pipeline

When a technique deserves to become a shared skill:

1. Student says `/flag-skill` — tutor adds a structured entry to `flagged-skills.md`
2. Student opens a PR touching `flagged-skills.md` — the skill-auditor agent evaluates the entry
3. Auditor posts a verdict: RECOMMEND FOR PROMOTION / NOT READY / NEEDS CLARIFICATION
4. Maintainer decides whether to open a draft skill PR

Full pipeline: `AGENTS.md` → Skill Promotion section.
Full auditor spec: `agents/skill-auditor.md`.
