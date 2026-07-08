---
name: identity-loader
description: Session-start identity resolution for student sessions. Runs before any
  workflow skill. Loads the student's profile, mastery, and optional class-note context
  from memory/students/{name}/, surfaces a one-line context header, and calibrates
  session depth to their current mastery levels and course context. If no subfolder
  exists, offers to register the student on the spot.
  Activate at the start of every student session — before role overlays and before
  workflow routing.
category: overlays
status: active
stage: overlay
role_compatibility:
  - student
default_interaction: socratic
runs_before:
  - tutor-mode
  - problem-framing
  - data-audit
  - modeling
  - model-evaluation
  - experiment-log
---

# Identity Loader

Run this at the start of every student session, before any workflow skill or overlay engages.

---

## Step 1: Resolve the student's name

If the student's name is already in context (e.g., from the session opener), use it.
Otherwise ask: "What's your name? I'll check if you have a session folder set up."

---

## Step 2: Find the memory subfolder

Look for `memory/students/{name}/` in the repository.

**If the subfolder exists:**

1. Read `profile.md` and `mastery.json`
2. Read optional `NOTATION.md` and `COURSE-CONTEXT.md` if present
3. Extract:
   - Last session date and topic (from `profile.md` → Last session line, or from the most recent entry in `session-log.md`)
   - Any open questions from `mastery.json` → `open_questions` array
   - Mastery levels for topics likely to come up this session
   - Professor/course notation and coverage boundaries that should shape tutoring
4. Surface a context header (see format below)
5. Proceed to session

**If the subfolder does not exist:**

Offer to register:

> "I don't have a record for you yet. Want me to set one up? It takes 30 seconds — I'll copy the template and we can fill in your profile together. Once it's there, I'll remember your progress across sessions."

If the student says yes: walk them through `profile.md` field by field (name, role, background, learning goals, style preference, source materials). The student provides values; write them into `memory/students/{name}/profile.md`. Copy `mastery.json` template as-is.

If the student says no: proceed without an identity file. Note internally that this is an unregistered session — do not offer registration again mid-session.

---

## Context header format

Surface this at the top of the first response, before engaging with the task:

```
Welcome back, {name}. Last session: {topic}, {date}.
{If open questions: "Open question carried forward: {first open question}."}
{If relevant mastery: "{topic}: {level} — {one calibration note}."}
{If course context exists: "Course context loaded: {course/unit or notation summary}."}
```

Examples:

> Welcome back, Will. Last session: cox proportional hazards, 2026-06-18.
> Open question carried forward: Does Breslow break down with many ties?
> cox_proportional_hazards: mastered — I'll push you toward the harder edge cases today.

> Welcome back, Priya. Last session: logistic regression, 2026-06-10.
> regularization_lasso_ridge: unknown — if ridge or lasso comes up, I'll pause to introduce it first.
> Course context loaded: use your professor's `lambda` notation and avoid cross-validation unless you ask for translation.

For a new session (no prior record):

> Hi {name}! No session history yet — let's start fresh. Tell me what you're working on.

---

## Step 3: Calibrate session depth

After loading mastery, set an internal calibration note that governs this session:

- Topics at `mastered`: push toward edge cases, counterexamples, and connections to other topics.
- Topics at `practiced`: ask for re-explanation before giving hints; use Feynman check prompts.
- Topics at `introduced`: scaffold carefully; give conceptual grounding before jumping to application.
- Topics at `unknown`: introduce before assuming familiarity; do not ask "what does X do?" without setup.

This calibration governs the socratic-tutor overlay's question depth for this session.

If `NOTATION.md` or `COURSE-CONTEXT.md` exists, add an internal tutoring note:

- mirror the professor's notation before using standard textbook notation
- respect the covered/not-yet-covered boundary before proposing methods
- flag possible issues in notes rather than silently correcting them
- ask before updating either course-context file

---

## Step 4: Check for open questions

If `mastery.json` → `open_questions` is non-empty, surface the most recent one:

> "Last time we left an open question: {question}. Want to pick up there, or are you working on something new?"

Do not surface all open questions at once — one is enough to re-establish continuity. Leave the rest in reserve.

---

## Handoff

Once identity is resolved and the context header is surfaced, hand off to:
1. The workflow skill matching the student's current task
2. With `socratic-tutor` governing the interaction style
3. With `NOTATION.md` and `COURSE-CONTEXT.md` shaping examples, notation, and method boundaries when present

Do not re-run this step mid-session.
