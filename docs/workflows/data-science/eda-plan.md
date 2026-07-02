# EDA Plan

The EDA plan is the third gate. It runs after the data audit confirms the dataset is fit for analysis. Its job is to design the exploration before it starts — defining what you're looking for and why, so that EDA produces insights that feed the analysis plan rather than a notebook full of plots that don't connect to any decision.

Unplanned EDA is one of the most common ways data science projects go sideways. You find patterns, get interested in them, spend three days exploring them, and eventually realize they don't answer the question in the problem frame. The EDA plan is a forcing function: exploration stays tethered to what the analysis actually needs.

---

## What Codex does at this gate

The `eda-plan` skill asks you to articulate what questions the exploration needs to answer before the modeling gate can open. It then structures the exploration into a bounded set of analytical tasks.

**Feature-target relationships** — which features appear to discriminate between positive and negative cases? This is the primary EDA question for supervised learning. Distributions of each feature split by the target variable, simple correlation with target, class-conditional means.

**Feature-feature correlations** — are any features highly collinear? Correlated features don't add independent information. In the cardiac dataset, thalach (max heart rate) and age are known to be inversely correlated — older patients achieve lower max heart rates. This is medically expected, not a data problem, but it should be documented.

**Distribution shape** — are features skewed, bimodal, or otherwise shaped in a way that affects model assumptions? Logistic regression is relatively robust to input distribution, but understanding the distributions matters for feature engineering decisions (log transforming a skewed variable, deciding whether to bin age into groups, etc.).

**Subgroup analysis** — does the feature-target relationship vary across subgroups? For cardiac risk, sex and age are natural subgrouping variables. A model that works well on average but fails systematically for one subgroup is a problem — and you want to know that before deployment, not after.

The EDA plan produces `analysis_plan.md`. This document specifies the modeling approach the exploration supports and the analytical decisions made during EDA.

---

## Why plan before exploring?

EDA without a plan produces three failure modes.

**Confirmation bias.** You look at data long enough, you'll find a pattern that supports almost any hypothesis. A plan forces you to specify in advance what you're looking for, which makes it harder to confuse "I found something" with "I looked for something and found it."

**Scope creep.** Every interesting pattern in the data creates a branch — what if we look at this stratified by age? What if we log-transform that? Each branch takes time. Without a plan, EDA expands to fill whatever time is available. The plan sets the scope.

**Disconnected insights.** Unplanned EDA often produces a rich notebook of plots that don't connect to any decision. The EDA plan ensures each plot answers a question that feeds into the analysis plan. If you can't say why a plot answers a specific question, it doesn't belong in the planned analysis.

---

## Try it: plan the cardiac dataset EDA

<style>
.ep-terminal{font-family:'JetBrains Mono','Courier New',monospace;font-size:0.82rem;line-height:1.65;background:#0d1b2e;border-radius:10px;padding:1.25rem 1.4rem;margin:1.4rem 0;border:1px solid #1a2f4a;}
.ep-label{font-size:0.7rem;letter-spacing:0.06em;text-transform:uppercase;color:#7d90a8;margin-bottom:0.9rem;}
.ep-q{color:#f4a261;margin-bottom:0.7rem;font-weight:600;}
.ep-ta{width:100%;background:#0a1628;border:1px solid #1e3a5f;border-radius:6px;color:#e2e8f0;padding:0.6rem 0.8rem;font-family:inherit;font-size:0.82rem;resize:vertical;min-height:70px;box-sizing:border-box;margin-bottom:0.6rem;}
.ep-ta:focus{outline:none;border-color:#3bc9db;}
.ep-btn{background:#1e3a5f;color:#e2e8f0;border:none;padding:0.4rem 1rem;border-radius:5px;cursor:pointer;font-family:inherit;font-size:0.8rem;margin-right:0.5rem;}
.ep-btn:hover{background:#2d5282;}
.ep-btn-play{background:#f4a261;color:#1a0a00;}
.ep-btn-play:hover{background:#e8935a;}
.ep-answer{display:none;margin-top:0.8rem;padding:0.8rem 1rem;background:#0a1e35;border-radius:6px;border-left:3px solid #a6e3a1;}
.ep-answer-label{color:#7d90a8;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.05em;margin-bottom:0.4rem;}
.ep-answer-text{color:#a6e3a1;white-space:pre-wrap;}
.ep-nav{margin-top:0.8rem;display:flex;align-items:center;gap:0.5rem;}
.ep-step{display:none;}
.ep-step.ep-active{display:block;}
.ep-progress{color:#7d90a8;font-size:0.75rem;}
</style>

<div class="ep-terminal">
<div class="ep-label">EDA Plan — Try It</div>
<div id="ep-step-1" class="ep-step ep-active">
  <div class="ep-q">Q1 of 3 — Scoping the exploration</div>
  <div style="color:#cbd5e1;margin-bottom:0.8rem;">You have 13 features and a binary target. The problem frame says this is a post-stress-test referral classifier. What are the three most important questions your EDA needs to answer before you write the analysis plan?</div>
  <textarea class="ep-ta" id="ep-a1" placeholder="Your answer…"></textarea>
  <div><button class="ep-btn" onclick="epSubmit(1)">Submit</button></div>
  <div class="ep-answer" id="ep-ans1">
    <div class="ep-answer-label">Expected EDA scope</div>
    <div class="ep-answer-text">1. Which features have the strongest individual association with the target? This determines which features are likely to be useful to the model and which might be noise. For a 13-feature dataset, this is feasible to assess directly.

2. Are any features highly correlated with each other, in ways that might cause redundancy? Particularly: age/thalach, and the several stress-test features (exang, oldpeak, slope) which measure related aspects of the exercise response.

3. Does the feature-target relationship look similar for male and female patients? Sex is a known moderator of cardiac risk presentation. A model that performs well overall but differently by sex has fairness and clinical implications.

These three questions each feed directly into the analysis plan: which features to include, whether to apply dimensionality reduction or feature selection, and whether to stratify the evaluation.</div>
  </div>
  <div class="ep-nav">
    <button class="ep-btn" onclick="epNav(1)">Next →</button>
    <span class="ep-progress" id="ep-prog1"></span>
  </div>
</div>
<div id="ep-step-2" class="ep-step">
  <div class="ep-q">Q2 of 3 — Feature-target relationship</div>
  <div style="color:#cbd5e1;margin-bottom:0.8rem;">You plot the distribution of `thalach` (max heart rate) split by target class and find that patients with heart disease have lower max heart rates on average. What does this tell you, and does it affect the analysis plan?</div>
  <textarea class="ep-ta" id="ep-a2" placeholder="Your answer…"></textarea>
  <div><button class="ep-btn" onclick="epSubmit(2)">Submit</button></div>
  <div class="ep-answer" id="ep-ans2">
    <div class="ep-answer-label">Expected EDA response</div>
    <div class="ep-answer-text">Lower max heart rate in disease-positive patients makes physiological sense — impaired cardiac function limits the heart's ability to increase rate under stress. This is a meaningful signal.

What it tells you: thalach is likely to be a useful predictor. Its inclusion in the model is supported both by the distribution plot and by domain logic (which provides independent confirmation).

What it doesn't tell you: how much independent predictive value thalach adds when controlling for age and other stress-test features. Two features can both correlate with the target while being so correlated with each other that only one adds information. That question requires the modeling stage.

Analysis plan implication: thalach is retained as a candidate feature. The analysis plan notes that its relationship with age should be examined further during feature engineering. This is not a feature selection decision — it's documentation of what the EDA found, so the modeling stage has the context to work with.</div>
  </div>
  <div class="ep-nav">
    <button class="ep-btn" onclick="epNav(2)">Next →</button>
    <span class="ep-progress" id="ep-prog2"></span>
  </div>
</div>
<div id="ep-step-3" class="ep-step">
  <div class="ep-q">Q3 of 3 — When to stop</div>
  <div style="color:#cbd5e1;margin-bottom:0.8rem;">After checking feature distributions, correlations, and the sex-stratified subgroup analysis, you notice that `chol` (cholesterol) shows almost no difference in distribution between disease-positive and disease-negative patients. How does this affect the analysis plan, and should you investigate further?</div>
  <textarea class="ep-ta" id="ep-a3" placeholder="Your answer…"></textarea>
  <div><button class="ep-btn" onclick="epSubmit(3)">Submit</button></div>
  <div class="ep-answer" id="ep-ans3">
    <div class="ep-answer-label">Expected EDA response</div>
    <div class="ep-answer-text">A weak univariate relationship doesn't mean the feature is useless — it might have value in combination with other features. Cholesterol is clinically meaningful for cardiac risk, so its near-zero univariate signal in this dataset is worth noting but not a reason to drop it preemptively.

How it affects the analysis plan: note that chol shows weak individual association with the target in this sample. The model should be tested with and without chol. If removing it doesn't change performance, the simpler model is preferable.

Should you investigate further in EDA? No — you've answered the EDA question about this feature: weak univariate signal. Going further would be feature engineering or feature selection work, which belongs in the modeling stage. The EDA plan scopes the exploration; "interesting pattern, warrants further modeling investigation" is a complete EDA finding.

This is the stopping criterion for planned EDA: when you've answered the scoped questions, you stop — not when you've exhausted all possible questions about the data.</div>
  </div>
  <div class="ep-nav">
    <button class="ep-btn ep-btn-play" onclick="epPlayAll()">▶ Show All</button>
    <span class="ep-progress" id="ep-prog3"></span>
  </div>
</div>
</div>

<script>
var epSubmitted=[false,false,false];
function epSubmit(n){
  epSubmitted[n-1]=true;
  document.getElementById("ep-ans"+n).style.display="block";
  var prog=document.getElementById("ep-prog"+n);
  if(prog){prog.textContent="Answer revealed";}
}
function epNav(n){
  epSubmit(n);
  document.getElementById("ep-step-"+n).classList.remove("ep-active");
  var next=document.getElementById("ep-step-"+(n+1));
  if(next){next.classList.add("ep-active");}
}
function epPlayAll(){
  for(var i=1;i<=3;i++){
    document.getElementById("ep-ans"+i).style.display="block";
    document.getElementById("ep-step-"+i).classList.add("ep-active");
  }
}
</script>

---

## Common mistakes

**EDA as a data audit.** If you're still checking for missing values and out-of-range values during EDA, the data audit wasn't complete. EDA assumes the data passed the audit. Mixing these phases makes it hard to know what you've formally checked versus what you noticed during exploration.

**Plotting everything.** A 13-feature dataset has 78 possible pairwise combinations. Plotting all of them produces noise, not insight. The EDA plan specifies which plots answer which questions. Plot what you need to answer those questions — nothing more.

**Treating EDA findings as modeling decisions.** "Chol has weak univariate signal" is an EDA finding. "We should drop chol from the model" is a modeling decision. Those are different stages. EDA findings feed the analysis plan, which then guides the modeling stage. Don't make modeling decisions during EDA.

**Open-ended EDA with no stopping criterion.** If you don't know when EDA is done, it's never done. The EDA plan defines done: when the scoped questions have been answered. New questions that emerge during EDA go into the analysis plan as open items for the modeling stage — they don't extend the EDA.

---

## In the basic-classification example

The EDA for the cardiac risk project is in [Basic Classification — Execution Lens](../../examples/basic-classification/execution.md). The three scoped questions from the EDA plan are answered in sequence: feature-target associations, correlation structure among the stress-test features, and sex-stratified subgroup analysis. The output feeds directly into the analysis plan's feature selection rationale.

---

## Run this gate with Codex

```text
Run the eda-plan skill.
The problem frame and data card are in problem_frame.md and data_card.md.
Ask me what questions the EDA needs to answer, then structure the exploration.
Write the output to analysis_plan.md.
```

```text
Run eda-plan in practitioner mode.
The key questions are: [feature-target associations, correlation structure, subgroup check by sex].
Write the analysis plan directly based on the data card.
```

---

*Previous gate: [Data Audit](data-audit.md) · Next gate: [Modeling](modeling.md)*
