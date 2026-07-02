# Basic Classification — Manager Lens

The practitioner builds the artifacts. The manager reviews them and decides whether the project is ready to advance.

This page shows the manager lens on the cardiac risk classification project: what questions a clinical PI or lab manager asks at each gate, how to use Codex to get a status summary without reading every file, and what a real go/no-go decision looks like at evaluation.

The manager doesn't write code, run models, or make imputation choices. Those belong to the practitioner. The manager asks: is the problem framed in a way I can defend? Is the leakage review complete? Can I explain the failure modes to the clinical team?

---

## Getting a status summary

Before diving into individual artifacts, use Codex to get an oriented summary of where the project stands. Paste this into Codex with the repo open:

```text
Read PROJECT_STATE.md, problem_frame.md, and data_card.md.

Tell me:
1. What decision this classifier is meant to support
2. Whether the prediction time has been explicitly defined
3. Whether the leakage review is complete and documented
4. What's blocking this project from moving to evaluation

Be direct. I'm reviewing for a go/no-go decision, not a technical briefing.
```

What you should get back:

<div style="font-family:'JetBrains Mono','Courier New',monospace;font-size:0.83rem;line-height:1.65;background:#0d1b2e;border-radius:10px;padding:1.25rem 1.4rem;margin:1.4rem 0;border:1px solid #1a2f4a;">
<div style="color:#7d90a8;font-size:0.72rem;letter-spacing:0.06em;margin-bottom:1rem;text-transform:uppercase;">Codex · Project Status Summary</div>
<div style="color:#f4a261;margin-bottom:1rem;white-space:pre-wrap;"><strong style="color:#e2e8f0;">Decision:</strong> Cardiology referral triage. Given 13 clinical features measured post-stress-test, predict whether a patient has heart disease (binary) to flag them for further evaluation.

<strong style="color:#e2e8f0;">Prediction time:</strong> Explicitly defined — post-stress-test. All 13 features including exang, oldpeak, and thal are available. Leakage review complete.

<strong style="color:#e2e8f0;">Current status:</strong> Baseline complete. Logistic regression, ROC-AUC 0.87, false negatives at default threshold: 12/61 test cases.

<strong style="color:#e2e8f0;">What's needed before evaluation review:</strong> Threshold recommendation documented. Subgroup analysis (sex) complete. Model card drafted.</div>
<div style="color:#a6e3a1;">→ Project is past baseline. Ready for evaluation review pending model card completion.</div>
</div>

---

## Reviewing the problem frame

Open `problem_frame.md`. The questions a manager asks are not technical — they're about whether the decision is honest.

**Is the target right?** The original dataset has a 0–4 severity scale. Binarizing to 0 / 1+ makes the referral decision cleaner, but it loses severity information. Does that tradeoff hold up if the clinical team asks about it?

**Is the metric appropriate?** ROC-AUC measures discrimination across all thresholds — good for comparing models. But deployment will use a single threshold. The model card needs to state what threshold the team recommends for this use case and why.

**Is the decision context realistic?** "Cardiology referral triage" is clear. What population does this model apply to? Cleveland clinic patients, 1988. Applying this to a general-population screening tool without revalidation is outside scope — that constraint belongs in the model card.

If any of these are unclear, the project is not ready for evaluation review. Flag them back to the practitioner before proceeding.

---

## Reviewing the data card

Open `data_card.md`. The manager questions here are about risk documentation, not data engineering.

**Is the leakage review signed off?** The data card should explicitly state which features were assessed for leakage, what the decision was, and why. "Leakage review: passed" without an explanation isn't sufficient.

**Is the missingness plan recorded?** ca and thal have missing values. The plan (mode impute for thal, unknown category for ca) must be documented so any future retraining applies the same transformations.

**Is there a fairness flag?** Sex is a feature. The data card should note that subgroup performance has not yet been validated.

---

## The evaluation go/no-go decision

This is the manager's primary decision point. The practitioner presents the evaluation results; the manager decides what happens next.

Typical results for this project:

| Model | ROC-AUC | FN at 0.5 | FN at 0.3 |
|---|---|---|---|
| Logistic regression | 0.87 | 12 | 6 |
| Random forest | 0.89 | 10 | 5 |

The manager's questions at this stage:

**What threshold are we using?** At 0.5, the random forest sends 10 patients with heart disease home as healthy. Lowering to 0.3 halves false negatives — at the cost of more unnecessary referrals. Which is acceptable in a clinical context? That's not a data science question. It's a clinical policy question that belongs in the model card and that the manager or PI is responsible for deciding.

**Is the performance gap worth the complexity?** Random forest ROC-AUC 0.89 vs. logistic regression 0.87. The simpler model is more interpretable and easier to audit. Unless the 0.02 gap is clinically meaningful, logistic regression may be the right deployment choice.

**Is the population scope documented?** Before any clinical deployment: the model was trained on Cleveland clinic data from the 1980s. Validation on a current, representative population is required before production use.

---

## Go/no-go rubric

The manager approves the project to advance when all three hold:

1. **Problem frame is defensible** — decision context, target, metric, and prediction time are explicitly documented and clinically coherent
2. **Risk documentation is complete** — leakage review signed off, missingness plan recorded, population scope stated, fairness flag acknowledged
3. **Threshold recommendation is explicit** — the model card states the recommended operating threshold, the false-negative rate at that threshold, and who made the threshold decision

If any of these are missing, the project goes back to the practitioner with specific items to resolve — not a vague "needs more work."

---

## Stress-testing the analysis plan

The go/no-go rubric tells you *what* to check. But on high-stakes projects — a clinical model going to a review board, a grant deliverable, anything where a missed assumption has real consequences — you want a harder test of the analysis plan before it goes to evaluation.

The pattern is borrowed from Chris Blattman's [`/council`](https://claudeblattman.com/workflows/council/) workflow: dispatch parallel critics, each with a single lens, and have a separate synthesis pass read their outputs. The key is that critics don't see each other's reasoning — you get independent critique, not group consensus.

For data science, three critics cover most of the risk surface:

| Critic | Role | What they look for |
|---|---|---|
| **Skeptic** | Challenges assumptions | Is the problem statement defensible? Are the success criteria realistic? Could a simpler model do this? |
| **Methodologist** | Checks statistical validity | Is the metric aligned with the decision? Is the split strategy appropriate? Are comparison conditions valid? |
| **Leakage checker** | Hunts for data leakage | Which features were available at prediction time? Was preprocessing done before or inside the fold? Does the evaluation window match the deployment window? |

### How to run it

Paste this into Codex with your `analysis_plan.md` and `data_card.md` open:

```text
Read analysis_plan.md and data_card.md. I want three independent critiques of this analysis plan — run them in parallel, each from a single perspective:

Critic 1 — Skeptic: Is the problem worth solving this way? Challenge the decision context, the target definition, and whether this level of modeling complexity is warranted.

Critic 2 — Methodologist: Evaluate the statistical choices. Is ROC-AUC the right metric? Is the split strategy sound? Are the baseline and candidate models being compared fairly?

Critic 3 — Leakage checker: Look only for data leakage. Which features might not be available at prediction time? Was imputation or scaling done before or inside the train/test split?

Run all three independently. Do not let the critics respond to each other. Then give me a synthesis: the top three problems and what to fix before proceeding to modeling.
```

### What comes back

<div style="font-family:'JetBrains Mono','Courier New',monospace;font-size:0.83rem;line-height:1.65;background:#0d1b2e;border-radius:10px;padding:1.25rem 1.4rem;margin:1.4rem 0;border:1px solid #1a2f4a;">
<div style="color:#7d90a8;font-size:0.72rem;letter-spacing:0.06em;margin-bottom:1rem;text-transform:uppercase;">Codex · Analysis Plan Council</div>
<div style="color:#cbd5e1;margin-bottom:1rem;white-space:pre-wrap;"><strong style="color:#e2e8f0;">Skeptic:</strong> The decision context (referral triage) is clear, but the population scope is buried in a footnote. If a referring physician asks "who does this model apply to?" the answer needs to be in the problem frame, not the data card.

<strong style="color:#e2e8f0;">Methodologist:</strong> ROC-AUC is appropriate for model selection. The stratified 80/20 split is correct given class imbalance. Issue: the analysis plan doesn't state whether preprocessing will happen inside the CV fold or before it. This needs to be explicit.

<strong style="color:#e2e8f0;">Leakage checker:</strong> exang, oldpeak, slope, thalach, and thal are all post-stress-test features — confirmed available at prediction time. No leakage detected. However: imputation of `ca` and `thal` must happen inside the fold. Not documented.</div>
<div style="color:#f4a261;font-weight:600;margin-bottom:0.5rem;">Synthesis — top 3 fixes before modeling:</div>
<div style="color:#a6e3a1;">1. Move population scope into problem_frame.md — "Cleveland clinic patients, 1988" belongs there, not in the data card
2. Add explicit statement to analysis_plan.md: "Imputation fitted on training fold only, inside each CV fold"
3. Add threshold recommendation section to analysis_plan.md — who decides 0.5 vs. 0.3 and when</div>
</div>

The synthesis identifies actionable items, not vague concerns. Each one maps to a specific artifact and a specific gap. The manager resolves items 1 and 3 (decision scope); the practitioner resolves item 2 (implementation detail).

### When to use this

Use the council review at the analysis plan stage — before any code is written, when the plan is locked but the experiment hasn't started. It's a 10-minute check that catches the class of problems that show up at evaluation as "we should have caught this earlier."

On simpler projects, the three-question go/no-go rubric above is enough. On projects going to external review, stakeholder presentation, or deployment, the council review replaces the rubric.

---

---

## Coordinating multiple projects

A single-project review like the one above is the building block. The lab manager role extends that upward: instead of reviewing one classifier, you're maintaining visibility across a portfolio — students, grant projects, paper replications, collaborations — all at different gates.

This is where the `lab-manager-agent` and `project-manager-agent` skills come in.

### The coordination layer

```text
Lab Manager Agent          ← portfolio view
  → Project Manager Agents ← one per active project
      → Worker Agents      ← practitioners running the analysis
```

The cardiac risk classifier is one project in that portfolio. A lab manager doesn't open each project's artifacts every week — they use `lab-manager-agent` to maintain a `LAB_DASHBOARD.md` that surfaces what needs attention across all projects at once.

### Getting the portfolio view

Paste this into Codex with your lab dashboard and project state files open:

```text
Run the lab-manager-agent skill.

Read LAB_DASHBOARD.md, ACTIVE_PROJECTS.md, and any PROJECT_STATE.md files present.

Tell me:
1. Which projects are blocked or stale
2. Which are approaching a deadline in the next two weeks
3. What I need to decide or unblock before the end of this week

Keep it to a short action list, not a full briefing.
```

### What a lab dashboard entry looks like

The cardiac risk classifier would appear in `LAB_DASHBOARD.md` as one row:

```markdown
| Project | Status | Last Gate | Next Action | Owner | Deadline |
|---|---|---|---|---|---|
| cardiac-risk-classifier | In progress | Baseline complete | Threshold decision needed | Practitioner A | Mar 15 |
| housing-price-regression | Blocked | Data audit | Leakage review awaiting sign-off | Practitioner B | Mar 20 |
| grant-analysis-2025 | Stale | Problem framing | No update in 10 days | Practitioner C | Apr 1 |
```

The manager's job at the portfolio level is to see which projects need a decision from them (threshold choice, leakage sign-off) vs. which are stalled on the practitioner's side (no update in 10 days).

### Weekly review

The `weekly-review` skill synthesizes the portfolio view into a brief:

```text
Run weekly-review.

Summarize: projects that advanced, projects that are stuck, things waiting on me, and one thing I should prioritize this week.
```

This is the difference between managing one project in isolation and managing a lab — the weekly review and portfolio dashboard are what make the coordination scalable.

---

## Where To Go Next

- [Learning lens →](learning.md) — how the practitioner built these artifacts step by step
- [Execution lens →](execution.md) — the practitioner's gate-by-gate workflow
- [Lab Manager Agent](../../workflows/manager/lab-manager-agent.md) — full documentation of the portfolio coordination layer
- [Managing Data Science](../../workflows/managing-data-science/index.md) — day-to-day operating workflow for managers
