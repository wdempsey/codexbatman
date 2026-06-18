# Linear Regression — Execution Lens

Same project as the learning lens — California Housing, median house value prediction — but without the scaffolding. Codex executes each gate directly, drafts artifacts for your review, and flags decisions that require your input. You direct the exceptions.

[See the learning lens →](learning.md) | [Manager review →](manager.md)

---

## What a practitioner session looks like

<div style="font-family:'JetBrains Mono','Courier New',monospace;font-size:0.84rem;line-height:1.6;background:#0d1b2e;border-radius:10px;padding:1.2rem 1.4rem;margin:1.5rem 0;border:1px solid #1a2f4a;">
<div style="color:#6c7a8d;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.06em;margin-bottom:0.8rem;">California Housing — Practitioner Session</div>
<div style="color:#3bc9db;margin-bottom:0.3rem;">$ codex run problem_frame.md --skill problem-framing --mode practitioner</div>
<div style="color:#a6e3a1;margin-bottom:1rem;">Decision: housing agency program prioritization<br>
Target: MedHouseVal (continuous, per census tract)<br>
Metric: RMSE on log-scale; report dollar-scale RMSE in model card<br>
Note: target capped at $500K — structural censoring, documented<br>
→ problem_frame.md written</div>

<div style="color:#3bc9db;margin-bottom:0.3rem;">$ codex run data_audit.md --skill data-audit</div>
<div style="color:#a6e3a1;margin-bottom:1rem;">20,640 rows, 8 features, no missing values<br>
⚠ MedHouseVal ceiling: 965 tracts (4.7%) at exactly 5.0<br>
AveRooms/AveBedrms correlation: 0.85 — flag for regularization<br>
AveOccup has right-skewed outliers (tracts with unusually high occupancy)<br>
Verdict: proceed — no stop conditions, ceiling documented<br>
→ data_card.md written</div>

<div style="color:#3bc9db;margin-bottom:0.3rem;">$ codex run baseline.py</div>
<div style="color:#a6e3a1;margin-bottom:1rem;">Log-transform target: confirmed (right skew, log residuals ≈ normal)<br>
OLS baseline, all 8 features, StandardScaler<br>
5-fold CV RMSE (log): 0.531 ± 0.006 | R²: 0.610<br>
→ experiment_log.md run_001 written</div>

<div style="color:#3bc9db;margin-bottom:0.3rem;">$ codex run ridge_lasso.py</div>
<div style="color:#a6e3a1;margin-bottom:1rem;">Ridge (alpha=1.0): RMSE 0.511 ± 0.008 | R²: 0.633 ✓ best<br>
Lasso (alpha=0.01): RMSE 0.519 ± 0.007 | R²: 0.624<br>
→ experiment_log.md run_002, run_003 written<br>
→ Selecting ridge for evaluation</div>

<div style="color:#3bc9db;margin-bottom:0.3rem;">$ codex run evaluation.py --skill model-evaluation</div>
<div style="color:#a6e3a1;margin-bottom:1rem;">Held-out RMSE (log): 0.517 | R²: 0.631<br>
Held-out RMSE (dollars): ~$68,400<br>
Residual plot: geographic structure visible — coastal underprediction confirmed<br>
Ceiling artifact: negative residual band at MedHouseVal = 5.0<br>
→ model_card.md written with limitations</div>

<div style="color:#3bc9db;margin-bottom:0.3rem;">$ codex run workflow_trace.md</div>
<div style="color:#a6e3a1;">Session complete. 3 runs logged, ridge selected.<br>
Open question: nonlinear geographic features (coastal/inland dummies)<br>
→ PROJECT_STATE.md updated</div>
</div>

Six gates, six artifact updates. The residual finding (coastal underprediction) is flagged as the primary open question — not resolved in this session, but documented so the next session starts from that finding rather than rediscovering it.

---

## Prompt to start

```text
Run the California Housing regression project using the Codex Batman backbone.

Dataset: sklearn.datasets.fetch_california_housing()
Goal: predict MedHouseVal with low RMSE. Decision context: housing agency
program prioritization — identify tracts where housing cost burden is highest.

Work in practitioner mode — be direct and artifact-oriented.
Do not skip workflow gates. Start with project-bootstrap.
Log every model run to experiment_log.md before we discuss results.
```

---

## Key decisions this session made

**Log-transform the target.** MedHouseVal is right-skewed. Log-transforming before modeling produces approximately normal residuals and a more stable fit. All model comparisons are on log-scale RMSE; dollar-scale RMSE is reported separately in the model card for the housing agency audience.

**Ridge over lasso.** With 8 features and moderate multicollinearity (AveRooms/AveBedrms at 0.85 correlation), ridge marginally outperforms lasso. Lasso zeroed nothing out — with only 8 features, there's nothing to select away. If feature engineering expands the feature set significantly, revisit lasso.

**Include lat/lon as linear features.** The analysis plan notes this is imprecise — geographic price variation isn't linear. But linear lat/lon captures the north-south and east-west gradients partially. The residual map confirmed the limitation (coastal underprediction). The next session will test geographic region dummies as an improvement.

**Ceiling artifact is a limitation, not a stop condition.** 4.7% of tracts hit the $500K cap. This is too small to stop the analysis but too important to ignore. It's in the data card and the model card. The housing agency is advised not to use model outputs alone for decisions affecting coastal high-cost tracts.

---

## The eight backbone artifacts

```
california-housing-repo/
  PROJECT_STATE.md          ← current model, open questions, next session start
  problem_frame.md          ← decision context, metric, population, ceiling note
  data_card.md              ← 8 features, ceiling documented, correlation flag
  analysis_plan.md          ← log-transform rationale, lat/lon handling, ridge selection
  experiment_log.md         ← 3 runs: OLS (001), Ridge (002), Lasso (003)
  model_card.md             ← Ridge performance, limitations, geographic residual finding
  workflow_trace.md         ← what happened, what was decided, where to resume
  decision_log.md           ← log-transform decision, ceiling disclosure decision
```

---

## What success looks like

The repo is handoff-ready when another analyst can open it and answer without reopening the chat: what problem is being solved, what data is in scope, what the $500K ceiling means for interpretation, what was tried, what model currently leads, and what should happen next.

The geographic residual finding in particular should be visible in the experiment log — so the next analyst doesn't run the same models hoping for different results, but instead tests the geographic feature hypothesis.

---

*Related: [Learning Lens](learning.md) · [Manager Lens](manager.md) · [Workflow Gates](../../workflows/data-science/index.md)*
