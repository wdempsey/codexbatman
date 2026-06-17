# Asset Prompt Pack

**Use this page when the site needs a new visual and you want the request to stay aligned with the current Codex Batman direction.**

This page is not an asset gallery.

It is the reusable prompt pack and request workflow for future homepage, role-page, and artifact-support visuals.

## Core Rule

Create visuals only after the page purpose and surrounding copy are clear.

If the structure is still changing, prefer placeholder text, artifact previews, or existing screenshots before requesting new art.

## When Codex Can Generate Directly

Codex is a good fit when the asset is:

- a lightweight concept illustration
- a simple artifact mockup
- a stylized scene for a homepage or role page
- a placeholder support visual
- a bitmap-first image that does not need a precise editable design system

Use direct generation when speed and iteration matter more than design-tool polish.

## When To Use A Separate Prompt Or Another Model

Use the prompt pack with another model or teammate when:

- you need a consistent series of related images
- the asset needs multiple rounds of stylistic tuning
- the image will be reused across several pages
- the request should survive beyond a single Codex session
- someone else may generate the image later

## Visual Direction

All prompts should stay inside this visual lane:

- modern but restrained
- atmospheric, not cartoon-chaotic
- data-science and workflow oriented, not generic AI fantasy
- readable at small sizes
- supportive of the page's message instead of competing with it
- clean enough to sit inside MkDocs Material layouts

Prefer visuals that suggest:

- project state
- workflow movement
- artifact production
- decision clarity
- collaboration across roles

Avoid:

- purple-on-white default AI art
- glossy sci-fi dashboards with unreadable microtext
- cluttered collage scenes
- text baked into images unless it is purely decorative
- visuals that imply a web app the repo does not actually have

## Standard Request Template

Use this structure for any new asset request:

```text
Asset name:
Page:
Purpose:
Audience:
Required feeling:
What the image should show:
What it must not show:
Aspect ratio:
Style notes:
Usage notes:
```

## Recommended Aspect Ratios

- homepage hero support art: `16:9`
- media-row support image: `4:3` or `3:2`
- artifact mockup card: `4:3`
- social/share preview candidate: `16:9`

## Prompt 1 - Homepage Hero Support Art

Use when the homepage needs a stronger background or supporting scene.

```text
Create a wide cinematic background illustration for a documentation homepage about an AI-native data science operating system.

The image should feel modern, calm, and structured rather than flashy. Show a data-science workflow world with subtle project artifacts, notebooks, model outputs, dashboards, and collaboration signals, but avoid making it look like a literal product UI screenshot.

Use deep blue, slate, and restrained cyan accents. Keep the center-left area visually calmer so large white homepage text can sit on top without fighting the artwork. The right side can carry more visual drama.

Do not add readable text labels, logos, or fake interface text. Do not make it look like a generic chatbot ad or a fantasy sci-fi poster.

Aspect ratio: 16:9.
```

## Prompt 2 - Student Path Support Visual

Use when a page needs to communicate guided learning without implying that the model gives the answer away.

```text
Create a warm, structured illustration for a student-facing data science workflow page.

Show a learner moving through a real analytics project with visible notes, a problem frame, a data checklist, and a small model experiment trace. The feeling should be guided, disciplined, and encouraging, not magical or chaotic.

The image should suggest attempt-before-answer tutoring and real project artifacts. Avoid classroom clichés, mascots, or exaggerated AI robot imagery.

Style: clean editorial tech illustration, restrained color palette, readable at small size.
Aspect ratio: 4:3.
```

## Prompt 3 - Practitioner Path Support Visual

Use when a page needs to communicate direct execution and artifact discipline.

```text
Create a structured editorial illustration for a practitioner-facing data science workflow page.

Show a working analysis environment centered on artifacts: experiment log, model comparison notes, workflow trace, and a reproducible project folder structure. The image should feel efficient, trustworthy, and focused.

Avoid flashy dashboards, startup marketing clichés, or giant floating chat bubbles. The point is disciplined execution, not generic AI hype.

Style: modern documentation-support art with restrained contrast and clear composition.
Aspect ratio: 4:3.
```

## Prompt 4 - Manager Path Support Visual

Use when a page needs to communicate coordination, waiting-on visibility, and next actions.

```text
Create a clean support visual for a data science manager workflow page.

Show a portfolio-level coordination scene with project summaries, waiting-on items, deadlines, and handoffs represented as tidy artifacts rather than a fictional software product. The image should suggest oversight, prioritization, and clarity.

Avoid dark command-center clichés, trading-floor aesthetics, or dense unreadable screens.

Style: restrained, modern, artifact-first, readable inside a documentation site.
Aspect ratio: 4:3.
```

## Prompt 5 - Artifact Mockup Card

Use when a page needs a visual proof artifact instead of a scenic illustration.

```text
Create a clean mock artifact card for a documentation site about reproducible data science workflows.

The image should resemble a tidy markdown or notebook-style project artifact such as a problem frame, experiment log, or model card. Use a small number of realistic fields and short lines, but do not rely on tiny text for meaning.

The result should look plausible, restrained, and easy to understand at a glance.

Aspect ratio: 4:3.
```

## Request Workflow

Before requesting a new asset:

1. confirm the page purpose
2. confirm the asset type: scene, support image, or artifact mockup
3. confirm where the image will appear
4. pick one base prompt from this page
5. add page-specific constraints
6. generate one asset first before asking for a series

After generation:

1. check readability at the real page size
2. verify it does not compete with adjacent text
3. verify it matches the audience and page purpose
4. keep or revise based on the actual page, not the prompt alone

## Related Pages

- [UI/UX Standards](ui-ux-standards.md)
- [Site Review](index.md)
- [Next Pass PR Roadmap](next-pass-pr-roadmap.md)
