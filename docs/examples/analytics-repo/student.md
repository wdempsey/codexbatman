# Analytics Repo Example — Student Path

This is the primary starting point for students building a real data science project with Codex.
You'll build a housing-price prediction repository step by step, following the same eight-gate workflow that practitioners use.
**Student mode means attempt-before-answer**: type your reasoning at each step before Codex reveals its output.
By the end you'll have eight durable artifacts — `problem_frame.md`, `data_card.md`, `analysis_plan.md`, `experiment_log.md` (×3), `model_card.md`, and `workflow_trace.md` — that any collaborator can pick up next session.

Already know the workflow? [See the practitioner path →](practitioner.md)

---

## Walk Through the 8-Step Sequence

At each gate below, Codex asks for your reasoning first. Type something in the box — even a rough guess — then click **See what Codex said** to reveal the answer. Step 1 is shown open so you can see the pattern before you start.

<div id="codex-terminal-root" style="font-family:'JetBrains Mono','Courier New',monospace;background:#0d1b2e;border-radius:10px;padding:24px 28px 20px 28px;max-width:660px;margin:32px 0;box-shadow:0 4px 32px rgba(0,0,0,0.45);border:1px solid #1a2f4a;">

  <div style="display:flex;align-items:center;gap:8px;margin-bottom:16px;">
    <span style="width:12px;height:12px;border-radius:50%;background:#ff5f56;display:inline-block;"></span>
    <span style="width:12px;height:12px;border-radius:50%;background:#ffbd2e;display:inline-block;"></span>
    <span style="width:12px;height:12px;border-radius:50%;background:#27c93f;display:inline-block;"></span>
    <span id="ct-step-label" style="margin-left:12px;font-size:0.78rem;color:#4a6885;letter-spacing:0.04em;">Step 1 of 8 — Problem Framing</span>
  </div>

  <div id="ct-body" style="min-height:310px;">

    <div id="ct-prompt" style="color:#3bc9db;font-size:0.85rem;margin-bottom:14px;"></div>

    <div style="color:#4a6885;font-size:0.72rem;margin-bottom:4px;text-transform:uppercase;letter-spacing:0.08em;">Codex asks</div>
    <div id="ct-question" style="color:#f4a261;font-size:0.87rem;line-height:1.55;margin-bottom:14px;min-height:44px;"></div>

    <div style="color:#4a6885;font-size:0.72rem;margin-bottom:6px;text-transform:uppercase;letter-spacing:0.08em;">Your attempt</div>
    <textarea id="ct-textarea" placeholder="Type your reasoning before seeing Codex's response…" style="width:100%;box-sizing:border-box;background:#091422;border:1px solid #1e3a5a;border-radius:6px;color:#e2e8f0;font-family:inherit;font-size:0.82rem;line-height:1.5;padding:8px 10px;resize:vertical;min-height:60px;outline:none;transition:border-color 200ms ease;" onfocus="this.style.borderColor='#3bc9db'" onblur="this.style.borderColor='#1e3a5a'"></textarea>
    <button id="ct-submit" onclick="ctSubmit()" style="margin-top:8px;background:#f4a261;color:#1a0a00;border:none;border-radius:5px;padding:6px 18px;font-family:inherit;font-size:0.8rem;font-weight:700;cursor:pointer;">See what Codex said →</button>

    <div id="ct-answer-wrap" style="display:none;margin-top:18px;">
      <div style="color:#4a6885;font-size:0.72rem;margin-bottom:4px;text-transform:uppercase;letter-spacing:0.08em;">Codex output</div>
      <div id="ct-answer" style="color:#a6e3a1;font-size:0.84rem;line-height:1.55;margin-bottom:16px;"></div>
      <div id="ct-badge" style="display:inline-block;background:#1a2f4a;border:1px solid #3bc9db;border-radius:5px;padding:4px 12px;font-size:0.74rem;color:#3bc9db;"></div>
    </div>

  </div>

  <div style="display:flex;gap:10px;margin-top:22px;align-items:center;flex-wrap:wrap;">
    <button id="ct-prev" onclick="ctNav(-1)" style="background:#1a2f4a;color:#3bc9db;border:1px solid #3bc9db;border-radius:5px;padding:6px 18px;font-family:inherit;font-size:0.8rem;cursor:pointer;">← Prev</button>
    <button id="ct-next" onclick="ctNav(1)" style="background:#1a2f4a;color:#3bc9db;border:1px solid #3bc9db;border-radius:5px;padding:6px 18px;font-family:inherit;font-size:0.8rem;cursor:pointer;">Next →</button>
    <button id="ct-play" onclick="ctPlay()" style="background:#0d1b2e;color:#f4a261;border:1px solid #f4a261;border-radius:5px;padding:6px 18px;font-family:inherit;font-size:0.8rem;cursor:pointer;">▶ Play all</button>
    <span id="ct-dots" style="margin-left:4px;color:#4a6885;font-size:0.78rem;letter-spacing:0.12em;"></span>
  </div>

</div>

<script>
(function () {
  var steps = [
    {
      label: "Step 1 of 8 — Problem Framing",
      prompt: "$ codex run problem_frame.md",
      question: "What do you think the prediction target is, and why would RMSE be a better metric here than accuracy?",
      answer: "Target: SalePrice | Metric: RMSE (continuous output, no class boundary) | Context: estimate likely sale price from structured housing features before listing.",
      artifact: "✓ artifact written: problem_frame.md"
    },
    {
      label: "Step 2 of 8 — Data Audit",
      prompt: "$ codex run data_audit.md",
      question: "Before I run the audit — which columns do you expect to have missing values, and what's your plan for them?",
      answer: "LotFrontage (~17% missing) and GarageYrBlt (~5%) are the biggest. Plan: median impute for LotFrontage, 0 for Garage numerics (no garage = 0), 'None' for Garage categoricals.",
      artifact: "✓ artifact written: data_card.md"
    },
    {
      label: "Step 3 of 8 — Train/Test Split",
      prompt: "$ codex run split_strategy.md",
      question: "What split ratio would you choose and why? What's the risk of using a random split on this dataset?",
      answer: "80/20 random split is standard. Risk: if sales data has time ordering, random splitting leaks future prices into training — a temporal split may be safer.",
      artifact: "✓ artifact updated: analysis_plan.md"
    },
    {
      label: "Step 4 of 8 — Baseline Model",
      prompt: "$ codex run baseline.md",
      question: "What should the baseline be before we try anything fancier? Why does it matter to establish one first?",
      answer: "Mean prediction or simple linear regression. The baseline sets the floor — if a complex model can't beat a mean predictor, the added complexity isn't helping.",
      artifact: "✓ artifact written: experiment_log.md (entry 001)"
    },
    {
      label: "Step 5 of 8 — Feature Handling",
      prompt: "$ codex run feature_plan.md",
      question: "Before encoding — flag any features you think might cause leakage, and explain your imputation plan.",
      answer: "MoSold and YrSold might leak if the model is deployed pre-sale. GarageYrBlt: impute with 0. Ordinal quality features: map to integers, not one-hot.",
      artifact: "✓ artifact updated: experiment_log.md (entry 002)"
    },
    {
      label: "Step 6 of 8 — Model Comparison",
      prompt: "$ codex run model_compare.md",
      question: "Predict: will random forest beat linear regression on this dataset, and what's your reasoning?",
      answer: "Likely yes — nonlinear interactions in housing data (neighborhood × size) favour ensembles. But watch for overfitting on a small Kaggle sample.",
      artifact: "✓ artifact updated: experiment_log.md (entry 003 — comparison result)"
    },
    {
      label: "Step 7 of 8 — Evaluation",
      prompt: "$ codex run evaluate.md",
      question: "Before I show you the results — what RMSE would you consider a good outcome here, and why?",
      answer: "Below $25,000 RMSE on a median price of ~$180k is reasonable: roughly 14% relative error. Much higher suggests underfitting or leakage.",
      artifact: "✓ artifact written: model_card.md"
    },
    {
      label: "Step 8 of 8 — Workflow Trace",
      prompt: "$ codex run workflow_trace.md",
      question: "Before I write the trace — what was the most important decision you made in this project, and what would you do differently?",
      answer: "Fixing the validation set early was the key decision. Next time: start with deeper EDA on missingness patterns before committing to an imputation strategy.",
      artifact: "✓ artifact written: workflow_trace.md"
    }
  ];

  var current = 0;
  var playing = false;
  var playTimer = null;
  var typeTimer = null;
  var submitted = new Array(steps.length).fill(false);
  var savedAttempts = new Array(steps.length).fill('');

  function dots() {
    var d = '';
    for (var i = 0; i < steps.length; i++) d += (i === current) ? '● ' : '○ ';
    return d.trim();
  }

  function showAnswer() {
    var s = steps[current];
    var wrap = document.getElementById('ct-answer-wrap');
    document.getElementById('ct-answer').textContent = s.answer;
    document.getElementById('ct-badge').textContent = s.artifact;
    wrap.style.display = 'block';
    wrap.style.opacity = '0';
    wrap.style.transition = 'opacity 350ms ease';
    wrap.getBoundingClientRect();
    wrap.style.opacity = '1';
  }

  function setStep(idx, skipType) {
    if (idx < 0 || idx >= steps.length) return;
    savedAttempts[current] = document.getElementById('ct-textarea').value;
    current = idx;
    var s = steps[current];

    document.getElementById('ct-step-label').textContent = s.label;
    document.getElementById('ct-prompt').textContent = s.prompt;
    document.getElementById('ct-dots').textContent = dots();
    document.getElementById('ct-prev').disabled = (current === 0);
    document.getElementById('ct-prev').style.opacity = (current === 0) ? '0.4' : '1';
    document.getElementById('ct-next').disabled = (current === steps.length - 1);
    document.getElementById('ct-next').style.opacity = (current === steps.length - 1) ? '0.4' : '1';

    var ta = document.getElementById('ct-textarea');
    ta.value = savedAttempts[current];
    ta.style.borderColor = '#1e3a5a';

    var wrap = document.getElementById('ct-answer-wrap');
    if (submitted[current]) {
      document.getElementById('ct-answer').textContent = s.answer;
      document.getElementById('ct-badge').textContent = s.artifact;
      wrap.style.display = 'block';
      wrap.style.opacity = '1';
      wrap.style.transition = '';
    } else {
      wrap.style.display = 'none';
    }

    if (typeTimer) clearInterval(typeTimer);
    var el = document.getElementById('ct-question');
    if (skipType) {
      el.textContent = s.question;
    } else {
      el.textContent = '';
      var i = 0;
      var text = s.question;
      typeTimer = setInterval(function () {
        if (i < text.length) { el.textContent += text[i]; i++; }
        else clearInterval(typeTimer);
      }, 28);
    }
  }

  window.ctSubmit = function () {
    var ta = document.getElementById('ct-textarea');
    if (!ta.value.trim()) {
      ta.style.borderColor = '#ff5f56';
      ta.placeholder = 'Type something first — even a rough guess counts.';
      setTimeout(function () {
        ta.style.borderColor = '#1e3a5a';
        ta.placeholder = 'Type your reasoning before seeing Codex\'s response…';
      }, 900);
      return;
    }
    savedAttempts[current] = ta.value;
    submitted[current] = true;
    showAnswer();
  };

  window.ctNav = function (dir) {
    if (playing) ctStop();
    setStep(current + dir, false);
  };

  function ctStop() {
    playing = false;
    if (playTimer) clearTimeout(playTimer);
    document.getElementById('ct-play').textContent = '▶ Play all';
  }

  function autoAdvance() {
    if (!playing) return;
    if (!submitted[current]) {
      submitted[current] = true;
      showAnswer();
    }
    playTimer = setTimeout(function () {
      if (!playing) return;
      if (current < steps.length - 1) {
        setStep(current + 1, false);
        setTimeout(autoAdvance, 2200);
      } else {
        ctStop();
      }
    }, 2000);
  }

  window.ctPlay = function () {
    if (playing) { ctStop(); return; }
    playing = true;
    document.getElementById('ct-play').textContent = '⏸ Pause';
    setStep(0, false);
    setTimeout(autoAdvance, 1800);
  };

  // init: step 1 shown open so page is readable without interaction
  submitted[0] = true;
  setStep(0, true);
  var initWrap = document.getElementById('ct-answer-wrap');
  document.getElementById('ct-answer').textContent = steps[0].answer;
  document.getElementById('ct-badge').textContent = steps[0].artifact;
  initWrap.style.display = 'block';
  initWrap.style.opacity = '1';
})();
</script>

---

## Try It for Real

The demo above is a simulation — here's how to run the actual project in Codex.

Copy this into Codex to begin:

```text
Use tutor mode to guide me through a housing-price prediction project using the Codex Batman workflow.

Dataset: Kaggle House Prices
(https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques)
Objective: predict SalePrice with low RMSE.

Start with the problem-framing skill.
At each step, ask for my reasoning before giving the answer.
```

Codex will ask for your attempt at every gate — just like the demo, but with real responses based on what you type. Your first output should be a `problem_frame.md` file.

Want to see what a real exchange looks like before you start? [Live Session Example →](live-session.md) captures an actual student-Codex conversation across the first two steps, including a wrong answer, a hint, and the correction.

---

## What You Built

Each step writes or updates a backbone artifact. Here's what each one records:

- **`problem_frame.md`** — prediction target, metric choice, decision context, and first risks
- **`data_card.md`** — dataset provenance, column types, missingness map, and leakage flags
- **`analysis_plan.md`** — split strategy, validation approach, and modeling sequence
- **`experiment_log.md` (entry 001)** — baseline model choice and rationale
- **`experiment_log.md` (entry 002)** — feature handling decisions and imputation strategy
- **`experiment_log.md` (entry 003)** — model comparison result across linear and ensemble candidates
- **`model_card.md`** — final model specs, evaluation results, known limits, and deployment notes
- **`workflow_trace.md`** — session narrative: what was decided, what changed, and what comes next

---

!!! tip "What is different about student mode"
    - **Codex asked for your reasoning first.** Every gate in this sequence started with Codex asking your attempt before revealing the output. That's intentional — the goal is to build your mental model, not just the artifact.
    - **You can ask for a nudge instead of the full answer.** At any step in a real Codex session, type `codex hint` to get a directional clue without Codex revealing the complete answer.
    - **The artifacts are identical to what a practitioner would produce.** Student mode changes the coaching style, not the artifact standard. The `model_card.md` and `workflow_trace.md` you built here are exactly what a senior analyst would hand off.

---

## Where To Go Next

- [For Students](../../students/index.md) — return to the student role page for the full recommended sequence
- [Live Session Example](live-session.md) — see a real student-Codex coaching exchange with wrong answers, hints, and corrections
- [Practitioner Path](practitioner.md) — see how the same eight-step project looks without the coaching scaffolding
- [Backbone Protocol](../../backbone/index.md) — understand the artifact system that underpins both paths
