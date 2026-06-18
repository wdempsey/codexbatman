# Experiment Log

The experiment log is the last gate in the workflow — and the one most consistently skipped.

An experiment log is not a journal or a reflection. It is a structured record of every modeling run: what was tried, what was measured, and what decision was made. Its purpose is to answer one question three months from now: "why did we build it this way?"

---

## Why this matters more than it looks

Without an experiment log, a project's decision history lives in one person's memory. When that person is out, questions arrive — "why did you use random forest instead of logistic regression?" "we ran this model last quarter, what was the ROC-AUC?" — and they either can't be answered or require reconstructing from notebooks.

The experiment log converts tacit knowledge into a shared record. It's not extra work. Every model comparison you do is a run; logging it takes 2 minutes and creates a permanent record of the analytical trajectory.

The log also prevents a specific failure mode: the project that cycles through model variants without making progress because no one remembers which configurations were already tried. The log shows the path. It makes iteration cheaper because you're not reconstructing what was already done.

---

## What a run entry contains

Each entry records a single modeling run — one configuration, one set of metrics, one decision.

**Run ID** — a sequential identifier. `run_001`, `run_002`. Simple, scannable.

**Date** — when the run was executed. Necessary for reconstructing the project timeline.

**Configuration** — what model, what features, what preprocessing, what hyperparameters. Enough detail to reproduce the run.

**Metric** — the primary metric from the problem frame, measured correctly (CV score for model selection, held-out score for final reporting). Include standard deviation for CV scores.

**Notes** — what you learned, what you decided, what the next step is. This is the most valuable field. A metric without a decision note is just a number.

**Status** — `active` (currently in use), `superseded` (replaced by a better run), `archived` (not used, kept for reference).

---

## The decision note

The notes field is where the experiment log becomes a decision log.

A good decision note is not "tried random forest, got 0.917 AUC." A good decision note is: "Random forest (0.917) vs. logistic regression (0.906). Difference within CV noise given dataset size. Logistic regression selected for interpretability — coefficient signs map directly to clinical feature importance. Random forest archived, superseded by run_001."

The decision note records three things: what the alternatives were, what was chosen, and why. Future you will thank present you for this.

---

## Try it: log a modeling run

<style>
.el-terminal{font-family:'JetBrains Mono','Courier New',monospace;font-size:0.82rem;line-height:1.65;background:#0d1b2e;border-radius:10px;padding:1.25rem 1.4rem;margin:1.4rem 0;border:1px solid #1a2f4a;}
.el-label{font-size:0.7rem;letter-spacing:0.06em;text-transform:uppercase;color:#6c7a8d;margin-bottom:0.9rem;}
.el-q{color:#f4a261;margin-bottom:0.7rem;font-weight:600;}
.el-ta{width:100%;background:#0a1628;border:1px solid #1e3a5f;border-radius:6px;color:#e2e8f0;padding:0.6rem 0.8rem;font-family:inherit;font-size:0.82rem;resize:vertical;min-height:70px;box-sizing:border-box;margin-bottom:0.6rem;}
.el-ta:focus{outline:none;border-color:#3bc9db;}
.el-btn{background:#1e3a5f;color:#e2e8f0;border:none;padding:0.4rem 1rem;border-radius:5px;cursor:pointer;font-family:inherit;font-size:0.8rem;margin-right:0.5rem;}
.el-btn:hover{background:#2d5282;}
.el-btn-play{background:#f4a261;color:#1a0a00;}
.el-btn-play:hover{background:#e8935a;}
.el-answer{display:none;margin-top:0.8rem;padding:0.8rem 1rem;background:#0a1e35;border-radius:6px;border-left:3px solid #a6e3a1;}
.el-answer-label{color:#6c7a8d;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.05em;margin-bottom:0.4rem;}
.el-answer-text{color:#a6e3a1;white-space:pre-wrap;}
.el-nav{margin-top:0.8rem;display:flex;align-items:center;gap:0.5rem;}
.el-step{display:none;}
.el-step.el-active{display:block;}
.el-progress{color:#6c7a8d;font-size:0.75rem;}
</style>

<div class="el-terminal">
<div class="el-label">Experiment Log — Try It</div>
<div id="el-step-1" class="el-step el-active">
  <div class="el-q">Q1 of 3 — What belongs in a run entry</div>
  <div style="color:#cbd5e1;margin-bottom:0.8rem;">You just finished run_002: random forest, all 13 features, 100 trees, max_depth=None, 5-fold stratified CV ROC-AUC 0.917 ± 0.031. Write the run entry. What fields do you need, and what goes in the notes?</div>
  <textarea class="el-ta" id="el-a1" placeholder="Your answer…"></textarea>
  <div><button class="el-btn" onclick="elSubmit(1)">Submit</button></div>
  <div class="el-answer" id="el-ans1">
    <div class="el-answer-label">Example run entry</div>
    <div class="el-answer-text">## run_002
Date: 2024-01-15
Model: RandomForestClassifier
Features: all 13 (post-audit, 6 rows dropped for missing ca/thal)
Preprocessing: median imputation → no scaling (tree-based)
Hyperparameters: n_estimators=100, max_depth=None, random_state=42
CV: 5-fold stratified, ROC-AUC 0.917 ± 0.031
Status: superseded

Notes: Slightly higher AUC than logistic regression (run_001: 0.906 ± 0.038).
Difference (0.011) within noise given ±0.031 std. No interpretable coefficients.
Selected run_001 (logistic regression) for evaluation — interpretability justified
by clinical context, AUC gap is not meaningful at this sample size.
Next step: run evaluation on run_001 using held-out test set.

The notes field is the most important part. A future reader needs to know not just what you ran but why you moved on from it.</div>
  </div>
  <div class="el-nav">
    <button class="el-btn" onclick="elNav(1)">Next →</button>
    <span class="el-progress" id="el-prog1"></span>
  </div>
</div>
<div id="el-step-2" class="el-step">
  <div class="el-q">Q2 of 3 — When to log</div>
  <div style="color:#cbd5e1;margin-bottom:0.8rem;">You ran a "quick test" — tried dropping the `chol` feature because EDA showed weak signal. CV ROC-AUC dropped to 0.891. You'll never use this configuration. Should you log it?</div>
  <textarea class="el-ta" id="el-a2" placeholder="Your answer…"></textarea>
  <div><button class="el-btn" onclick="elSubmit(2)">Submit</button></div>
  <div class="el-answer" id="el-ans2">
    <div class="el-answer-label">Expected answer</div>
    <div class="el-answer-text">Yes. Log every run — including the ones that didn't work.

Reason: "we tried dropping chol and performance dropped 0.015" is information. It tells future readers that chol was investigated and found useful despite its weak univariate signal (which was noted in the EDA). Without this log entry, a future collaborator might try the same thing and waste time rediscovering it.

The entry can be short:

## run_003
Date: 2024-01-15
Model: LogisticRegression
Features: 12 (chol excluded)
CV ROC-AUC: 0.891 ± 0.042
Status: archived

Notes: Tested dropping chol based on EDA finding (weak univariate signal).
AUC dropped ~0.015 vs. run_001. chol retained in final model.

"We never use this configuration" is not a reason to skip the log. The log is for the trajectory, not just the endpoint. Skipped experiments are invisible experiments — and invisible experiments get repeated.</div>
  </div>
  <div class="el-nav">
    <button class="el-btn" onclick="elNav(2)">Next →</button>
    <span class="el-progress" id="el-prog2"></span>
  </div>
</div>
<div id="el-step-3" class="el-step">
  <div class="el-q">Q3 of 3 — The final log entry</div>
  <div style="color:#cbd5e1;margin-bottom:0.8rem;">The project is wrapping up. The selected model (run_001) has passed evaluation. What's the final entry in the experiment log, and what does it say?</div>
  <textarea class="el-ta" id="el-a3" placeholder="Your answer…"></textarea>
  <div><button class="el-btn" onclick="elSubmit(3)">Submit</button></div>
  <div class="el-answer" id="el-ans3">
    <div class="el-answer-label">Example final entry</div>
    <div class="el-answer-text">## run_001 — FINAL
Date selected: 2024-01-15
Date evaluated: 2024-01-16
Model: LogisticRegression (C=1.0, solver='lbfgs', max_iter=1000)
Features: all 13 (6 rows dropped for missing ca/thal, 297 rows total)
Preprocessing: median imputation → StandardScaler → LogisticRegression (Pipeline)
CV ROC-AUC: 0.906 ± 0.038
Held-out test ROC-AUC: 0.878
Confusion matrix (threshold=0.5): TP=28, FP=8, TN=27, FN=10
Status: active

Notes: Selected for evaluation based on interpretability and AUC within noise of
random forest (run_002). Held-out performance 0.878 satisfies success criterion
(≥ 0.85). Confusion matrix presented to PI at threshold 0.5. Threshold decision
deferred to clinical team — see decision_log.md entry 2024-01-16.
Model card: model_card.md. Limitations: validated on Cleveland Clinic data 1988
only, 68% male, ages 29-77.

The final entry holds the complete record: what was built, how it performed, who saw the results, and where the decisions are documented. It's the closing bracket for the analytical work.</div>
  </div>
  <div class="el-nav">
    <button class="el-btn el-btn-play" onclick="elPlayAll()">▶ Show All</button>
    <span class="el-progress" id="el-prog3"></span>
  </div>
</div>
</div>

<script>
var elSubmitted=[false,false,false];
function elSubmit(n){
  elSubmitted[n-1]=true;
  document.getElementById("el-ans"+n).style.display="block";
  var prog=document.getElementById("el-prog"+n);
  if(prog){prog.textContent="Answer revealed";}
}
function elNav(n){
  elSubmit(n);
  document.getElementById("el-step-"+n).classList.remove("el-active");
  var next=document.getElementById("el-step-"+(n+1));
  if(next){next.classList.add("el-active");}
}
function elPlayAll(){
  for(var i=1;i<=3;i++){
    document.getElementById("el-ans"+i).style.display="block";
    document.getElementById("el-step-"+i).classList.add("el-active");
  }
}
</script>

---

## Common mistakes

**Logging only the winning configuration.** The log documents the analytical trajectory, not just the selected model. Failed experiments are part of the record. Without them, the log doesn't show why the selected model was chosen.

**Notes that just repeat the metrics.** "Run_002: ROC-AUC 0.917" is not a note. "Run_002 tested random forest; marginally higher AUC than baseline (0.011), within noise — logistic regression selected for interpretability" is a note. The note contains the decision, not just the result.

**Logging after the fact.** Logging from memory after a modeling session is less accurate and takes longer than logging as you run. Add the entry immediately after the run while the configuration is in front of you.

**No status field.** Without a status field, a reader scanning the log can't tell which configuration is in use. `active` / `superseded` / `archived` on each entry makes the log scannable in seconds.

---

## In the basic-classification example

The experiment log for the cardiac risk project is in [Basic Classification — Practitioner Lens](../../examples/basic-classification/practitioner.md). It shows the full run sequence: baseline logistic regression, random forest comparison, chol-exclusion test, and the final evaluation entry with the held-out performance and the decision note pointing to `decision_log.md`.

---

## Run this gate with Codex

```text
Run the experiment-log skill.
Log the run I just completed: [model, features, preprocessing, CV score].
Include a decision note — I chose this because [reason].
```

```text
Update the experiment log with the final evaluation results.
held-out ROC-AUC: [X]. Confusion matrix at threshold 0.5: [TP/FP/TN/FN].
Mark run_001 as active and write the final entry with the limitations reference.
```

---

*Previous gate: [Evaluation](evaluation.md) · Back to [Workflow Overview](index.md)*
