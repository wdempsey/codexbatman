# Modeling

The modeling gate runs after the EDA plan produces an analysis plan. It is where model selection, feature engineering, and cross-validated comparison happen. The gate's output is a trained model, a model card, and a comparison table in the experiment log.

The modeling gate is bounded by the analysis plan. You don't explore freely — you execute what the analysis plan specified, document any deviations, and update the analysis plan if you learn something that changes the approach.

---

## What happens at this gate

**Baseline first.** Every analysis starts with a baseline — a simple model that the more complex approach should beat. For classification, logistic regression with no feature engineering is the standard baseline. It establishes the floor and forces the question: does added complexity actually help?

**Preprocessing inside the fold.** The single most common leakage source at the modeling stage is fitting preprocessing steps on the full dataset before the train/test split. Imputers, scalers, and encoders must be fit on the training fold only, then applied to the test fold. In sklearn, this means using a `Pipeline` — not calling `fit_transform` on the whole dataset and then splitting.

**Cross-validation, not a single split.** A single train/test split produces an estimate that depends on which 20% ended up in the test set. K-fold cross-validation produces a more stable estimate by averaging performance across multiple splits. For a dataset of 303 rows, 5-fold or 10-fold CV is standard.

**Model comparison.** After the baseline, run at least one alternative that the analysis plan specified. For the cardiac risk project: logistic regression (baseline), random forest, and gradient boosting. The comparison goes in the experiment log. The best model by the problem-frame metric (ROC-AUC) advances to evaluation.

**Model card.** The selected model's configuration, training data, preprocessing steps, and performance summary go in `model_card.md`. This document travels with the model — it's what someone reading your work years later uses to understand what was built and why.

---

## The preprocessing-inside-the-fold rule

This is where the data audit's leakage check connects to the modeling stage.

The problem: if you fit an imputer on all 303 rows before splitting, the imputer "knows" about the test rows. The test-set mean it uses for imputation was influenced by the test data. That's a form of leakage — not a severe one, but one that produces optimistic test-set estimates.

In practice for small datasets the difference is often small. But the principle matters: every preprocessing step that uses data to make a decision (means, medians, encodings, principal components) must be fit only on training data.

```python
# Wrong — preprocessing leaks information from test fold
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)  # fit on all data including test
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y)

# Right — preprocessing inside the pipeline
pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler()),
    ('model', LogisticRegression())
])
cv_scores = cross_val_score(pipeline, X, y, cv=5, scoring='roc_auc')
```

The sklearn `Pipeline` enforces this correctly. Use it.

---

## Try it: model the cardiac dataset

<style>
.md-terminal{font-family:'JetBrains Mono','Courier New',monospace;font-size:0.82rem;line-height:1.65;background:#0d1b2e;border-radius:10px;padding:1.25rem 1.4rem;margin:1.4rem 0;border:1px solid #1a2f4a;}
.md-label{font-size:0.7rem;letter-spacing:0.06em;text-transform:uppercase;color:#6c7a8d;margin-bottom:0.9rem;}
.md-q{color:#f4a261;margin-bottom:0.7rem;font-weight:600;}
.md-ta{width:100%;background:#0a1628;border:1px solid #1e3a5f;border-radius:6px;color:#e2e8f0;padding:0.6rem 0.8rem;font-family:inherit;font-size:0.82rem;resize:vertical;min-height:70px;box-sizing:border-box;margin-bottom:0.6rem;}
.md-ta:focus{outline:none;border-color:#3bc9db;}
.md-btn{background:#1e3a5f;color:#e2e8f0;border:none;padding:0.4rem 1rem;border-radius:5px;cursor:pointer;font-family:inherit;font-size:0.8rem;margin-right:0.5rem;}
.md-btn:hover{background:#2d5282;}
.md-btn-play{background:#f4a261;color:#1a0a00;}
.md-btn-play:hover{background:#e8935a;}
.md-answer{display:none;margin-top:0.8rem;padding:0.8rem 1rem;background:#0a1e35;border-radius:6px;border-left:3px solid #a6e3a1;}
.md-answer-label{color:#6c7a8d;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.05em;margin-bottom:0.4rem;}
.md-answer-text{color:#a6e3a1;white-space:pre-wrap;}
.md-nav{margin-top:0.8rem;display:flex;align-items:center;gap:0.5rem;}
.md-step{display:none;}
.md-step.md-active{display:block;}
.md-progress{color:#6c7a8d;font-size:0.75rem;}
</style>

<div class="md-terminal">
<div class="md-label">Modeling — Try It</div>
<div id="md-step-1" class="md-step md-active">
  <div class="md-q">Q1 of 3 — Baseline rationale</div>
  <div style="color:#cbd5e1;margin-bottom:0.8rem;">Before running random forest or gradient boosting on the cardiac dataset, why run logistic regression first? What specifically would a strong logistic regression baseline tell you?</div>
  <textarea class="md-ta" id="md-a1" placeholder="Your answer…"></textarea>
  <div><button class="md-btn" onclick="mdSubmit(1)">Submit</button></div>
  <div class="md-answer" id="md-ans1">
    <div class="md-answer-label">Expected reasoning</div>
    <div class="md-answer-text">A strong logistic regression baseline tells you the problem is approximately linearly separable — the features, as they are, have enough linear signal to do the job. If logistic regression achieves, say, ROC-AUC ≥ 0.85, then the bar for a more complex model is "beats 0.85 by enough to justify the added complexity and reduced interpretability."

More importantly: a strong baseline limits your exploration. If logistic regression already achieves your success criterion (whatever the problem frame set), then the analysis plan is satisfied. You don't need random forest. You move to evaluation.

A weak baseline (ROC-AUC < 0.75) tells you linear separability isn't enough — either the feature relationships are nonlinear, or there's important feature engineering missing, or the problem is harder than the problem frame assumed. That changes the analysis plan.

Skipping the baseline and going straight to random forest means you don't know whether the complexity was necessary — and you'll have a harder time explaining why you used it.</div>
  </div>
  <div class="md-nav">
    <button class="md-btn" onclick="mdNav(1)">Next →</button>
    <span class="md-progress" id="md-prog1"></span>
  </div>
</div>
<div id="md-step-2" class="md-step">
  <div class="md-q">Q2 of 3 — Cross-validation setup</div>
  <div style="color:#cbd5e1;margin-bottom:0.8rem;">You're setting up 5-fold cross-validation on the cardiac dataset (297 rows after dropping missing values). The target is 54% negative, 46% positive. Should you use stratified k-fold or regular k-fold? Why?</div>
  <textarea class="md-ta" id="md-a2" placeholder="Your answer…"></textarea>
  <div><button class="md-btn" onclick="mdSubmit(2)">Submit</button></div>
  <div class="md-answer" id="md-ans2">
    <div class="md-answer-label">Expected reasoning</div>
    <div class="md-answer-text">Stratified k-fold. Always use stratified k-fold for classification.

Reason: with regular k-fold, the class distribution in each fold is random. For a 54/46 split on 297 rows, you'd expect roughly 60/30 or 59/31 per fold on average — close enough that regular k-fold would probably give similar results. But for small datasets or any class imbalance, unstratified folds can produce folds where one class is significantly over- or underrepresented, which produces unstable metric estimates.

Stratified k-fold guarantees that each fold maintains approximately the same class distribution as the full dataset. In sklearn: `StratifiedKFold` or use `cross_val_score` with the default `cv` parameter on a classification task — it uses stratified k-fold automatically.

This is a correctness issue, not just a precision issue: an unstratified fold that happens to get all positive cases in one fold produces a wildly different metric estimate from the true performance, and you won't know it happened unless you check.</div>
  </div>
  <div class="md-nav">
    <button class="md-btn" onclick="mdNav(2)">Next →</button>
    <span class="md-progress" id="md-prog2"></span>
  </div>
</div>
<div id="md-step-3" class="md-step">
  <div class="md-q">Q3 of 3 — Model selection decision</div>
  <div style="color:#cbd5e1;margin-bottom:0.8rem;">After cross-validation: logistic regression achieves ROC-AUC 0.906, random forest achieves 0.917. The problem frame success criterion was ROC-AUC ≥ 0.85. Which model do you advance to evaluation, and why?</div>
  <textarea class="md-ta" id="md-a3" placeholder="Your answer…"></textarea>
  <div><button class="md-btn" onclick="mdSubmit(3)">Submit</button></div>
  <div class="md-answer" id="md-ans3">
    <div class="md-answer-label">Expected reasoning</div>
    <div class="md-answer-text">Both models satisfy the success criterion. The 0.011 AUC difference between them is the key question.

The case for logistic regression: it achieves the criterion, it's interpretable (coefficients have clinical meaning — you can say "a one-unit increase in oldpeak increases log-odds of disease by X"), it's simpler to deploy and audit, and it generalizes more reliably on small datasets. In a clinical deployment context, interpretability has direct value — a physician who understands why the model flagged a patient is more likely to act on it appropriately.

The case for random forest: if 0.011 AUC corresponds to a meaningful number of additional correct referrals at the operating threshold, the gain is clinically significant. Run the calculation: at the deployment threshold (say, 0.5), how many additional true positives does random forest capture?

Most practitioners would advance logistic regression here and document the reasoning. The 0.011 difference is within CV noise for a dataset this small. Unless you can show it corresponds to a meaningful clinical improvement, the simpler model wins.

Either choice is defensible — what's not defensible is choosing without documenting the reasoning in the experiment log.</div>
  </div>
  <div class="md-nav">
    <button class="md-btn md-btn-play" onclick="mdPlayAll()">▶ Show All</button>
    <span class="md-progress" id="md-prog3"></span>
  </div>
</div>
</div>

<script>
var mdSubmitted=[false,false,false];
function mdSubmit(n){
  mdSubmitted[n-1]=true;
  document.getElementById("md-ans"+n).style.display="block";
  var prog=document.getElementById("md-prog"+n);
  if(prog){prog.textContent="Answer revealed";}
}
function mdNav(n){
  mdSubmit(n);
  document.getElementById("md-step-"+n).classList.remove("md-active");
  var next=document.getElementById("md-step-"+(n+1));
  if(next){next.classList.add("md-active");}
}
function mdPlayAll(){
  for(var i=1;i<=3;i++){
    document.getElementById("md-ans"+i).style.display="block";
    document.getElementById("md-step-"+i).classList.add("md-active");
  }
}
</script>

---

## Common mistakes

**Fitting preprocessing on all data before splitting.** This is the most common leakage source at the modeling stage. Use `sklearn.Pipeline` to prevent it.

**Hyperparameter tuning before validating the baseline.** Many practitioners tune hyperparameters before confirming the baseline is solid. If the baseline already meets the criterion, there's nothing to tune. If it doesn't, you need to understand why before tuning can help.

**Treating cross-validation score as the final performance estimate.** CV score is a model selection tool, not a final performance estimate. The final estimate comes from a held-out test set that was never used during model selection or tuning. If you tuned hyperparameters using CV score, you need a held-out set to estimate true performance.

**Not writing the model card.** The selected model goes in `model_card.md` before evaluation. The model card specifies what was built — feature set, preprocessing steps, hyperparameters, CV performance. Without it, the evaluation stage doesn't have a clear record of what it's evaluating.

---

## In the basic-classification example

The modeling walkthrough for the cardiac risk project is in [Basic Classification — Execution Lens](../../examples/basic-classification/execution.md): baseline logistic regression, random forest comparison, the preprocessing-inside-the-fold pipeline, and the experiment log entry documenting the model selection rationale.

---

## Run this gate with Codex

```text
Run the modeling skill.
The analysis plan is in analysis_plan.md, the data card is in data_card.md.
Start with the baseline. Use a Pipeline with preprocessing inside the fold.
Write each run to the experiment log before we discuss results.
```

```text
Run modeling in practitioner mode.
Baseline: logistic regression. Compare: random forest.
Metric: ROC-AUC with 5-fold stratified CV.
Write model_card.md for the selected model.
```

---

*Previous gate: [EDA Plan](eda-plan.md) · Next gate: [Evaluation](evaluation.md)*
