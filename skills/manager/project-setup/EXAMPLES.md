# Examples: Project Setup

## Example 1

User request:

> Set up a project management layer for this RCT workspace so we can start running weekly reviews.

Expected behavior:

- inspect the current workspace
- identify missing project artifacts
- draft a project-specific config with team roster, source keywords, source map, and decision-log rules
- define or create the living Research Design and Progress document as the weekly-review anchor
- propose a minimal operating layer
- implement only after approval

## Example 2

User request:

> We have docs in Google Drive, meetings in Granola, and a messy local folder. Create the project structure Codex should use.

Expected behavior:

- preserve the existing folder logic where possible
- define transcript and review locations
- record project aliases and keywords for finding relevant source material
- identify the authoritative place where decisions and research-design changes will be recorded
- create a project instruction file or equivalent anchor
- document external system dependencies

## Example 3

User request:

> Before changing anything, audit this project and tell me what setup is still missing.

Expected behavior:

- perform assessment only
- do not create files
- return a gap analysis and next-step plan
- flag missing team roster, keyword map, decision log, or Research Design and Progress document as setup blockers

## Example 4

User request:

> We decided in chat to change the primary outcome and move the midline pilot by two weeks. Make sure the project is up to date.

Expected behavior:

- route to project setup or project-manager maintenance depending on whether the operating layer already exists
- update the Research Design and Progress document or decision log, not just the chat summary
- capture the date, source, owner, rationale, impact, and open follow-up for each decision
- flag any downstream workflow artifacts that may need human review

## Example 5

User request:

> Set up the project folder and then start modeling the baseline outcome.

Expected behavior:

- set up only the manager operating layer
- stop before modeling if problem framing, data audit, EDA plan, and experiment-log conventions are missing
- recommend the relevant data-science workflow gates before analysis proceeds
