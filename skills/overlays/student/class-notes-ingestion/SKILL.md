---
name: class-notes-ingestion
description: Ingest uploaded class notes into persistent student course-context files. Use when a student wants future tutoring to follow their professor's notation, course vocabulary, covered methods, assignment constraints, or note-specific quirks; write only `memory/students/{name}/NOTATION.md` and `memory/students/{name}/COURSE-CONTEXT.md` after student confirmation. Do not use for one-off pre-answer alignment, ordinary tutor-mode help, or misconception repair.
category: overlays
status: active
stage: overlay
role_compatibility:
  - student
default_interaction: socratic
interaction_skill: socratic-tutor
runs_after:
  - identity-loader
  - grill-the-student
recommended_next:
  - grill-the-student
  - tutor-mode
inputs:
  - uploaded class notes
  - student identity folder
  - course or assignment context
outputs:
  - notation registry
  - course context summary
artifacts:
  - memory/students/{name}/NOTATION.md
  - memory/students/{name}/COURSE-CONTEXT.md
human_review_required: false
---

# Class Notes Ingestion

Persist the parts of a student's class notes that future tutoring must respect.

This is not `grill-the-student`. `grill-the-student` extracts enough context for the next answer and stores nothing. This skill turns uploaded notes into durable `NOTATION.md` and `COURSE-CONTEXT.md` files so later tutoring can mirror the professor's notation, vocabulary, coverage boundary, and known note issues.

## Use When

Use this skill when:

- a student uploads lecture notes, slides, annotated screenshots, OCR output, or course handouts
- the student wants future tutoring to use the professor's notation instead of a textbook default
- course coverage or assignment constraints need to persist across sessions
- the notes contain messy OCR, ambiguous symbols, inconsistent naming, or possible errors
- future `tutor-mode` answers would be risky without course-specific context

## Inputs

- identity-loader context and confirmed student name
- uploaded notes or pasted note excerpts
- existing `memory/students/{name}/NOTATION.md`, if present
- existing `memory/students/{name}/COURSE-CONTEXT.md`, if present
- assignment prompt or course title, if available

## Outputs

Write only after student confirmation:

- `memory/students/{name}/NOTATION.md`
- `memory/students/{name}/COURSE-CONTEXT.md`

## Stop Conditions

Stop and ask before continuing when:

- identity has not been resolved by `identity-loader`
- the student has not confirmed that the notes are theirs to use for persistent tutoring context
- the uploaded notes are too messy to distinguish notation from OCR noise
- a note statement appears mathematically or statistically wrong
- the update would touch any named student folder other than the confirmed student's folder
- the student asks for help with the material now rather than persistent ingestion; route to `grill-the-student` or `tutor-mode`

## Procedure

Ask one question at a time when clarification is needed.

1. Confirm scope.
   - Confirm the student identity folder.
   - Name the source notes being ingested.
   - Ask whether the student wants durable course context written for future sessions.

2. Read existing context.
   - Read existing `NOTATION.md` and `COURSE-CONTEXT.md` if they exist.
   - Preserve prior confirmed entries unless the student explicitly corrects them.

3. Extract notation.
   - Capture symbols, terms, variable names, subscripts, superscripts, estimators, and abbreviations.
   - Record the professor's notation first.
   - Add a "standard equivalent" only when it is useful and clearly supported.
   - Include a short source pointer such as lecture title, slide/page number, or pasted excerpt label when available.

4. Extract course context.
   - Record course, unit, covered methods, not-yet-covered methods, allowed tools, off-limits shortcuts, and assignment constraints.
   - Separate what the notes say from what Codex infers.
   - Keep the summary compact enough to load at session start.

5. Handle messy notes.
   - Mark unclear OCR as `[unclear]` rather than normalizing it silently.
   - Preserve idiosyncratic notation if the professor uses it consistently.
   - If the notes appear inconsistent or wrong, create a `Possible issues in notes` entry with evidence and ask the student before treating it as an error.

6. Draft the update.
   - Show the student the proposed `NOTATION.md` and `COURSE-CONTEXT.md` changes.
   - Ask: "Should I write these context files for future tutoring sessions?"
   - Do not write until the student confirms.

7. Handoff.
   - Tell the student future tutoring will use the confirmed professor notation and coverage boundary.
   - If the student wants help with the material, route to `grill-the-student` when the immediate confusion boundary is unclear; otherwise route to `tutor-mode`.

## Output Templates

Use the repository templates in `memory/students/_template/` when creating a new student folder. Keep named student copies concise.

### `NOTATION.md`

```markdown
# NOTATION.md

## Course Notation

| Symbol or term | Professor/course meaning | Standard equivalent | Source | Notes |
| --- | --- | --- | --- | --- |
| `{symbol}` | `{meaning in course language}` | `{optional standard name}` | `{lecture/page}` | `{uncertainty or usage note}` |

## Translation Preferences

- Use `{professor notation}` when explaining `{topic}`.
- Avoid `{textbook notation}` unless the student asks for translation.

## Unclear Or Conflicting Notation

- `{symbol}`: `[unclear] {what was visible}` from `{source}`. Ask before relying on it.
```

### `COURSE-CONTEXT.md`

```markdown
# COURSE-CONTEXT.md

## Course Snapshot

- Course:
- Instructor or source:
- Current unit:
- Last updated:

## Covered So Far

- `{method or concept}`: `{course wording and scope}`

## Not Yet Covered Or Off Limits

- `{method or concept}`: `{why to avoid or pause before using}`

## Assignment Constraints

- `{constraint}`

## Possible Issues In Notes

- `{source}`: `{suspected issue}`. Evidence: `{short evidence}`. Status: `unconfirmed`.
```

## Guardrails

- Do not silently correct the professor's notation.
- Do not silently correct the notes. Flag possible errors and ask.
- Do not answer the substantive homework question during ingestion.
- Do not create extra files beyond `NOTATION.md` and `COURSE-CONTEXT.md` unless the student explicitly asks.
- Do not edit `mastery.json`, `session-log.md`, or `flagged-skills.md`; those belong to `session-wrap`.
- Do not write to `memory/students/` without explicit student confirmation.
