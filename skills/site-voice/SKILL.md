---
name: site-voice
description: >
  Voice and writing style guide for the Codex Batman MkDocs site. Use this skill
  whenever editing, writing, or reviewing any page in the docs/ directory of this
  repository — including role pages (students/, data-scientists/, managers/),
  examples, backbone, setup, quickstart, or the homepage. Trigger on any request
  that involves: writing or rewriting site copy, reviewing page voice or tone,
  making pages less robotic, warming up documentation language, fixing "too formal"
  or "too bullet-heavy" feedback, or any content pass on site markdown files.
  Also use for homepage sections, navigation labels, and admonition text.
category: site
status: active
stage: site-review
role_compatibility:
  - student
  - data scientist
  - data science manager
inputs:
  - docs page draft
  - surrounding page context
  - relevant site standards
outputs:
  - voice-aligned copy
  - minimal editorial recommendations
artifacts:
  - edited markdown
recommended_next:
  - ui-ux-review
  - navigation-review
source_attribution:
  - "Repo-native voice guide from the 2026 site rewrite."
---

# Codex Batman Site Voice Guide

This skill captures the voice decisions made during the 2026 site rewrite. Apply it whenever you're writing or editing any page in `docs/`.

## Quick Start

Use this skill for site copy, not general skill prose. Preserve page structure unless the user asks for a structural pass.

Inputs are the page draft, nearby navigation context, and any relevant rule from `docs/site/ui-ux-standards.md`. Output edited markdown or a short editorial review.

Ask before continuing if the edit would change navigation, rewrite a full page, alter a July 2026 design decision, or move content between sections.

## Why This Matters

The site's first-pass content was technically accurate but robotically structured: heavy on bullet lists, third-person role summaries, and "This section is for users who..." openers. The goal of the rewrite was to make the site feel like a colleague explaining a real system, not a spec sheet describing a product.

The voice is: direct, warm, second-person, technically precise. It respects the reader's intelligence while acknowledging that learning a new workflow is genuinely confusing at first.

---

## Core Voice Rules

### Lead with payoff, not setup

Don't explain what a section covers before telling the reader why they're there. Cut the context paragraph and open with the thing that matters.

**Before:**
> This section covers the workflow backbone used across all three roles in Codex Batman. It is designed to support reproducible data science projects.

**After:**
> The backbone keeps your project state legible when you return to it — or hand it off — a week later.

### Second person, always

Write "you" not "the user" or "students" or "researchers." Even on role pages, address the reader directly.

**Before:**
> Students should begin with the analytics repo example before attempting independent projects.

**After:**
> Start with the analytics repo example before trying a project on your own.

### Contractions are fine

"You're" beats "you are." "Don't" beats "do not." "It's" beats "it is." The site shouldn't read like a legal document.

### Prose over bullet lists (under 4 items)

If a list has three items or fewer, write it as a sentence. Lists are for genuinely enumerable things — artifact names, install steps, skill catalogs.

**Before:**
> What changes in student mode:
> - Codex asks for your attempt first
> - hints come before answers
> - scaffolding stays visible

**After:**
> In student mode Codex asks for your attempt before offering an answer, gives hints before solutions, and keeps the scaffolding visible throughout.

### Short paragraphs

Two sentences is often enough for a paragraph. Never write a paragraph longer than five sentences. If it's longer, it probably needs a header or it should be two paragraphs.

### "Where to go next" = a recommendation, not a link dump

The final section of a page should feel like "here's what I'd do next" — one or two links with a sentence of context, not a bulleted list of six alternatives.

**Before:**
> ## Where To Go Next
> - [Core Data Science Workflow](../workflows/data-science/index.md)
> - [Backbone Protocol](../backbone/index.md)
> - [Examples](../examples/index.md)
> - [Skill Library](../setup/skill-reference.md)
> - [How Skills Work](../system/skills-explained.md)

**After:**
> Start with [Core Data Science Workflow](../workflows/data-science/index.md) if you haven't already. Once that makes sense, open [Examples](../examples/index.md) before adapting anything to your own project.

---

## Header Anti-Patterns

Avoid these header patterns — they signal the robotic voice:

| Avoid | Use instead |
|-------|-------------|
| "Role Summary" | Remove — integrate into the lede |
| "This path is for you if..." | Move into the opening sentence |
| "What Changes In X Mode" | "How X works differently" or just describe it inline |
| "Typical Outputs" | Keep only if listing real artifact names |
| "What Each Page Is For" | Replace with a sentence or two of prose |
| "Overview" as a heading | Remove — it's always redundant |

---

## Page Opening Template

Every page should open with:

1. **A direct lede sentence** — who this is for and what they get. One sentence, second person, no hedging.
2. **The first action or concept** — immediately useful, no background first.
3. (Optional) A short "If you're not sure..." clarifying sentence for readers who landed here by accident.

**Example (students/index.md):**
> This is for you if you're learning data science workflows for the first time and want Codex to coach your reasoning rather than just hand you answers — while still producing real project artifacts.
>
> Start with [Analytics Repo Example — Student Path](../examples/analytics-repo/student.md).

---

## Specifics for Role Pages

Each role page (students, data-scientists, managers) should follow this order:

1. Lede (one sentence, second person, what Codex does for this role)
2. "Start Here" — one link, one sentence
3. What changes in this mode (prose, 2–4 sentences, NOT a bullet list)
4. Recommended sequence (numbered list is fine here — it's genuinely sequential)
5. Typical artifacts or outputs (brief, real names)
6. Skills relevant to this role (list with short descriptions)
7. "Where to go next" (2 sentences max, 1–2 links)

Do NOT include:
- "Role Summary" header
- "This section is for..." bullet lists
- Link dumps at the end

---

## Tone Calibration

The site explains a real technical system. It shouldn't be so warm it feels like a startup pitch, but it also shouldn't feel like reading API documentation.

Aim for: **the tone a thoughtful senior colleague uses in a Notion doc explaining their workflow to a new teammate.** Technically precise. Direct. Assumes the reader is smart. Does not apologize for complexity, but also does not bury the lede.

If a sentence sounds like it belongs in a product brochure, cut it.
If a section is all bullets, ask whether it would read better as prose.
If an opener starts with "This section...", rewrite it.

---

## Checking Your Work

Before finishing an edit, read the page aloud (mentally). Ask:
- Does the first sentence tell me why I'm here?
- Is there a bullet list that would be clearer as a sentence?
- Does the "where to go next" section feel like a recommendation or a sitemap?
- Have I used "the user" or "students" when I could have written "you"?
- Is any paragraph longer than 5 sentences?
