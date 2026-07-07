# Planning

Last updated: 2026-07-07

## Active: Skill Intake And Capability Matrix

- [x] Add `SKILL-STYLE.md` as the authoring and verification guide for folder-based skills.
- [x] Add `CAPABILITY-MATRIX.md` as the role x task-type intake map for current `SKILL.md` files.
- [x] Update skill metadata guidance to point to the new intake sources.
- [x] Run PR-1 flow audit for trigger collisions, progressive disclosure gaps, and identity-loader enforcement boundary.
- [x] Add `ask-codexbatman` as the cross-lane router skill.
- [x] Normalize `site-voice` frontmatter in PR-1.
- [x] Normalize legacy role aliases such as `practitioner` to `data scientist` in skill frontmatter.
- [ ] Track gradual command-style skill migration, archive, and keep decisions as cleanup proceeds.
- [x] Add eval-task scaffolding before admitting new skill imports.
- [ ] PR-2: decide deterministic enforcement for student identity/session-start config reads.
- [ ] PR-3: convert `evals/` scaffold into a runnable eval harness.

## Active: Repository Identity, Skills, And Workflow Architecture

- [x] Rewrite repository identity files around the Codex-native data science operating system.
- [x] Replace inherited MkDocs navigation with role-aware navigation.
- [x] Reorganize `skills/` into `data-science`, `manager`, and `overlays`.
- [x] Create folder-based manager workflow skills.
- [x] Create student tutoring overlays.
- [x] Establish the first-wave canonical data science skills.
- [x] Add workflow documentation pages for Project Bootstrap, Problem Framing, Data Audit, and Experiment Log.
- [x] Add role-aware overlays for student, practitioner, and manager delivery.
- [x] Restore top-level tabs while keeping Skill Library as the shared catalog hub and role pages as summary pages.
- [ ] Review the repository for duplicate or conflicting files, redundant workflow pages, and stale site language after the architecture changes.
- [ ] Decide whether to add a real `devlog/` directory and template or remove stale references to that system.

## Active: Homepage Redesign

- [x] Switch Material palette to indigo-inspired defaults.
- [x] Build custom four-section landing page flow.
- [x] Add initial transition effects and full-bleed sections.
- [x] Remove Tax Workflow from primary navigation.
- [x] Propose structural UI/UX pass for role routing and navigation in `docs/site/structural-ui-ux-pass-002.md`.
- [x] Move role selection earlier on the homepage and make role paths the dominant routing choice.
- [x] Replace homepage final section with user-centered next actions instead of internal site-review links.
- [ ] Tune hero background composition to avoid edge cutoff across common viewport sizes.
- [ ] Keep section 1 -> section 2 handoff smooth with gradient-only transition.
- [ ] Replace section 2 icon placeholders with final icon set.
- [ ] Replace section 3 media placeholders with final images and captions.
- [ ] Validate homepage appearance on mobile and tablet breakpoints.
- [ ] Decide and link final destination for "digital garden" CTA.

## Active: Site Alignment And UI Reset

- [ ] Decide the canonical public identity and URL strategy for this repo: `claudeblattman.com`, GitHub Pages, or a new domain aligned to Codex Batman.
- [ ] Audit and resolve stale cross-branding across `docs/`, `overrides/`, `README.md`, contact emails, analytics, newsletter hooks, and external links.
- [ ] Align deployment configuration (`mkdocs.yml`, `docs/CNAME`, GitHub Pages expectations) with the chosen public identity.
- [ ] Restore local verification by documenting or installing the repo build toolchain so `mkdocs build` runs successfully in a fresh environment.
- [x] Create a `Roles` landing page that routes students, researchers/data scientists, and managers.
- [x] Collapse role tabs under `Roles` and rename the practitioner nav label to `Researchers & Data Scientists`.
- [x] Move `Backbone Protocol` under `Workflow` and `Tooling Stack` under `Build` if the structural proposal is accepted.
- [x] Standardize student, researcher/data scientist, and manager role pages around one shared landing-page structure.
- [x] Fix broken About page asset paths for profile and tweet images.
- [ ] Run a full visual QA pass across primary nav pages after the next asset/link cleanup.
- [x] Compare the local homepage, role pages, and navigation against the live site and list exact content, branding, and UX mismatches.
- [x] Produce a prioritized UI redesign brief covering homepage visuals, navigation clarity, typography, imagery, and mobile/tablet behavior.
- [x] Produce a structural site review covering orphaned pages, duplicated explanation layers, and newcomer-path ambiguity before a full content pass.
- [x] Decide which remaining legacy sections stay as companion references versus move toward archive status after the cleanup pass.

## Active: Roadmap Execution

- [x] PR 1: Add Tooling Stack registry docs and nav.
- [x] PR 2: Add Backbone Protocol v0.1 docs and nav.
- [x] PR 3: Add minimal data science project template and template docs.
- [x] PR 4: Add `core-ml` skill pack and links.
- [x] PR 5: Add workflow-trace, trace-distillation, and handoff skills.
- [x] PR 6: Add Lab Manager workflow docs.
- [x] PR 7: Add Research OS templates and docs.
- [x] PR 8: Add Lab Manager and Project Manager skills.
- [x] PR 9: Add worked examples across learning, execution, and manager lenses.
- [x] PR 10: Add UI/UX standards and repo-local site review skills, using `UI_REDESIGN_BRIEF.md` and `SITE_STRUCTURE_REVIEW.md`.
- [x] PR 11: Run first site UI/UX pass and write `docs/site/ui-pass-001.md`.

## Active: Next Pass PR Sequence

- [ ] PR 19: Add a concrete analytics repo example with student and practitioner paths around the same standard ML pipeline.
- [ ] PR 20: Make the setup and quickstart path concrete for the first 10 minutes in the repo, including stronger student entry points.
- [ ] PR 21: Add proof artifacts across the homepage and role lanes so each audience sees a concrete output.
- [ ] PR 22: Run a focused UI/UX polish pass on homepage readability, spacing, and navigation weight.
- [ ] PR 23: Add an asset prompt pack and asset request workflow for future homepage and role-page visuals.
- [ ] Prepare a Claude audit handoff with agent-specific scope, constraints, and expected outputs.

## Backlog (Low Priority)

- [ ] Revisit advanced foliage/foreground transition inspired by Material once final artwork direction is locked.
