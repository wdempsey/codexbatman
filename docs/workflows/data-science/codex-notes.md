# Codex Notes: Workflow for Managing Data Science

## Primary Instruction

Create this as its own tab in the site called:

**Workflow for Managing Data Science**

This should be treated as a distinct top-level workflow page for managers, not as a subsection of a generic assistant page.

---

## What This File Is For

This file tells Codex how to interpret and implement the workflow materials.

There are three distinct artifacts:

1. the public-facing workflow page
2. the PRD
3. these implementation notes

Do not collapse them into one document.

Each has a different purpose.

---

## The Most Important Distinction

Codex must keep **components** separate from **phases**.

### Components answer:

> What parts make up the system?

Examples:

- project registry
- Gmail layer
- Calendar layer
- Drive / Docs layer
- Slack layer
- Dropbox layer
- Obsidian layer
- task / waiting-for layer
- review layer

### Phases answer:

> In what order should a new user install and adopt the system?

Examples:

- prerequisites
- core Google setup
- project-centered organization
- Slack integration
- Dropbox integration
- Obsidian integration
- full review workflow

Do not merge these ideas.

Do not present architecture as though it were installation order.

Do not describe installation order as though it were the system definition.

---

## Site Intent

The public page should be digestible for a new person trying to replicate the workflow.

That means the site should explain:

- what the workflow is
- why it exists
- what problem it solves
- what components it contains
- what order to install things in
- examples of what each phase enables

This page should be clear enough for a manager to follow, not just for an engineer.

---

## Content Framing

This is not merely an executive assistant workflow.

It is a **workflow for managing data science**.

That means the framing should emphasize:

- project-centered management
- cross-project context
- follow-up tracking
- meeting prep
- weekly review
- communication synthesis
- strategic use of personal notes

Do not frame it as a simple inbox automation page.

Do not reduce it to prompting advice.

Do not make email the center of the workflow.

The center is **project memory**.

---

## Core Design Rule

Throughout implementation, keep this principle explicit:

> projects are primary; inbox, meetings, docs, Slack, and notes all feed project memory

This should be visible in:

- page introduction
- component descriptions
- phase descriptions
- examples
- implementation notes

---

## What the Public Page Should Contain

The public page should be readable and structured for replication.

Recommended section order:

### 1. Why this workflow exists

Explain the manager problem:

- too many projects
- fragmented context
- too much time spent reconstructing state
- weak follow-up reliability

### 2. Core idea

Explain that projects, not inbox folders, are the main unit of organization.

### 3. What the workflow does

Summarize daily brief, inbox triage, meeting prep, project tracking, communication support, and weekly review.

### 4. Components

Describe the major system parts in plain language.

### 5. How to adopt it

Introduce the phased setup path.

### 6. Final takeaway

Emphasize that the point is better managerial awareness, not just faster replies.

---

## What the PRD Should Contain

The PRD should remain more implementation-oriented.

It should include:

- goals
- users
- scope
- architecture
- required components
- data model
- requirements
- user journeys
- risks
- success criteria

Do not over-simplify the PRD.

It should help Codex understand the system deeply.

---

## How to Present Phases on the Website

The site should show phased installation clearly.

Each phase should include:

- what gets installed
- why this phase matters
- what the user can do after completing it
- a few example use cases

This matters because the site is not only describing the system.

It is also teaching people how to replicate it.

---

## Required Phase Structure

Use this general order unless there is a very strong reason not to:

### Phase 0: Prerequisites

Include:

- Google access and auth
- MCP or equivalent tool connectivity
- active project list cleanup
- key folders and channels identified
- Obsidian installed if used later

Important: if Google MCP or Google integration is part of the stack, it should be established before Gmail or Drive workflows are described as active.

### Phase 1: Core Google setup

Include:

- Gmail
- Calendar
- Drive
- Docs
- basic project registry
- daily brief
- basic weekly review

### Phase 2: Project-centered organization

Include:

- project hub docs
- email-to-project assignment
- waiting-for extraction
- project summaries

This is the phase where the workflow becomes a true manager workflow rather than an inbox helper.

### Phase 3: Slack integration

Include:

- selected channels
- thread summaries
- blocker detection
- Slack-informed meeting prep

### Phase 4: Dropbox integration

Include:

- file indexing
- change awareness
- project linkage

### Phase 5: Obsidian integration

Include:

- private notes
- project-linked notes
- meeting prep with private context
- clear private/shared boundary

### Phase 6: Full review workflow

Include:

- cross-source synthesis
- stronger reviews
- better dashboards
- provenance and confidence signaling

---

## Examples Matter

Each phase should have example use cases.

Examples are especially important because this page is meant to be replicable by a new manager.

Use examples like:

- "Summarize important email related to Project Atlas"
- "Prepare me for today’s meetings"
- "What am I waiting on across active projects?"
- "Summarize Slack blockers for the hiring initiative"
- "Use my private notes plus project email to prep me for tomorrow’s meeting"
- "Generate my weekly review across active projects"

Examples should be concrete, short, and tied to actual managerial behavior.

---

## Guidance on Prerequisites

Because this page is partly instructional, Codex should make prerequisites visible rather than hiding them.

Especially call out setup dependencies when relevant, such as:

- Google auth or Google integration
- MCP-compatible tool setup
- Slack access
- Dropbox access
- Obsidian folder selection
- project naming cleanup

Do not assume a new user already understands the required setup sequence.

---

## Guidance on Privacy and Note Boundaries

Codex should preserve a strong distinction between:

- shared operational memory
- private personal memory

Use language like:

- Google Docs / project hubs = shared memory
- Obsidian = private memory

Make it clear that private notes may inform prep and synthesis, but should not automatically become shared artifacts.

This is an important trust property of the workflow.

---

## Guidance on Tone

Tone should be:

- academic but practical
- structured
- clear
- manager-facing
- serious but readable

Avoid:

- hype language
- startup-marketing language
- vague “AI assistant” phrasing
- overly casual onboarding language

The page should feel like a real operating workflow for thoughtful managers.

---

## Implementation Constraints

Codex should preserve these distinctions:

- workflow page = readable overview
- PRD = deeper implementation spec
- codex notes = build and presentation guidance

Codex should not:

- merge all three into one page
- make the page purely technical
- make the page purely promotional
- center the whole workflow on email
- omit phased setup
- omit examples
- omit prerequisites

---

## Final Instruction

Build and present this as a project-centered operating workflow under the site tab:

**Workflow for Managing Data Science**

The page should help a new manager understand the workflow.

The PRD should help implement it.

These notes should help Codex keep the structure clean and intentional.
