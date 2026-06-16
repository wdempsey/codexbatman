---
name: navigation-review
description: Review mkdocs navigation, section naming, cross-links, and orphan pages to improve discoverability with minimal changes.
category: site
status: active
stage: site-review
role_compatibility:
  - student
  - data scientist
  - data science manager
inputs:
  - mkdocs.yml
  - section landing pages
  - major cross-links
outputs:
  - navigation findings
  - orphan-page notes
  - minimal nav recommendations
artifacts:
  - nav review notes
recommended_next:
  - ui-ux-review
  - visual-polish-pass
human_review_required: true
---

# Skill: Navigation Review

## Purpose

Review the site's navigation structure so users can find the right page with fewer decisions and less confusion.

## When To Use

Use this skill when:

- top-level nav feels crowded or abstract
- section names overlap
- pages exist but are difficult to discover
- major site pillars are weakly connected

## Primary Checks

- top-level nav clarity
- duplicate or confusing section names
- orphan pages that should be discoverable
- weak links among major sections
- landing pages that do not explain what belongs in the section

## Procedure

### Step 1: Review `mkdocs.yml`

Identify the main section structure and the first-run user journey it implies.

### Step 2: Check Naming

Flag labels that are abstract, repetitive, or hard for newcomers to distinguish.

### Step 3: Check Discoverability

Look for important pages that are missing from nav and missing from meaningful cross-links.

### Step 4: Check Major Pillar Connections

Review links among:

- Backbone Protocol
- Tooling Stack
- Examples
- Lab Manager / Research OS
- Skill Library

### Step 5: Recommend Minimal Changes

Suggest the smallest nav or landing-page changes that improve orientation.

## Output Format

Produce:

```markdown
## Current Nav Shape

## What Works

## Confusing Or Duplicate Labels

## Orphan Or Weakly Linked Pages

## Recommended Minimal Changes
```

## Guardrails

- Prefer minimal nav changes.
- Do not restructure the whole site unless explicitly asked.
- Use landing pages and cross-links before adding more top-level tabs.
