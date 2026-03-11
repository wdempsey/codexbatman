# PRD: Workflow for Managing Data Science

## Product Name

**Workflow for Managing Data Science**

This should appear as its own tab in the site.

---

## Product Summary

A project-centered executive organizational assistant for managers leading data science, analytics, research, and technical work.

The system unifies:

- Gmail
- Google Calendar
- Google Drive / Docs
- Slack
- Dropbox
- Obsidian

into one workflow for:

- inbox triage
- meeting prep
- project tracking
- follow-up management
- private note integration
- weekly review

---

## Product Goal

The goal is to create a manager workflow where:

- communication is linked to projects
- shared documents act as operational memory
- personal notes support strategic thinking
- follow-ups are not dropped
- reviews are generated from project state rather than from scattered tools

The system should reduce context reconstruction and improve managerial awareness.

---

## Primary Users

Primary users:

- data science managers
- heads of data
- analytics managers
- research leads
- technical program leads
- founders managing technical teams

Secondary users:

- chiefs of staff
- project leads
- executive assistants supporting technical work
- collaborators consuming summaries and reviews

---

## Core Jobs To Be Done

The workflow should help users:

- understand what matters today
- triage email without losing project context
- prepare for meetings quickly
- capture project movement from meetings and Slack
- track follow-ups and waiting-for items
- maintain project awareness across multiple workstreams
- generate weekly project reviews

---

## Scope

### In Scope

- Gmail triage and thread summarization
- Calendar-based meeting prep
- Google Drive / Docs project hubs
- Slack ingestion and summarization
- Dropbox file awareness
- Obsidian private note integration
- project registry
- waiting-for extraction
- daily brief generation
- weekly review generation
- provenance-aware summaries
- human-supervised drafting

### Out of Scope for V1

- fully autonomous outbound communication
- enterprise-wide knowledge graph
- full CRM replacement
- automatic publication of private notes
- mobile-native application
- broad write-back automation across every system

---

## Product Principles

### 1. Projects Are Primary

The system organizes work around projects, not inbox folders.

### 2. Human-Supervised by Default

The system can draft and recommend, but important outbound communication should be reviewed.

### 3. Shared Memory and Private Memory Are Distinct

Google Docs and project hubs are shared operational memory.

Obsidian is private memory.

### 4. Every Source Should Reinforce Context

Email, calendar, docs, Slack, Dropbox, and notes should strengthen project memory rather than fragment it.

### 5. The System Should Be Adoptable in Phases

A new manager should be able to get value from an early version before full installation.

### 6. The Workflow Should Be Replicable

The website should explain the workflow clearly enough that another manager can reproduce it.

---

## Canonical Data Model

### Core Entities

- Project
- Person
- Email thread
- Slack thread
- Meeting
- Document
- Task
- Waiting-for item
- Note
- Decision
- Risk / blocker
- Objective / milestone

### Required Project Fields

Each project should have:

- `project_id`
- `title`
- `aliases`
- `status`
- `owner`
- `collaborators`
- `goals`
- `blockers`
- `next_steps`
- `next_review_date`
- `primary_drive_folder`
- `primary_project_hub_doc`
- `related_dropbox_paths`
- `related_slack_channels`
- `email_patterns`
- `related_note_paths`

---

## System Architecture

### Source Systems

- Gmail
- Google Calendar
- Google Drive
- Google Docs
- Slack
- Dropbox
- Obsidian

### Coordination Layer

- MCP-compatible orchestration
- Google integration layer
- Slack integration layer
- Dropbox integration layer
- Obsidian ingestion layer
- project registry
- source indexing
- summarization and extraction routines
- provenance and confidence tracking

### Output Surfaces

- daily brief
- project dashboard
- meeting prep packet
- follow-up list
- weekly review
- draft responses

---

## Component Requirements

### 1. Project Registry

The system must maintain a canonical project registry.

It must:

- define active projects
- map aliases and related keywords
- connect each project to its main folders, docs, channels, and notes
- support manual correction when mappings are wrong

### 2. Gmail Layer

The system must support:

- reading relevant email
- summarizing threads
- detecting likely project assignment
- extracting action items
- extracting waiting-for items
- distinguishing FYI from action-oriented communication
- drafting responses using project context

### 3. Calendar Layer

The system must support:

- reading calendar events
- associating meetings with projects
- generating meeting prep packets
- supporting post-meeting follow-up capture

### 4. Drive / Docs Layer

The system must support:

- project hub documents
- canonical shared project records
- linking recent documents into project context
- using shared docs as a stable operational memory layer

### 5. Slack Layer

The system must support:

- selected channel ingestion
- selected thread summarization
- mention monitoring
- extraction of blockers, commitments, and recent movement
- project-level attachment of relevant Slack activity

### 6. Dropbox Layer

The system must support:

- folder indexing
- file change awareness
- linking relevant Dropbox files to projects
- including major Dropbox changes in project review

Dropbox should be treated as a secondary source rather than the primary system of action.

### 7. Obsidian Layer

The system must support:

- designated vault or folder access
- classification of notes by project relevance
- linking notes to projects
- private use of note content during prep and synthesis
- explicit boundary rules between private notes and shared outputs

Nothing from private notes should be promoted to shared artifacts automatically.

### 8. Task and Waiting-for Layer

The system must distinguish:

- actions for the manager
- waiting-for items owed by others
- FYI items
- risks / blockers

This is a core requirement, not an optional enhancement.

### 9. Review Layer

The system must support:

- daily brief generation
- weekly review generation
- project-level summaries
- meeting prep synthesis
- source-aware outputs
- confidence signaling where assignment or summary quality is uncertain

---

## Functional Requirements

The workflow must:

- maintain a project-centered registry
- connect email, meetings, docs, Slack, Dropbox, and notes to projects
- generate daily and weekly managerial summaries
- preserve a private/shared memory distinction
- support human review before major external writes
- allow phased setup and adoption
- expose examples that a new user can replicate

---

## Non-Functional Requirements

The workflow should aim for:

- clear setup steps
- easy replication by a technically capable manager
- understandable site structure
- traceable source provenance
- graceful degradation when one connector is unavailable
- strong privacy defaults for personal notes
- minimal ambiguity about the current canonical project record

---

## Recommended Phased Rollout

### Phase 0: Prerequisites

- Google access and authentication
- Slack access
- Dropbox access if used
- Obsidian installation
- MCP-compatible integration layer
- basic project list cleanup

### Phase 1: Core Google Setup

- Gmail
- Calendar
- Drive
- Docs
- basic project registry
- daily brief
- basic weekly review

### Phase 2: Project-Centered Organization

- project hub docs
- email-to-project assignment
- waiting-for extraction
- project summaries
- review templates

### Phase 3: Slack Integration

- selected channels
- thread summaries
- blocker and commitment extraction
- Slack-informed prep and review

### Phase 4: Dropbox Integration

- file indexing
- change detection
- project linkage
- review inclusion

### Phase 5: Obsidian Integration

- private note linkage
- project note association
- private/shared boundary enforcement
- meeting prep with private context

### Phase 6: Full Review Workflow

- cross-source synthesis
- provenance and confidence layer
- mature dashboards and reviews

---

## Key User Journeys

### Journey 1: Daily Brief

The user asks:

> What matters today?

The system should combine:

- today's meetings
- urgent email
- important Slack movement
- waiting-for items
- project blockers

and return a concise managerial brief.

### Journey 2: Project Update from Communication

A new email or Slack thread arrives.

The system should:

- identify the likely project
- summarize the change
- classify the communication
- update the project context
- surface follow-up implications

### Journey 3: Meeting Prep

Before a meeting, the user asks for context.

The system should combine:

- recent email
- Slack movement
- relevant docs
- project status
- private notes if appropriate

and return a prep packet.

### Journey 4: Weekly Review

At the end of the week, the user asks for a weekly review.

The system should gather major signals across systems, organize them by project, and synthesize:

- progress
- stalled work
- risks
- blockers
- follow-ups
- next-week priorities

---

## Risks

The main product risks are:

- weak project/entity assignment
- duplicate document authority across systems
- over-automation of ambiguous communication
- leakage between private and shared memory
- connector reliability issues
- unclear ownership across projects

---

## Success Criteria

The workflow is succeeding if it helps the user:

- reduce context reconstruction time
- improve follow-up reliability
- strengthen project awareness
- prepare for meetings faster
- produce more useful weekly reviews
- manage multiple technical projects with less fragmentation

---

## Implementation Note for Site Structure

This PRD should support a public-facing page titled:

**Workflow for Managing Data Science**

That page should be readable for new users, while this PRD should remain the implementation-oriented definition behind it.
