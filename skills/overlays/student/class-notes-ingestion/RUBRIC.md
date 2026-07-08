# class-notes-ingestion Rubric

| Criterion | Pass |
| --- | --- |
| Identity boundary | Runs only after identity is resolved and writes only to the confirmed student's folder. |
| Artifact scope | Writes only `NOTATION.md` and `COURSE-CONTEXT.md` for persistent course context. |
| Confirmation | Shows the proposed update and waits for explicit student confirmation before writing. |
| Notation fidelity | Preserves the professor's notation first and treats standard notation as secondary. |
| Coverage boundary | Records covered, not-yet-covered, allowed, and off-limits methods separately. |
| Messy input handling | Marks OCR uncertainty and ambiguous symbols instead of cleaning them silently. |
| Error handling | Flags possible note errors with evidence and asks before correcting. |
| Handoff | Routes immediate help to `grill-the-student` or `tutor-mode` after ingestion. |

Common failures:

- treating uploaded notes as enough context to start solving a homework problem
- converting professor notation to a textbook default without preserving the course version
- writing memory files before confirmation
- creating extra per-student files beyond the two PR-5 artifacts
- editing real student folders during repository-maintenance PRs
