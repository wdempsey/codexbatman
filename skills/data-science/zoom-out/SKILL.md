---
name: zoom-out
description: Go up a layer of abstraction and map how an unfamiliar section of data science code fits into the broader system. Use when a data scientist is new to a codebase, needs to understand where a pipeline step connects to downstream consumers, or wants to know what depends on a model before modifying it. Adapted from Matt Pocock's zoom-out skill (github.com/mattpocock/skills).
category: data-science
status: active
role_compatibility:
  - data scientist
  - practitioner
---

# Skill: Zoom Out

## Credit

Adapted from Matt Pocock's [`/zoom-out`](https://github.com/mattpocock/skills/blob/main/skills/engineering/zoom-out/SKILL.md) skill. His original is a single instruction: "Go up a layer of abstraction. Give me a map of all relevant modules and callers, using the project's domain glossary." This adaptation adds data science-specific layers — the data flow from ingestion through features to inference — and the backbone artifact context that practitioners carry.

## What this skill does

When you're unfamiliar with a section of code — a feature pipeline you didn't write, a model inference wrapper someone else built, a data ingestion step you're about to modify — this skill tells Codex to stop going deeper and go broader instead.

It produces a map: what calls this? what does this call? where does the data come from and where does it go? what backbone artifacts describe the decisions made here?

Use it before modifying anything you don't fully understand. Modifying a feature transform without knowing what the downstream model expects is how you introduce silent failures.

## Invocation

In any session where you're looking at unfamiliar code, say:

```text
Zoom out. I don't know this part of the codebase well. Map the relevant modules,
callers, and data flow. Use the project's domain vocabulary. Check backbone
artifacts (data_card.md, model_card.md, experiment_log.md) for any documented
decisions about this area.
```

Or shorter:

```text
Zoom out — map this and its dependencies before we change anything.
```

## What Codex should produce

A concise map covering:

**1. What is this?**
One sentence naming the module/function/class using the project's domain vocabulary.

**2. Inputs**
Where does the data come from? Raw files? A feature store? An API? Another pipeline step? Include schema if it's in the data card.

**3. Outputs**
What does this produce? Who consumes it? If it's a feature transform: which model depends on these features? If it's a model: which inference endpoint calls it? If it's a pipeline step: what comes next?

**4. Callers**
Which scripts, notebooks, or services call this directly? Are there scheduled jobs? API handlers?

**5. Backbone artifact references**
Which backbone files document decisions relevant to this area?
- `data_card.md` — does it mention this feature or transform?
- `model_card.md` — does it specify input feature expectations?
- `experiment_log.md` — are there logged experiments that changed this?
- `analysis_plan.md` — was this step planned or improvised?

**6. What breaks if this changes?**
List the downstream dependencies that would need updating if the interface, schema, or behavior of this module changes.

## Example output

```
Module: cardiac_features.transform()

What: Produces the 13 post-stress-test features expected by CardiacRiskModel v1.

Inputs: Raw Cleveland Heart Disease CSV (303 rows, 14 columns including target).
        Schema documented in data_card.md §3.

Outputs: DataFrame with 13 columns (see data_card.md §4 for feature list).
         Consumed by: train_model.py, inference_api.py /predict endpoint.

Callers:
  - scripts/train_model.py (line 42)
  - api/predict.py (line 18)
  - tests/test_features.py (3 test cases)

Backbone artifacts:
  - data_card.md §3: leakage review documents why exang/oldpeak/thal are included
  - model_card.md §2: specifies expected input schema for v1
  - experiment_log.md run_003: documents switch from mean to median imputation for ca

What breaks if this changes:
  - inference_api.py /predict — expects exactly 13 features in this order
  - CardiacRiskModel.predict() — trained on this exact schema; feature order matters
  - test_features.py — 3 schema contract tests would fail if columns change
```

## When NOT to use this

- You wrote this code recently and know it well — just proceed
- You're doing exploratory analysis in a notebook that doesn't connect to production code
- The codebase has no structure yet — zoom-out needs something to map

If backbone artifacts are missing (no `data_card.md`, no `model_card.md`), zoom-out will note the gaps. That's useful information — it means decisions were made undocumented and the area carries higher risk.
