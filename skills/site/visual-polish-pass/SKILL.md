---
name: visual-polish-pass
description: Apply a restrained visual cleanup after page structure and content are in place, using MkDocs Material-native patterns.
category: site
status: active
stage: site-review
role_compatibility:
  - student
  - data scientist
  - data science manager
inputs:
  - reviewed page or section
  - current styling patterns
  - approved content structure
outputs:
  - light visual cleanup plan
  - minimal polish changes
artifacts:
  - visual pass notes
depends_on:
  - ui-ux-review
recommended_next:
  - ui-ux-review
human_review_required: true
---

# Skill: Visual Polish Pass

## Purpose

Improve a page's visual clarity after the structure, wording, and next-action flow are already in decent shape.

This skill is for finishing touches, not redesigning the site.

## When To Use

Use this skill after a page already has:

- a clear purpose
- readable headings
- reasonable copy density
- visible next actions

## Preferred Moves

Prefer:

- concise summaries
- cards where they improve scannability
- admonitions for small orientation cues
- section landing pages
- restrained grouping of related links

## Avoid

- new dependencies
- custom JavaScript
- heavy CSS
- theme rewrites
- decorative layout changes that do not improve understanding

## Procedure

### Step 1: Confirm Readiness

Make sure the page already works structurally. If not, route back to `ui-ux-review`.

### Step 2: Identify Friction

Look for places where the page feels visually flat, noisy, or harder to scan than necessary.

### Step 3: Apply Minimal Material-Native Improvements

Prefer existing MkDocs Material patterns over custom solutions.

### Step 4: Recheck Restraint

Confirm that the page still feels like documentation, not a marketing microsite.

## Output Format

Produce:

```markdown
## Page Readiness

## Visual Friction

## Minimal Polish Moves

## Changes To Avoid
```

## Guardrails

- Preserve the existing MkDocs Material structure.
- Keep the diff minimal and reversible.
- Improve aesthetics only where it also improves comprehension.
