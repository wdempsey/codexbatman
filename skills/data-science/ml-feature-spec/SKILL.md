---
name: ml-feature-spec
description: Write a machine learning feature spec (PRD) and break it into independently-trackable GitHub issues using vertical slices. Use when a data scientist needs to propose an ML feature to a software team, write a spec that engineers can review and track, or plan an ML project as a sequence of shippable slices. Combines to-prd and to-issues patterns adapted for ML. Adapted from Matt Pocock's to-prd and to-issues skills (github.com/mattpocock/skills).
category: data-science
status: active
role_compatibility:
  - data scientist
  - practitioner
---

# Skill: ML Feature Spec

## Credit

Adapted from Matt Pocock's [`/to-prd`](https://github.com/mattpocock/skills/blob/main/skills/engineering/to-prd/SKILL.md) and [`/to-issues`](https://github.com/mattpocock/skills/blob/main/skills/engineering/to-issues/SKILL.md) skills. His versions target software engineers writing feature specs for general-purpose software. This version adapts those patterns for ML features: the user stories, implementation decisions, and vertical slice structure are specific to the data-in → model-out → monitoring pipeline that ML features follow.

## When to use this

Use when:
- A practitioner has completed a proof-of-concept analysis and needs to propose productionizing the model
- A data scientist needs to write a spec that an engineering team can review, estimate, and track
- A manager needs to understand the work breakdown before giving a go/no-go on resourcing

Do NOT use for:
- Internal analysis planning (use `analysis_plan.md` in the backbone protocol instead)
- Exploratory prototypes that aren't heading toward production

## Two outputs

This skill produces two things:

1. **The ML Feature Spec** — a structured document describing the problem, the model approach, the interface contract, and what's out of scope
2. **Vertical slice issues** — independently-grabbable GitHub issues, each representing a thin end-to-end slice of the ML feature

## Step 1: Synthesize the spec

Do NOT interview the practitioner. Synthesize from what's already in the session context — the problem frame, data card, experiment log, model card, and any prior discussion.

Use the project's domain vocabulary from `DATA_CONTEXT.md` if it exists.

### ML Feature Spec template

```markdown
# ML Feature Spec: [Feature Name]

## Problem Statement
[What decision or user need does this model support? From the user/stakeholder perspective, not the technical framing.]

## Proposed Model
[What model type, trained on what data, producing what output? One paragraph.]

## Input Contract
[What features does the model expect at inference time? Where do they come from in the production system?
Include schema — column names, types, expected ranges.]

## Output Contract
[What does the model return? Format, type, range. Example: {"prediction": 0|1, "probability": float in [0,1]}]

## Validation Criteria
[What performance threshold is required before deployment? Which metric? Measured on what population?
Who signs off — the data scientist, the PM, the clinical/domain expert?]

## User Stories
[Numbered list. Each: "As a [role], I want [capability], so that [benefit]."]

1. As a [role], I want ...
2. As a [role], I want ...

## Implementation Decisions
[Key decisions made during the proof-of-concept that the engineering team should know:
- Why this metric (not accuracy, not F1)
- Why this threshold (clinical policy? business rule?)
- Why these features (prediction-time availability, leakage review outcome)
- Model serialization format
- Retraining trigger (when does the model need to be retrained?)]

## Testing Decisions
[What will be tested and how:
- Unit tests: which pipeline functions, which contracts
- Integration tests: inference endpoint input/output contract
- NOT tested: model accuracy — that's in the validation criteria above]

## Monitoring Requirements
[What needs to be monitored in production:
- Prediction distribution drift
- Feature distribution drift  
- False negative rate at current threshold
- Subgroup performance flags]

## Out of Scope
[What this spec explicitly does not cover.]
```

Show the spec draft to the practitioner. Ask: does this match your intent? Is anything missing or wrong? Iterate once before moving to issues.

## Step 2: Break into vertical slices

Each issue is a **thin vertical slice** — a narrow path through ALL layers end-to-end, demonstrable on its own. Not a layer-by-layer breakdown.

### ML feature vertical slice layers

```
Data ingestion → Feature engineering → Model training → Inference API → Monitoring
```

Each slice should touch as many layers as needed to be independently verifiable. Prefer many thin slices over few thick ones.

### Classifying slices

Each slice is either:
- **HITL** (Human-in-the-loop): requires a decision, review, or sign-off from a person
- **AFK** (Away-from-keyboard): can be implemented and merged without human interaction

Examples:
- "Define input contract and get sign-off from engineering team" → **HITL**
- "Implement feature pipeline with unit tests" → **AFK**
- "Deploy inference endpoint to staging" → **AFK**
- "Validate model performance against criteria — go/no-go sign-off" → **HITL**

### Typical slice breakdown for an ML feature

Present as a numbered list. For each slice: title, HITL/AFK, blocked-by, what it delivers.

```
1. [HITL] Define input/output contract — agree on schema with engineering team
2. [AFK]  Implement feature pipeline with schema contract tests
3. [AFK]  Serialize trained model and write model card
4. [HITL] Validate performance against criteria — go/no-go
5. [AFK]  Build inference wrapper with contract tests
6. [AFK]  Deploy inference endpoint to staging
7. [AFK]  Add prediction distribution monitoring
8. [HITL] Production sign-off — threshold decision, population scope review
```

Ask the practitioner:
- Does the granularity feel right?
- Are the dependency relationships correct?
- Should any slices be merged or split?

## Step 3: Publish issues

For each approved slice, create a GitHub issue using this template:

```markdown
## What to build
[One paragraph: end-to-end behavior of this slice, not layer-by-layer steps.]

## Acceptance criteria
- [ ] [Verifiable criterion 1]
- [ ] [Verifiable criterion 2]
- [ ] [Verifiable criterion 3]

## Blocked by
[Issue reference, or "None — can start immediately"]
```

Publish in dependency order (blockers first). Apply a `needs-triage` label if the team uses one.
