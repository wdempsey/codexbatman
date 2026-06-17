# Next Pass PR Roadmap

This page turns the current review into the next focused PR sequence.

The goal is to make Codex Batman easier to start, easier to trust, and easier to navigate without drifting into a broad redesign.

## Why These PRs Exist

The current site already has the right architecture:

- role-aware entry points
- a shared workflow backbone
- examples across lenses
- manager and artifact layers

What is still missing is a clearer newcomer path and stronger proof that the system produces useful work for each audience.

These PRs target the highest-leverage gaps first.

## PR 19 - Concrete Analytics Repo Example

### Goal

Add one canonical example of a real analytics repo built around a standard supervised ML workflow.

This PR should become the clearest answer to:

> What does a real Codex Batman data science project look like?

### Core Direction

Use one shared project scenario based on a standard Kaggle-style analysis workflow:

- tabular dataset
- target definition
- train/test split
- baseline
- feature handling
- model comparison
- evaluation
- model card
- workflow trace

The same project should be shown through two execution styles:

- student path: step-by-step, attempt-before-answer, Codex scaffolds but does not simply give the solution
- practitioner path: shorter sequence, more delegation to Codex, stronger emphasis on artifact discipline and decision quality

### Deliverables

- expand or add a canonical example page under `docs/examples/`
- make the student sequence explicit
- make the practitioner sequence explicit
- link the repo example from `quickstart`, `students`, and `data-scientists`
- ensure the example reinforces the shared backbone rather than becoming a side system

### Constraints

- keep it documentation-first
- no heavy codebase buildout
- no dataset download automation
- avoid textbook exposition
- make the difference between student and practitioner be interaction style, not different standards

## PR 20 - Concrete Setup And Quickstart Path

### Goal

Turn setup and quickstart into a true first-10-minutes path.

### Problems To Fix

- `quickstart` is still too installation-heavy
- the student repo bootstrap path is still not surfaced strongly enough
- the first action after install is still too abstract

### Deliverables

- tighten `docs/quickstart.md`
- tighten `docs/setup/index.md`
- strengthen links to `repo-bootstrap-student`
- add one recommended sequence per role
- add a blunt "if you only do one thing next" line on the key entry pages

### Constraints

- preserve current information architecture
- keep the path short and scannable
- do not turn quickstart into a long reference page

## PR 21 - Proof Artifacts Across Lanes

### Goal

Show concrete outputs for students, practitioners, and managers.

### Problems To Fix

- homepage proof is currently manager-heavy
- artifact-first value is still too abstract for students and practitioners

### Deliverables

- add a student-facing proof artifact example
- add a practitioner-facing proof artifact example
- keep the manager dashboard proof artifact
- surface these on the homepage and relevant role pages
- prefer existing repo-native artifacts, screenshots, or small mock artifact previews

### Constraints

- no large visual redesign
- no custom JavaScript
- keep assets minimal and reversible

## PR 22 - UI/UX Polish Pass

### Goal

Run a restrained visual pass after the structural content issues above are improved.

### Problems To Fix

- homepage hero image competes with text
- there is too much dead space after the hero in some views
- quickstart and role pages still feel denser than they should
- internal audit/build pages are visually too prominent in navigation

### Deliverables

- improve homepage hero readability
- tighten section spacing and transitions
- improve opening summaries and scannability on key pages
- reduce visible nav weight where possible without large restructuring
- validate desktop and narrower in-app browser views

### Constraints

- prefer Material-native patterns
- avoid heavy CSS
- no custom JavaScript
- preserve the current site identity

## PR 23 - Asset Prompt Pack

### Goal

Create the prompt pack and request workflow needed for new visuals.

### Why This Is Separate

Codex can add assets directly when the asset is simple, illustrative, or bitmap-first.

Examples:

- concept art
- diagram-like illustrations
- artifact mockups
- visual placeholders

This is usually enough for homepage and role-page support art.

What still benefits from a separate prompt pack:

- when the style needs to stay consistent across multiple assets
- when another model or teammate may generate the images
- when we want reusable prompts instead of one-off requests

### Deliverables

- a reusable prompt pack for homepage, student, practitioner, and manager visuals
- guidance on when to generate directly in Codex versus request externally
- recommended aspect ratios and usage notes

### Constraints

- documentation only unless a specific asset request is approved
- keep prompts aligned with the site's current visual direction

## Recommended Order

1. PR 19
2. PR 20
3. PR 21
4. PR 22
5. PR 23

This keeps structure ahead of polish and keeps prompts ahead of any larger art request wave.
