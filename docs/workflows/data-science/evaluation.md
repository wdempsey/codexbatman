# Evaluation

The evaluation gate runs after modeling selects a model. It asks a harder question than "does the model perform well?" — it asks "does the model perform well enough to be trusted for the decision in the problem frame?"

These are different questions. A model with ROC-AUC 0.90 is impressive on paper. Whether it's trustworthy for a clinical referral decision requires examining the failure modes: where does it fail, how badly, and for whom?

---

## What the evaluation gate covers

**Metric evaluation against the success criterion.** The first check is mechanical: does the model meet the criterion the problem frame set? If ROC-AUC ≥ 0.85 was the criterion, report the held-out test set performance. Not the CV score used for model selection — a separate held-out test set that was never used during training or selection.

**Confusion matrix at the operating threshold.** ROC-AUC aggregates performance across all thresholds. Deployment uses one threshold. The confusion matrix at the chosen threshold shows the actual count of true positives, false positives, true negatives, and false negatives. For a referral classifier, that means: how many patients with disease get correctly flagged, and how many patients without disease get unnecessarily referred?

**Error analysis.** Where does the model fail? Look at the misclassified cases. Are false negatives concentrated in a particular age group, sex, or presentation type? Systematic errors reveal limitations that aggregate metrics hide.

**Subgroup performance.** If the EDA identified subgroups of interest (sex, age band, symptom type), report performance separately for each. A model that achieves ROC-AUC 0.90 overall but 0.75 for female patients has a fairness and clinical concern that the overall metric doesn't surface.

**Limitations section in the model card.** The evaluation gate produces the limitations section: what the model does poorly, what populations it shouldn't be applied to, and what deployment conditions it requires. This section is not optional — it's the primary accountability artifact.

---

## Threshold is a policy decision

The ROC curve traces model performance across all possible operating thresholds. Choosing a threshold is not a data science decision — it's a policy decision that depends on the cost of each error type.

For the cardiac referral classifier: a false negative (missed disease, no referral) means a sick patient doesn't get seen by a cardiologist. A false positive (unnecessary referral) means a healthy patient gets an unnecessary follow-up. These costs are not symmetric, and clinicians will have a view on the acceptable tradeoff.

At threshold 0.5, the model treats both error types equally. At threshold 0.3, the model is more sensitive — it catches more disease cases, but generates more unnecessary referrals. The right threshold is determined by clinical context and institutional tolerance.

The evaluation gate documents what the confusion matrix looks like at several candidate thresholds and surfaces the decision to the domain expert or PI. It does not pick the threshold — it provides the information for the threshold to be chosen.

---

## Try it: evaluate the cardiac classifier

<style>
.ev-terminal{font-family:'JetBrains Mono','Courier New',monospace;font-size:0.82rem;line-height:1.65;background:#0d1b2e;border-radius:10px;padding:1.25rem 1.4rem;margin:1.4rem 0;border:1px solid #1a2f4a;}
.ev-label{font-size:0.7rem;letter-spacing:0.06em;text-transform:uppercase;color:#7d90a8;margin-bottom:0.9rem;}
.ev-q{color:#f4a261;margin-bottom:0.7rem;font-weight:600;}
.ev-ta{width:100%;background:#0a1628;border:1px solid #1e3a5f;border-radius:6px;color:#e2e8f0;padding:0.6rem 0.8rem;font-family:inherit;font-size:0.82rem;resize:vertical;min-height:70px;box-sizing:border-box;margin-bottom:0.6rem;}
.ev-ta:focus{outline:none;border-color:#3bc9db;}
.ev-btn{background:#1e3a5f;color:#e2e8f0;border:none;padding:0.4rem 1rem;border-radius:5px;cursor:pointer;font-family:inherit;font-size:0.8rem;margin-right:0.5rem;}
.ev-btn:hover{background:#2d5282;}
.ev-btn-play{background:#f4a261;color:#1a0a00;}
.ev-btn-play:hover{background:#e8935a;}
.ev-answer{display:none;margin-top:0.8rem;padding:0.8rem 1rem;background:#0a1e35;border-radius:6px;border-left:3px solid #a6e3a1;}
.ev-answer-label{color:#7d90a8;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.05em;margin-bottom:0.4rem;}
.ev-answer-text{color:#a6e3a1;white-space:pre-wrap;}
.ev-nav{margin-top:0.8rem;display:flex;align-items:center;gap:0.5rem;}
.ev-step{display:none;}
.ev-step.ev-active{display:block;}
.ev-progress{color:#7d90a8;font-size:0.75rem;}
</style>

<div class="ev-terminal">
<div class="ev-label">Evaluation — Try It</div>
<div id="ev-step-1" class="ev-step ev-active">
  <div class="ev-q">Q1 of 3 — CV vs. held-out performance</div>
  <div style="color:#cbd5e1;margin-bottom:0.8rem;">Your logistic regression achieved CV ROC-AUC of 0.906 during model selection. On the held-out test set, it achieves 0.878. Is this concerning? How do you report it?</div>
  <textarea class="ev-ta" id="ev-a1" placeholder="Your answer…"></textarea>
  <div><button class="ev-btn" onclick="evSubmit(1)">Submit</button></div>
  <div class="ev-answer" id="ev-ans1">
    <div class="ev-answer-label">Expected evaluation response</div>
    <div class="ev-answer-text">A 0.028 drop from CV to held-out is expected and not concerning. CV estimates have variance — with 5 folds on 297 rows, you're averaging over folds of about 60 rows each, which means each fold estimate has sampling variance. A difference of ~0.03 is well within expected noise.

It would be concerning if the gap were large (>0.1) — that would suggest overfitting, possibly from tuning hyperparameters against the CV score. Here, no tuning was done, so the gap is pure sampling variance.

How to report: report both numbers. "5-fold CV ROC-AUC: 0.906 (±std). Held-out test set ROC-AUC: 0.878." The held-out number is the honest estimate of performance on new data. The CV number is what was used to select the model. Both belong in the model card.

The success criterion was ≥ 0.85. Held-out performance of 0.878 satisfies the criterion. Advance to the confusion matrix analysis.</div>
  </div>
  <div class="ev-nav">
    <button class="ev-btn" onclick="evNav(1)">Next →</button>
    <span class="ev-progress" id="ev-prog1"></span>
  </div>
</div>
<div id="ev-step-2" class="ev-step">
  <div class="ev-q">Q2 of 3 — Confusion matrix interpretation</div>
  <div style="color:#cbd5e1;margin-bottom:0.8rem;">At threshold 0.5, the model produces: TP=28, FP=8, TN=27, FN=10 (test set of 73 patients). What is the clinical interpretation, and what would you present to the PI?</div>
  <textarea class="ev-ta" id="ev-a2" placeholder="Your answer…"></textarea>
  <div><button class="ev-btn" onclick="evSubmit(2)">Submit</button></div>
  <div class="ev-answer" id="ev-ans2">
    <div class="ev-answer-label">Expected evaluation response</div>
    <div class="ev-answer-text">Clinical interpretation: of 38 patients with disease, the model correctly flags 28 (73.7% sensitivity). It misses 10 (26.3% miss rate). Of 35 patients without disease, it correctly clears 27 (77.1% specificity) and unnecessarily refers 8 (22.9% unnecessary referral rate).

For a clinical PI, the key question is: is a 26% miss rate on disease acceptable? At threshold 0.5, the model catches about 3 in 4 disease cases. Whether that's good enough depends on the clinical context — what happens to the 1 in 4 who are missed?

What to present to the PI: the confusion matrix at threshold 0.5, plus the same table at threshold 0.4 (more sensitive: catches more disease but more unnecessary referrals) and threshold 0.6 (more specific: fewer unnecessary referrals but more missed cases). The PI chooses the threshold based on clinical policy, not model optimization.

Sensitivity and specificity at the current threshold belong in the model card limitations section, with explicit acknowledgment that the miss rate has clinical significance.</div>
  </div>
  <div class="ev-nav">
    <button class="ev-btn" onclick="evNav(2)">Next →</button>
    <span class="ev-progress" id="ev-prog2"></span>
  </div>
</div>
<div id="ev-step-3" class="ev-step">
  <div class="ev-q">Q3 of 3 — Limitations</div>
  <div style="color:#cbd5e1;margin-bottom:0.8rem;">Write one limitation that belongs in the model card for the cardiac risk classifier. It should be specific enough that a clinician who read it would know what situation to be cautious in.</div>
  <textarea class="ev-ta" id="ev-a3" placeholder="Your answer…"></textarea>
  <div><button class="ev-btn" onclick="evSubmit(3)">Submit</button></div>
  <div class="ev-answer" id="ev-ans3">
    <div class="ev-answer-label">Example limitation</div>
    <div class="ev-answer-text">Example: "The model was trained on data from the Cleveland Clinic collected in 1988 (n=303). The training population was 68% male, with an age range of 29–77. Performance on female patients, patients outside this age range, or patients from different clinical settings has not been validated. Exercise caution when applying this classifier to populations substantially different from the training sample."

What makes this specific: it names the source institution, the year, the demographic composition, and the unstudied populations. A clinician reading this knows that for a 28-year-old female patient, this model hasn't been tested and shouldn't be trusted without caution.

Vague limitations ("model may not generalize to all populations") are worse than no limitations — they create the appearance of caution without providing actionable guidance. Specific limitations name what was and wasn't tested.</div>
  </div>
  <div class="ev-nav">
    <button class="ev-btn ev-btn-play" onclick="evPlayAll()">▶ Show All</button>
    <span class="ev-progress" id="ev-prog3"></span>
  </div>
</div>
</div>

<script>
var evSubmitted=[false,false,false];
function evSubmit(n){
  evSubmitted[n-1]=true;
  document.getElementById("ev-ans"+n).style.display="block";
  var prog=document.getElementById("ev-prog"+n);
  if(prog){prog.textContent="Answer revealed";}
}
function evNav(n){
  evSubmit(n);
  document.getElementById("ev-step-"+n).classList.remove("ev-active");
  var next=document.getElementById("ev-step-"+(n+1));
  if(next){next.classList.add("ev-active");}
}
function evPlayAll(){
  for(var i=1;i<=3;i++){
    document.getElementById("ev-ans"+i).style.display="block";
    document.getElementById("ev-step-"+i).classList.add("ev-active");
  }
}
</script>

---

## Common mistakes

**Reporting CV score as final performance.** If you tuned any hyperparameters, the CV score is optimistic. Final performance must be reported on a held-out test set that was never used during model selection or tuning.

**Only reporting aggregate metrics.** ROC-AUC 0.90 sounds good. The confusion matrix at the deployment threshold tells you what "0.90" actually means in terms of missed cases and false alarms. Always report the confusion matrix.

**Skipping subgroup analysis.** A model that works well on average can fail badly for a specific group. If you identified subgroups during EDA, you're committed to checking them at evaluation. Reporting only overall metrics when subgroup failures are likely is a methodological choice that should be explicit.

**Vague limitations.** "Model may not generalize" is not a limitation — it's a platitude. Limitations specify what hasn't been tested, for whom, and under what conditions. If you can't write a specific limitation, you haven't finished the evaluation.

---

## In the basic-classification example

The full evaluation for the cardiac risk project is in [Basic Classification — Practitioner Lens](../../examples/basic-classification/practitioner.md), including the confusion matrix at threshold 0.5, the sex-stratified performance check, and the limitations section of the model card.

---

## Run this gate with Codex

```text
Run the model-evaluation skill.
The model card is in model_card.md. The test set has not been used during training.
Report performance on the held-out set, generate the confusion matrix at threshold 0.5,
and check performance by sex. Write limitations to model_card.md.
```

```text
Run model-evaluation in practitioner mode.
Metric: ROC-AUC. Generate confusion matrices at thresholds 0.4, 0.5, 0.6.
Write a specific limitations section to model_card.md.
```

---

*Previous gate: [Modeling](modeling.md) · Next gate: [Experiment Log](experiment-log.md)*
