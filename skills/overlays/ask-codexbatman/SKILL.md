---
name: ask-codexbatman
description: Route a Codex Batman request to the right role overlay, workflow skill, method skill, manager operation, or repository-maintenance skill. Use when the user is unsure where to start, a request crosses student/data-scientist/manager/repo-maintainer lanes, a skill choice is ambiguous, or a session needs a safe next flow without doing the work itself.
category: overlays
status: active
stage: overlay
role_compatibility:
  - student
  - data scientist
  - data science manager
source_attribution:
  - "Modeled on Matt Pocock's ask-matt router pattern; rewritten for Codex Batman's role-first data science operating system."
---

# Ask Codex Batman

Route only. Do not run the downstream workflow, edit project artifacts, or solve the user's substantive task unless the user confirms the route and asks you to proceed.

This skill is the map over the Codex Batman operating system: role first, then overlay, then workflow gate or maintenance skill.

## Use When

Use this skill when:

- the user does not know which Codex Batman skill or workflow should start
- the request could fit more than one role lane
- a student request might need identity loading, method teaching, or tutoring overlays before workflow execution
- a data scientist request might violate the problem-framing, data-audit, modeling, or experiment-log gates
- a manager request might be project operations, project tracking, or stakeholder communication
- a repository-maintenance request needs the skill intake, site voice, navigation, or UI/UX review layer

## Inputs

- the user's stated task or situation
- any known role context: student, data scientist, data science manager, or repository maintainer
- current workflow artifacts, if named
- the relevant skill inventory from `CAPABILITY-MATRIX.md`

## Output

Return a short route:

```text
Role/lane:
Start with:
Then:
Use overlays:
Stop or ask before:
Why this route:
```

Name one primary route. Add at most one nearby alternative when it prevents a likely misroute.

## Stop Conditions

Stop and ask before continuing when:

- the student identity is unknown and the session is student-facing; run `identity-loader` before any other student overlay
- the user asks for modeling, EDA, or method selection before problem framing and data audit are approved
- the request would write to `memory/students/` outside a student identity/session-wrap flow
- the request would delete, archive, or migrate skills without a signed-off keep/delete list
- the request needs deterministic enforcement rather than skill prose; route that finding to PR-2 or a hook-oriented change

## Routing Procedure

1. Classify the lane.
   - Student: the user is learning, asks for hints, references class context, or needs coaching.
   - Data scientist: the user wants direct analytical execution or artifact production.
   - Data science manager: the user wants coordination, status, risks, decisions, or stakeholder communication.
   - Repository maintainer: the user is changing this repo, the docs site, skills, metadata, or intake process.

2. Pick the role overlay.
   - Student: `identity-loader` first, then `tutor-mode` with `socratic-tutor`; add `hint-ladder`, `exercise-generator`, or `misconception-diagnosis` only when their trigger is explicit.
   - Data scientist: `execution-mode` and `artifact-enforcer` wrap canonical workflow skills.
   - Data science manager: manager overlays such as `project-tracker`, `executive-summary`, or `communication-workflows` wrap manager workflow skills.
   - Repository maintainer: use the matrix and style guides first; use site skills for docs/site work.

3. Pick the workflow or maintenance skill.
   - Core data science gate: `project-bootstrap`, `problem-framing`, `data-audit`, `eda-plan`, `modeling`, `model-evaluation`, `experiment-log`.
   - Method teaching: route to the method skill when the learner is unfamiliar with the method, then return to the workflow gate.
   - Manager operations: `project-setup`, `project-manager-agent`, `lab-manager-agent`, `weekly-review`, or `inbox-triage`.
   - Manager communication: `stakeholder-update`, `communication-workflows`, or `executive-summary`.
   - Site and skill maintenance: `site-voice`, `ui-ux-review`, `navigation-review`, `visual-polish-pass`, `SKILL-STYLE.md`, and `CAPABILITY-MATRIX.md`.

4. Check gates and handoffs.
   - No EDA or modeling before problem framing approval.
   - No modeling before data audit yields `PROCEED` or `PROCEED WITH CONDITIONS` with conditions satisfied.
   - Every modeling run needs an experiment log entry.
   - Final or shared models need a model card.
   - Repository-maintenance changes should be small, reversible, and tracked in `planning.md`.

5. Answer with the route and wait.
   - Keep the response short.
   - Explain the route in one or two sentences.
   - If a downstream skill should execute next, name it and the artifact it should inspect first.

## Nearby Routes

- If the user asks "teach me" but already has approved workflow artifacts, route through student overlays first and then the same canonical workflow gate a data scientist would use.
- If the user asks "review this project" as a manager, start with `project-tracker` or `weekly-review`; do not route to `model-evaluation` unless the task is technical model review.
- If the user asks for a site copy pass, use `site-voice`; if they ask whether the page works structurally, use `ui-ux-review`; if they ask whether users can find it, use `navigation-review`.
- If the user asks to add a new skill, use `SKILL-STYLE.md` and `CAPABILITY-MATRIX.md` before drafting the skill.
