---
description: Codex-native quickstart for structured, reproducible data science workflows with explicit gates and artifact outputs.
---

# Quickstart — Codex-Native Data Science Workflow

## Goal

Install Codex and execute structured, reproducible data science workflows.

This system is:

- Codex-native
- Workflow-gated
- Reproducible
- Architected for data science managers and senior data scientists

This is not a prompting guide.

It is a structured execution layer.

This diverges from the prior Claude-focused version. Codex is now the execution engine.

## Step 1 — Install & Verify Codex

Codex must be installed locally before executing structured workflows.

Choose your operating system.

### macOS

#### Option A — Install via Terminal (Recommended for CLI workflows)

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

#### Option B — Install via Codex Desktop App (Recommended for macOS users)

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

#### Option A — Install via Terminal (PowerShell)

Using npm:

```bash
npm install -g codex
```

Verify:

```bash
codex --version
```

If using WSL, follow Linux instructions below.

#### Option B — Install via Website

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

## Step 2 — Execute Structured Workflows

### Example 1 — Reproducible Regression Pipeline

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
   - R²
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
✔ Dataset loaded: 5 rows
✔ No missing values
✔ OLS model fit

R²: 0.91

Coefficients:
square_feet: 120.4
bedrooms: 15000
age: -1800

✔ model_summary.txt written
```

This is a structured workflow gate.

### Example 2 — Repository Architecture Analysis

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
✔ Repository indexed
✔ 2,300+ Python files analyzed

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

✔ repo_report.md written
```

Structured prompts produce structured outputs.

## Step 3 — Avoid Vague Instructions

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
- Devlog → Digital Garden System (in progress)
- Manager Playbooks (coming soon)

## Codex Flexibility Clause

If Codex detects:

- Broken formatting
- Inconsistent heading structure
- mkdocs rendering conflicts
- Redundant legacy Claude references

It may:

- Adjust wording minimally
- Normalize headings
- Remove legacy references

It must:

- Stay within Quickstart files
- Not restructure navigation
- Not introduce new sections beyond spec
