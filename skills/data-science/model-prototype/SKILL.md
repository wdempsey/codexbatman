---
name: model-prototype
description: Build a quick throwaway model to test a specific hypothesis before committing to the full workflow. Use when you need to answer a narrow question — is this problem learnable? does this feature carry signal? is this architecture worth pursuing? — without producing a full experiment log entry. The output is a clear answered/rejected note, not a deployable model. Adapted from Matt Pocock's prototype pattern for data science.
category: data-science
status: active
stage: modeling
role_compatibility:
  - student
  - data scientist
inputs:
  - specific question to answer
  - minimal dataset or data subset
  - proposed feature set or architecture
outputs:
  - answered/rejected note
  - recommendation for whether to pursue in full workflow
  - nothing else — no artifact files, no experiment log entry unless explicitly requested
depends_on:
  - problem-framing
  - data-audit
recommended_next:
  - modeling
  - experiment-log
---

# Skill: Model Prototype

## Purpose

Answer a specific question quickly without polluting the workflow with a half-formed experiment.

A model prototype is throwaway work. It exists to test a hypothesis in the smallest way possible and produce a clear yes/no. If the answer is yes, the work gets properly recorded in the workflow. If the answer is no, the prototype is discarded cleanly without cluttering the experiment log.

Adapted from Matt Pocock's `prototype` pattern — build to learn, not to deploy.

## When To Invoke

Use a prototype when:

- you want to know if a problem is learnable before investing in a full feature pipeline
- a new feature seems promising but you want to check its signal value quickly
- you're unsure whether a modeling family (linear vs. tree vs. neural) is worth the overhead
- a student wants to see what happens before understanding why

Do NOT use a prototype when the goal is to establish a formal baseline. That belongs in `modeling` with a full `experiment_log.md` entry.

## How To Run A Prototype

**1. State the hypothesis**
Write one sentence: "I believe that [X] will [predict/improve/reduce] because [Y]."

This is not optional. A prototype without a hypothesis is just random exploration.

**2. Define minimum viable setup**
- Use at most 20% of the full feature set
- Use a simple model (logistic regression, single decision tree, linear regression)
- Use a fast train/test split — no cross-validation needed for a prototype
- No preprocessing beyond what's strictly required to run

**3. Run and observe**
Note the metric. Note whether the result is better than chance, better than a simple rule, or worse than expected.

**4. Answer the hypothesis**
One paragraph:
- Was the hypothesis confirmed or rejected?
- What does that imply for the full workflow?
- Should this be pursued as a proper experiment?

## Output

```
Hypothesis: [one sentence]
Setup: [model, features used, data subset]
Result: [metric value]
Verdict: confirmed / rejected / inconclusive
Recommendation: [proceed to full experiment / discard / adjust hypothesis]
```

No artifact files. No experiment_log entry. If the prototype confirms a promising direction, hand off to `modeling` to run it properly.

## What A Prototype Is Not

A prototype is not a baseline. A baseline is a formal artifact — it has a fixed split, a seed, a logged metric, and it exists for the life of the project. A prototype is a question with a quick answer. It does not set a performance floor; the proper baseline does that.

A prototype is not a reason to skip the workflow gates. If a prototype reveals that the problem is learnable, the correct response is to run the full workflow — not to extend the prototype into a deployment.
