---
name: grill-with-codebase
description: Grilling session for a data scientist joining or working inside an existing software codebase. Builds a shared domain language between the data scientist and the engineering team, surfaces naming conventions and architectural decisions that affect the analysis, and documents key decisions as ADRs. Use before starting analysis on an unfamiliar codebase, before writing a feature engineering function that must match existing conventions, or when a data scientist needs to align their vocabulary with the engineering team. Adapted from Matt Pocock's grill-with-docs skill (github.com/mattpocock/skills).
category: data-science
status: active
role_compatibility:
  - data scientist
  - practitioner
---

# Skill: Grill With Codebase

## Credit

Adapted from Matt Pocock's [`/grill-with-docs`](https://github.com/mattpocock/skills/blob/main/skills/engineering/grill-with-docs/SKILL.md) skill. His version builds a shared domain language (`CONTEXT.md`) and ADRs for software engineers aligning on a domain model. This version adapts that pattern for data scientists who need to align with an engineering codebase before writing production data science code — the vocabulary is different (features, targets, pipelines, model versions) but the need is identical.

## The problem this solves

A data scientist joining a software team often speaks a different language from the engineering team. The engineers say "event stream"; the data scientist says "raw log." The engineers have a `UserProfile` object; the data scientist calls it "demographic features." The engineers version their APIs with semantic versioning; the data scientist calls their model "the new one."

This gap produces bugs, duplicated work, and features that can't be deployed because they assume a data schema the production system doesn't expose.

The fix is a grilling session that builds a shared `DATA_CONTEXT.md` — a glossary of the terms that appear in both the analysis code and the production system, resolved to single canonical definitions.

## What this skill does

Interview the data scientist relentlessly about the codebase they're working in until key terms, conventions, and decisions are pinned down. Explore the codebase to resolve questions where possible rather than always asking the practitioner.

One question at a time. Proposed answer included with each question. Waiting for confirmation before proceeding.

## What to build: DATA_CONTEXT.md

Create `DATA_CONTEXT.md` in the project root (or `docs/DATA_CONTEXT.md` if a `docs/` folder exists). This is a glossary only — no implementation details, no specs, no scratch notes.

```markdown
# Data Context

## Domain Terms

**[term]**: [one-sentence definition using the engineering team's vocabulary]

## Feature Conventions

**[feature name]**: [what it measures, where it comes from, which model version introduced it]

## Pipeline Conventions

**[convention]**: [what it means in this codebase]
```

Update `DATA_CONTEXT.md` inline as terms are resolved. Don't batch — capture as they happen.

## What to ask about

### Naming alignment

- What does the engineering team call the primary entity? (Customer? User? Patient? Account?)
- Does the data science code use the same term? If not, resolve it.
- What are the canonical names for the features that exist in both the feature store and the analysis notebooks?

### Data access

- Where does raw data come from? (database? S3? event stream? API?) What's the schema?
- What transformations have already been applied before the data scientist sees the data? (ETL? deduplication? PII removal?)
- Is there a feature store? If yes, what's the naming convention for features in it?

### Model conventions

- How are model versions tracked? (semantic versioning? experiment IDs? date stamps?)
- What's the canonical input schema that inference endpoints expect? Where is it documented?
- When a new model version ships, what does the engineering team need from the data scientist? (a serialized artifact? an API endpoint? a schema spec?)

### Deployment expectations

- Where does the model run in production? (batch job? real-time API? embedded in a service?)
- What format does the model output need to be in? (raw probability? binary class? structured dict?)
- Who owns the inference infrastructure — the data scientist, the engineering team, or both?

## When to write an ADR

Only when all three are true:
1. **Hard to reverse** — changing this decision later would require retraining a model, migrating a schema, or breaking a deployed API
2. **Surprising without context** — a future reader would wonder "why did they do it this way?"
3. **The result of a real tradeoff** — genuine alternatives existed and one was chosen for specific reasons

Example ADR triggers: binarizing a multi-class target, choosing ROC-AUC over accuracy, deciding to impute rather than drop, fixing a prediction-time feature set.

Place ADRs in `docs/adr/` using the format:
```
# ADR-[NNN]: [title]
Date: YYYY-MM-DD
Status: Accepted
Context: [what prompted this decision]
Decision: [what was decided]
Consequences: [what this enables and what it forecloses]
```

## Challenge fuzzy language

When the practitioner uses a term that conflicts with `DATA_CONTEXT.md` or the engineering team's vocabulary, call it out: "Your data card says 'patient age' but the feature store calls it `user_age_at_signup` — which is it?"

When the practitioner uses vague terms, propose a canonical definition: "You're saying 'the features' — do you mean the 13 post-stress-test clinical features, or the full raw dataset?"

Cross-reference with the codebase: if the practitioner states how something works, check whether the code agrees. Surface contradictions immediately.
