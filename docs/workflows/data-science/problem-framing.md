# Problem Framing

Problem framing is the first analytical gate. Nothing else runs until it's done.

The goal is to pin down four things before any data is touched: what decision this analysis will support, what the model needs to predict, how you'll measure success, and when the prediction happens. If any of these are unclear, the analysis can be technically correct and operationally useless.

---

## What Codex does at this gate

When you run the `problem-framing` skill, Codex asks you a sequence of questions — one at a time, waiting for your answer before continuing. It is not trying to generate a problem statement. It is trying to find the gaps in yours.

The questions it focuses on:

**Decision context** — what human decision does this model support? "Predict heart disease" is not a decision. "Flag patients for cardiology referral after a stress test" is.

**Target definition** — what exactly are you predicting? If the raw data has five severity levels, why are you binarizing, and does that tradeoff hold up when someone asks?

**Metric alignment** — does the metric match the decision cost structure? ROC-AUC measures discrimination. Accuracy measures raw correctness. Precision/recall trades off false positives against false negatives. Which one reflects what going wrong actually costs in this context?

**Prediction time** — at what moment in the real world does the prediction happen? Every feature in your dataset must be available at that moment. Features available only after the prediction is made are leakage.

**Population scope** — who does this model apply to? "Patients at the Cleveland Clinic in 1988" is a precise answer. "Heart disease patients generally" is not.

Codex writes the output to `problem_frame.md`. The document is short — a few paragraphs and a table. Its purpose is to give every subsequent skill a stable anchor so the analysis doesn't drift.

---

## The hardest question: prediction time

Prediction time is the single most important framing decision and the one most often skipped.

The question is: **in the real deployment scenario, when does the model run, and what information exists at that moment?**

In the cardiac risk example, the answer is: *after the stress test, before the referral decision*. That means exang (exercise-induced angina), oldpeak (ST depression during exercise), thalach (max heart rate during test), and thal (thalassemia from the test) are all valid features — they exist at prediction time. If instead we were predicting before the test, none of those would be available, and including them would be leakage.

Prediction time is easy to get wrong because datasets are collected historically. Every feature was observed *at some point* — but not necessarily *at the right point*.

---

## Try it: frame the problem before Codex does

These are the questions Codex would ask you at the problem-framing gate for the cardiac risk dataset. Try answering them before revealing the expected response.

<style>
.pf-terminal{font-family:'JetBrains Mono','Courier New',monospace;font-size:0.82rem;line-height:1.65;background:#0d1b2e;border-radius:10px;padding:1.25rem 1.4rem;margin:1.4rem 0;border:1px solid #1a2f4a;}
.pf-label{font-size:0.7rem;letter-spacing:0.06em;text-transform:uppercase;color:#6c7a8d;margin-bottom:0.9rem;}
.pf-q{color:#f4a261;margin-bottom:0.7rem;font-weight:600;}
.pf-context{color:#94a3b8;margin-bottom:0.8rem;font-size:0.8rem;}
.pf-ta{width:100%;background:#0a1628;border:1px solid #1e3a5f;border-radius:6px;color:#e2e8f0;padding:0.6rem 0.8rem;font-family:inherit;font-size:0.82rem;resize:vertical;min-height:70px;box-sizing:border-box;margin-bottom:0.6rem;}
.pf-ta:focus{outline:none;border-color:#3bc9db;}
.pf-btn{background:#1e3a5f;color:#e2e8f0;border:none;padding:0.4rem 1rem;border-radius:5px;cursor:pointer;font-family:inherit;font-size:0.8rem;margin-right:0.5rem;}
.pf-btn:hover{background:#2d5282;}
.pf-btn-play{background:#f4a261;color:#1a0a00;}
.pf-btn-play:hover{background:#e8935a;}
.pf-answer{display:none;margin-top:0.8rem;padding:0.8rem 1rem;background:#0a1e35;border-radius:6px;border-left:3px solid #a6e3a1;}
.pf-answer-label{color:#6c7a8d;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.05em;margin-bottom:0.4rem;}
.pf-answer-text{color:#a6e3a1;white-space:pre-wrap;}
.pf-nav{margin-top:0.8rem;display:flex;align-items:center;gap:0.5rem;}
.pf-step{display:none;}
.pf-step.pf-active{display:block;}
.pf-progress{color:#6c7a8d;font-size:0.75rem;}
</style>

<div class="pf-terminal">
<div class="pf-label">Problem Framing — Try It</div>
<div id="pf-step-1" class="pf-step pf-active">
  <div class="pf-q">Q1 of 3 — Decision context</div>
  <div class="pf-context">Dataset: Cleveland Heart Disease (303 patients, 13 features, target = presence/absence of heart disease)</div>
  <div style="color:#cbd5e1;margin-bottom:0.8rem;">What human decision does this classifier support? Describe the deployment scenario in one sentence.</div>
  <textarea class="pf-ta" id="pf-a1" placeholder="Your answer…"></textarea>
  <div><button class="pf-btn" onclick="pfSubmit(1)">Submit</button></div>
  <div class="pf-answer" id="pf-ans1">
    <div class="pf-answer-label">Expected framing</div>
    <div class="pf-answer-text">A physician sees a patient after a stress test. The classifier flags whether the patient likely has heart disease, supporting the decision of whether to refer them to a cardiologist for further evaluation.

The key word is "referral" — the model doesn't diagnose, it triages. That distinction matters for how you frame false negatives vs. false positives: a false negative (missed disease) sends a sick patient home; a false positive (false alarm) creates an unnecessary referral. Those costs are not symmetric, and the problem frame should say so.</div>
  </div>
  <div class="pf-nav">
    <button class="pf-btn" onclick="pfNav(1)">Next →</button>
    <span class="pf-progress" id="pf-prog1"></span>
  </div>
</div>
<div id="pf-step-2" class="pf-step">
  <div class="pf-q">Q2 of 3 — Metric alignment</div>
  <div style="color:#cbd5e1;margin-bottom:0.8rem;">The dataset's target ranges from 0 (no disease) to 4 (severe). The standard approach binarizes it to 0 / 1+. The proposed metric is ROC-AUC. What does ROC-AUC actually measure, and is it the right choice here?</div>
  <textarea class="pf-ta" id="pf-a2" placeholder="Your answer…"></textarea>
  <div><button class="pf-btn" onclick="pfSubmit(2)">Submit</button></div>
  <div class="pf-answer" id="pf-ans2">
    <div class="pf-answer-label">Expected framing</div>
    <div class="pf-answer-text">ROC-AUC measures how well the model ranks positive cases above negative cases across all possible thresholds. It doesn't commit to a single threshold — which makes it good for model comparison but not for deployment decisions.

For this problem: ROC-AUC is the right metric for model selection (comparing logistic regression vs. random forest). But the deployment decision — what threshold to use for referral — is a clinical policy choice, not a data science choice. The problem frame should acknowledge that the final operating threshold will be chosen based on the acceptable false-negative rate, not by maximizing AUC.

Binarizing 0–4 to 0/1+ is defensible for triage (we care whether disease is present, not its severity). But that tradeoff belongs in the problem frame explicitly.</div>
  </div>
  <div class="pf-nav">
    <button class="pf-btn" onclick="pfNav(2)">Next →</button>
    <span class="pf-progress" id="pf-prog2"></span>
  </div>
</div>
<div id="pf-step-3" class="pf-step">
  <div class="pf-q">Q3 of 3 — Prediction time</div>
  <div style="color:#cbd5e1;margin-bottom:0.8rem;">The dataset includes: age, sex, cp (chest pain type), trestbps (resting blood pressure), chol (cholesterol), fbs (fasting blood sugar), restecg (resting ECG), thalach (max heart rate during exercise), exang (exercise-induced angina), oldpeak (ST depression during exercise), slope (slope of peak exercise ST), ca (vessels colored by fluoroscopy), thal (thalassemia result). Which features require special scrutiny before you proceed?</div>
  <textarea class="pf-ta" id="pf-a3" placeholder="Your answer…"></textarea>
  <div><button class="pf-btn" onclick="pfSubmit(3)">Submit</button></div>
  <div class="pf-answer" id="pf-ans3">
    <div class="pf-answer-label">Expected framing</div>
    <div class="pf-answer-text">The stress-test features (thalach, exang, oldpeak, slope) and the diagnostic results (ca, thal) must be verified as available at prediction time. The scenario is post-stress-test referral — so all of these were measured before the referral decision is made. Prediction time check: passed.

The features that don't need scrutiny: age, sex, cp, trestbps, chol, fbs, restecg — these are all pre-test measurements, no leakage risk.

The features that do: the remaining 7 are all stress-test outputs or test-ordered diagnostics. If the deployment scenario were different (e.g., pre-test triage), every single one of them would be leakage. Defining prediction time first, before touching the data, is what allows you to make this call cleanly.</div>
  </div>
  <div class="pf-nav">
    <button class="pf-btn pf-btn-play" onclick="pfPlayAll()">▶ Show All</button>
    <span class="pf-progress" id="pf-prog3"></span>
  </div>
</div>
</div>

<script>
var pfSubmitted=[false,false,false];
var pfAttempts=["","",""];
function pfSubmit(n){
  var ta=document.getElementById("pf-a"+n);
  if(ta&&ta.value.trim()){pfAttempts[n-1]=ta.value.trim();}
  pfSubmitted[n-1]=true;
  document.getElementById("pf-ans"+n).style.display="block";
  var prog=document.getElementById("pf-prog"+n);
  if(prog){prog.textContent="Answer revealed";}
}
function pfNav(n){
  pfSubmit(n);
  document.getElementById("pf-step-"+n).classList.remove("pf-active");
  var next=document.getElementById("pf-step-"+(n+1));
  if(next){next.classList.add("pf-active");}
}
function pfPlayAll(){
  for(var i=1;i<=3;i++){
    document.getElementById("pf-ans"+i).style.display="block";
    document.getElementById("pf-step-"+i).classList.add("pf-active");
  }
}
</script>

---

## Common mistakes

**Skipping to EDA without a written problem frame.** The first instinct is to load the data and start plotting. This produces exploration without direction — you find patterns, but you don't know which ones matter. The problem frame defines what matters before you look.

**Choosing accuracy for imbalanced classification.** If 60% of patients are negative, a model that always predicts negative achieves 60% accuracy. ROC-AUC and F1 are better for imbalanced datasets because they don't reward predicting the majority class.

**Not defining prediction time.** Prediction time is skipped more often than any other framing question. The cost is leakage: features that look available in the historical dataset but would not exist at the moment the real-world prediction fires.

**"The model predicts X" without saying what X enables.** A model that predicts house prices is not useful by itself. A model that supports a buyer's decision about offer amount is. The decision context forces you to think about who uses the output and what they do with it.

---

## In the basic-classification example

The cardiac risk problem frame is the first thing the learning lens walks through. See [Basic Classification — Learning Lens](../../examples/basic-classification/learning.md) step 1 for the full framing session, including the prediction-time decision that governs which features are valid.

The manager's review of the problem frame is in [Basic Classification — Manager Lens](../../examples/basic-classification/manager.md) — specifically the questions a clinical PI asks about decision defensibility and population scope.

---

## Run this gate with Codex

```text
Run the problem-framing skill on this dataset.
Ask me one question at a time. Wait for my answer before continuing.
Write the output to problem_frame.md.
```

```text
Run problem-framing in practitioner mode.
The decision context is [X]. The target is [Y]. The metric is [Z].
Identify any prediction-time risks and write the problem frame directly.
```

---

*Next gate: [Data Audit](data-audit.md)*
