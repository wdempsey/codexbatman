# Basic Classification — Execution Lens

Same project as the learning lens — cardiac risk classification on the Cleveland Heart Disease dataset — but without the coaching scaffolding. Codex moves through the gates directly, drafts artifacts for your review, and expects you to direct the exceptions.

Working through the learning path first? [See the learning lens →](learning.md) | Reviewing as a manager? [Manager lens →](manager.md)

---

## What a practitioner session looks like

<div style="font-family:'JetBrains Mono','Courier New',monospace;font-size:0.84rem;line-height:1.6;background:#0d1b2e;border-radius:10px;padding:1.2rem 1.4rem;margin:1.5rem 0;border:1px solid #1a2f4a;">
<div style="color:#3bc9db;margin-bottom:0.8rem;">$ codex run problem_frame.md --skill problem-framing</div>
<div style="color:#a6e3a1;margin-bottom:0.6rem;">Target: binary (0 = no disease, 1+ = disease present)<br>
Metric: ROC-AUC | Decision: cardiology referral triage<br>
Prediction time: DECISION REQUIRED — stress-test features available or not?<br>
→ Awaiting your call before proceeding.</div>
<div style="color:#3bc9db;margin-bottom:0.8rem;">You: post-stress-test — all 13 features available at prediction time.</div>
<div style="color:#a6e3a1;margin-bottom:0.6rem;">→ Prediction time confirmed. Leakage risk cleared for exang, oldpeak, slope, thalach, thal.<br>
→ problem_frame.md written. Ready for data-audit.</div>
<div style="color:#3bc9db;margin-bottom:0.8rem;">$ codex run data_audit.md --skill data-audit</div>
<div style="color:#a6e3a1;margin-bottom:0.6rem;">303 rows, 13 features, 165 positive (54.5%)<br>
ca: 4 missing → flag as unknown (ordinal, clinical meaning)<br>
thal: 2 missing → mode impute (categorical)<br>
No other missingness. Leakage: cleared (prediction time confirmed above)<br>
→ data_card.md written. Audit status: proceed.</div>
<div style="color:#3bc9db;margin-bottom:0.8rem;">$ codex run baseline.md --skill modeling</div>
<div style="color:#a6e3a1;">Split: 80/20 stratified, seed=42 → 242 train / 61 test<br>
Baseline: logistic regression, default threshold 0.5<br>
ROC-AUC: 0.87 | Sensitivity: 0.79 | Specificity: 0.88<br>
False negatives at 0.5: 12/61 test cases<br>
→ experiment_log.md entry 001 written. Baseline established.</div>
</div>

Three gates, three artifact updates. The prediction-time call at gate 1 is the kind of judgment that practitioners direct — Codex flags the ambiguity and waits, rather than guessing.

---

## Prompt to start

```text
Set up and execute a cardiac risk classification repository using the Codex Batman backbone.

Dataset: Heart Disease Cleveland UCI (UCI ML Repository, no login required)
Run `python examples/basic-classification/data/get_heart.py` to download heart.csv first.
Goal: predict presence of heart disease. Binary target (0 = no disease, 1+ = disease).
Decision context: cardiology referral triage (post-stress-test tool).
Metric: ROC-AUC.

Work in practitioner mode — be direct and artifact-oriented.
Do not skip workflow gates.
Start with project-bootstrap, then problem-framing and data-audit.
```

---

## The seven-gate sequence

1. Initialize with `project-bootstrap` — folder structure, backbone files, README stub
2. Draft `problem_frame.md` — binary target, ROC-AUC metric, prediction time, leakage scope
3. Run `data-audit` — missingness plan for ca and thal, class balance noted → `data_card.md`
4. Define split strategy in `analysis_plan.md` — stratified 80/20, seed locked, test set frozen
5. Fit logistic regression baseline; record ROC-AUC and confusion matrix at 0.5 threshold
6. Fit one or two justified candidate models (random forest, gradient boosting); compare ROC-AUC
7. Evaluate against framing: what's the false-negative rate? Should the threshold be lowered for clinical use?
8. Draft `model_card.md` — population scope, threshold recommendation, fairness flag for sex subgroup
9. Update `workflow_trace.md` and `PROJECT_STATE.md` before ending the session

Gates 1–4 are setup. Gates 5–7 are modeling. Gates 8–9 are documentation. The documentation gates are not optional — a model without a card isn't finished.

---

## What success looks like

The repo is review-ready when a manager can open `PROJECT_STATE.md` and answer: what decision this model supports, what population it was trained on, what the recommended threshold is and why, what the known failure modes are, and what should happen before any clinical deployment — all from the artifact files, without reopening the chat.

---

## Where To Go Next

- [Learning lens →](learning.md) — same project with attempt-before-answer coaching
- [Manager lens →](manager.md) — how a clinical stakeholder reviews these artifacts
- [Linear Regression — Execution Lens](../analytics-repo/execution.md) — the regression counterpart
- [Core Data Science Workflow](../../workflows/data-science/index.md)
