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
- When routing among folder-based skills, prefer skill metadata front matter fields before falling back to prose.

Scope for Codex collaborators:
- Make focused, reversible changes that improve correctness, clarity, and maintainability.
- Preserve existing information architecture and editorial voice.
- Prefer additive updates over rewrites.
- Work in a single PR per task unless explicitly instructed otherwise.

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

