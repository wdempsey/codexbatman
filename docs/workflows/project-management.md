---
description: AI-powered project management for data science and research teams - living dashboards, weekly reviews, and proposal drafting from meeting transcripts, emails, and docs.
---

# Project Management

How I went from scattered information across five platforms to living project dashboards that write weekly reviews and draft proposals on demand. Built in four layers over several months - each one building on the last.

---

## The Mess

Anyone managing multiple research projects might recognize this.

Emails scattered across Gmail and institutional accounts. Documents in Google Docs, papers in Overleaf, sensitive data in university Box folders, field project files on partner servers, personal files in Dropbox. Zoom meetings rarely transcribed - and when they were, Zoom's transcriptions were poor. WhatsApp conversations across multiple groups. Overlapping projects with no central memory. No accountability system. No way to prepare for meetings without digging through five platforms. Years of discussions with no institutional record.

I'd walk into a meeting and spend the first ten minutes trying to remember what we decided last time. An RA would ask about a decision from three months ago and I'd have to search through hundreds of emails. Proposals would cite outdated figures because nobody remembered which version was current.

I know some teams use Slack to manage all of this. I tried it and it didn't fit my workflow, so I built the system below.

---

## Layer 0 (Optional): Clean Up Your Digital Life

Before organizing individual projects, you might want to clean house. If you have thousands of unread emails, files scattered across Dropbox, Google Drive, Box, and iCloud, a full hard drive, and calendars split across platforms - a one-time cleanup makes everything that follows easier.

This isn't required. You can skip straight to Layer 1 and organize projects on top of whatever mess currently exists. But if your digital infrastructure is chaotic, spending a day or two with Codex to get it under control pays dividends.

[:octicons-arrow-right-24: The One-Time Cleanup](../toolkit/executive-assistant.md#the-one-time-cleanup) - what I cleaned, how long it took, and prompts you can use yourself

[:octicons-download-16: Cloud Storage Organization Guide](../downloads/cloud-storage-guide.md) - detailed step-by-step walkthrough with scripts and decision frameworks

---

## Layer 1: Organize the Project Folder

**Skill:** [`/setup-project-management`](../setup/skill-reference.md#setup-project-management-project-setup)

The foundation. Before Codex can help manage a project, it needs a structured place to look.

**What this does:**

- Walks through an interactive discovery process for your project
- Pulls core materials from scattered locations into one project folder
- Creates a folder structure that Codex understands
- Sets up a Google Doc hub: first tab for the project overview and meeting history, additional tabs for core documents
- Creates a project-specific instruction file with team roster, keywords, and configuration

---

## Layer 2: Capture Everything

**Tool:** [Granola](../essentials/granola.md) (meeting transcription) + Codex

Once the project folder exists, the next step is to stop losing information. Meetings are where most decisions happen and most context gets lost.

---

## Layer 3: The Weekly Review

**Skill:** [`/weekly-review`](../setup/skill-reference.md#weekly-review-weekly-project-review) `[PM]`

This is where the system comes alive. The weekly review pulls from every source and produces two outputs: a high-level dashboard and a detailed weekly log.

---

## Layer 4: Proposals and Reports on Demand

**Skills:** [`/proposal-write`](../setup/skill-reference.md#proposal-write-proposal-drafting) and [`/proposal-revise`](../setup/skill-reference.md#proposal-revise-proposal-revision) `[PM]`

Because the project document hub contains research design, project history, prior proposals, and weekly updates, Codex can draft and revise deliverables from structured context.

---

## The Key Insights

### Each layer builds on the previous one

You don't need to build all four at once. Start with organizing your folders. Add transcription when you're ready. The weekly review only works because the folder structure exists. The proposal skills only work because the weekly review keeps everything current.

### Every skill took about three weeks of iteration

None of these worked perfectly on day one. Each one required back-and-forth with Codex - adapting it to specific projects, adjusting what the weekly review emphasized, tuning the proposal voice, and refining outputs for the team.

---

## Get the Skills

All skills referenced above are available for download:

| Skill | What it does | Install |
|-------|-------------|---------|
| `/setup-project-management` | Interactive project folder setup | [Details](../setup/skill-reference.md#setup-project-management-project-setup) |
| `/weekly-review` | Multi-source weekly synthesis | [Details](../setup/skill-reference.md#weekly-review-weekly-project-review) |
| `/proposal-write` | Draft proposals from project context | [Details](../setup/skill-reference.md#proposal-write-proposal-drafting) |
| `/proposal-revise` | Apply feedback to drafts | [Details](../setup/skill-reference.md#proposal-revise-proposal-revision) |
| Writing Reviewer | Academic prose QA (agent) | [Details](../setup/skill-reference.md#review-writing) |
| Methodology Reviewer | Empirical methods QA (agent) | [Details](../setup/skill-reference.md#review-methodology) |
