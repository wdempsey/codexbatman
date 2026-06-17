---
name: repo-bootstrap-student
description: Teach a student how to create a GitHub-backed data science repository with Codex, including basic structure, artifact locations, Git setup, and first commit.
category: data-science
status: active
stage: bootstrap
role_compatibility:
  - student
inputs:
  - project idea
  - repository name
  - local workspace path
  - preferred language or tool stack
outputs:
  - repo bootstrap plan
  - repository structure
  - first commit checklist
artifacts:
  - README.md
  - .gitignore
  - PROJECT_STATE.md
  - analysis/ scaffold
  - data/ scaffold
  - reports/ scaffold
  - memory/ scaffold
depends_on: []
recommended_next:
  - project-bootstrap
  - problem-framing
overlays:
  - tutor-mode
human_review_required: true
halts_if_missing:
  - project idea
  - repository name
---

# Skill: Repo Bootstrap For Students

## Purpose

Teach a student how to create a clean, GitHub-backed data science repository with Codex without skipping the reasoning behind the structure.

This skill is for the first repository setup step:

- create the repo
- create the basic project structure
- connect local work to Git and GitHub
- make the first meaningful commit
- prepare the repo for the repository's artifact-first workflow

It should teach the student what each piece is for instead of silently doing everything with no explanation.

## When To Use

Use this skill when:

- a student wants to start a new data science project repo
- a student needs help structuring a first GitHub repo
- a student has never connected local project work to GitHub before
- a project needs the minimum repository scaffolding before `project-bootstrap` and `problem-framing`

## Required Inputs

- project idea or working title
- repository name
- where the repo should live locally
- preferred language or notebook/tooling context if known

If the student does not know all of these yet, guide them to choose the smallest acceptable defaults.

## Teaching Contract

This skill should teach in student mode:

- explain why each major file or folder exists
- ask for short confirmations before major steps
- prefer one step at a time
- avoid assuming GitHub knowledge
- keep commands copy-pasteable

## Procedure

### Step 1: Confirm The Project Goal

Help the student state:

- what the project is about
- what the repo will contain
- whether this is analysis, learning, replication, or class work

If the scope is fuzzy, keep it small and say so explicitly.

### Step 2: Choose A Minimal Repository Structure

Create or propose the smallest structure that supports the repository workflow:

```text
repo-name/
  README.md
  .gitignore
  PROJECT_STATE.md
  analysis/
  data/
  reports/
  memory/
```

Explain:

- `README.md` -> what the project is
- `.gitignore` -> what should not be tracked
- `PROJECT_STATE.md` -> current project memory
- `analysis/` -> framing, plans, and analytical work
- `data/` -> data documentation and data-related notes
- `reports/` -> outputs to share
- `memory/` -> traces, handoffs, and session memory

### Step 3: Initialize Git Carefully

Teach the student how to:

- create the directory
- initialize Git
- inspect status
- understand tracked vs untracked files

Do not assume prior Git vocabulary without explanation.

### Step 4: Add Minimal Starter Files

Help the student create:

- `README.md`
- `.gitignore`
- `PROJECT_STATE.md`

Keep contents simple and readable.

If helpful, explain that this is the first version, not the final design.

### Step 5: Make The First Commit

Teach the student how to:

- review `git status`
- stage files
- write a meaningful first commit message

Explain what a commit is in plain language.

### Step 6: Connect To GitHub

If the student already has a GitHub repo, help connect the local repo to it.

If not, explain the next step clearly:

- create the repo on GitHub
- add the remote
- push the first commit

If GitHub authentication becomes the blocker, stop and explain exactly what remains.

### Step 7: Hand Off To The Analytical Workflow

Once the repo exists, route to:

- `project-bootstrap` for artifact discipline
- `problem-framing` for the first real analytical step

## Expected Output

Produce:

```markdown
## Repo Goal

## Proposed Structure

## Commands To Run

## What Each File Or Folder Does

## First Commit

## GitHub Connection Step

## Recommended Next Skill
```

## Guardrails

- Keep the structure minimal.
- Do not over-engineer folder trees.
- Do not assume GitHub credentials or CLI setup already work.
- Do not move into modeling or analysis before repository setup is clear.
- Explain commands before or as you give them.

## Common Failure Modes

- building too much scaffolding before the student has a real project
- assuming the student already knows Git
- skipping the explanation of why files exist
- jumping into GitHub auth troubleshooting before the local repo is sound
- treating bootstrap as if it already completed problem framing
