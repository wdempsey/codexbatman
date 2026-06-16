---
name: ui-ux-review
description: Review one documentation page at a time for purpose, audience, hierarchy, copy density, and next-action clarity.
category: site
status: active
stage: site-review
role_compatibility:
  - student
  - data scientist
  - data science manager
inputs:
  - page content
  - surrounding nav context
  - relevant cross-links
outputs:
  - page review findings
  - minimal improvement recommendations
artifacts:
  - page review notes
recommended_next:
  - navigation-review
  - visual-polish-pass
human_review_required: true
---

# Skill: UI/UX Review

## Purpose

Review one page at a time and identify the smallest useful UI/UX improvements that make the page easier to understand and act on.

This skill is for evaluation first, not wholesale rewriting.

## When To Use

Use this skill when reviewing a page for:

- weak opening summaries
- unclear audience or purpose
- confusing hierarchy
- dense copy
- missing next actions
- missing or weak cross-links

## Review Questions

For the selected page, answer:

1. What is the page for?
2. Who is it for?
3. What should the reader do next?
4. Is the first screenful strong enough?
5. Is the section hierarchy easy to scan?
6. Is any section denser than it needs to be?

## Procedure

### Step 1: Identify Purpose And Audience

State the page's intended purpose and primary audience in one or two lines.

### Step 2: Check The Opening

Flag whether the page quickly explains value, scope, and next action.

### Step 3: Review Hierarchy

Check headings, section order, and whether important content is buried.

### Step 4: Review Actionability

Look for missing links, unclear calls to action, and absent follow-on pages.

### Step 5: Recommend Minimal Fixes

Recommend the smallest changes that would materially improve clarity.

## Output Format

Produce a short review with:

```markdown
## Purpose

## Audience

## What Works

## Issues

## Recommended Minimal Fixes
```

## Guardrails

- Review one page at a time.
- Prefer minimal fixes over rewrites.
- Do not rewrite the whole page unless explicitly asked.
- Prioritize hierarchy, clarity, and next actions over visual decoration.
