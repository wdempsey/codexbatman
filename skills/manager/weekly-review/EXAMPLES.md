# Examples: Weekly Review

## Example 1

User request:

> Generate this week's project review from the project docs and Granola transcripts, then update the dashboard draft.

Expected behavior:

- read the project config and Research Design and Progress document first
- identify the review window from the weekly history baseline
- gather project docs and meeting transcripts for that window
- draft a three-page overview with strategic reminder, near-term imperatives, and per-person priorities
- append a weekly summary to the configured history tab or section
- update files only if the destination is configured and safe to edit

## Example 2

User request:

> I have transcripts and the project folder, but email and WhatsApp are unavailable. Do the weekly review anyway.

Expected behavior:

- proceed with file-and-transcript sources
- note email and WhatsApp as missing source coverage
- avoid implying full coverage
- include confidence notes for claims that depend on unavailable sources

## Example 3

User request:

> Give me a manager-ready review for the last two weeks, focused on strategic priorities, deadlines, and what each person should do next.

Expected behavior:

- use the user-provided two-week review window
- organize around objectives, deadlines, blockers, and owners
- keep the output decision-oriented rather than chronological
- include per-person priorities with dependencies and due dates

## Example 4

User request:

> The transcripts say we changed the primary outcome and delayed the midline pilot. Make the weekly review and update the project history.

Expected behavior:

- distinguish confirmed decisions from discussion
- include the change in the weekly history entry
- flag the Research Design and Progress document and decision log for update
- identify any workflow gates or human-review artifacts affected by the decision

## Example 5

User request:

> Run the weekly review, pull the latest Gmail and calendar events automatically, and file everything on a schedule.

Expected behavior:

- run only the file-and-transcript weekly-review portion if local sources are available
- stop before live Gmail, calendar, scheduled filing, or outbound actions
- route scheduled or credentialed integration needs to the PR-13 n8n integration layer
