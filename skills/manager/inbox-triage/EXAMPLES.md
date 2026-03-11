# Examples: Inbox Triage

## Example 1

User request:

> Triage my inbox for Project Atlas and tell me what I need to act on before tomorrow’s meeting.

Expected behavior:

- filter to Project Atlas threads
- preserve thread context
- extract actions and meeting prep items
- suppress irrelevant inbox noise

## Example 2

User request:

> Turn the last three days of collaborator email into waiting-fors and owner-tagged next steps.

Expected behavior:

- group by thread
- identify owners and pending dependencies
- distinguish actual commitments from loose discussion

## Example 3

User request:

> I do not need replies drafted. Just summarize the important email movement for this project.

Expected behavior:

- focus on state changes and decisions
- omit drafting suggestions except where a response is blocked
