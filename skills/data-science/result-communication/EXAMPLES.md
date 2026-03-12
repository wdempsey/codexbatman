# Examples: Result Communication

## Example 1

User request:

> Draft a manager update from this evaluation report with risks and next actions.

Expected behavior:

- summarize decision-relevant findings
- include caveats and uncertainty
- provide clear recommendation and next-step actions

Expected artifacts:

- manager-facing update
- uncertainty/caveat section
- action list

## Example 2

User request:

> Convert these technical results into a one-page memo and a slide-ready summary.

Expected behavior:

- produce memo with evidence-linked claims
- produce concise slide bullets with caveats
- keep interpretation aligned across both formats

Expected artifacts:

- memo draft
- slide-ready summary
- recommendation note

## Example 3 (Bad Invocation)

User request:

> Make this sound definitive for leadership.

Expected Codex response:

- refuse certainty inflation
- require evidence-consistent language
- include explicit uncertainty and limits

Expected artifacts after correction:

- balanced executive update
- caveat and uncertainty section
- realistic next-step recommendation
