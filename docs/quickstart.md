---
description: Codex-native quickstart for structured, reproducible data science workflows with explicit gates and artifact outputs.
---

# Quickstart

**Use this page when you want the fastest path from installation to a working Codex Batman workflow.**

If you are brand new, do not read the whole site first. Install Codex, verify local execution, then move into the setup, examples, and role pages that match your use case.

If you only do one thing after install, open [Choose Your Role](roles/index.md) and follow one path instead of browsing the whole site.

## Goal

Install Codex and execute structured, reproducible data science workflows.

This system is:

- Codex-native
- Workflow-gated
- Reproducible
- Role-aware for students, practitioners, and managers

This is not a prompting guide.

It is a structured execution layer.

Codex is the primary execution engine for this workflow system.

## Recommended First Ten Minutes

1. Install and verify Codex locally.
2. Open [Setup Overview](setup/index.md) for the repository-specific environment and workflow checks.
3. Open [Choose Your Role](roles/index.md).
4. Pick one concrete next page:
   [Students](students/index.md),
   [Researchers & Data Scientists](data-scientists/index.md),
   [Managers](managers/index.md).
5. If you want a real project shape immediately, open [Analytics Repo Example](examples/analytics-repo/index.md).

## Choose Your Route After Install

- If you are a student and want the real first action, go next to [Repo Bootstrap For Students](setup/skill-reference.md#additional-shared-skills) and then [Analytics Repo Example - Student Path](examples/analytics-repo/student.md).
- If you are a researcher or data scientist and want the real project path, go next to [Analytics Repo Example - Practitioner Path](examples/analytics-repo/practitioner.md).
- If you are a manager and want the coordination path, go next to [Lab Manager Agent](workflows/manager/lab-manager-agent.md).
- If you want the full workflow model first, go next to [Core Data Science Workflow](workflows/data-science/index.md).

## Practitioner Shortcut

If you are a researcher or data scientist and want the intended route without deciding among multiple concepts, use this order:

1. [Core Data Science Workflow](workflows/data-science/index.md)
2. [Backbone Protocol](backbone/index.md)
3. [Analytics Repo Example - Practitioner Path](examples/analytics-repo/practitioner.md)
4. [Skill Library](setup/skill-reference.md)

## Concrete Repo Example

If you want to see a real repo shape before changing your own workflow, open [Analytics Repo Example](examples/analytics-repo/index.md).

Use [Student Path](examples/analytics-repo/student.md) if you want scaffolded, attempt-before-answer guidance.

Use [Practitioner Path](examples/analytics-repo/practitioner.md) if you want the shorter execution-oriented version of the same project.

## Best Next Page By Role

- Students: [For Students](students/index.md)
- Researchers & Data Scientists: [For Researchers & Data Scientists](data-scientists/index.md)
- Managers: [For Data Science Managers](managers/index.md)

## Step 1 - Install & Verify Codex

Codex must be installed locally before executing structured workflows.

Choose your operating system.

### macOS

#### Option A - Install via Terminal (Recommended for CLI workflows)

Using Homebrew:

```bash
brew install codex
```

Or using npm (if applicable to your environment):

```bash
npm install -g codex
```

Verify installation:

```bash
codex --version
```

#### Option B - Install via Codex Desktop App (Recommended for macOS users)

Download the Codex Desktop App from the official website.

Install and sign in.

The macOS app provides:

- Local execution
- Integrated terminal
- Structured prompt management
- Project-level context

After installation, verify CLI access from Terminal:

```bash
codex --version
```

### Windows

#### Option A - Install via Terminal (PowerShell)

Using npm:

```bash
npm install -g codex
```

Verify:

```bash
codex --version
```

If using WSL, follow Linux instructions below.

#### Option B - Install via Website

Download the Windows installer from the official Codex website.

Run installer and follow setup prompts.

After installation, open PowerShell and verify:

```bash
codex --version
```

### Linux

#### Install via Terminal

Using npm:

```bash
npm install -g codex
```

Or via package manager if available:

```bash
sudo apt install codex
```

Verify:

```bash
codex --version
```

### Verify Local Execution

Create a test file:

`example_prompt.md`

```text
# Task: Installation Verification

Output: "Codex is installed and executing locally."
```

Run:

```bash
codex run example_prompt.md
```

Expected result:

- Prompt executed
- Output written to disk

Codex must execute locally before proceeding to structured workflows.

## Step 2 - Start With One Real Workflow

Do not try to learn the whole architecture at once.

Pick one route:

- student: [Analytics Repo Example - Student Path](examples/analytics-repo/student.md)
- practitioner: [Analytics Repo Example - Practitioner Path](examples/analytics-repo/practitioner.md)
- manager: [Lab Manager Agent](workflows/manager/lab-manager-agent.md)

## Step 3 - Execute Structured Workflows

### Example 1 - Reproducible Regression Pipeline

Create dataset:

`housing_sample.csv`

```csv
price,square_feet,bedrooms,age
350000,2000,3,20
450000,2500,4,10
275000,1500,3,30
500000,3000,5,5
325000,1800,3,25
```

Create prompt:

`regression_prompt.md`

```text
# Task: Structured Regression Workflow

You are operating inside a reproducible data science pipeline.

Objectives:
1. Load housing_sample.csv
2. Validate schema and missing values
3. Fit OLS model:
   price ~ square_feet + bedrooms + age
4. Report:
   - coefficients
   - R^2
   - diagnostics
5. Output executable Python code
6. Save summary to model_summary.txt

Constraints:
- Do not skip validation
- Do not assume columns
- Document assumptions

Expected output structure:
1. Validation Summary
2. Model Specification
3. Results
4. Diagnostics
5. Files Written
6. Reproducibility Notes
```

Run:

```bash
codex run regression_prompt.md
```

Example output (replace with your real run output):

```text
$ codex run regression_prompt.md
Dataset loaded: 5 rows
No missing values
OLS model fit

R^2: 0.91

Coefficients:
square_feet: 120.4
bedrooms: 15000
age: -1800

model_summary.txt written
```

This is a structured workflow gate.

## Next Step

After you finish installation and the first verification run, move to:

- [Setup Overview](setup/index.md) for repository-specific environment guidance
- [Core Data Science Workflow](workflows/data-science/index.md) for the shared execution sequence
- [Examples](examples/index.md) for concrete backbone scenarios

### Example 2 - Repository Architecture Analysis

Target repository:

`https://github.com/pandas-dev/pandas`

Create prompt:

`repo_analysis.md`

```text
# Task: Repository Architecture Review

You are performing structured engineering analysis.

Objectives:
1. Analyze repository structure
2. Identify core packages
3. Identify test architecture
4. Identify build system
5. Output structured report

Expected output structure:
- Entry Points
- Core Modules
- Testing Strategy
- Build System
- Architectural Risks

Constraints:
- Do not summarize generically
- Base analysis on repository structure
```

Run:

```bash
codex run repo_analysis.md
```

Example output (replace with your real run output):

```text
$ codex run repo_analysis.md
Repository indexed
2,300+ Python files analyzed

Core Modules:
- pandas/core
- pandas/io
- pandas/tests

Testing:
- pytest-based
- extensive fixtures

Build:
- pyproject.toml
- C extensions present

repo_report.md written
```

Structured prompts produce structured outputs.

## Step 3 - Avoid Vague Instructions

Vague regression:

```text
Run a regression on this dataset.
```

Weak CLI-style output:

```text
$ codex run vague_regression.md
This dataset appears suitable for regression.
A model can be fit.
```

Vague repository request:

```text
Tell me about this repository.
```

Weak CLI-style output:

```text
$ codex run vague_repo.md
This repository contains Python code and tests.
It is likely a data library.
```

Why vague instructions fail:

- Reproducibility: no explicit seed, environment, or output artifacts
- Validation: no schema checks or guardrails
- Architectural clarity: no required output structure

## Next Steps

- Structured Workflow Gates (in progress)
- Data Science Layer Architecture (in progress)
- Devlog -> Digital Garden System (in progress)
- Manager Playbooks (coming soon)

## Codex Flexibility Clause

If Codex detects:

- Broken formatting
- Inconsistent heading structure
- mkdocs rendering conflicts
- Redundant legacy references

It may:

- Adjust wording minimally
- Normalize headings
- Remove legacy references

It must:

- Stay within Quickstart files
- Not restructure navigation
- Not introduce new sections beyond spec
