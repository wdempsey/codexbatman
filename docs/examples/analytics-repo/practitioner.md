# Analytics Repo Example — Practitioner Path

Same project as the student path — housing-price prediction on the Ames dataset — but without the coaching scaffolding. Codex moves through the gates directly, drafts artifacts for your review, and expects you to direct the exceptions.

Already on the student path? [See the student version →](student.md) or [see a real coaching exchange →](live-session.md)

---

## What a practitioner session looks like

This is the kind of exchange you get in practitioner mode. No pedagogical framing — just gates, artifacts, and forward progress.

<div style="font-family:'JetBrains Mono','Courier New',monospace;font-size:0.84rem;line-height:1.6;background:#0d1b2e;border-radius:10px;padding:1.2rem 1.4rem;margin:1.5rem 0;border:1px solid #1a2f4a;">
<div style="color:#3bc9db;margin-bottom:0.8rem;">$ codex run problem_frame.md --skill execution-mode</div>
<div style="color:#a6e3a1;margin-bottom:0.6rem;">Target: SalePrice | Metric: RMSE | Prediction time: pre-listing<br>
Risks flagged: MoSold/YrSold leakage, LotFrontage missingness<br>
→ problem_frame.md written. Ready for data-audit.</div>
<div style="color:#3bc9db;margin-bottom:0.8rem;">$ codex run data_audit.md</div>
<div style="color:#a6e3a1;margin-bottom:0.6rem;">LotFrontage 17.7% missing → median impute<br>
Garage cols cluster on no-garage → 0/None impute<br>
Leakage watch: MoSold, YrSold confirmed<br>
→ data_card.md written. Audit status: proceed with noted risks.</div>
<div style="color:#3bc9db;margin-bottom:0.8rem;">$ codex run baseline.md</div>
<div style="color:#a6e3a1;">Baseline: linear regression, 80/20 split, fixed validation set<br>
RMSE: $31,420 | R²: 0.81<br>
→ experiment_log.md entry 001 written. Baseline established.</div>
</div>

Three gates, three artifact updates, no detours. That's the practitioner pace.

---

## Prompt to start

```text
Set up and execute a housing-price analytics repository using the Codex Batman backbone.

Dataset: House Prices: Advanced Regression Techniques
(https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques)
Goal: predict SalePrice with low RMSE.

Work in practitioner mode — be direct and artifact-oriented.
Do not skip workflow gates.
Start with project-bootstrap, then problem-framing and data-audit.
```

---

## The eight-gate sequence

1. Initialize the project with `project-bootstrap` — folder structure and backbone files
2. Draft `problem_frame.md` — target, metric, decision context, stop conditions
3. Run `data-audit` — missingness, feature classes, leakage risks → `data_card.md`
4. Define split strategy and baseline in `analysis_plan.md`
5. Fit the baseline, then one or two justified candidate models
6. Log every run in `experiment_log.md`
7. Draft `model_card.md` for the best current model
8. Update `workflow_trace.md` and `PROJECT_STATE.md` before ending the session

The gates are the same as the student path. What's different is that Codex won't ask for your reasoning at each step — it executes and expects you to review the output.

---

## What success looks like

The repo is handoff-ready when another analyst can open it and answer: what problem is being solved, what data is in scope, what's been tried, what model currently leads, and what should happen next — all from the artifact files, without reopening the chat.

---

## Where To Go Next

- [Analytics Repo Overview](index.md)
- [Student Path](student.md) — same project with attempt-before-answer coaching
- [For Researchers & Data Scientists](../../data-scientists/index.md)
- [Core Data Science Workflow](../../workflows/data-science/index.md)
