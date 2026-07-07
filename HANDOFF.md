# Handoff

## Current State

The repository has completed the first major architecture and docs wave:

- role-aware site navigation
- backbone protocol docs
- tooling stack docs
- project templates
- manager workflow docs
- examples across learning, execution, and manager lenses
- UI/UX standards and site-review skills
- first structural and light UI cleanup passes
- archive-vs-companion policy
- student repo bootstrap skill

The site is now coherent enough to audit seriously, but it still needs a stronger newcomer path, clearer proof artifacts, and a tighter UI pass.

As of 2026-07-07, skill-system work is moving through the intake sequence
defined by `SKILL-STYLE.md` and `CAPABILITY-MATRIX.md`. Use those files before
adding, importing, or deduplicating folder-based skills.

## Current Skill-System Priority

Next skill PR: PR-3 telemetry, eval harness, and `/improve-skill`.

Focus:

- turn `evals/` into a runnable harness
- define telemetry conventions for skill invocations, trigger misses, user corrections, and deviation logs
- add `/improve-skill` as a reflection pass that proposes diffs but never edits skills in place
- route proposed improvements through the PR-2 lifecycle gate and human review process
- keep command-style skill migration gradual and tracked in `planning.md`

## Highest-Priority Next PRs

Use `docs/site/next-pass-pr-roadmap.md` as the source of truth.

Priority order:

1. PR 19 - concrete analytics repo example with student and practitioner paths
2. PR 20 - concrete setup and quickstart path
3. PR 21 - proof artifacts across homepage and role lanes
4. PR 22 - UI/UX polish pass
5. PR 23 - asset prompt pack

## Critical Product Direction

The most important directional constraint is this:

- the student path must show how a learner builds the solution step by step without Codex simply giving away the answer
- the practitioner path should use the same backbone and standards, but Codex can do more of the work directly
- the difference is delivery style and scaffolding, not weaker standards for students

For the concrete repo example, use a standard Kaggle-style ML pipeline as the shared project shape:

- problem framing
- data audit
- train/test split
- baseline
- feature handling
- model comparison
- evaluation
- model card
- workflow trace

## Constraints

- do not touch deployment/domain strategy files such as `docs/CNAME` or `docs/robots.txt`
- leave `.cache/` alone
- prefer additive, reversible edits
- run `make docs` before closing each PR
- use one commit per PR
- do not broaden into a full redesign

## Claude Audit Request

Run two agents in parallel, then synthesize their findings into one short audit.

### Agent 1 - UI/UX

Focus:

- homepage readability
- hero image legibility
- spacing and section transitions
- page scannability
- navigation weight
- mobile / narrow viewport behavior

Stay on task:

- do not propose a total redesign
- do not invent new dependencies
- prefer MkDocs Material-native improvements
- prioritize the highest-traffic pages first

Pages to inspect:

- `docs/index.md`
- `docs/quickstart.md`
- `docs/setup/index.md`
- `docs/students/index.md`
- `docs/data-scientists/index.md`
- `docs/managers/index.md`
- `docs/examples/index.md`
- `docs/roles/index.md`

Expected output:

- 5-10 highest-priority UI/UX issues
- minimal fixes recommended
- issues that should wait until after content changes

### Agent 2 - Content And Flow

Focus:

- newcomer path clarity
- student flow
- practitioner flow
- manager flow
- proof of utility
- unclear or duplicated explanations
- missing "do this next" guidance

Stay on task:

- do not rewrite the whole site
- do not debate architecture that is already settled
- prioritize flow, clarity, and trust over line editing

Pages to inspect:

- `docs/index.md`
- `docs/quickstart.md`
- `docs/setup/index.md`
- `docs/roles/index.md`
- `docs/students/index.md`
- `docs/data-scientists/index.md`
- `docs/managers/index.md`
- `docs/examples/index.md`
- `docs/backbone/index.md`

Expected output:

- critical missing elements
- broken or weak flow points by audience
- highest-value next edits
- confirmation that student vs practitioner direction remains aligned

## Suggested Claude Prompt

Use this prompt to keep the Claude audit focused:

```text
You are auditing the codexbatman repository as a Codex-native data science operating system.

Read HANDOFF.md and docs/site/next-pass-pr-roadmap.md first.

Start two agents:
1. one focused only on UI/UX
2. one focused only on content and user flow across students, practitioners, and managers

Constraints:
- stay focused on the next-pass priorities in the handoff
- do not propose a full redesign
- do not broaden into deployment or domain strategy
- keep recommendations additive and reversible
- distinguish clearly between issues that block PR 19-23 and issues that can wait

Then synthesize:
- top findings
- recommended PR order confirmation or changes
- concrete warnings before implementation
```

## Verification Status

Most recent local site checks:

- `make docs` passes
- `mkdocs serve` works locally
- the current site is reviewable at `http://127.0.0.1:8000/codexbatman/`

## Immediate Next Action

Begin PR 19.
