# Workflow for Managing Data Science

## 1. Why This Workflow Exists

Managing data science is unusually context-heavy.

Most managers run multiple project streams at once, while context is fragmented across:

- email
- meetings
- shared docs
- Slack threads
- file systems
- personal notes

The result is predictable:

- too much time spent reconstructing project state
- follow-ups dropped because ownership is unclear
- poor meeting prep due to missing context
- weak weekly visibility across active workstreams

This workflow exists to reduce reconstruction cost and improve managerial awareness.

---

## 2. Core Idea

Most assistant workflows start from email.

This workflow starts from **projects**.

Core rule:

> projects are primary; inbox, meetings, docs, Slack, and notes all feed project memory

That means:

- email is interpreted through project context
- meetings update project state
- Slack movement is attached to projects
- shared docs act as operational memory
- personal notes support strategic thinking
- reviews are generated at project level, not inbox level

---

## 3. What the Workflow Does

A complete manager workflow should support six recurring jobs:

### Daily prioritization

Use today’s meetings, urgent email, major Slack movement, blockers, and waiting-for items to answer:

> What matters today?

### Inbox triage

Convert email into:

- project-linked context
- action items
- waiting-for items
- draft responses
- meeting prep inputs

### Meeting prep and follow-up

Before meetings: pull recent project updates, relevant communication, key docs, unresolved questions, and optional private notes.

After meetings: capture decisions, owners, next steps, open questions, and project implications.

### Project tracking

Maintain a reliable view of:

- current projects
- goals
- blockers and risks
- collaborators
- next steps
- recent movement

### Communication support

Draft and refine:

- email replies
- project updates
- meeting prep notes
- recap notes
- Slack updates

### Weekly review

Synthesize weekly movement by project and identify:

- progress
- stalled work
- escalation needs
- waiting-for dependencies
- next-week priorities

---

## 4. Components

Components define what the system is made of. They are not installation phases.

### Project registry

Defines active projects and maps aliases, owners, collaborators, status, goals, blockers, review cadence, and linked systems.

### Gmail layer

Supports triage, thread summarization, project assignment, action extraction, waiting-for extraction, and draft support.

### Calendar layer

Supports meeting-aware prioritization, meeting prep, and post-meeting follow-up capture.

### Drive / Docs layer

Shared operational memory for project hubs, status records, meeting notes, and canonical documents.

### Slack layer

Captures channel and thread movement, blocker signals, commitments, and project-relevant updates.

### Dropbox layer

Secondary source for project artifacts, archive files, and change awareness when teams rely on Dropbox.

### Obsidian layer

Private thinking layer for strategy notes, prep notes, and reflections.

### Task / waiting-for layer

Separates:

- manager actions
- waiting-for items owed by others
- FYI items
- blockers and risks

### Review layer

Produces daily briefs, project dashboards, meeting prep packets, follow-up lists, and weekly reviews.

---

## 5. How To Adopt It (Phased Setup)

Phases define installation/adoption order. They are not architecture.

### Phase 0: Prerequisites

What gets installed:

- Google access and authentication
- MCP-compatible connectivity (or equivalent)
- active project naming cleanup
- key folders/channels identified
- Obsidian installed (if used later)

Why this phase matters:

- prevents downstream setup failures
- makes project assignment more reliable

After completing this phase, you can:

- start Google-connected workflows without rework

Example use cases:

- "Prepare me for today’s meetings"
- "What are my active projects and aliases?"

### Phase 1: Core Google Setup

What gets installed:

- Gmail
- Calendar
- Drive
- Docs
- basic project registry
- daily brief
- basic weekly review

Why this phase matters:

- creates first usable project-centered workflow

After completing this phase, you can:

- triage inbox with project context
- produce a basic project-level daily and weekly view

Example use cases:

- "Summarize important email related to Project Atlas"
- "Prepare me for today’s meetings"

### Phase 2: Project-Centered Organization

What gets installed:

- project hub docs
- email-to-project assignment refinement
- waiting-for extraction
- project summaries

Why this phase matters:

- turns the workflow into a real manager operating system, not an inbox helper

After completing this phase, you can:

- track cross-project dependencies and follow-up reliability

Example use cases:

- "What am I waiting on across active projects?"
- "Summarize project movement since last review"

### Phase 3: Slack Integration

What gets installed:

- selected channels
- thread summaries
- blocker detection
- Slack-informed meeting prep

Why this phase matters:

- captures operational signals that never land in email

After completing this phase, you can:

- include team momentum and blockers in briefs and prep

Example use cases:

- "Summarize Slack blockers for the hiring initiative"
- "What changed in project channels this week?"

### Phase 4: Dropbox Integration

What gets installed:

- file indexing
- change awareness
- project linkage

Why this phase matters:

- prevents Dropbox artifacts from becoming invisible project context

After completing this phase, you can:

- include important file changes in project reviews

Example use cases:

- "Show Dropbox changes relevant to Project Atlas"
- "What documents changed before tomorrow’s review?"

### Phase 5: Obsidian Integration

What gets installed:

- private note access to designated paths
- project-linked note association
- private/shared boundary rules
- meeting prep with private context

Why this phase matters:

- adds strategic context while preserving trust boundaries

After completing this phase, you can:

- use private thinking to improve decisions and prep quality

Example use cases:

- "Use my private notes plus project email to prep me for tomorrow’s meeting"
- "Surface unresolved strategic questions from my notes"

### Phase 6: Full Review Workflow

What gets installed:

- cross-source synthesis
- stronger dashboards
- provenance and confidence signaling

Why this phase matters:

- produces mature managerial reviews across active projects

After completing this phase, you can:

- run high-confidence weekly project reviews with explicit uncertainty handling

Example use cases:

- "Generate my weekly review across active projects"
- "Which projects need escalation next week?"

---

## 6. Privacy and Memory Boundaries

Keep this boundary explicit:

- Google Docs and project hubs = shared operational memory
- Obsidian = private personal memory

Private notes may inform prep and synthesis, but must not automatically become shared artifacts.

---

## 7. Final Takeaway

This workflow is not designed to help a manager merely reply faster.

It is designed to help managers:

- preserve project memory
- manage complexity across workstreams
- reduce dropped follow-ups
- prepare for meetings with stronger context
- make better decisions with less reconstruction work

To implement the system in detail, use:

1. [PRD: Workflow for Managing Data Science](prd.md)
2. [Codex Notes: Workflow for Managing Data Science](codex-notes.md)
