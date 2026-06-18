# Student Tutor Overlays

This directory contains tutoring overlays for student-facing work.

- These overlays wrap existing skills rather than replacing them.
- The purpose is scaffolded learning: hints, guided decomposition, misconception diagnosis, and practice generation.
- Default behavior is to avoid directly executing the full solution for the student.
- All student overlays use `socratic-tutor` as the default interaction style — see `socratic-tutor/SKILL.md`.

## Session lifecycle

Student sessions follow a consistent lifecycle:

1. **Identity resolution** (`identity-loader`) — runs before anything else. Loads the student's profile and mastery, surfaces a context header, calibrates session depth. Offers registration if the student is new.
2. **Workflow + interaction** (`tutor-mode` + `socratic-tutor`) — the session itself. Workflow skill decomposes the task; socratic-tutor governs the question pattern.
3. **Session wrap** (`session-wrap`) — triggered by `/wrap`. Writes the session summary and confirmed mastery updates to `memory/students/{name}/`.

## Default interaction style

`socratic-tutor` is the default for all student sessions. It governs the question pattern, session arc, and teaching quality self-check. The other overlays handle structural decomposition and escalation; socratic-tutor handles how each response is delivered.

## Available overlays

- `identity-loader` — **pre-session** — loads student profile and mastery; registers new students; surfaces context header
- `socratic-tutor` — **default interaction style** — three-layer Socratic system (turn-level question ladder, RHRS session arc, self-check)
- `tutor-mode` — structural decomposition of workflow skills into student-paced steps
- `hint-ladder` — progressive hint escalation when the student is stuck
- `exercise-generator` — targeted practice generation after understanding is demonstrated
- `misconception-diagnosis` — conceptual error diagnosis when hints have not worked
- `session-wrap` — **post-session** — triggered by `/wrap`; writes session summary and confirmed mastery updates; handles `/flag-skill`
