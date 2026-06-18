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

## Established Design Decisions (Do Not Reverse)

Before making visual changes, read `docs/site/ui-ux-standards.md` for the current state. Key decisions already in effect:

- **Amber CTAs on dark sections**: `#f4a261` fill, `#1a0a00` text — applies to `.hf-hero`, `.hf-section--dark`, `.hf-section--connect` only. Light sections keep indigo. Do not revert to indigo on dark backgrounds.
- **Bubble hover**: `180ms cubic-bezier(0.2, 0, 0, 1)` — do not change back to `220ms ease`.
- **Decision Guide cards**: the `.decision-grid` / `.decision-card` pattern replaces the Quick Decision Guide table on roles/index.md.
- **Voice**: see `skills/site-voice/SKILL.md` before touching any copy.

## Guardrails

- Preserve the existing MkDocs Material structure.
- Keep the diff minimal and reversible.
- Improve aesthetics only where it also improves comprehension.
- Do not introduce new CSS classes when an existing one already covers the case.
