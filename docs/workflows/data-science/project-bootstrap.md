# Project Bootstrap

Project bootstrap is the first operational step in the canonical data science workflow.

It exists to make the workspace legible before analytical work begins.

Without bootstrap, later skills fail for avoidable reasons:

- framing artifacts have no stable location
- audit results get mixed with scratch work
- raw and derived data boundaries stay implicit
- experiment logs appear late or not at all

Bootstrap is not analysis.
It is infrastructure for disciplined analysis.

## Why This Workflow Matters

Most workflow failures start before modeling.

The common pattern is familiar:

- project files are scattered
- data boundaries are unclear
- reproducibility expectations are informal
- no one knows where canonical artifacts should live

Project bootstrap fixes that early.

It gives Codex a stable operating surface and gives humans a stable review surface.

## Common Mistakes

- Creating a generic folder tree without inspecting the actual project.
- Mixing raw inputs, processed data, and final outputs in the same path.
- Treating bootstrap as permission to reorganize the repository broadly.
- Leaving framing, audit, and experiment artifacts unnamed or unstored.
- Starting data audit before the workspace has a defined artifact backbone.

## Step-by-Step Workflow

### 1. Inspect the current workspace

Read the project root first.

Identify:

- current folders
- existing analysis files
- any existing notes, logs, or config
- where raw data currently lives
- where derived outputs currently live

### 2. Define the minimum canonical backbone

The bootstrap phase should define, at minimum:

- a location for the framing artifact
- a location for the audit artifact
- a location for the experiment log
- a location for derived analytical outputs
- a documented raw vs processed boundary

### 3. Preserve existing conventions where possible

This repository prefers additive changes over rewrites.

If the project already has a working layout, Codex should map the canonical artifacts onto it rather than replacing it with a new naming system.

### 4. Record workspace assumptions

Codex should write down:

- what counts as raw data
- what counts as processed data
- where code should live
- where artifacts should be reviewed

### 5. Confirm readiness for problem framing

The bootstrap phase is complete only when the next skill can run against an explicit workspace structure.

## Expected Artifacts

- Bootstrap readiness summary
- Defined path for the problem framing artifact
- Defined path for the data audit artifact
- Defined path for the experiment log artifact
- Raw vs processed boundary note

## How Codex Should Use The Skill

Codex should use `skills/data-science/project-bootstrap/SKILL.md` as a setup protocol, not as a file-generation script.

That means:

- inspect first
- create only missing structure
- preserve existing project logic where possible
- avoid touching raw data
- stop before restructuring anything major without approval

This skill should usually be followed by [`problem-framing`](problem-framing.md).

## Run With Codex

```text
Use the project-bootstrap skill on this repository and tell me what artifact locations are missing.
```

```text
Run project-bootstrap for this workspace. Preserve the current folder layout and only add the canonical data science artifact backbone.
```

```text
Apply project-bootstrap in planning mode only. Do not create files yet. I want the bootstrap plan first.
```
