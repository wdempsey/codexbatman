# improve-skill Rubric

| Criterion | Pass |
| --- | --- |
| Evidence first | Ties the proposal to telemetry, evals, user corrections, or deviation logs. |
| Small patch | Proposes the smallest useful skill change rather than a broad rewrite. |
| No in-place edit | Produces a proposal and diff text, but does not modify the target skill. |
| Eval hygiene | Uses improvement evals for diagnosis and preserves held-out evals for final checks. |
| Lifecycle safety | Routes student-flagged changes through the PR-2 gate and human review. |

Common failures:

- editing `SKILL.md` directly during the reflection pass
- using held-out evals as the source of the improvement idea
- mixing student memory updates with shared skill changes
- proposing a new skill before checking the matrix cell
- giving vague advice without a reviewable diff
