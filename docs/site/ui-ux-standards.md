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

## Voice And Writing Style

The site voice is second-person, direct, and warm. See `skills/site-voice/SKILL.md` for the full voice guide. Key rules:

- Lead with payoff, not setup — open with the thing that matters, not context paragraphs
- Write "you", never "the user" or "students" or "researchers"
- Contractions are fine ("you're", "don't", "it's")
- Prose over bullet lists for three items or fewer
- Keep paragraphs short — two sentences is often enough
- "Where to go next" sections: one or two links with a sentence of context, not a link dump
- Avoid these headers: "Role Summary", "This path is for you if...", "Overview", "What Each Page Is For"

## Design Decisions (July 2026 Warm Editorial Pass)

The site's soft direction is guided by two references: the maintainer's digital garden ([wdempsey/digitalrandomforest](https://github.com/wdempsey/digitalrandomforest), see its `QUARTZ_DESIGN_TARGET.md` — warm paper palette, quiet chrome, reading comfort first) and [pi.dev](https://pi.dev/) (calm, copy-first, terminals as the single dark flourish). Decisions in effect:

- **Warm paper light scheme**: light mode uses the garden palette — background `#f8f4ec`, ink `#2f2b27`, borders `#e6dfd3`, links `#776657`, accent `#6f5b46`, warm dark-brown header `#3d362e` — defined as variable overrides in the "Warm Editorial Restyle" block of `extra.css`. This supersedes "light sections keep indigo" from the June 2026 pass. The slate (dark) scheme is unchanged.
- **Terminals stay dark**: demo widgets keep the navy terminal palette deliberately — on a soft page the terminal is the one dark flourish, per pi.dev. Light-mode shadow and border are softened so widgets sit calmly on paper.
- **Serif headings, sans body**: Fraunces now extends through h3. Body stays DM Sans; code stays JetBrains Mono.
- **What "soft" means here**: prefer warmth in color, calm in motion, and generosity in whitespace over new decorative elements. When in doubt, consult the garden's avoid-list: nothing that reads as dashboard, SaaS UI, or heavy developer styling on light surfaces.

## Design Decisions (June 2026 Pass)

These decisions are in effect and should not be reversed without cause (the July 2026 pass above supersedes the light-section indigo rule only):

- **Amber CTAs on dark sections**: `#f4a261` fill, `#1a0a00` text, `#e8914f` hover — applies to `.hf-hero`, `.hf-section--dark`, `.hf-section--connect` only. Light sections keep indigo.
- **Bubble hover**: `180ms cubic-bezier(0.2, 0, 0, 1)` — snappier than the default `220ms ease`
- **Role grid**: `repeat(3, 1fr)` → `repeat(2, 1fr)` at 960px → `1fr` at 600px
- **Decision Guide**: card grid (`.decision-grid` / `.decision-card` classes), not a table — wraps at 760px and 375px
- **Student first step**: basic-classification/learning.md is the canonical first action for students. first-session.md is optional warm-up only. analytics-repo/student.md and practitioner.md are redirect stubs — do not link to them directly.
- **New SVGs**: setup-installation.svg, workflow-backbone.svg, examples-three-lenses.svg in `docs/assets/home/`

## Inputs For Future Passes

The current repo-local sources of truth for site improvement are:

- `UI_REDESIGN_BRIEF.md`
- `SITE_STRUCTURE_REVIEW.md`
- `mkdocs.yml`
- `skills/site-voice/SKILL.md` — voice and writing style
- the relevant page being reviewed

Use those together with the site review skills to guide future passes.

When a future pass needs new visuals, use [Asset Prompt Pack](asset-prompt-pack.md) so image requests stay aligned with the site's actual visual direction.
