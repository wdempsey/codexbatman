---
description: Boundary between n8n automation and Codex reasoning for manager workflows, meeting loops, and live project inputs.
---

# Integration Boundary and Meeting Loop

This page defines the boundary between automated integration work and Codex
reasoning for manager workflows.

Use it after [Project Management](../project-management.md), once
`project-setup` and `weekly-review` are already in place.

## Core Rule

n8n owns scheduled, audited, credentialed execution.

Codex skills own reasoning, synthesis, and drafting.

The boundary matters because project management workflows touch inboxes,
calendars, transcripts, and sometimes sensitive people decisions. Anything that
runs on a schedule, touches live accounts, needs credential handling, or needs
an execution history should live in the integration layer.

## n8n Responsibilities

n8n is the right layer for:

- scheduled triggers
- credentialed Gmail, calendar, or storage access
- repeatable filing into project folders
- execution logs and audit history
- retries, failure alerts, and idempotent runs
- human approval gates for outbound actions

Initial n8n flows should stay narrow:

1. Gmail trigger.
2. Classify messages against project config, roster, aliases, and source keywords.
3. File project-relevant material into the configured project folder or review inbox.
4. Produce a calendar digest for upcoming project meetings.
5. Hand the digest and filed sources to `meeting-pre-brief` or `weekly-review`.
6. Hold all outbound emails, calendar changes, or external updates behind human approval.

## Codex Skill Responsibilities

Codex skills are the right layer for:

- interpreting project artifacts
- preparing meeting briefs
- summarizing transcripts
- drafting follow-ups
- updating local project memory when explicitly asked
- identifying risks, blockers, decisions, and human-review needs

Codex should not be the layer that silently runs every morning, handles OAuth
credentials, mutates live inboxes, or sends messages without review.

## Meeting Loop

The meeting loop has four parts:

1. **Intake:** n8n or a human provides the meeting title, attendees, agenda,
   calendar digest, recent filed sources, and sensitive-meeting classification.
2. **Pre-brief:** `meeting-pre-brief` reads project artifacts and produces
   agenda context, decision prompts, owner-specific questions, and a capture
   plan.
3. **Post-meeting capture:** `meeting-post-brief` reads notes or transcripts and
   drafts decisions, actions, Research Design and Progress updates, and
   human-reviewed follow-ups.
4. **Weekly synthesis:** `weekly-review` consumes the project docs and meeting
   outputs into the overview and weekly history.

## Sensitive-Meeting Exclusions

Do not route the following meetings into shared project memory by default:

- personnel performance, hiring, firing, compensation, or health
- legal, disciplinary, or confidential institutional matters
- sensitive student feedback not intended for project artifacts
- private strategy that should not enter shared records

If classification is uncertain, stop for human review before running pre-brief,
post-brief, filing, or outbound follow-up workflows.

## Human-In-The-Loop Gates

Human approval is required before:

- sending email or stakeholder updates
- changing calendar events
- filing sensitive meeting material into shared folders
- changing project status in a way that creates external commitments
- recording personnel-sensitive content anywhere outside a private note

The system may draft, classify, and recommend. A human approves and acts.

## Boundary Checklist

Use n8n when the task:

- runs on a schedule
- touches live Gmail, calendar, storage, or transcript tools
- needs credential handling
- needs audit logs or retries
- sends, files, labels, archives, or changes live records

Use Codex skills when the task:

- reads already-provided project artifacts
- reasons about decisions, blockers, risks, or owners
- drafts a pre-brief, post-meeting summary, weekly review, or follow-up
- updates local files at the user's explicit request

## Related Skills

- [`project-setup`](../../setup/skill-reference.md#setup-project-management-project-setup)
- [`weekly-review`](../../setup/skill-reference.md#weekly-review-weekly-project-review)
- `meeting-pre-brief`
- `meeting-post-brief`
- `project-manager-agent`
- `stakeholder-update`
