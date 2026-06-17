# Role Flow Audit 001

**Purpose:** evaluate the current site flow by pretending to be each primary user role and tracing the likely first-run journey.

This is an audit pass, not an implementation pass. The goal is to identify fundamental issues in routing, concept load, and page-to-page flow before making larger design or information-architecture changes.

## Roles Tested

- student
- researcher / data scientist
- data science manager

## Overall Finding

The site is much clearer than the earlier mixed-state version, but the fundamental flow still has one recurring problem:

**the architecture is coherent for maintainers before it is effortless for first-time users.**

The current version has strong pieces:

- clearer role routing
- stronger role pages
- a real workflow backbone
- examples that make the system more concrete

But the journey still asks users to understand too many concepts too early:

- workflow
- backbone
- skills
- overlays
- examples
- tooling
- build

That concept load shows up differently for each role.

## Cross-Role Findings

### P0: Too Many Valid Starting Points

A first-time user can reasonably start at:

- Home
- Quickstart
- Choose Your Role
- Core Data Science Workflow
- Examples
- Setup Overview

This is better than before, but still too many equally legitimate first actions.

Impact:

- students may skip the best concrete exercise
- practitioners may bounce between workflow, backbone, and skills without knowing which is primary
- managers may open several overlapping workflow pages before finding the most relevant one

### P0: The Homepage Promise Is Better Than The Role-Level Payoff

The homepage now routes users better, but it still frames the system more as architecture than as a solved pain point for each role.

Impact:

- users understand that the site is structured
- they do not always understand why their role-specific path will feel easier or safer than ordinary AI usage

### P1: Canonical Vs Companion Material Is Clearer Locally Than Globally

Many legacy pages now identify themselves as companion material, but the site still has a large reference surface that remains outside nav and outside the main journey.

Impact:

- search and direct links can still land users in non-canonical material
- the conceptual boundary between "current backbone" and "older companion guide" is not yet visually system-wide

### P1: Some Key Labels Still Require Internal Vocabulary

Terms like:

- Backbone Protocol
- overlays
- artifact-first
- project memory

make sense after a little exposure, but they still create friction in first-run moments.

Impact:

- the site rewards patient readers
- it is still harder than it should be for skimmers

## Student Journey

### Entry Simulation

Likely route:

1. Home
2. Choose Your Role
3. Students
4. Student First Session
5. Core Data Science Workflow

### What Works

- the student path now has a concrete first action
- the student page explains how learner support differs from practitioner mode
- the student role is clearly connected to the shared backbone rather than treated as separate content

### P0: The Student Route Still Splits Too Early Between Concrete Exercise And Abstract Workflow

The student page rightly points to `First Session`, but it also quickly asks the learner to think about:

- canonical workflow
- overlays
- shared backbone
- skill library

Impact:

- a learner who just wants guided practice can still get pulled back into architecture too early

Recommended direction:

- make `Student First Session` even more dominant than the abstract workflow explanation
- treat the architecture as "what this exercise is teaching you underneath" rather than parallel reading

### P1: Student Mode Still Depends On Terms A Beginner Does Not Yet Need

The page explains student overlays clearly enough, but a beginner does not need the word `overlay` early in the journey.

Impact:

- a concept that matters structurally adds unnecessary cognitive cost pedagogically

Recommended direction:

- translate the first-run student explanation into plain language first
- move overlay terminology lower on the page or into an expandable section

## Researcher / Data Scientist Journey

### Entry Simulation

Likely route:

1. Home
2. Choose Your Role
3. Researchers & Data Scientists
4. Core Data Science Workflow
5. Backbone Protocol
6. Examples
7. Skill Library

### What Works

- this role now has a clearer identity than the older `Data Scientists` label alone
- the core sequence is visible
- the backbone and examples are meaningfully connected

### P0: Practitioners Still Have To Decide Between Workflow, Backbone, Examples, And Skills Too Soon

All four destinations are reasonable, but their relationship is still not obvious enough on first pass.

A practitioner can ask:

- Do I read the workflow first?
- Do I need the backbone before the workflow?
- Are examples optional or required?
- Do I install skills first or understand the system first?

Impact:

- users who are ready to execute still have to stop and model the documentation structure

Recommended direction:

- create one explicit practitioner sequence:
  workflow first, backbone second, examples third, skills fourth
- express that sequence on the practitioner page and possibly on quickstart

### P1: The Practitioner Page Has A Small Hierarchy Gap

`What Changes In Practitioner Mode` currently introduces the concept but then the concrete list of relevant items appears under a later section.

Impact:

- the page reads slightly flatter than the student and manager pages

Recommended direction:

- tighten the hierarchy so the role-specific difference and the relevant tools feel like one unit

## Manager Journey

### Entry Simulation

Likely route:

1. Home
2. Choose Your Role
3. Managers
4. Lab Manager Agent
5. Research OS Template
6. Project Management / Managing Data Science
7. Examples

### What Works

- the manager role is now much more concrete
- the Lab Manager Agent page gives a clear portfolio-level concept
- the Research OS template adds practical structure

### P0: The Manager Path Still Has Overlapping Mid-Level Pages

A manager still encounters multiple pages that feel adjacent:

- Project Management
- Managing Data Science
- Lab Manager Agent
- Research OS Template

These are all defensible, but the difference among them is not yet sharp enough in the path itself.

Impact:

- managers can still feel like they are comparing near-duplicates
- the system risks reading like layered notes rather than one guided route

Recommended direction:

- make the manager page define one recommended reading order
- explicitly label each linked page by purpose:
  concept, operating model, template, or example

### P1: The Manager Role Promise Is Stronger Than The Supporting Proof

The manager pages describe a compelling coordination system, but the site still has fewer visible concrete artifacts for managers than for the analytical backbone.

Impact:

- the manager lane feels promising, but slightly less proved-out than the practitioner lane

Recommended direction:

- surface one or two more concrete manager artifacts or snapshots near the role page and Lab Manager page

## Design Findings

### P0: The Homepage Still Needs More Evidence, Not More Explanation

The structural routing is better, but the page still leans on explanation more than proof.

Best next move:

- show one real artifact preview, dashboard snapshot, workflow trace excerpt, or example card that feels undeniably practical

### P1: Some Role Pages Are Stronger Structurally Than Visually

The role pages are clearer now, but they still read more like well-organized documentation than distinctive landing pages.

Best next move:

- use one shared visual pattern for the three role pages so the user feels they are moving through one designed system

### P1: Legacy Material Still Creates Search And Discovery Noise

Even after cleanup, orphaned and companion material remains large enough that search and direct links can still bypass the best route.

Best next move:

- decide what remains a supported companion layer
- decide what becomes clearly archived or reference-only

## Highest-Leverage Next Changes

1. Define one recommended sequence per role and repeat it consistently across homepage, quickstart, and role pages.
2. Make practitioner routing more opinionated so workflow, backbone, examples, and skills no longer feel like equal first choices.
3. Simplify the manager route by labeling each manager page by job-to-be-done.
4. Add visible proof artifacts to the homepage and manager lane.
5. Decide which remaining legacy pages are supported companions and which should move toward archive status.
