# Basic Classification — Learning Lens

You're predicting whether a patient has heart disease — a binary classification task with real clinical stakes. The dataset is the [Cleveland Heart Disease dataset](https://www.kaggle.com/datasets/cherngs/heart-disease-cleveland-uci): 303 patients, 13 features, one question: should this patient be referred for further cardiac evaluation?

**Student mode means attempt-before-answer**: type your reasoning at each step before Codex reveals its output. By the end you'll understand why each gate exists and have a full set of artifacts a collaborator could pick up and continue.

Ready to execute yourself? [See the practitioner path →](execution.md) | Want to see how a manager reviews this project? [Manager lens →](manager.md)

---

## Walk Through the 7 Gates

At each gate below, Codex asks for your reasoning first. Type something — even a rough guess — then click **See what Codex said** to reveal the output. Step 1 is shown open so you can see the pattern.

<div id="cl-root" style="font-family:'JetBrains Mono','Courier New',monospace;background:#0d1b2e;border-radius:10px;padding:24px 28px 20px 28px;max-width:680px;margin:32px 0;box-shadow:0 4px 32px rgba(0,0,0,0.45);border:1px solid #1a2f4a;">

  <div style="display:flex;align-items:center;gap:8px;margin-bottom:16px;">
    <span style="width:12px;height:12px;border-radius:50%;background:#ff5f56;display:inline-block;"></span>
    <span style="width:12px;height:12px;border-radius:50%;background:#ffbd2e;display:inline-block;"></span>
    <span style="width:12px;height:12px;border-radius:50%;background:#27c93f;display:inline-block;"></span>
    <span id="cl-step-label" style="margin-left:12px;font-size:0.78rem;color:#4a6885;letter-spacing:0.04em;">Step 1 of 7 — Problem Framing</span>
  </div>

  <div id="cl-body" style="min-height:320px;">
    <div id="cl-prompt" style="color:#3bc9db;font-size:0.85rem;margin-bottom:14px;"></div>
    <div style="color:#4a6885;font-size:0.72rem;margin-bottom:4px;text-transform:uppercase;letter-spacing:0.08em;">Codex asks</div>
    <div id="cl-question" style="color:#f4a261;font-size:0.87rem;line-height:1.55;margin-bottom:14px;min-height:44px;white-space:pre-wrap;"></div>
    <div style="color:#4a6885;font-size:0.72rem;margin-bottom:6px;text-transform:uppercase;letter-spacing:0.08em;">Your attempt</div>
    <textarea id="cl-textarea" placeholder="Type your reasoning before seeing Codex's response…" style="width:100%;box-sizing:border-box;background:#091422;border:1px solid #1e3a5a;border-radius:6px;color:#e2e8f0;font-family:inherit;font-size:0.82rem;line-height:1.5;padding:8px 10px;resize:vertical;min-height:60px;outline:none;transition:border-color 200ms ease;" onfocus="this.style.borderColor='#3bc9db'" onblur="this.style.borderColor='#1e3a5a'"></textarea>
    <button id="cl-submit" onclick="clSubmit()" style="margin-top:8px;background:#f4a261;color:#1a0a00;border:none;border-radius:5px;padding:6px 18px;font-family:inherit;font-size:0.8rem;font-weight:700;cursor:pointer;">See what Codex said →</button>

    <div id="cl-answer-wrap" style="display:none;margin-top:18px;">
      <div style="color:#4a6885;font-size:0.72rem;margin-bottom:4px;text-transform:uppercase;letter-spacing:0.08em;">Codex output</div>
      <div id="cl-answer" style="color:#a6e3a1;font-size:0.84rem;line-height:1.55;margin-bottom:16px;white-space:pre-wrap;"></div>
      <div id="cl-badge" style="display:inline-block;background:#1a2f4a;border:1px solid #3bc9db;border-radius:5px;padding:4px 12px;font-size:0.74rem;color:#3bc9db;"></div>
    </div>
  </div>

  <div style="display:flex;gap:10px;margin-top:22px;align-items:center;flex-wrap:wrap;">
    <button id="cl-prev" onclick="clNav(-1)" style="background:#1a2f4a;color:#3bc9db;border:1px solid #3bc9db;border-radius:5px;padding:6px 18px;font-family:inherit;font-size:0.8rem;cursor:pointer;">← Prev</button>
    <button id="cl-next" onclick="clNav(1)" style="background:#1a2f4a;color:#3bc9db;border:1px solid #3bc9db;border-radius:5px;padding:6px 18px;font-family:inherit;font-size:0.8rem;cursor:pointer;">Next →</button>
    <button id="cl-play" onclick="clPlay()" style="background:#0d1b2e;color:#f4a261;border:1px solid #f4a261;border-radius:5px;padding:6px 18px;font-family:inherit;font-size:0.8rem;cursor:pointer;">▶ Play all</button>
    <span id="cl-dots" style="margin-left:4px;color:#4a6885;font-size:0.78rem;letter-spacing:0.12em;"></span>
  </div>
</div>

<script>
(function () {
  var steps = [
    {
      label: "Step 1 of 7 — Problem Framing",
      prompt: "$ codex run problem_frame.md --skill problem-framing",
      question: "The dataset has a 'target' column that ranges from 0 to 4 — 0 means no disease, 1–4 indicates increasing severity. Should the model predict the full 0–4 scale, or convert this to a binary target? What decision does this model support?",
      answer: "Binary target (0 = no disease, 1+ = disease present). The decision is a referral: should this patient proceed to further cardiac evaluation? A 5-class severity prediction doesn't map cleanly to that binary gate. Metric: ROC-AUC — more informative than accuracy for an imbalanced clinical dataset where the threshold choice matters.\n\n✓ Decision context: cardiology referral triage\n✓ Target: binary (0 / 1+)\n✓ Metric: ROC-AUC",
      artifact: "✓ artifact written: problem_frame.md"
    },
    {
      label: "Step 2 of 7 — Data Audit",
      prompt: "$ codex run data_audit.md --skill data-audit",
      question: "The features exang (exercise-induced angina), oldpeak (ST depression after exercise), slope, thalach (max heart rate), and thal (thalassemia type) are all measured during or after a stress test. What's the leakage risk here, and what do you need to know before deciding whether to include them?",
      answer: "Leakage risk: if the model is used before the stress test has been run, these features aren't available at prediction time — including them would train on future information.\n\nThe fix: clarify prediction time. If this model is meant to flag patients before any stress test, drop all stress-test features. If it runs after the stress test as a second-opinion tool, they're fine.\n\nThis is a design decision that must be documented in problem_frame.md before proceeding.\n\n✓ Leakage risk flagged for: exang, oldpeak, slope, thalach, thal\n✓ Prediction time: requires explicit decision",
      artifact: "✓ artifact written: data_card.md"
    },
    {
      label: "Step 3 of 7 — Missingness",
      prompt: "$ codex run data_audit.md — missingness review",
      question: "The thal (thalassemia type) and ca (number of major vessels) columns have a handful of missing values. What would you do with them, and why does the choice matter more here than in a large dataset?",
      answer: "With only 303 rows, every dropped row costs meaningful signal. For thal (categorical, 2 missing): mode imputation or a dedicated 'unknown' category — don't drop. For ca (ordinal count, 4 missing): median imputation is risky because ca has clinical meaning (0, 1, 2, 3 vessels affected). Flag as 'unknown' or impute with caution and document the decision.\n\nThe key principle: imputation choices must be documented. A future session that retrains the model needs to apply the same transformations.\n\n✓ Missingness plan documented in data_card.md",
      artifact: "✓ artifact updated: data_card.md"
    },
    {
      label: "Step 4 of 7 — Split Strategy",
      prompt: "$ codex run split_strategy.md --skill analysis-plan",
      question: "With 303 rows and roughly 54% positive class, what split strategy would you use? Is standard random splitting appropriate here, or does anything about the dataset call for a different approach?",
      answer: "Stratified 80/20 split. Reason: with only ~165 positive cases, a random split could produce an unrepresentative test set by chance. Stratification preserves the class ratio in both halves.\n\nNo time-ordering concern here (unlike longitudinal data), so temporal split isn't needed. Fix the random seed for reproducibility — the test set must not be touched until final evaluation.\n\n✓ Split: 80/20 stratified, seed=42\n✓ Test set locked — no peeking",
      artifact: "✓ artifact written: analysis_plan.md"
    },
    {
      label: "Step 5 of 7 — Baseline Model",
      prompt: "$ codex run baseline.md --skill modeling",
      question: "What's the simplest baseline you'd fit first? Why does it matter to run a baseline before trying random forests or gradient boosting?",
      answer: "Logistic regression. It's interpretable, trains instantly on 303 rows, and gives you a calibrated probability — useful for threshold analysis.\n\nThe baseline matters because it sets the floor. If logistic regression gets ROC-AUC 0.87, a random forest that gets 0.88 after hours of tuning probably isn't worth the added complexity. If the baseline is 0.65, there's room to improve and it makes sense to try more.\n\nBaseline result: logistic regression, ROC-AUC 0.87 on holdout.\n\n✓ experiment_log.md entry 001 written\n✓ Baseline established — no model should be accepted below this",
      artifact: "✓ artifact written: experiment_log.md (entry 001)"
    },
    {
      label: "Step 6 of 7 — Evaluation",
      prompt: "$ codex run evaluation.md --skill model-evaluation",
      question: "The logistic regression baseline gets ROC-AUC 0.87. Before declaring it good enough, what else would you want to know? Think about the clinical context — what kind of errors matter most here?",
      answer: "At the default 0.5 threshold: 12 false negatives (patients with heart disease predicted as healthy). In a referral tool, false negatives are more costly than false positives — a missed referral is worse than an unnecessary one.\n\nThe threshold should be lowered (e.g., to 0.3) to reduce false negatives, accepting more false positives. This is a clinical policy decision, not a data science one — it belongs in the model card as a configurable parameter.\n\nAlso check: calibration (do predicted probabilities match observed rates?), performance across sex subgroups (sex is a feature — is performance equal across groups?).\n\n✓ Threshold recommendation: 0.3 for referral use case\n✓ Subgroup analysis flagged for model card",
      artifact: "✓ artifact written: model_card.md (draft)"
    },
    {
      label: "Step 7 of 7 — Model Card",
      prompt: "$ codex run model_card.md --skill model-card",
      question: "What are the three most important things to document in the model card for a classifier like this — trained on 303 patients from one clinic in Cleveland?",
      answer: "1. Population scope: trained on patients referred to a Cleveland clinic in the 1980s. Should not be applied to general-population screening without validation on a more representative sample.\n\n2. Failure modes: false negatives at default threshold — patients with disease can be predicted healthy. The threshold must be explicitly set for the deployment context.\n\n3. Fairness flag: sex is a predictive feature. Performance should be validated separately for male and female patients before clinical deployment.\n\n✓ Model card complete\n✓ Workflow trace updated — project ready for review",
      artifact: "✓ artifact written: model_card.md, workflow_trace.md"
    }
  ];

  var current = 0;
  var submitted = new Array(steps.length).fill(false);
  var savedAttempts = new Array(steps.length).fill('');
  submitted[0] = true;

  function dots() {
    var d = '';
    for (var i = 0; i < steps.length; i++) d += (i === current ? '●' : '○');
    document.getElementById('cl-dots').textContent = d;
  }

  function showAnswer() {
    var s = steps[current];
    var wrap = document.getElementById('cl-answer-wrap');
    var ans = document.getElementById('cl-answer');
    var badge = document.getElementById('cl-badge');
    ans.textContent = s.answer;
    badge.textContent = s.artifact;
    wrap.style.display = 'block';
    wrap.style.opacity = '0';
    wrap.style.transition = 'opacity 350ms ease';
    setTimeout(function(){ wrap.style.opacity = '1'; }, 10);
  }

  function setStep(idx, skipType) {
    savedAttempts[current] = document.getElementById('cl-textarea').value;
    current = idx;
    var s = steps[current];
    document.getElementById('cl-step-label').textContent = s.label;
    document.getElementById('cl-prompt').textContent = s.prompt;
    document.getElementById('cl-question').textContent = s.question;
    document.getElementById('cl-textarea').value = savedAttempts[current];
    document.getElementById('cl-answer-wrap').style.display = 'none';
    document.getElementById('cl-prev').disabled = (current === 0);
    document.getElementById('cl-next').disabled = (current === steps.length - 1);
    if (submitted[current]) showAnswer();
    if (!skipType) {
      document.getElementById('cl-prompt').style.opacity = '0';
      setTimeout(function(){ document.getElementById('cl-prompt').style.opacity = '1'; }, 100);
    }
    dots();
  }

  window.clSubmit = function() {
    var ta = document.getElementById('cl-textarea');
    if (!ta.value.trim()) {
      ta.style.borderColor = '#e05c5c';
      setTimeout(function(){ ta.style.borderColor = '#1e3a5a'; }, 700);
      return;
    }
    submitted[current] = true;
    showAnswer();
  };

  window.clNav = function(dir) {
    var next = current + dir;
    if (next >= 0 && next < steps.length) setStep(next);
  };

  var playing = false;
  window.clPlay = function() {
    if (playing) return;
    playing = true;
    document.getElementById('cl-play').disabled = true;
    var i = 0;
    function autoAdvance() {
      if (i >= steps.length) { playing = false; document.getElementById('cl-play').disabled = false; return; }
      setStep(i, true);
      submitted[i] = true;
      showAnswer();
      i++;
      setTimeout(autoAdvance, 2200);
    }
    autoAdvance();
  };

  setStep(0, true);
  dots();
})();
</script>

---

## Try It for Real

Once you've worked through the demo, run this in Codex to start the actual project:

```text
Use tutor mode to guide me through a cardiac risk classification project.

Dataset: Heart Disease Cleveland UCI
(https://www.kaggle.com/datasets/cherngs/heart-disease-cleveland-uci)
Goal: predict presence of heart disease. Binary target (0 = no disease, 1+ = disease).
Decision context: should this patient be referred for further cardiac evaluation?
Metric: ROC-AUC.

Start with the problem-framing skill. Ask for my reasoning before each gate output.
```

---

## What You Built

Seven artifact files and a clear sense of why each gate exists:

- `problem_frame.md` — binary target, ROC-AUC metric, referral decision context
- `data_card.md` — leakage risk documented, missingness plan recorded
- `analysis_plan.md` — stratified 80/20 split, seed locked, test set frozen
- `experiment_log.md` — baseline result on record; any future run must beat it
- `model_card.md` — population scope, failure modes, fairness flag
- `workflow_trace.md` — full session record; next session starts from real project state

The same backbone runs regardless of problem type. The artifacts change in content, not in structure.

---

## Where To Go Next

- [Execution lens →](execution.md) — same project, practitioner pace, no coaching scaffolding
- [Manager lens →](manager.md) — how a clinical stakeholder reviews these artifacts and makes a go/no-go call
- [Core Data Science Workflow](../../workflows/data-science/index.md) — the seven-stage sequence underneath this example
