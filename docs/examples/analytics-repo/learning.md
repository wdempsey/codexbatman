# Linear Regression — Learning Lens

You're predicting median house values across California census tracts — a regression task with real policy stakes. The dataset is [California Housing](https://scikit-learn.org/stable/datasets/real_world.html#california-housing-dataset): 20,640 census tracts, 8 features, one question: what is the median house value for this tract, and where is the model systematically wrong?

**Student mode means attempt-before-answer**: type your reasoning at each step before Codex reveals its output. By the end you'll understand what's different about regression compared to classification, and have a full artifact set a collaborator can continue.

Ready to execute yourself? [See the execution lens →](execution.md) | Want to see how a manager reviews this project? [Manager lens →](manager.md)

---

## Walk Through the 7 Gates

*This session follows Socratic mode — expect questions, not answers.*

At each gate below, Codex asks for your reasoning first. Type something — even a rough guess — then click **See what Codex said** to reveal the output.

<div id="lr-root" style="font-family:'JetBrains Mono','Courier New',monospace;background:#0d1b2e;border-radius:10px;padding:24px 28px 20px 28px;max-width:680px;margin:32px 0;box-shadow:0 4px 32px rgba(0,0,0,0.45);border:1px solid #1a2f4a;">

  <div style="display:flex;align-items:center;gap:8px;margin-bottom:16px;">
    <span style="width:12px;height:12px;border-radius:50%;background:#ff5f56;display:inline-block;"></span>
    <span style="width:12px;height:12px;border-radius:50%;background:#ffbd2e;display:inline-block;"></span>
    <span style="width:12px;height:12px;border-radius:50%;background:#27c93f;display:inline-block;"></span>
    <span id="lr-step-label" style="margin-left:12px;font-size:0.78rem;color:#4a6885;letter-spacing:0.04em;">Step 1 of 7 — Problem Framing</span>
  </div>

  <div id="lr-body" style="min-height:320px;">
    <div id="lr-prompt" style="color:#3bc9db;font-size:0.85rem;margin-bottom:14px;"></div>
    <div style="color:#4a6885;font-size:0.72rem;margin-bottom:4px;text-transform:uppercase;letter-spacing:0.08em;">Codex asks</div>
    <div id="lr-question" style="color:#f4a261;font-size:0.87rem;line-height:1.55;margin-bottom:14px;min-height:44px;white-space:pre-wrap;"></div>
    <div style="color:#4a6885;font-size:0.72rem;margin-bottom:6px;text-transform:uppercase;letter-spacing:0.08em;">Your attempt</div>
    <textarea id="lr-textarea" placeholder="Type your reasoning before seeing Codex's response…" style="width:100%;box-sizing:border-box;background:#091422;border:1px solid #1e3a5a;border-radius:6px;color:#e2e8f0;font-family:inherit;font-size:0.82rem;line-height:1.5;padding:8px 10px;resize:vertical;min-height:60px;outline:none;transition:border-color 200ms ease;" onfocus="this.style.borderColor='#3bc9db'" onblur="this.style.borderColor='#1e3a5a'"></textarea>
    <button id="lr-submit" onclick="lrSubmit()" style="margin-top:8px;background:#f4a261;color:#1a0a00;border:none;border-radius:5px;padding:6px 18px;font-family:inherit;font-size:0.8rem;font-weight:700;cursor:pointer;">See what Codex said →</button>

    <div id="lr-answer-wrap" style="display:none;margin-top:18px;">
      <div style="color:#4a6885;font-size:0.72rem;margin-bottom:4px;text-transform:uppercase;letter-spacing:0.08em;">Codex output</div>
      <div id="lr-answer" style="color:#a6e3a1;font-size:0.84rem;line-height:1.55;margin-bottom:16px;white-space:pre-wrap;"></div>
      <div id="lr-badge" style="display:inline-block;background:#1a2f4a;border:1px solid #3bc9db;border-radius:5px;padding:4px 12px;font-size:0.74rem;color:#3bc9db;"></div>
    </div>
  </div>

  <div style="display:flex;gap:10px;margin-top:22px;align-items:center;flex-wrap:wrap;">
    <button id="lr-prev" onclick="lrNav(-1)" style="background:#1a2f4a;color:#3bc9db;border:1px solid #3bc9db;border-radius:5px;padding:6px 18px;font-family:inherit;font-size:0.8rem;cursor:pointer;">← Prev</button>
    <button id="lr-next" onclick="lrNav(1)" style="background:#1a2f4a;color:#3bc9db;border:1px solid #3bc9db;border-radius:5px;padding:6px 18px;font-family:inherit;font-size:0.8rem;cursor:pointer;">Next →</button>
    <button id="lr-play" onclick="lrPlay()" style="background:#0d1b2e;color:#f4a261;border:1px solid #f4a261;border-radius:5px;padding:6px 18px;font-family:inherit;font-size:0.8rem;cursor:pointer;">▶ Play all</button>
    <span id="lr-dots" style="margin-left:4px;color:#4a6885;font-size:0.78rem;letter-spacing:0.12em;"></span>
  </div>
</div>

<script>
(function () {
  var steps = [
    {
      label: "Step 1 of 7 — Problem Framing",
      prompt: "$ codex run problem_frame.md --skill problem-framing",
      question: "The dataset has one row per census tract. The target is MedHouseVal — median house value in $100,000s, capped at $500K. What human decision does this model support, and should your metric be RMSE or MAE? What's the difference?",
      answer: "Decision context: a state housing agency estimating median house values across California tracts to identify where housing cost burden is highest relative to income — to prioritize assistance program deployment.\n\nUnit of observation: one census tract, not one house. The model predicts tract-level medians.\n\nRMSE vs MAE: RMSE squares errors before averaging — a single tract with a $200K prediction error hurts much more than ten tracts with $20K errors. MAE treats all errors equally. For policy allocation, RMSE is the right choice: a catastrophically wrong prediction for one high-need tract is worse than moderate errors spread across many. We'll also evaluate on log-scale RMSE (RMSLE) because the target is skewed.\n\n✓ Decision context: housing assistance program prioritization\n✓ Target: MedHouseVal (continuous, per tract)\n✓ Metric: RMSE (log-scale)\n✓ Population: California census tracts, 1990",
      artifact: "✓ artifact written: problem_frame.md"
    },
    {
      label: "Step 2 of 7 — Data Audit",
      prompt: "$ codex run data_audit.md --skill data-audit",
      question: "The dataset has no missing values — but there's a data quality issue hiding in plain sight. Look at the target distribution: MedHouseVal has an unusually large spike at exactly 5.0 ($500K). What causes this, and why does it matter for modeling?",
      answer: "The $500K cap is a censoring artifact. Any tract where the true median house value was above $500K was recorded as exactly $500K. About 965 tracts (~4.7%) hit the ceiling.\n\nWhy it matters: the model will be trained as if $500K is the true value for those tracts. At prediction time, the model will systematically underestimate values for high-value tracts. Residuals for those tracts will show a predictable pattern — actual values at the ceiling, predictions below it.\n\nData card entry: 'MedHouseVal is censored at 5.0 ($500K). 965 tracts (4.7%) hit the ceiling. Model will underestimate values for high-cost tracts. This is a structural limitation, not a data quality error — it reflects the data collection methodology.'\n\nThis does not stop the analysis — but it must be in the model card limitations section and disclosed to the housing agency before deployment.\n\n✓ artifact written: data_card.md",
      artifact: "✓ artifact written: data_card.md"
    },
    {
      label: "Step 3 of 7 — EDA Plan",
      prompt: "$ codex run analysis_plan.md --skill eda-plan",
      question: "Before you start plotting: what are the two most important EDA questions for this dataset? One should be about the target distribution. One should be about the geographic features.",
      answer: "Question 1 — Target distribution: is MedHouseVal skewed enough to warrant a log transform before modeling? If the distribution is right-skewed (long tail of high values), linear regression on the raw target will produce non-normal residuals and will underfit the high end. Plot the histogram; if the right tail is long, log-transform the target.\n\nQuestion 2 — Geographic features: do Latitude and Longitude show a strong visual pattern with MedHouseVal? A scatter plot of lat/lon colored by house value would reveal whether geographic clustering exists. If coastal tracts are systematically higher-valued than inland tracts, this signal is real — but it's not a linear relationship, so raw lat/lon will only partially capture it.\n\nBoth questions feed directly into the analysis plan: whether to log-transform, and how to handle lat/lon (include as-is, bin into regions, or note the nonlinearity as a modeling limitation).\n\n✓ artifact written: analysis_plan.md",
      artifact: "✓ artifact written: analysis_plan.md"
    },
    {
      label: "Step 4 of 7 — Modeling: Baseline",
      prompt: "$ codex run baseline.py --skill modeling",
      question: "What should the baseline model be, and why log-transform the target before fitting? What does that change about how you interpret predictions?",
      answer: "Baseline: linear regression on all 8 features (no feature engineering, no regularization). StandardScaler on all numeric features (required for ridge/lasso comparison later — though not strictly needed for OLS, it makes coefficients comparable).\n\nLog-transform: np.log(MedHouseVal). EDA confirmed the distribution is right-skewed. Fitting on log(target) means the model predicts log(house value) — a 1-unit change in a feature predicts a proportional change in house value, not an additive change. This is more appropriate for prices.\n\nInterpreting predictions: to get back to dollars, exponentiate: np.exp(model.predict(X)). Report RMSE on the log scale during model comparison; report dollar-scale RMSE in the model card for the housing agency.\n\nBaseline result: RMSE (log-scale) ≈ 0.53, R² ≈ 0.61. This is the floor — any more complex model must beat it.\n\n✓ artifact written: experiment_log.md (run_001)",
      artifact: "✓ artifact: experiment_log.md — run_001"
    },
    {
      label: "Step 5 of 7 — Modeling: Ridge & Lasso",
      prompt: "$ codex run ridge_lasso.py --skill modeling",
      question: "AveRooms and AveBedrms are highly correlated (tracts with more rooms tend to have more bedrooms). What problem does this cause for linear regression, and which regularization method addresses it?",
      answer: "The problem is multicollinearity. When two features are highly correlated, linear regression can't reliably estimate their individual coefficients — small changes in the data produce large changes in the coefficient values. The model may assign a large positive coefficient to AveRooms and a large negative one to AveBedrms, even though both genuinely predict house value.\n\nRidge regression adds a penalty proportional to the sum of squared coefficients (L2 penalty). This shrinks all coefficients toward zero, reducing their variance. Correlated features end up with similar (smaller) coefficients rather than large, unstable ones. Ridge keeps all features.\n\nLasso adds a penalty proportional to the sum of absolute coefficients (L1 penalty). This can shrink some coefficients to exactly zero — effectively performing feature selection. For this dataset with only 8 features, lasso is unlikely to drop many; but with engineered features it becomes more useful.\n\nResult: Ridge (alpha=1.0) achieves RMSE ≈ 0.51, R² ≈ 0.63 — modest improvement over baseline. Lasso similar. The gain is small because 8 features aren't enough for severe multicollinearity to dominate.\n\n✓ artifact: experiment_log.md — run_002 (ridge), run_003 (lasso)",
      artifact: "✓ artifact: experiment_log.md — run_002, run_003"
    },
    {
      label: "Step 6 of 7 — Evaluation",
      prompt: "$ codex run evaluation.py --skill model-evaluation",
      question: "After fitting ridge regression, you plot residuals (predicted − actual) against predicted values and notice a horizontal band of residuals at the top right — actual values all near 5.0 but predicted values spread below 5.0. What is this pattern telling you?",
      answer: "That's the $500K ceiling artifact showing up in residuals. Tracts where the true value is at or above $500K have actual = 5.0 (the cap), but the model predicts a range of values below 5.0 based on their features. The residuals for those tracts are all negative — the model 'overpredicts' relative to the censored target.\n\nThis pattern confirms two things: (1) the model correctly learned that high-income, coastal tracts should have high values, but (2) the training signal for those tracts was systematically pulled down by the cap. The model is probably underestimating the true values for those tracts in deployment.\n\nResidual plot also reveals: geographic structure — errors are not random by location. Coastal tracts (low longitude, mid-latitude) have systematically negative residuals (model underestimates). Inland Central Valley tracts have near-zero residuals (model fits well).\n\nModel card limitation entry: 'Model systematically underestimates values for high-cost tracts (MedHouseVal near $500K ceiling). RMSE for tracts with MedHouseVal > $400K is approximately 2× the overall RMSE. Housing agency should not use model outputs alone for decisions affecting coastal high-cost tracts.'\n\n✓ artifact: model_card.md written",
      artifact: "✓ artifact written: model_card.md"
    },
    {
      label: "Step 7 of 7 — Experiment Log",
      prompt: "$ codex run workflow_trace.md --skill experiment-log",
      question: "You ran 3 model configurations. The ridge model (run_002) has the best RMSE. Write the decision note for the final experiment log entry — what did you find, what did you choose, and what should the next session start with?",
      answer: "## run_002 — FINAL (Ridge Regression)\nDate: [today]\nModel: Ridge (alpha=1.0), all 8 features, log-transformed target\nPreprocessing: StandardScaler → Ridge (Pipeline)\nCV RMSE (log-scale): 0.511 ± 0.008\nHeld-out RMSE (log-scale): 0.517\nHeld-out R²: 0.633\nStatus: active\n\nNotes: Ridge marginally outperforms OLS baseline (0.517 vs 0.531 RMSE) and lasso (0.519). Improvement is modest — 8 features with moderate multicollinearity between AveRooms/AveBedrms. Log-transform of target confirmed important: raw-target OLS residuals were right-skewed, log-scale residuals approximately normal.\n\nKey finding: geographic residual structure visible — model underpredicts coastal tracts. Lat/lon treated as linear predictors; nonlinear spatial modeling (kernel methods, spatial interpolation, or geographic region dummies) is the clearest path to improvement. See analysis_plan.md §next-steps.\n\nNext session: try adding geographic region features (coastal vs inland dummy, county groupings) before committing to a more complex model.\n\n✓ artifact: experiment_log.md final entry\n✓ artifact: workflow_trace.md updated\n✓ artifact: PROJECT_STATE.md updated",
      artifact: "✓ session complete — 7 artifacts written"
    }
  ];

  var cur = 0;
  var revealed = [];
  for (var i = 0; i < steps.length; i++) revealed.push(false);

  function render() {
    var s = steps[cur];
    document.getElementById('lr-step-label').textContent = s.label;
    document.getElementById('lr-prompt').textContent = s.prompt;
    document.getElementById('lr-question').textContent = s.question;
    document.getElementById('lr-textarea').value = '';
    var aw = document.getElementById('lr-answer-wrap');
    aw.style.display = revealed[cur] ? 'block' : 'none';
    if (revealed[cur]) {
      document.getElementById('lr-answer').textContent = s.answer;
      document.getElementById('lr-badge').textContent = s.artifact;
    }
    document.getElementById('lr-prev').style.opacity = cur === 0 ? '0.3' : '1';
    document.getElementById('lr-next').style.opacity = cur === steps.length - 1 ? '0.3' : '1';
    var dots = '';
    for (var i = 0; i < steps.length; i++) dots += (i === cur ? '●' : '○');
    document.getElementById('lr-dots').textContent = dots;
  }

  window.lrSubmit = function () {
    revealed[cur] = true;
    var s = steps[cur];
    document.getElementById('lr-answer').textContent = s.answer;
    document.getElementById('lr-badge').textContent = s.artifact;
    document.getElementById('lr-answer-wrap').style.display = 'block';
  };

  window.lrNav = function (dir) {
    var next = cur + dir;
    if (next < 0 || next >= steps.length) return;
    cur = next;
    render();
  };

  window.lrPlay = function () {
    for (var i = 0; i < steps.length; i++) revealed[i] = true;
    cur = 0;
    render();
  };

  render();
})();
</script>

---

## What you just built

Seven artifacts — the backbone for any analyst picking this project back up:

- `problem_frame.md` — housing agency decision context, RMSE metric, census-tract unit
- `data_card.md` — $500K ceiling documented, 8 features described, no missing values
- `analysis_plan.md` — log-transform rationale, lat/lon handling decision, ridge selection
- `experiment_log.md` — 3 runs: OLS baseline, ridge, lasso with decision notes
- `model_card.md` — performance, limitations (coastal underprediction, ceiling artifact)
- `workflow_trace.md` — what happened this session, where to resume
- `PROJECT_STATE.md` — current model, open questions, next step

The experiment log documents both the winner (ridge) and the alternatives, with the reasoning that chose between them.

---

## Try It for Real

No file download needed — California Housing ships with scikit-learn.

```python
from sklearn.datasets import fetch_california_housing
data = fetch_california_housing(as_frame=True)
df = data.frame  # 20,640 rows × 9 columns (8 features + MedHouseVal target)
df.to_csv("california_housing.csv", index=False)
```

Then paste this into Codex:

```text
Use tutor mode to guide me through a housing price regression project.

Dataset: California Housing (sklearn fetch_california_housing, saved to california_housing.csv)
Target: MedHouseVal (median house value in units of $100,000; values capped at $500K)
Goal: predict median house value per census tract.
Metric: RMSE.

Start with problem-framing. Ask for my reasoning before each gate output.
```

---

## What this example didn't cover

**Nonlinear geographic modeling.** Lat/lon as linear predictors captures only a fraction of the geographic signal. The residual map shows clear coastal underprediction. Geographic region dummies (coastal/inland/valley/mountain), spatial interpolation, or kernel methods would address this — but that's a feature engineering problem, not a workflow problem.

**Interaction terms.** MedInc × HouseAge might capture neighborhoods where old housing stock is in high-income areas (a different market from old housing in low-income areas). Not covered here — the analysis plan flags it as a next-step hypothesis.

**The causal question.** This model predicts house values, it doesn't explain them. If the housing agency wants to know whether investing in neighborhood amenities *causes* higher property values, that's a causal inference question — see the [causal inference example](../causal-inference/index.md) when it's available.

---

*Previous example: [Basic Classification](../basic-classification/index.md) · Next: [Causal Inference](../causal-inference/index.md) (coming soon)*
