---
description: Lab Manager Agent workflow for coordinating projects, people, deadlines, handoffs, and weekly reviews across a research or data science portfolio.
---

# Lab Manager Agent

The Lab Manager Agent is the portfolio-level coordination layer above project-specific workflows.

It does not replace project-level analysis. It organizes many projects at once, keeps state visible, and turns fragmented updates into short actionable management outputs.

## Start Here If

Use this page when you need to coordinate many projects, students, deadlines, and handoffs at once rather than manage one analysis task in isolation.

This is the portfolio-level concept page for the manager lane. Read this first if you want to understand the coordination model before looking at templates, examples, or implementation stories.

## Hierarchy

```text
Lab Manager Agent
  -> Project Manager Agents
      -> Worker Agents
          -> Codex / Cursor / Claude in local folders
```

This hierarchy matters because the Lab Manager Agent should not do everything itself.

- The Lab Manager Agent coordinates the portfolio.
- Project Manager Agents maintain one project's state.
- Worker Agents execute scoped tasks inside a local project context.

## Purpose

Use the Lab Manager Agent when the management problem is no longer one project at a time.

Its job is to maintain visibility across:

- active students
- grants
- collaborations
- papers
- repositories
- deadlines
- handoffs
- waiting-on dependencies

## How This Extends The Manager Lane

The existing manager lane already supports:

- project setup
- weekly review
- stakeholder updates
- inbox triage

The Lab Manager Agent extends that layer upward.

Instead of managing one project workflow in isolation, it synthesizes many project states into a lab- or portfolio-level operating view.

## Core Responsibilities

The Lab Manager Agent should:

- track active students, grants, collaborations, papers, and code repositories
- identify who is waiting on whom
- surface stale or blocked projects
- prepare weekly lab briefs
- draft meeting agendas and follow-up emails
- track grant and paper deadlines
- route work to project manager agents
- keep Walter's next actions visible and prioritized

## Required Artifacts

At minimum, the Lab Manager Agent should read from durable artifacts rather than relying on memory alone.

Portfolio-level inputs often include:

- `ACTIVE_PROJECTS.md`
- `LAB_DASHBOARD.md`
- `PEOPLE.md`
- `DEADLINES.md`
- `WAITING_ON.md`
- project `PROJECT_STATE.md` files
- project `NEXT_ACTIONS.md` files
- recent `HANDOFF.md` files
- meeting notes
- email summaries

The exact file layout may vary, but the operating principle should remain artifact-first.

## Weekly Review Ritual

The weekly review is the core recurring ritual for the Lab Manager Agent.

### Inputs

```text
ACTIVE_PROJECTS.md
each project PROJECT_STATE.md
each project NEXT_ACTIONS.md
recent HANDOFF.md files
meeting notes
email summaries
deadline files
```

### Outputs

```text
WEEKLY_REVIEW.md
LAB_DASHBOARD.md
WALTER_NEXT_ACTIONS.md
WAITING_ON.md
```

### Weekly Brief Questions

The weekly brief should answer:

1. What needs Walter?
2. Who is waiting on Walter?
3. Who is Walter waiting on?
4. Which projects are stale?
5. Which deadlines are approaching?
6. Which student meetings need preparation?
7. Which emails should be drafted?
8. What are the recommended focus blocks this week?

## Communication Policy

The Lab Manager Agent may draft, summarize, classify, and recommend communications.

It should not send external communications autonomously unless explicitly authorized.

> Default rule: the agent may draft; Walter approves and sends.

This applies especially to:

- external emails
- grant communications
- collaborator updates
- student feedback with institutional consequences

## Operating Rules

- Projects remain the unit of durable state.
- Shared artifacts matter more than chat history.
- Portfolio summaries should point back to project artifacts.
- The agent should surface blockers and decisions, not bury them in prose.
- The agent should prefer short action-oriented outputs over long narratives.

## Stop Conditions

Stop and escalate when:

- required project artifacts are missing or stale enough that the summary would be misleading
- deadline or responsibility ownership is unclear
- the agent would need to infer scientific claims without project-level evidence
- communication risk is high and the message requires human judgment
- portfolio priorities conflict and require Walter to choose among them explicitly

## Relationship To Project Workflows

The Lab Manager Agent is not the substitute for:

- problem framing
- data audit
- model evaluation
- project-level handoffs

Those remain inside the backbone and project-specific workflows.

The Lab Manager Agent depends on those workflows being real and current.

## Recommended Outputs

Good Lab Manager outputs are short and operational:

- weekly brief
- stale-project list
- waiting-on list
- next-actions list
- meeting prep notes
- draft follow-up messages

## Example Artifact Shape

An artifact in this lane should look like a working management surface, not just a narrative summary.

![Example project overview dashboard showing project status, next actions, metrics, and risks](../../images/project-overview-dashboard-v1.png)

Use [Project Overview Example](../examples/project-overview-example.md) as a concrete reference for the kind of output this layer should support.

## Related Pages

- [For Data Science Managers](../../managers/index.md)
- [Project Management](../project-management.md)
- [Managing Data Science](../managing-data-science/index.md)
- [Research OS Template](research-os-template.md)
- [Integration Boundary and Meeting Loop](integration-boundary.md)
- [Examples](../../examples/index.md)
- [Backbone Protocol](../../backbone/index.md)
