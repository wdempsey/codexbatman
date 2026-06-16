# Site Structure Review

Last updated: 2026-06-15

## Scope

This review is structural only:

- information architecture
- page coverage
- route and nav consistency
- stale inherited sections
- entry-point clarity

It does not recommend rewriting page content yet.

## High-Level Assessment

The repository now contains two overlapping site shapes:

1. a newer `Codex Batman` data-science operating-system structure
2. an older, broader `Claude Code for researchers/managers` structure

The newer structure is more coherent for the repo mission in [AGENTS.md](/Users/wdem/Documents/github/codexbatman/AGENTS.md:1). The older structure still contributes useful pages, but many of them are partially disconnected from the active navigation and current positioning.

## Structural Strengths

- Clear role split:
  students, practitioners, managers.
- Clear canonical workflow backbone:
  project bootstrap through experiment logging.
- Shared skill catalog exists as a central hub.
- Build/customization section already exists.
- The repo has enough material for a substantial site once the routing is clarified.

## Structural Problems

### P0: Active Navigation Covers Only Part Of The Actual Site

Evidence:
- `NAV_COUNT 35`
- `MISSING_COUNT 45`

Major orphan groups:
- `downloads/*`
- `essentials/*`
- `tax-workflow/*`
- `toolkit/claude-md.md`
- `toolkit/executive-assistant.md`
- `toolkit/skills-guide.md`
- `workflows/index.md`
- `workflows/first-session-skills.md`
- several older workflow reference pages

Impact:
- Useful content exists but is hard to discover.
- The site can feel smaller than it is from the nav, and messier than it should be from search or direct links.

### P0: The Site Mission And Some Legacy Sections No Longer Match Cleanly

Locations:
- [docs/downloads/index.md](/Users/wdem/Documents/github/codexbatman/docs/downloads/index.md:1)
- [docs/system/index.md](/Users/wdem/Documents/github/codexbatman/docs/system/index.md:1)
- [docs/resources.md](/Users/wdem/Documents/github/codexbatman/docs/resources.md:1)
- [docs/privacy.md](/Users/wdem/Documents/github/codexbatman/docs/privacy.md:1)

Problems:
- Some sections still frame the site around `Claude Code`, executive-assistant workflows, or the inherited personal operating system.
- Other sections now frame it around a disciplined data science operating system.
- The mixture creates ambiguity about whether the site is:
  a data-science OS, a general Claude Code guide, or an academic productivity hub.

### P1: Newcomer Entry Points Are Competing With Each Other

Locations:
- [docs/quickstart.md](/Users/wdem/Documents/github/codexbatman/docs/quickstart.md:1)
- [docs/setup/index.md](/Users/wdem/Documents/github/codexbatman/docs/setup/index.md:1)
- [docs/students/first-session.md](/Users/wdem/Documents/github/codexbatman/docs/students/first-session.md:1)
- [docs/index.md](/Users/wdem/Documents/github/codexbatman/docs/index.md:59)

Problems:
- `Quickstart` is broad and somewhat tool-install heavy.
- `Setup` is student-oriented and more concrete.
- `First Session` is the clearest beginner flow for one audience.
- The homepage suggests role entry, but not one universal first action.

Impact:
- A first-time visitor may not know whether to start with install docs, setup docs, the homepage role lanes, or the first-session tutorial.

### P1: Role Pages Are Uneven As Landing Pages

Locations:
- [docs/students/index.md](/Users/wdem/Documents/github/codexbatman/docs/students/index.md:1)
- [docs/data-scientists/index.md](/Users/wdem/Documents/github/codexbatman/docs/data-scientists/index.md:1)
- [docs/managers/index.md](/Users/wdem/Documents/github/codexbatman/docs/managers/index.md:1)

Problems:
- Student page has a concrete first-session pointer.
- Practitioner and manager pages are thinner and less action-oriented.
- Links are not fully standardized:
  practitioner page still points to older `toolkit/skills-guide.md` guidance instead of the newer shared explanation layer.

### P1: Downloads And Reference Material Are Structurally Rich But Poorly Positioned

Locations:
- [docs/downloads/index.md](/Users/wdem/Documents/github/codexbatman/docs/downloads/index.md:1)

Problems:
- The page is substantial and potentially valuable.
- It is placed under `Build Your Own`, which may undersell it for power users.
- It still links heavily to the inherited repo identity.

Impact:
- Power-user material exists, but it is not integrated cleanly into the current site story.

### P2: Duplicate Or Overlapping Explanation Layers Exist

Examples:
- `How Skills Work` appears through multiple entry points.
- `setup/skill-reference.md` serves as a hub while older skill-guide material still exists.
- `workflows/data-science/index.md` is the active canonical workflow page, but older workflow pages remain in the tree.

Impact:
- Readers can encounter two explanations for similar ideas with different framing and ages.

## Recommended Structural Direction

### Keep As Core

- Homepage
- Setup
- Role pages
- Core data-science workflow pages
- Skill library
- Build-your-own pages that directly support the current system

### Review For Reintegration Or Retirement

- `downloads/*`
- `essentials/*`
- `tax-workflow/*`
- older Claude-focused toolkit pages
- legacy workflow example pages not referenced by the current mission

### Likely Structural Decision Needed

Choose one of these:

1. `Narrow`
   Keep the site tightly focused on the data-science operating system and move legacy general-AI material out of the main journey.
2. `Layered`
   Keep broader material, but explicitly label it as a reference library or legacy companion layer.

## Prioritized Structural Tasks

### P0

- Decide which sections are primary versus legacy.
- Resolve the nav/orphan-page mismatch.
- Align site identity files and inherited infrastructure pages with the current mission.

### P1

- Pick one canonical newcomer path.
- Standardize the three role landing pages.
- Reposition downloads/reference material in the information architecture.

### P2

- Remove or consolidate duplicated explanation layers.
- Create a clear policy for examples, archives, and legacy compatibility pages.

## Suggested Sequencing

1. Identity and domain alignment
2. Navigation simplification
3. Homepage and role-page redesign
4. Structural cleanup of orphan sections
5. Content pass page by page

## Notes For The Upcoming Content Pass

When we do the content pass, the highest-value targets will be:

- [docs/downloads/index.md](/Users/wdem/Documents/github/codexbatman/docs/downloads/index.md:1)
- [docs/resources.md](/Users/wdem/Documents/github/codexbatman/docs/resources.md:1)
- [docs/privacy.md](/Users/wdem/Documents/github/codexbatman/docs/privacy.md:1)
- [docs/system/index.md](/Users/wdem/Documents/github/codexbatman/docs/system/index.md:1)
- [docs/quickstart.md](/Users/wdem/Documents/github/codexbatman/docs/quickstart.md:1)
- [docs/data-scientists/index.md](/Users/wdem/Documents/github/codexbatman/docs/data-scientists/index.md:1)
