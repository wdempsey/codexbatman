# Problem Framing

Problem framing is the first analytical gate in the canonical data science workflow.

Its purpose is to define the problem before data work begins.

This phase is intentionally restrictive.

If the problem is poorly framed, later rigor does not repair it.

## Why This Workflow Matters

The most expensive modeling mistakes often begin as framing mistakes:

- the task is descriptive but treated as predictive
- the metric is named but not operationalized
- the stakeholder decision is unclear
- data requirements are implied instead of stated
- causal language appears without identification logic

This workflow exists to make those errors visible before audit or modeling.

The broader rationale is documented in [Goals of the Data Science Layer](goals.md) and [Data Science Layer Blueprint](blueprint.md).

## Common Mistakes

- Assuming the task is predictive by default.
- Defining success with vague metrics such as “accuracy” or “better performance.”
- Skipping the decision context.
- Treating causal and predictive objectives as interchangeable.
- Listing data needs too loosely for later audit.
- Starting exploration before the framing artifact is reviewed.

## Step-by-Step Workflow

### 1. Classify the objective type

State whether the task is:

- predictive
- descriptive
- causal
- policy evaluation
- exploratory

If the answer is ambiguous, stop and surface the ambiguity.

### 2. Define the decision context

Codex should identify:

- who will use the result
- what decision it informs
- what action follows from the output
- what costs matter if the output is wrong

### 3. Define success metrics

Each metric should have:

- a name
- an operational definition
- a measurement window
- a threshold if relevant

### 4. Document constraints

This includes:

- timing
- interpretability
- fairness
- deployment context
- computational limits

### 5. Build a risk register

The framing artifact should name risks early, including:

- leakage risk
- proxy bias
- temporal misalignment
- feedback effects
- ethical risks

### 6. Define data requirements

State what the later audit must verify:

- variables needed
- time structure needed
- minimum sample assumptions
- external data dependencies
- identification assumptions where relevant

## Expected Artifacts

- Problem statement
- Objective type
- Decision context
- Success metrics section
- Constraints section
- Risk register
- Data requirements checklist

## How Codex Should Use The Skill

Codex should use `skills/data-science/problem-framing/SKILL.md` before any data audit, EDA, or modeling.

Codex should:

- force explicit definitions
- surface ambiguity instead of filling it silently
- require review before continuing
- produce a framing artifact that later phases can reference directly

Codex should not:

- jump to feature ideas
- suggest models prematurely
- treat framing as a conversational warm-up

## Run With Codex

```text
Use the problem-framing skill on this project description and produce the canonical framing artifact before we inspect the data.
```

```text
Run problem-framing in a strict mode. If the objective type is ambiguous, stop and explain why.
```

```text
Apply the problem-framing skill and give me the problem statement, decision context, success metrics, constraints, risks, and data requirements.
```
