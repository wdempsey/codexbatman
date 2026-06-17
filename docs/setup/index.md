# Codex Setup for New Users

This section takes you from zero to a working Codex setup for this repository.

If you only do one thing after setup, start one concrete path instead of browsing:

- students: [Analytics Repo Example - Student Path](../examples/analytics-repo/student.md)
- practitioners: [Analytics Repo Example - Practitioner Path](../examples/analytics-repo/practitioner.md)
- managers: [Lab Manager Agent](../workflows/manager/lab-manager-agent.md)

## What This Setup Path Covers

This setup path is for students and other new users who want to:

1. install Codex
2. clone this repository
3. open the repository in Codex
4. begin one real workflow path

## Two Ways to Run Codex

**Option 1: Terminal.** A plain terminal window is enough for this repository.

**Option 2: A code editor.** A code editor such as VS Code gives you a file explorer, an editor, and a built-in terminal in one place. Codex still runs in the terminal, but the visual layout is easier for many students.

## Get Started

### Step 1: Install Codex

Open a terminal and verify that Codex is available:

```bash
codex --version
```

If Codex is not installed yet, complete your usual Codex installation first, then return here.

### Step 2: Open This Repository

Clone the repository locally, then open the repository folder itself in Codex or in a code editor with a terminal.

### Step 3: Optional Editor Setup

If you want a visual working environment, use [Set Up VS Code](vscode-setup.md).

### Step 4: Understand Modes

Read [How Codex Modes Work](modes.md) for the basic interaction model.

### Step 5: Start One Concrete Path

- If you are learning, start with [Analytics Repo Example - Student Path](../examples/analytics-repo/student.md). This is the primary student starting point.
- If you want a shorter warm-up before the repo example, open [First Session - Predict Housing Prices with Tutor Mode](../students/first-session.md) first.
- If you are executing a real project, start with [Analytics Repo Example - Practitioner Path](../examples/analytics-repo/practitioner.md).

## Learn and Browse

| Page | What You'll Learn |
|------|-------------------|
| [Analytics Repo Example](../examples/analytics-repo/index.md) | What a real Codex Batman analytics repository should look like |
| [How Skills Work](../system/skills-explained.md) | How workflow skills, tutor overlays, and method skills fit together |
| [Skill Library](skill-reference.md) | The shared catalog of skills in this repository |

## What You End Up With

After this section you'll have Codex running locally, the repository cloned and open, and one clear next step waiting — not a list of things to read.

## Student First Action

If you're a student, start with [Repo Bootstrap For Students](skill-reference.md#additional-shared-skills). It builds the right folder and file structure so you're not starting from a blank slate when the workflow asks for artifacts.

## Common Issues

!!! warning "Stuck? Check these first."
    | Problem | Fix |
    |---------|-----|
    | `codex` command not found | Reopen the terminal after installation and verify Codex is on your PATH |
    | Codex cannot see the repository | Open the repository folder itself, not a single file |
    | The workflow feels abstract | Start with [Analytics Repo Example](../examples/analytics-repo/index.md) instead of the full workflow docs |
