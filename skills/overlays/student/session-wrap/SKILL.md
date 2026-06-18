---
name: session-wrap
description: End-of-session summary and memory update for student sessions. Triggered
  by /wrap. Generates a structured session summary, proposes mastery updates for the
  student to confirm, appends the confirmed summary to session-log.md, and updates
  mastery.json. Also handles /flag-skill — adds a structured entry to flagged-skills.md
  for skill-auditor review. Activate when the student says /wrap or /flag-skill, or
  when the session is clearly ending.
category: overlays
status: active
stage: overlay
role_compatibility:
  - student
default_interaction: socratic
writes_to:
  - memory/students/{name}/session-log.md
  - memory/students/{name}/mastery.json
  - memory/students/{name}/flagged-skills.md
  - memory/students/{name}/profile.md
---

# Session Wrap

Two triggers activate this skill: `/wrap` (end of session) and `/flag-skill` (single technique promotion during session).

---

## `/wrap` — End of session

### Step 1: Draft the session summary

Generate a summary in the standard session-log.md format:

```
## Session: {today's date}

**Duration:** {short | medium | long — estimate from session length}
**Topics covered:** {comma-separated list of topics actually discussed}
**Starting mastery context:** {relevant mastery levels at session start, pulled from mastery.json}

### What we worked on

{1-3 sentences on the arc of the session — what was attempted, what was resolved}

### Win

{One specific thing the student demonstrated understanding of. Prefer something
the student explained in their own words, not just answered correctly.}

### Misconception surfaced

{One thing the student believed that turned out to be incorrect, and the corrected
framing. If none surfaced: "none this session"}

### Open questions

{Questions raised but not resolved. These carry forward.}
- {question 1}
- {question 2}

### Mastery updates confirmed

{Leave blank until student confirms — see Step 2}

### Flagged for promotion

{Leave blank unless /flag-skill was used this session — see /flag-skill section}
```

Present the draft to the student: "Here's my summary of today's session — does this look right?"

---

### Step 2: Propose mastery updates

Based on the session, propose specific mastery level changes. Err conservative — do not promote to `mastered` without a Feynman check.

Feynman check prompt (use when considering `practiced → mastered`):

> "Before I mark {topic} as mastered — can you explain {topic} to me as if you were teaching it to a colleague who hasn't seen it? I'll listen and ask one or two follow-up questions."

If the student completes the Feynman check successfully: promote to `mastered` and log it in `mastery.json` → `feynman_checks_passed`.

Present proposed updates like this:

> "Based on today's session, here are the mastery updates I'd like to record. Confirm each one or correct it:"
>
> - cox_proportional_hazards: unknown → mastered (Feynman check passed ✓)
> - likelihood_and_estimation: introduced → practiced
> - log_rank_test: unknown — no change (we didn't cover this today)

Wait for explicit confirmation before writing. The student can decline any update, adjust a level, or add a topic.

---

### Step 3: Write confirmed outputs

Only after the student confirms:

1. **Append to `session-log.md`** — add the confirmed session entry with mastery updates filled in
2. **Update `mastery.json`** — apply confirmed mastery level changes; append to `open_questions`, `misconceptions_resolved`, and `feynman_checks_passed` arrays as appropriate
3. **Update `profile.md` → Last session line** — format: `YYYY-MM-DD | {primary topic} | {one-line summary}`

Tell the student what was written:

> "Session recorded. mastery.json updated. See you next time, Will."

---

### Step 4: Suggest a commit

If the student has a Git workflow, suggest:

> "When you're ready, commit your memory folder:
> `git add memory/students/{name}/ && git commit -m 'session: {date} — {primary topic}'`"

---

## `/flag-skill` — Flag a technique for promotion

Use this when the student says `/flag-skill` during or after a session.

### Step 1: Identify the technique

Ask: "What technique or framing do you want to flag? Describe it in a sentence — what is it, and when would you use it?"

If the student already described it in the session, confirm you're capturing the right thing.

### Step 2: Gather the required fields

Walk through the flag format fields with the student:

- **Context:** what problem were you working on when this came up?
- **Technique or framing:** the specific thing being flagged
- **Why it seemed generalizable:** why would another student at a similar stage find this useful?
- **Source:** session / textbook / student-invented / external

### Step 3: Write the entry to `flagged-skills.md`

Append a new entry in the required format:

```markdown
## [FLAGGED] {short title — 4-8 words}

**Session date:** {today's date}
**Student:** {name}
**Context:** {student's answer}
**Technique or framing:** {student's answer}
**Why it seemed generalizable:** {student's answer}
**Source:** {student's answer}
```

Confirm with the student before writing:

> "Here's the entry I'll add to your flagged-skills.md — does this capture it correctly?"

### Step 4: Explain what happens next

> "To get this reviewed, open a PR that includes your updated flagged-skills.md. The skill-auditor will run automatically and post a verdict comment — RECOMMEND, NOT READY, or NEEDS CLARIFICATION. If it recommends promotion, a maintainer can open a draft skill PR."

---

## Limits

- Never write to mastery.json without student confirmation.
- Never infer mastery from a single correct answer — `practiced` requires working through at least one exercise; `mastered` requires a Feynman check.
- Never promote a level more than one step in a single session without a Feynman check (unknown → practiced skips `introduced` — flag this and ask to confirm).
- Do not run `/wrap` automatically at session end — wait for the explicit command.
