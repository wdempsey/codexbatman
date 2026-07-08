# misconception-diagnosis Rubric

| Criterion | Pass |
| --- | --- |
| Trigger boundary | Uses diagnosis only for repeated conceptual errors with visible reasoning. |
| Reasoning reproduction | Restates the student's reasoning before correcting it. |
| Broken step | Localizes the earliest invalid step, not just the final wrong answer. |
| Minimal counterexample | Gives a small contrast case that isolates the misconception. |
| Socratic repair | Asks the student to repair or re-explain one piece of reasoning. |
| Evidence record | Emits a `session-wrap` evidence record with mastery-compatible fields. |
| Memory boundary | Does not write `mastery.json` directly. |
| Notation fidelity | Uses `NOTATION.md` / `COURSE-CONTEXT.md` when present. |

Common failures:

- just says the student is wrong
- jumps directly to the correct answer
- diagnoses a misconception when the issue is only lack of effort or missing information
- skips the repair check
- marks a misconception as resolved before the student explains the repair
- invents new `mastery.json` topic keys during the diagnosis
