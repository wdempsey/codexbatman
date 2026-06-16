# UI/UX Standards

**These standards keep the Codex Batman site polished, legible, and useful without turning documentation work into a redesign project.**

They are intentionally lightweight. The preferred path is to improve page purpose, navigation, hierarchy, and cross-linking before adding new visual treatments.

## Core Standard

Every page should answer three questions quickly:

1. What is this page for?
2. Who is it for?
3. What should the reader do next?

If a page fails one of those tests, fix that before adding visual polish.

## Page Purpose

Each page should have:

- a clear opening summary in the first screenful
- a visible scope so readers know whether the page explains, teaches, or directs action
- an obvious next action, such as a related workflow, setup step, example, or skill

Avoid openings that begin with background before the user understands the page's purpose.

## Reading Experience

Prefer:

- short paragraphs
- headings that describe decisions or tasks
- concise bullets when the content is list-shaped
- one concept per section
- restrained callouts only when they improve orientation

Avoid:

- dense text walls
- vague heading labels
- repeated explanations across adjacent pages
- decorative blocks that do not help navigation or comprehension

## Terminology

Use terminology consistently across the site:

- `Codex Batman`
- `Backbone Protocol`
- `Tooling Stack`
- `Skill Library`
- `student`, `data scientist`, and `data science manager`

When older inherited wording appears, prefer updating the surrounding page so the active framing stays consistent.

## Navigation And Cross-Links

Navigation should reduce decisions, not create more of them.

Prefer:

- clear top-level section names
- section landing pages that explain what belongs there
- cross-links among major pillars
- one obvious starting page for newcomers

Review especially for:

- duplicate or confusing section names
- orphan pages that matter but are hard to discover
- pages that mention a concept without linking to the canonical explanation
- role pages that do not point to a next action

Major sections that should usually cross-link when relevant:

- Start Here
- Core Data Science Workflow
- Skill Library
- Tooling Stack
- Backbone Protocol
- Examples
- Lab Manager / Research OS pages

## Visual Direction

The site should feel modern but restrained.

Prefer:

- MkDocs Material-native cards, admonitions, tables, and section indexes
- consistent spacing and heading rhythm
- accessible contrast
- low visual clutter
- mobile-friendly layouts

Avoid:

- heavy CSS for one-off effects
- custom JavaScript
- redesigning page chrome to solve content problems
- adding ornament before the page hierarchy works

## Mobile Readability

Pages should remain usable on laptop, tablet, and phone widths.

Check for:

- overly long hero or intro blocks
- tables that become hard to scan on narrow screens
- callouts or cards that stack awkwardly
- headings that are too abstract once the page compresses

When in doubt, simplify rather than add layout complexity.

## Recommended Review Order

When reviewing a page or section:

1. confirm page purpose
2. tighten the opening summary
3. improve heading clarity
4. add or fix next-action links
5. reduce copy density
6. polish visuals only after the structure is working

## Guardrails

- Prefer additive edits over rewrites.
- Keep changes minimal and reversible.
- Preserve existing MkDocs Material structure unless there is a clear navigation problem.
- Do not introduce new dependencies for UI work.
- Do not add custom JavaScript.
- Do not use visual polish to hide structural confusion.

## Inputs For Future Passes

The current repo-local sources of truth for site improvement are:

- `UI_REDESIGN_BRIEF.md`
- `SITE_STRUCTURE_REVIEW.md`
- `mkdocs.yml`
- the relevant page being reviewed

Use those together with the site review skills to guide future passes.
