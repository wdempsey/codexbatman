# ask-codexbatman Rubric

Score each route on four criteria.

| Criterion | Pass |
| --- | --- |
| Role fit | Names the correct primary lane and does not confuse product roles with repository-maintenance work. |
| Gate safety | Preserves data science stop conditions, especially problem framing, data audit, modeling, and experiment logging. |
| Overlay fit | Uses overlays as wrappers, not replacements for canonical workflow logic. |
| Brevity | Gives one primary route, one optional alternative at most, and does not execute the downstream task. |

Common failures:

- routing student sessions directly to workflow skills without `identity-loader`
- treating manager summaries as technical model evaluation
- treating site-maintenance work as a data scientist workflow
- giving a long skill catalog instead of a route
- doing the work instead of handing off to the next skill
