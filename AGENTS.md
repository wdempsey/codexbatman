# AGENTS.md

## Mission And Scope

This repository exists to maintain and improve a Codex-native Data Science Operating System: the documentation site, downloadable skills, agents, templates, and workflow artifacts that support it.

The operating system serves three roles:
- student
- data scientist
- data science manager

Core architecture:
- Skills encode best practices.
- The website explains workflows.
- Codex executes workflows.

## Routing Order

Route requests in this order:

0. **Identity** *(student sessions only)*
   - Before role overlays engage, run `skills/overlays/student/identity-loader/SKILL.md`.
   - This loads `memory/students/{name}/profile.md` and `mastery.json`, surfaces a one-line context header, and calibrates session depth to the student's current mastery levels.
   - If no subfolder exists for the student, offer to register them on the spot (copy `memory/students/_template/` and walk through `profile.md`).
   - Identity resolution happens once per session — do not re-run mid-session.
   - If the session is not in student role, skip this step entirely.
1. **Role**
   - `student` -> apply overlays from `skills/overlays/student/`
   - `data scientist` -> apply overlays from `skills/overlays/practitioner/`
   - `data science manager` -> apply overlays from `skills/overlays/manager/`
2. **Mode**
   - Role overlays determine delivery style, not workflow logic.
   - Student mode is scaffolded, hint-first, and attempt-before-answer.
   - Practitioner mode is direct, artifact-enforcing, and execution-oriented.
   - Manager mode is summary-oriented, project-tracking, and communication-oriented.
3. **Workflow skill**
   - After role and mode are set, choose the shared workflow skill that matches the task.
   - Prefer canonical data science skills for the analytical backbone:
     - `project-bootstrap`
     - `problem-framing`
     - `data-audit`
     - `experiment-log`
   - Use manager workflow skills when the task is coordination or project operations.

Rule:
- Overlays wrap shared workflow skills. They do not replace canonical workflow logic.
- Canonical workflow logic must live in shared skills, and overlays must not duplicate that logic.
- When routing among folder-based skills, prefer skill metadata front matter fields before falling back to prose. Use `skills/METADATA.md` as the schema source of truth for those fields.
- When a workflow skill includes method-handoff metadata, prefer that metadata over ad hoc method suggestions.
- If the learner is a student and a proposed method is unfamiliar, route to the relevant method skill before continuing the workflow.

## Skill Promotion Pipeline

When a student discovers a technique or framing worth sharing, it travels through this pipeline before entering the shared skill library.

1. **Flag** — Student says `/flag-skill` during a session. The `session-wrap` overlay (`skills/overlays/student/session-wrap/SKILL.md`) collects the structured entry and appends it to `memory/students/{name}/flagged-skills.md`.

2. **PR** — Student opens a PR that includes their updated `flagged-skills.md`. This triggers the skill-auditor agent.

3. **Audit** — The skill-auditor (`agents/skill-auditor.md`) reads every new entry in the diff and evaluates each against three criteria: not already covered, generalizable beyond this session, has a clear trigger description. It posts a structured verdict comment: **RECOMMEND FOR PROMOTION / NOT READY / NEEDS CLARIFICATION**.

4. **Draft skill PR** — If the verdict is RECOMMEND, a maintainer opens a draft skill PR using the suggested title and trigger from the audit comment. The student may contribute the draft content.

5. **Human review** — A maintainer reviews the draft skill for fit with the existing skill architecture (metadata schema, overlay compatibility, editorial voice). Edits as needed.

6. **Merge** — On approval, the skill is merged into the appropriate `skills/` subfolder and added to `skills/METADATA.md`.

Rules:
- The skill-auditor produces verdicts only — it does not merge, create, or modify files.
- Maintainer approval is required before any student-flagged entry becomes a shared skill.
- Entries that fail the audit stay in `flagged-skills.md` — they are not deleted. The student can revise and re-submit.
- See `memory/students/README.md` → Skill promotion pipeline for the student-facing view of this process.
- The deterministic file-level gate lives in `scripts/hooks/codexbatman_lifecycle_gate.py` and `.github/workflows/skill-promotion-gate.yml`. It blocks PRs that mix student flagged-skill updates with shared skill changes, and blocks accidental deletions under `memory/students/`.

Scope for Codex collaborators:
- Make focused, reversible changes that improve correctness, clarity, and maintainability.
- Preserve existing information architecture and editorial voice.
- Prefer additive updates over rewrites.
- Work in a single PR per task unless explicitly instructed otherwise.
- Grow the methods skill library incrementally from trusted sources such as ISLP, ISLR-Python, and Hands-On Machine Learning (`handson-ml3`), and add new entries as repo-native teaching adapters rather than chapter-summary copies.
- When creating or updating method skills, treat ISLP, ISLR-Python, and Hands-On Machine Learning (`handson-ml3`) as preferred source materials and implementation-pattern references. Do not copy chapter structure directly; create concise repo-native teaching adapters that fit this system's workflow and overlay architecture.

Out of scope unless explicitly requested:
- Large-scale reorganizations of docs, nav, or folder structure that go beyond necessary identity alignment.
- Broad rewrites of established pages.
- Changes that alter project direction without maintainer approval.

## Decision Priorities

When tradeoffs appear, choose in this order:
1. Correctness and factual integrity.
2. User safety and risk reduction.
3. Navigation and link integrity.
4. Voice and style consistency.
5. Minimal, reversible diffs.
6. Speed.

## Working Style (Balanced, Leaning Strict)

Default mode:
- Be pragmatic and concise.
- Make progress autonomously on clear tasks.
- Keep diffs small and intentional.

Leaning strict means:
- Do not infer major intent beyond the request.
- Do not silently broaden scope.
- Do not "clean up" unrelated files.
- Flag assumptions when confidence is low.

Execution norms:
- Read relevant local context before edits.
- Prefer adding new files over rewriting existing ones.
- Keep naming explicit and predictable.
- Preserve backwards compatibility for links and docs references.
- Do not change existing workflows unless the task explicitly requires workflow changes.

## Planning File

- Use `/planning.md` at the repository root as the central running TODO list.
- When work adds follow-up tasks, append concise checklist items under the active section in `planning.md`.
- If priorities change, update `planning.md` in the same change set so plans remain current.

## Data Science Policy

### DS workflow gates

- No modeling or EDA before Problem Framing approval.
- No modeling before Data Audit yields `PROCEED`, or `PROCEED WITH CONDITIONS` with all conditions satisfied.
- Every modeling run requires an Experiment Log entry.
- Any final or shared model must have a Model Card.

### Explicit stop conditions

- If asked to train without these artifacts, stop and propose the missing steps.

### Reproducibility enforcement

- Use deterministic seeds.
- Use pinned environments.
- Do not edit raw data directly.

### Human-in-the-loop clause

- Agent may draft artifacts; human approves claims and conclusions.

## Stop Conditions

Stop and ask for direction if any of the following occurs:
- The requested change conflicts with existing architecture or published guidance.
- Required facts or source-of-truth inputs are missing.
- A change would require restructuring directories or rewriting major docs sections.
- Security/privacy implications are uncertain.
- Build/test verification cannot run in the current environment.

## Build Verification Rules

Use existing repository commands and workflows only.

Primary references in this repo:
- CI deploy workflow: `.github/workflows/deploy.yml`
- Dependencies: `requirements.txt`

Verification policy:
1. Run the least-destructive local verification first (`mkdocs build`) when available.
2. Do not run deploy commands (`mkdocs gh-deploy --force`) for routine verification.
3. If required tools are missing, report exact missing commands/packages and stop.
4. In summaries, list exactly what command ran and its result.

## Devlog + Distillation Protocol

Purpose:
- Preserve decision context across sessions.
- Convert one-off work into reusable operating knowledge.

Current status:
- `devlog/` infrastructure is planned but not yet active in this repository.
- Until `devlog/` is added, capture non-trivial change context in PR summaries and `planning.md` follow-up items.

Distillation standard:
- Prefer principles over narrative.
- Keep each learning atomic and testable.
- If a learning implies a process change, propose a minimal docs update in a future PR.
