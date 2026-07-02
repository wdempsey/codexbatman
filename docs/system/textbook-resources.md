# Textbook Resources

You're mid-workflow. Codex introduces cross-validation, and you've never seen it before. What do you do?

Codexbatman has a resource layer for exactly this: method skills that pause the workflow, teach the concept, and hand you back to where you were. The canonical textbook behind them is *An Introduction to Statistical Learning* (ISLR) — freely available at [statlearning.com](https://www.statlearning.com/).

This page shows you how to use it.

---

## Where the skills live

The [Skill Library](../setup/skill-reference.md) has two sections that matter here:

**Methods Skills** — one skill per ML technique. Each one teaches the method in context, references the ISLR chapter, and returns you to the workflow gate where you need it.

**Textbook Resources** — the `islr-resource` skill is a chapter router. It maps ISLR chapters to the method skills in this repo, so Codex knows which skill to invoke when you hit a method you haven't seen.

---

## The chapter map

| ISLR Chapter | Topic | Codexbatman Skill | StatQuest video |
|---|---|---|---|
| Ch. 3 | Linear Regression | `linear-regression` | [Linear Regression, Clearly Explained](https://www.youtube.com/watch?v=nk2CQITm_eo) |
| Ch. 4 | Classification — logistic regression, ROC | *not yet built — taught inline* | [Logistic Regression](https://www.youtube.com/watch?v=yIYKR4sgzI8) · [ROC and AUC](https://www.youtube.com/watch?v=4jRBRDbJemM) |
| Ch. 5 | Resampling — cross-validation, bootstrap | `cross-validation` | [Cross Validation](https://www.youtube.com/watch?v=fSytzGwwBVw) |
| Ch. 6 | Regularization — ridge, lasso, elastic net | `ridge-regression`, `lasso` | [Ridge (L2)](https://www.youtube.com/watch?v=Q81RR3yKn30) · [Lasso (L1)](https://www.youtube.com/watch?v=NGf0voTMlcs) |
| Ch. 8 | Tree-based methods — random forests, boosting | `random-forest`, `gradient-boosting` | [Random Forests Pt 1](https://www.youtube.com/watch?v=J4Wdy0Wc_xQ) · [Gradient Boost Pt 1](https://www.youtube.com/watch?v=3CC4N4z3GJc) |

Chapters 7, 9, 12 (splines, SVMs, unsupervised) are mapped in the skill but method skills for them are not yet built. When Codex encounters one of these chapters — or Chapter 4, whose classification methods sit on the primary student path — it will explain the concept inline rather than routing to a dedicated skill.

The videos are by [StatQuest with Josh Starmer](https://statquest.org/) — free on YouTube, linked here with attribution (not affiliated with this repo). The full topic index is at [statquest.org/video-index](https://statquest.org/video-index/). Watching the video *before* the workflow gate is the fastest way to build intuition; the ISLR chapter is the reference you go back to.

---

## How to ask for a textbook explanation

You don't need to know which skill to call. In tutor mode, you can ask directly:

```text
I don't understand cross-validation. Can you explain it before we continue?
```

Codex will pause the workflow, invoke the `cross-validation` skill, teach the concept (with the ISLR Chapter 5 reference), and then return you to the gate where CV applies.

You can also be more specific:

```text
I've seen the term "k-fold cross-validation" but I don't know what k means or how to choose it.
Can you explain and then we'll continue.
```

Or ask for the textbook anchor explicitly:

```text
Where does ISLR cover this? I want to read the chapter tonight.
```

Codex will cite the chapter and section, and provide the canonical reference:

> James, G., Witten, D., Hastie, T., Tibshirani, R. (2023). *An Introduction to Statistical Learning with Applications in Python.* Springer. Free at [statlearning.com](https://www.statlearning.com/).

---

## What happens in tutor mode

When you're running tutor mode and hit a workflow gate that introduces a new method, this is the sequence:

1. **Codex pauses** the gate and signals that a new method is about to be used
2. **You decide** whether to learn it now or proceed directly
3. **If you ask to learn it**: Codex invokes the method skill, walks through the concept, and asks you to demonstrate understanding before moving on
4. **Codex returns** to the gate and continues — the method is now anchored to a workflow decision you made, not just explained in the abstract

The method skill handles the teaching. The workflow skill handles the execution. They don't overlap.

---

## An example: cross-validation at the modeling gate

You're at the modeling gate for a regression project. Codex suggests using k-fold cross-validation instead of a single train/test split. You haven't seen this before.

<div style="font-family:'JetBrains Mono','Courier New',monospace;font-size:0.83rem;line-height:1.65;background:#0d1b2e;border-radius:10px;padding:1.25rem 1.4rem;margin:1.4rem 0;border:1px solid #1a2f4a;">
<div style="color:#7d90a8;font-size:0.72rem;letter-spacing:0.06em;margin-bottom:0.9rem;text-transform:uppercase;">Tutor Mode — Modeling Gate</div>

<div style="margin-bottom:0.9rem;">
<div style="color:#3bc9db;margin-bottom:0.3rem;">Codex</div>
<div style="color:#cbd5e1;">Before we run the model, I want to use 5-fold cross-validation to choose between logistic regression and random forest. Have you worked with CV before, or should we cover it first?</div>
</div>

<div style="margin-bottom:0.9rem;">
<div style="color:#a6e3a1;margin-bottom:0.3rem;">You</div>
<div style="color:#cbd5e1;">Let's cover it first.</div>
</div>

<div style="margin-bottom:0.9rem;">
<div style="color:#3bc9db;margin-bottom:0.3rem;">Codex</div>
<div style="color:#cbd5e1;">Cross-validation answers a question training error can't: how well does the model generalize to data it hasn't seen?<br><br>The basic idea: split your training data into k groups. Train on k–1 of them, evaluate on the remaining one. Repeat k times so each group gets a turn as the test set. Average the scores.<br><br>This is ISLR Chapter 5. The key insight is that a single train/test split gives you one noisy estimate — it depends on which observations ended up where. k-fold averages that noise away.</div>
</div>

<div style="margin-bottom:0.9rem;">
<div style="color:#f4a261;margin-bottom:0.3rem;">Codex asks</div>
<div style="color:#cbd5e1;">Before we continue: if I impute missing values on the full dataset and then run CV, is that correct or is something wrong?</div>
</div>

<div style="margin-bottom:0.9rem;">
<div style="color:#a6e3a1;margin-bottom:0.3rem;">You</div>
<div style="color:#cbd5e1;">That leaks test-fold information into the training step.</div>
</div>

<div style="color:#3bc9db;margin-bottom:0.3rem;">Codex</div>
<div style="color:#cbd5e1;">Exactly. Imputation has to happen inside each fold — fitted only on the training portion of that fold. We use a Pipeline to enforce this. Ready to continue to the modeling gate?</div>
</div>

---

## What the method skill produces

After the explanation, Codex anchors the concept to the actual workflow decision:

- Which variant to use (k-fold, LOOCV, validation set) and why — documented in `analysis_plan.md`
- A Pipeline snippet that puts preprocessing inside the fold
- A clear statement of what CV is for (model selection) vs. what the held-out test set is for (final honest estimate)

You don't get a standalone lecture that floats free of the project. You get an explanation followed immediately by "here's how we apply this to your dataset."

---

## What's not covered yet

Methods without a dedicated skill (ISLR Ch. 4, 7, 9, 12) are taught inline when they come up, without the structured skill scaffolding. If you want to add a method skill for one of these, see [Building Skills](building-skills.md).

---

## More free resources

ISLR is the canonical anchor, but three other free resources cover gaps it doesn't:

- [**Python Data Science Handbook**](https://jakevdp.github.io/PythonDataScienceHandbook/) (Jake VanderPlas) — if the *Python itself* is what's blocking you (NumPy, pandas, sklearn basics), not the statistics. Chapters 2–3 cover NumPy and pandas; chapter 5 covers the sklearn patterns these workflows use. Free online; text CC-BY-NC-ND, code MIT.
- [**Causal Inference: The Mixtape**](https://mixtape.scunning.com/) (Scott Cunningham) — when a project raises a *why* question instead of a *what* question. Prediction models don't answer causal questions; chapters 1–4 explain the potential-outcomes framing. Free official web edition, Yale University Press.
- [**The Elements of Statistical Learning**](https://hastie.su.domains/ElemStatLearn/) (Hastie, Tibshirani, Friedman) — the theory-depth companion to ISLR, for when the ISLR chapter feels too gentle. Free PDF from the authors' site.

## See also

- [Skill Library](../setup/skill-reference.md) — full catalog of method and resource skills
- [Building Skills](building-skills.md) — how to add a method skill for a chapter not yet covered
- [Cross-Validation Skill](https://github.com/wdempsey/codexbatman/tree/main/skills/methods/cross-validation) — the most complete example of a method skill with ISLR anchoring
