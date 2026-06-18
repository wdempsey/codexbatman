# Flagged Skills

Techniques and framings that emerged during sessions and may deserve promotion into the shared skill library. Entries are added by the tutor when the student says `/flag-skill`. Each entry is evaluated by the skill-auditor agent when this file changes in a PR.

---

## Flag format

Each entry must follow this structure exactly. The skill-auditor will return a DEFER verdict for entries with missing fields and ask for the missing information.

```
## [FLAGGED] {short title — 4-8 words}

**Session date:** YYYY-MM-DD
**Student:** {name}
**Context:** {1-2 sentences on what problem was being worked on when this came up}
**Technique or framing:** {the thing being flagged — a question pattern, a way of
explaining a concept, a heuristic, a connection between ideas}
**Why it seemed generalizable:** {1-2 sentences on why this might help other students,
not just this one session}
**Source:** {session | textbook | student-invented | external}
```

---

## How the skill-auditor evaluates entries

When this file changes in a PR, the skill-auditor agent runs three checks:

1. **Not already covered** — is this already in `skills/`?
2. **Generalizable beyond this session** — would another student at a similar stage benefit?
3. **Has a clear trigger description** — is it specific enough to write a 1-2 sentence trigger from?

PASS on all three → RECOMMEND FOR PROMOTION.
FAIL on any → NOT READY (with a specific reason).
Unclear on any → NEEDS CLARIFICATION (with one targeted question).

See `agents/skill-auditor.md` for the full audit spec.

---

<!-- Flagged entries are appended below this line by the tutor at /flag-skill. -->
