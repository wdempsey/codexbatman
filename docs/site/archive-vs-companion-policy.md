# Archive Vs Companion Policy

**This page defines how older, inherited, and reference-heavy documentation should be classified in Codex Batman.**

The goal is not to delete useful material prematurely. The goal is to make the status of each page legible so users know whether they are reading the current operating path, a still-supported companion reference, or an older page that should no longer shape the main journey.

## The Three Status Levels

### Canonical

Canonical pages define the active Codex Batman operating system.

These pages should:

- appear in the main navigation or be directly linked from major landing pages
- match the current repository mission and terminology
- be kept current when workflows or structure change
- be the preferred destination for first-run users

Examples of canonical material:

- role pages
- quickstart
- core data science workflow pages
- backbone protocol pages
- manager workflow pages that define the current operating model
- examples that demonstrate the current backbone

### Companion

Companion pages are still useful, but they are not the main route through the site.

These pages may:

- provide older build stories or implementation narratives
- cover adjacent workflows that are still helpful but not central
- offer general AI foundations that support the main system
- remain outside the primary newcomer path

Companion pages should:

- say clearly what they are for
- point back to the canonical route when relevant
- preserve useful reference value without pretending to be the primary workflow

Examples of companion material:

- legacy workflow stories
- general chatbot habits and tooling guides
- specialized case studies such as tax workflow
- longer-form downloads and setup references

### Archive Candidate

Archive-candidate pages are pages that may still contain useful ideas, but should no longer guide users unless they are revised or intentionally retained as reference-only material.

Signals that a page may be an archive candidate:

- it uses outdated branding or repo references
- it duplicates a canonical page without adding distinct value
- it assumes an older architecture that is no longer the active system
- it is hard to maintain and not central to current user journeys
- it is discoverable mainly by search or old links rather than intentional routing

Archive-candidate does not necessarily mean delete immediately. It means the page should be reviewed for one of three outcomes:

1. promote to canonical
2. keep as companion
3. retire or clearly archive

## Decision Rules

When deciding how to classify a page, use this order:

1. Does this page define the current operating model?
2. Would a first-time user be better served by a newer page?
3. Does this page add unique reference value that the newer page does not?
4. Is the page worth maintaining as the system evolves?

If the answer pattern is:

- yes, yes, yes, yes -> canonical
- no, yes, yes, maybe -> companion
- no, yes, little unique value, unlikely to maintain -> archive candidate

## Practical Handling Rules

### For Canonical Pages

- keep in nav or in obvious first-run routes
- update when workflows or terminology change
- prefer cross-links outward to companion references rather than the reverse

### For Companion Pages

- add a short `Start Here If` or equivalent status cue
- link back to canonical pages
- avoid presenting them as the default entry path

### For Archive Candidates

- do not expand them casually
- either add a clear archive/reference note or schedule them for consolidation
- avoid linking them from primary landing pages until their status is resolved

## Current Working Interpretation

In the current repository:

- role pages, quickstart, workflow, backbone, examples, and the active manager lane are canonical
- essentials, toolkit, downloads, and tax workflow are generally companion material unless a page is explicitly promoted
- duplicate or older architecture pages outside the main journey should be treated as archive candidates until reviewed

## What This Policy Does Not Do

This policy does not force immediate deletion, nav removal, or URL changes.

It gives maintainers a shared rule for future cleanup so the site can keep useful older material without confusing users about what is current.
