---
description: Codex-native quickstart for structured data science workflows with workflow gates, reproducibility, and explicit outputs.
---

# Quickstart: Codex-Native Workflow

**Goal:** Run Codex locally with structured prompts that enforce reproducibility, validation, and clear output contracts.

---

## Step 1 — Install & Verify Codex

Install Codex for your environment, then verify local execution.

```bash
codex --version
codex run example_prompt.md
```

Successful local execution confirms your runtime is ready for structured workflow tasks.

---

## Step 2 — Run Structured Prompts

Use prompts with explicit objectives, guardrails, and output structure.

### Example 1 — Regression Workflow

Inline dataset (`housing_sample.csv`):

```csv
sqft,bedrooms,age,price
850,2,30,215000
920,2,22,235000
1100,3,18,290000
1250,3,12,325000
1400,3,8,360000
1600,4,6,420000
1750,4,4,455000
1900,4,3,495000
2100,5,2,540000
2300,5,1,610000
```

Structured prompt:

```text
Task: Run a reproducible OLS regression for housing price prediction.

Objectives:
1. Validate dataset schema and numeric types.
2. Estimate model: price ~ sqft + bedrooms + age.
3. Report coefficients, standard errors, R^2, and residual diagnostics.
4. Save reproducible code and outputs.

Guardrails:
- Halt if required columns are missing or non-numeric.
- Do not impute without stating method.
- Set and report deterministic seed.
- Do not edit raw input data; write transformed data separately if needed.

Expected output structure:
1. Validation Summary
2. Model Specification
3. Results Table
4. Diagnostics
5. Reproducibility Notes
6. Files Written

Required file outputs:
- outputs/regression/analysis.py
- outputs/regression/model_summary.md
- outputs/regression/coefficients.csv
- outputs/regression/diagnostics.json
```

Example local CLI output:

```text
$ codex run regression_prompt.md
[OK] Validation Summary: schema valid, 10 rows loaded.
[OK] Model fit complete: OLS(price ~ sqft + bedrooms + age)
[OK] Results written:
  - outputs/regression/analysis.py
  - outputs/regression/model_summary.md
  - outputs/regression/coefficients.csv
  - outputs/regression/diagnostics.json
[OK] Reproducibility: seed=42, environment pinned.
```

### Example 2 — Repository Architecture Analysis

Repository target:

`https://github.com/pandas-dev/pandas`

Structured prompt:

```text
Task: Analyze the repository architecture of pandas-dev/pandas for maintainability and contribution onboarding.

Objectives:
1. Identify top-level architectural domains (core, io, tests, docs, tooling).
2. Describe module boundaries and dependency patterns.
3. Highlight contributor entry points and high-risk complexity zones.
4. Produce a structured analysis that is actionable for maintainers.

Guardrails:
- Do not provide a vague summary.
- Separate observed structure from inferred recommendations.
- Cite concrete paths/directories when making claims.
- Flag uncertainty explicitly where repository context is incomplete.

Expected output structure:
1. Repository Topology
2. Architectural Domains
3. Dependency and Boundary Notes
4. Contributor Onboarding Paths
5. High-Risk Complexity Areas
6. Recommended Next Actions
```

Example local CLI output:

```text
$ codex run repo_architecture_prompt.md
[OK] Repository Topology mapped.
[OK] Domains identified: core, io, tests, docs, tooling.
[OK] Output sections generated:
  1. Repository Topology
  2. Architectural Domains
  3. Dependency and Boundary Notes
  4. Contributor Onboarding Paths
  5. High-Risk Complexity Areas
  6. Recommended Next Actions
```

---

## Step 3 — Avoid Vague Instructions

Vague input example 1:

```text
Run a regression on this dataset
```

Weak CLI-style output:

```text
$ codex run vague_regression_prompt.md
Done. I ran a regression and it looks good.
```

Vague input example 2:

```text
Tell me about this repository
```

Weak CLI-style output:

```text
$ codex run vague_repo_prompt.md
This repository is large and has many files. It seems well organized.
```

Why vague instructions fail:
- Reproducibility: no explicit seed, environment, or file outputs.
- Validation: no schema checks, guardrails, or halt conditions.
- Architectural clarity: no required structure, boundaries, or evidence.

---

## Next Steps

- Structured Workflow Gates (in progress)
- Data Science Layer Architecture (in progress)
- Devlog → Digital Garden System (in progress)
- Manager Playbooks (coming soon)

---

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
