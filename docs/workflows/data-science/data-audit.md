# Data Audit

The data audit is the second gate. It runs after problem framing and before any exploratory analysis. Its job is to determine whether the dataset is fit to answer the question in the problem frame — or whether there are quality issues, structural problems, or leakage risks that need to be addressed first.

A data audit is not EDA. EDA asks "what patterns exist?" The data audit asks "is this data trustworthy enough to draw conclusions from?"

---

## What Codex checks at this gate

**Schema and structure** — what columns exist, what types they are, how many rows, whether any columns are obviously mislabeled or mistyped. This is table stakes. A column called `age` storing string values is a problem before anything else.

**Missingness** — which columns have missing values, how many, and whether the missingness is random or systematic. Random missingness (5% of patients are missing cholesterol) is manageable. Systematic missingness (all patients missing cholesterol happen to be the sickest) introduces bias that no imputation strategy fixes.

**Distribution checks** — are numeric values in plausible ranges? Are categorical levels what you'd expect? A `thalach` (max heart rate) value of 500 is impossible — it's either an error or a coding artifact. Out-of-range values propagate through every downstream step.

**Leakage checks** — does anything in the dataset carry information that wouldn't be available at prediction time? This is where prediction time from the problem frame connects to the data. Every column gets reviewed against the prediction-time anchor.

**Stop conditions** — is there a data quality problem serious enough that analysis shouldn't proceed? The audit has an explicit decision point: proceed, stop-and-fix, or flag-and-proceed-with-caveats.

Codex writes the output to `data_card.md`. The data card is a living document — it gets updated as the project advances and new data quality facts emerge.

---

## Why missingness matters more than you think

The instinct when encountering missing values is to impute them and move on. Imputation is often correct — but only after you've understood *why* values are missing.

In the Cleveland dataset, the `ca` (vessels colored by fluoroscopy) and `thal` (thalassemia result) columns each have a small number of missing values (about 4-6 patients). For this dataset, the missingness is probably random — data entry artifacts from a 1988 clinical collection. Dropping or imputing is defensible, and the data card should say so.

But if you found that `thal` was missing for all patients who didn't proceed past an initial screening, that's systematic. Those patients are probably systematically different from those who stayed in the study. No imputation strategy handles that correctly — it would need to be flagged as a structural limitation of the analysis.

The data audit forces this question before modeling starts.

---

## Try it: audit the cardiac dataset

These are the questions Codex would ask you at the data audit gate. Try answering before revealing the expected response.

<style>
.da-terminal{font-family:'JetBrains Mono','Courier New',monospace;font-size:0.82rem;line-height:1.65;background:#0d1b2e;border-radius:10px;padding:1.25rem 1.4rem;margin:1.4rem 0;border:1px solid #1a2f4a;}
.da-label{font-size:0.7rem;letter-spacing:0.06em;text-transform:uppercase;color:#6c7a8d;margin-bottom:0.9rem;}
.da-q{color:#f4a261;margin-bottom:0.7rem;font-weight:600;}
.da-ta{width:100%;background:#0a1628;border:1px solid #1e3a5f;border-radius:6px;color:#e2e8f0;padding:0.6rem 0.8rem;font-family:inherit;font-size:0.82rem;resize:vertical;min-height:70px;box-sizing:border-box;margin-bottom:0.6rem;}
.da-ta:focus{outline:none;border-color:#3bc9db;}
.da-btn{background:#1e3a5f;color:#e2e8f0;border:none;padding:0.4rem 1rem;border-radius:5px;cursor:pointer;font-family:inherit;font-size:0.8rem;margin-right:0.5rem;}
.da-btn:hover{background:#2d5282;}
.da-btn-play{background:#f4a261;color:#1a0a00;}
.da-btn-play:hover{background:#e8935a;}
.da-answer{display:none;margin-top:0.8rem;padding:0.8rem 1rem;background:#0a1e35;border-radius:6px;border-left:3px solid #a6e3a1;}
.da-answer-label{color:#6c7a8d;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.05em;margin-bottom:0.4rem;}
.da-answer-text{color:#a6e3a1;white-space:pre-wrap;}
.da-nav{margin-top:0.8rem;display:flex;align-items:center;gap:0.5rem;}
.da-step{display:none;}
.da-step.da-active{display:block;}
.da-progress{color:#6c7a8d;font-size:0.75rem;}
</style>

<div class="da-terminal">
<div class="da-label">Data Audit — Try It</div>
<div id="da-step-1" class="da-step da-active">
  <div class="da-q">Q1 of 3 — Missingness assessment</div>
  <div style="color:#cbd5e1;margin-bottom:0.8rem;">The Cleveland dataset has missing values in `ca` (4 missing) and `thal` (2 missing) out of 303 rows. All other columns are complete. How do you handle this, and what goes in the data card?</div>
  <textarea class="da-ta" id="da-a1" placeholder="Your answer…"></textarea>
  <div><button class="da-btn" onclick="daSubmit(1)">Submit</button></div>
  <div class="da-answer" id="da-ans1">
    <div class="da-answer-label">Expected audit response</div>
    <div class="da-answer-text">6 missing values out of 303 rows (~2%) across two columns. First question: is the missingness random?

For ca and thal: these are diagnostic results from fluoroscopy and a thalassemia test — both test-ordered results. Plausible reasons for missingness: test not ordered, patient declined, result not recorded. No strong reason to believe missingness correlates with disease severity. Verdict: likely missing at random.

Decision: drop the 6 rows for the baseline model. This leaves 297 rows — negligible information loss. Imputation is also defensible (mean/median for numeric, mode for categorical) and should be explored during EDA.

Data card entry: "ca and thal have 6 missing values total (2%). Assumed MCAR based on clinical context. Rows dropped for baseline; imputation explored as a robustness check."

If missingness were higher (>10%) or systematically correlated with the target, the decision would be different and the data card would say so explicitly.</div>
  </div>
  <div class="da-nav">
    <button class="da-btn" onclick="daNav(1)">Next →</button>
    <span class="da-progress" id="da-prog1"></span>
  </div>
</div>
<div id="da-step-2" class="da-step">
  <div class="da-q">Q2 of 3 — Distribution check</div>
  <div style="color:#cbd5e1;margin-bottom:0.8rem;">During the data audit you notice that `thalach` (maximum heart rate achieved) has a minimum value of 71. The normal clinical range for maximum heart rate during a stress test is roughly 120–200 bpm for adults. Is 71 a red flag, and what do you do?</div>
  <textarea class="da-ta" id="da-a2" placeholder="Your answer…"></textarea>
  <div><button class="da-btn" onclick="daSubmit(2)">Submit</button></div>
  <div class="da-answer" id="da-ans2">
    <div class="da-answer-label">Expected audit response</div>
    <div class="da-answer-text">71 bpm is low but not impossible — elderly patients, patients on beta blockers, or patients who couldn't complete the full stress test may have a max HR well below 120. It's not necessarily an error.

The audit response: flag it, document it, but don't drop it. Check: what's the age and clinical context of that patient? If the low HR corresponds to an elderly patient with known comorbidities, it's probably real. If it's a 35-year-old with no noted limitations, it warrants investigation.

Data card entry: "thalach has a minimum of 71 bpm. Flagged for clinical plausibility review. Low values retained unless corroborating evidence of data entry error."

The goal is to document the flag and keep it visible for the EDA and modeling stages. The data audit doesn't require resolution — it requires honesty about what you found.</div>
  </div>
  <div class="da-nav">
    <button class="da-btn" onclick="daNav(2)">Next →</button>
    <span class="da-progress" id="da-prog2"></span>
  </div>
</div>
<div id="da-step-3" class="da-step">
  <div class="da-q">Q3 of 3 — Stop condition</div>
  <div style="color:#cbd5e1;margin-bottom:0.8rem;">Imagine you discovered that the `thal` column (thalassemia result) was entered by the physician doing the final diagnosis — after they already knew whether the patient had heart disease. Would this be a stop condition? Why or why not?</div>
  <textarea class="da-ta" id="da-a3" placeholder="Your answer…"></textarea>
  <div><button class="da-btn" onclick="daSubmit(3)">Submit</button></div>
  <div class="da-answer" id="da-ans3">
    <div class="da-answer-label">Expected audit response</div>
    <div class="da-answer-text">Yes — this would be a stop condition for the feature as currently used.

If the physician entered thal after knowing the diagnosis, then thal carries information from the future — it's outcome-correlated not because of underlying biology, but because of how it was recorded. Including it in the model would produce a classifier that appears to predict heart disease but is actually partially encoding the diagnosis itself.

This is one of the most damaging forms of leakage: it's not visible in the data, it doesn't produce obvious out-of-range values, and it can produce an apparently great model that falls apart in deployment (because in production, thal is filled in before the diagnosis is known — or it isn't filled in yet at all).

The data audit action: escalate to the domain expert or PI. If confirmed, thal should be excluded from the model. If the concern is unresolvable without more documentation, the data card should flag it and the model card should document the risk explicitly.

This is why the data audit is a gate, not a checkbox. It surfaces decisions that no amount of modeling sophistication can work around.</div>
  </div>
  <div class="da-nav">
    <button class="da-btn da-btn-play" onclick="daPlayAll()">▶ Show All</button>
    <span class="da-progress" id="da-prog3"></span>
  </div>
</div>
</div>

<script>
var daSubmitted=[false,false,false];
function daSubmit(n){
  var ta=document.getElementById("da-a"+n);
  daSubmitted[n-1]=true;
  document.getElementById("da-ans"+n).style.display="block";
  var prog=document.getElementById("da-prog"+n);
  if(prog){prog.textContent="Answer revealed";}
}
function daNav(n){
  daSubmit(n);
  document.getElementById("da-step-"+n).classList.remove("da-active");
  var next=document.getElementById("da-step-"+(n+1));
  if(next){next.classList.add("da-active");}
}
function daPlayAll(){
  for(var i=1;i<=3;i++){
    document.getElementById("da-ans"+i).style.display="block";
    document.getElementById("da-step-"+i).classList.add("da-active");
  }
}
</script>

---

## Common mistakes

**Treating the data audit as a formality.** Running a quick `.info()` and moving on is not a data audit. The audit has an explicit decision point: is this dataset fit for the analysis in the problem frame? That question requires checking against the problem frame, not just against the data.

**Conflating data audit with EDA.** EDA is open-ended exploration. The data audit is scoped: schema, missingness, plausibility, leakage. EDA comes after the audit confirms the data is usable. Mixing them obscures whether the data passed the quality gate.

**Dropping missing values without documenting why.** "I dropped 6 rows with missing data" is not a data card entry. "6 rows missing ca or thal, assumed MCAR based on clinical context, dropped for baseline" is. The difference matters when someone later asks why the sample size is 297, not 303.

**Skipping the leakage check on columns already in the dataset.** Leakage isn't just about joining in future data — it's about any feature whose value in the training dataset encodes information that wouldn't exist at prediction time. Features collected historically can still be leaky if they were collected *after* the outcome.

---

## In the basic-classification example

The data card for the cardiac risk project is produced at this gate. See [Basic Classification — Practitioner Lens](../../examples/basic-classification/practitioner.md) for the full data audit session, including the missingness decision for `ca` and `thal`, the leakage review against the post-stress-test prediction time anchor, and the resulting `data_card.md`.

---

## Run this gate with Codex

```text
Run the data-audit skill.
Check for schema issues, missingness, distribution anomalies, and leakage risks.
Write the output to data_card.md.
Ask me before deciding on any stop conditions.
```

```text
Run data-audit in practitioner mode.
Summarize findings and write data_card.md directly.
Flag anything that requires a decision from me before proceeding.
```

---

*Previous gate: [Problem Framing](problem-framing.md) · Next gate: [EDA Plan](eda-plan.md)*
