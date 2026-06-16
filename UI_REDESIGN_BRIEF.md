# UI Redesign Brief

Last updated: 2026-06-15

## Goal

Make the site feel intentional, polished, and trustworthy while preserving the stronger data-science operating-system direction already present in the newer repo pages.

This brief focuses on interface, layout, navigation, visual hierarchy, and page-to-page user flow. It does not propose copy rewrites yet.

## Current State Summary

The site is in a mixed state:

- The newer pages establish a clear `Codex Batman` and data-science-operating-system identity.
- The live `claudeblattman.com` site still presents a more polished funnel, stronger homepage merchandising, and a clearer newcomer path.
- The local homepage is visually ambitious, but it still reads like a partially completed shell: placeholder elements remain, navigation is dense, and some sections feel abstract before they feel useful.

## What The Live Claude Blattman Site Does Better

- Stronger homepage funnel for first-time visitors.
- Clearer top-of-page merchandising:
  `Starter Kit`, `Get Skills & Templates`, and a strong power-user banner.
- Better sense of momentum:
  the live site feels like an actively maintained product, not just a framework.
- More obvious utility on the homepage:
  concrete use cases appear earlier.
- Simpler category naming for non-experts.

## What The Local Codex Batman Site Does Better

- Stronger conceptual backbone around workflow gates and reproducibility.
- Better separation by role:
  student, practitioner, and manager.
- Stronger articulation of a canonical data-science workflow.
- More promising long-term system architecture.

## Main UI Problems

### P0: Identity Is Visually Unsettled

Locations:
- [mkdocs.yml](/Users/wdem/Documents/github/codexbatman/mkdocs.yml:1)
- [docs/CNAME](/Users/wdem/Documents/github/codexbatman/docs/CNAME:1)
- [docs/privacy.md](/Users/wdem/Documents/github/codexbatman/docs/privacy.md:1)
- [docs/resources.md](/Users/wdem/Documents/github/codexbatman/docs/resources.md:1)

Problems:
- Domain, brand, and supporting site chrome are not yet aligned.
- Some pages still imply the older `Claude Blattman` product framing.
- This makes the visual layer feel less trustworthy before the user even evaluates the design.

Design requirement:
- Finish identity alignment before polishing secondary visuals.

### P1: Homepage Is Attractive But Not Yet Convincing

Locations:
- [docs/index.md](/Users/wdem/Documents/github/codexbatman/docs/index.md:12)
- [docs/stylesheets/extra.css](/Users/wdem/Documents/github/codexbatman/docs/stylesheets/extra.css:542)

Problems:
- Hero explains the system, but it does not immediately show why a visitor should care.
- The second section uses placeholder numerals instead of finished iconography.
- The role-entry section has placeholder media blocks for most lanes.
- The last section is lightweight compared with the live site's stronger conversion cues.

Design requirement:
- Shift the homepage from "architecture overview" toward "clear value + guided entry points + proof of utility."

### P1: Navigation Is Dense And Concept-Heavy

Locations:
- [mkdocs.yml](/Users/wdem/Documents/github/codexbatman/mkdocs.yml:52)

Problems:
- Top-level tabs are numerous and abstract.
- `Start Here`, `Core Data Science Workflow`, `Skill Library`, and `Build Your Own` are all reasonable, but together they create a heavy cognitive load.
- Some important pages are in nav while many others are orphaned from nav entirely.

Design requirement:
- Reduce the number of top-level decisions.
- Make the first path obvious for newcomers.
- Separate beginner entry, workflow reference, and advanced build/customization.

### P1: Role Pages Need A Shared Visual Template

Locations:
- [docs/students/index.md](/Users/wdem/Documents/github/codexbatman/docs/students/index.md:1)
- [docs/data-scientists/index.md](/Users/wdem/Documents/github/codexbatman/docs/data-scientists/index.md:1)
- [docs/managers/index.md](/Users/wdem/Documents/github/codexbatman/docs/managers/index.md:1)

Problems:
- These pages are structurally sound but visually bare.
- They read as text summaries rather than strong entry pages.
- The student page is the most actionable; the practitioner and manager pages feel thinner.

Design requirement:
- Standardize each role page around:
  role promise, who this is for, what changes in this mode, recommended first 3 steps, key skills, and next actions.

### P2: Visual System Needs More Finish

Locations:
- [docs/stylesheets/extra.css](/Users/wdem/Documents/github/codexbatman/docs/stylesheets/extra.css:542)

Problems:
- The page has a good base direction, but several pieces still feel placeholder or unfinished.
- The style language is split between older bento/card treatments and the newer homepage-specific classes.
- Imagery is inconsistent:
  one illustrated tile exists, others are blank placeholders.

Design requirement:
- Consolidate around one visual language for cards, illustrations, section dividers, and CTAs.

### P2: Mobile And Tablet Reliability Is Not Yet Proven

Locations:
- [docs/stylesheets/extra.css](/Users/wdem/Documents/github/codexbatman/docs/stylesheets/extra.css:935)
- [planning.md](/Users/wdem/Documents/github/codexbatman/planning.md:25)

Problems:
- The CSS includes responsive rules, but the homepage still has known open items for hero cropping and section transitions.
- No recent visual QA evidence exists for breakpoint behavior.

Design requirement:
- Verify the homepage and role pages at common laptop, tablet, and phone widths before deeper design polish.

## Recommended Information Architecture Direction

### Top-Level Navigation

Recommended tabs:

1. `Start Here`
2. `Workflow`
3. `Roles`
4. `Skills`
5. `Build`
6. `About`

Notes:
- Collapse `Data Science Students`, `Data Scientists`, and `Data Science Managers` under one `Roles` top-level entry.
- Keep `Downloads` accessible from `Build` or `Skills`, not as its own primary first-run decision.
- Keep `Privacy` and `Resources` secondary, not primary journey drivers.

### Homepage Flow

Recommended homepage sequence:

1. Hero:
   concise promise, one primary CTA, one secondary CTA.
2. Why this system:
   workflow gates, role overlays, reproducibility.
3. Choose your path:
   student, practitioner, manager, builder.
4. Proof section:
   sample skills, example artifacts, or a worked workflow snapshot.
5. Getting started:
   setup, first session, skill library.
6. Trust/footer actions:
   GitHub, about, privacy, contact.

## Prioritized Design Work

### Phase 1: Stabilize The Shell

Locations:
- [mkdocs.yml](/Users/wdem/Documents/github/codexbatman/mkdocs.yml:1)
- [overrides/main.html](/Users/wdem/Documents/github/codexbatman/overrides/main.html:1)
- [docs/index.md](/Users/wdem/Documents/github/codexbatman/docs/index.md:12)

Tasks:
- Finalize canonical identity and domain.
- Remove remaining stale old-brand references from non-homepage pages.
- Replace homepage placeholder links/media treatments with final patterns.
- Confirm the homepage CTA hierarchy.

### Phase 2: Simplify Navigation

Locations:
- [mkdocs.yml](/Users/wdem/Documents/github/codexbatman/mkdocs.yml:52)

Tasks:
- Reduce top-level tabs.
- Group role pages under one clear parent.
- Decide which orphan pages are intentionally hidden versus missing from nav.
- Remove duplicated routes like repeated `How Skills Work` exposure unless it serves a strong purpose.

### Phase 3: Strengthen Entry Pages

Locations:
- [docs/index.md](/Users/wdem/Documents/github/codexbatman/docs/index.md:12)
- [docs/students/index.md](/Users/wdem/Documents/github/codexbatman/docs/students/index.md:1)
- [docs/data-scientists/index.md](/Users/wdem/Documents/github/codexbatman/docs/data-scientists/index.md:1)
- [docs/managers/index.md](/Users/wdem/Documents/github/codexbatman/docs/managers/index.md:1)

Tasks:
- Give each role page a stronger above-the-fold summary and action box.
- Add consistent visual patterning across role pages.
- Make the next action obvious on every page.

### Phase 4: Add Visual Proof

Locations:
- [docs/index.md](/Users/wdem/Documents/github/codexbatman/docs/index.md:59)
- [docs/workflows/examples/project-overview-example.md](/Users/wdem/Documents/github/codexbatman/docs/workflows/examples/project-overview-example.md:1)
- [docs/students/first-session.md](/Users/wdem/Documents/github/codexbatman/docs/students/first-session.md:1)

Tasks:
- Surface one or two realistic screenshots, artifact previews, or workflow diagrams.
- Show what the system produces, not just what it believes.

## Success Criteria

The redesign is successful when:

- a first-time visitor can identify the audience and starting point in under 10 seconds
- the homepage feels finished rather than partially scaffolded
- the primary user paths are obvious
- the design supports the data-science operating-system identity instead of competing with it
- the site feels at least as polished as the live Claude Blattman site, while being more coherent for the new mission
