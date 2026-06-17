# For Data Science Managers

**This is for you if your job is coordinating analytical work — keeping projects moving, making blockers visible, and turning distributed effort into clear next actions.**

## Start Here

If you coordinate multiple analytical projects or a lab portfolio, begin with:

[**Lab Manager Agent**](../workflows/manager/lab-manager-agent.md)

Managers use the same operating system as researchers and students, but the focus is coordination rather than direct model execution. The shared workflow still matters — teams should only advance when required artifacts and gates are in place. Manager mode wraps that workflow with summaries, tracking, communication, and governance. Start with the manager workflow pages, then use this page to find which skills and overlays fit your role.

## What Changes In Manager Mode

In manager mode, Codex shifts from executing analysis to helping you track and communicate it. Instead of producing experiment logs and model outputs, it produces weekly reviews, waiting-on lists, and stakeholder updates. The workflow gates still apply — you're using them to verify your team is ready to advance, not to run the steps yourself.

## Recommended Sequence

1. [Lab Manager Agent](../workflows/manager/lab-manager-agent.md) — start here for the portfolio-level coordination model
2. [Research OS Template](../workflows/manager/research-os-template.md) — the durable files that support weekly review
3. [Examples](../examples/index.md) — see project and portfolio coordination in practice before changing your own process
4. [Project Management](../workflows/project-management.md) and [Managing Data Science](../workflows/managing-data-science/index.md)

## What Each Manager Page Is For

Start with [Lab Manager Agent](../workflows/manager/lab-manager-agent.md) — it's the portfolio-level operating model that explains how coordination actually works. [Research OS Template](../workflows/manager/research-os-template.md) gives you the actual files and folders that hold manager-facing state week to week. [Examples](../examples/index.md) shows concrete project and portfolio coordination before you change your own process. [Project Management](../workflows/project-management.md) is the build story for dashboards, weekly reviews, and proposal support, and [Managing Data Science](../workflows/managing-data-science/index.md) is where the day-to-day workflow lives.

## If You Only Need One Starting Point

Start with [Lab Manager Agent](../workflows/manager/lab-manager-agent.md).

That page explains the coordination model. Open the template page second if you want the actual artifact structure, or the examples third if you want to see the system in use before adapting it.

## Typical Manager Outputs

- weekly reviews
- waiting-on lists
- next-actions lists
- meeting prep notes
- stakeholder-facing updates

## Example Manager Artifact

This is the kind of artifact the manager path should leave behind during a weekly review:

```md
# weekly_review.md — 2026-06-17

## Status
- housing-price-model: in evaluation phase, on track
- grant-proposal-analysis: blocked on data access approval

## Waiting On
- data team: access credentials for Q2 dataset (due 2026-06-19)
- PI: sign-off on model card draft (due 2026-06-20)

## Next Actions
- schedule model card review with stakeholders
- follow up on data access blocker
- draft stakeholder update for end of sprint

## Decisions Made This Week
- fixed validation set chosen for model comparison (see experiment_log.md)
- grant project paused until data access resolves
```

The point is that a manager can open this file and immediately know what is moving, what is blocked, and what they need to do without re-reading the chat history.

## What A Project Dashboard Can Look Like

![Example project overview dashboard showing priorities, metrics, milestones, and owner tasks](../images/project-overview-dashboard-v1.png)

This kind of artifact is the practical target of the manager lane: a durable project or portfolio view that makes it obvious what moved, what is blocked, and what needs attention next.

See [Project Overview Example](../workflows/examples/project-overview-example.md) for the full example.

## Manager-Focused Skills

- `executive-summary`
- `project-tracker`
- `communication-workflows`
- `project-setup`
- `weekly-review`
- `inbox-triage`
- `stakeholder-update`

## Where To Go Next

- Use [Choose Your Role](../roles/index.md) if you want to compare this path with the student or researcher/data scientist paths.
- Use the [Skill Library](../setup/skill-reference.md) for the shared catalog of manager skills, overlays, and workflow skills.
- Use [Project Management](../workflows/project-management.md) when you want a build story for dashboards and reviews.
- Use [Managing Data Science](../workflows/managing-data-science/index.md) when you want the manager workflow organized around daily execution.
- Use [Lab Manager Agent](../workflows/manager/lab-manager-agent.md) when you want the portfolio-level coordination model first.
- Use [Backbone Protocol](../backbone/index.md) when you need to verify which project artifacts should exist before a team advances.
- Return to [Core Data Science Workflow](../workflows/data-science/index.md) when you need to verify whether a project is ready to move forward.
