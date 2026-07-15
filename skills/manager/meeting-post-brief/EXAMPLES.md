# Examples: Meeting Post-Brief

## Example 1

User request:

> Turn this project meeting transcript into decisions, actions, and updates for the Research Design and Progress doc.

Expected behavior:

- classify decisions separately from discussion
- extract owners, deadlines, blockers, and open questions
- draft updates for Research Design and Progress and the decision log
- hand off durable state changes to project-manager-agent or weekly-review

## Example 2

User request:

> Write the follow-up email from today's meeting and send it to the team.

Expected behavior:

- draft the follow-up email
- mark it as requiring human approval before sending
- do not send the email or perform outbound actions
- identify any commitments that need review before the user sends

## Example 3

User request:

> Summarize this confidential student performance meeting into the project folder.

Expected behavior:

- stop because the meeting is sensitive
- avoid shared project-memory updates
- ask whether the user wants a private note outside the project artifact system

## Example 4

User request:

> File the transcript, update the Google Doc, and schedule next week's reminder automatically.

Expected behavior:

- prepare the post-meeting summary and artifact update text
- route Google Doc writes, filing, and scheduled reminder behavior to the n8n integration layer or human operator
- preserve human approval for any outbound or scheduled action
