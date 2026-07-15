# Examples: Meeting Pre-Brief

## Example 1

User request:

> Prep me for tomorrow's Nairobi Digital Futures meeting using the project docs and latest weekly review.

Expected behavior:

- read project setup artifacts, Research Design and Progress, and weekly review
- summarize why the meeting matters
- surface open decisions, blockers, and owner-specific questions
- name what should be captured after the meeting

## Example 2

User request:

> Use this calendar digest and project folder to brief me before the cohort 2 randomization meeting.

Expected behavior:

- treat the calendar digest as an input, not something to fetch live
- tie agenda items to project state and upcoming deadlines
- identify decision prompts and artifacts likely to need updates

## Example 3

User request:

> Prep me for a performance discussion with the RA on this project.

Expected behavior:

- stop because the meeting may involve personnel-sensitive content
- ask whether the user wants a private, non-project-memory note
- do not pull the matter into shared project artifacts

## Example 4

User request:

> Automatically pull my calendar every morning and prep all meetings.

Expected behavior:

- explain that scheduled calendar pulls belong to the n8n integration layer
- offer the artifact-based pre-brief workflow for a provided meeting summary
- preserve human review for sensitive meeting classification
