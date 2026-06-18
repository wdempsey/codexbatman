# Linear Regression — Manager Lens

A state housing agency program director is reviewing a model before approving its use in assistance program allocation decisions. The model predicts median house values across California census tracts. The outputs will influence which tracts receive priority for housing assistance.

The director is not running the model. She's deciding whether to trust it for this use.

[See how the model was built →](execution.md) | [Learning walkthrough →](learning.md)

---

## What a manager reviews at this gate

The manager lens for a regression model with policy stakes has three concerns that go beyond "does it have good RMSE":

**Systematic errors by region.** A model that achieves RMSE $68,400 on average is not equally accurate everywhere. If the model systematically underpredicts values for coastal tracts, those tracts look artificially low-cost in the outputs — and get deprioritized for assistance relative to their true need. That's a fairness and policy concern, not just a modeling limitation.

**What the metric means to a non-technical audience.** RMSE $68,400 is meaningful to a data scientist. "On average, our estimate for a census tract's median house value is off by about $68,000" is meaningful to a program director. The manager review confirms the model card translates the metric into terms the decision-maker can act on.

**The $500K ceiling disclosure.** The data caps house values at $500K. The program director needs to know this before using outputs for high-cost coastal tracts — not buried in a technical appendix, but explicit in the summary.

---

## Go/No-Go rubric

Before signing off on model use for program allocation, a manager should be able to answer yes to each of these:

| Question | What to check |
|---|---|
| Is the decision context documented? | Does `problem_frame.md` name the agency, the decision, and the population? |
| Is the $500K ceiling disclosed? | Is it in the executive summary and the model card, not just the data card? |
| Is regional performance reported? | Is RMSE broken out by coastal vs. inland tracts, not just overall? |
| Are the limitations specific? | Does the model card name which tracts are affected by the coastal underprediction? |
| Is there a threshold for action? | Is there a clear rule for when not to use model outputs (e.g., tracts within 50 miles of coast, top 5% of predicted values)? |

A model card that answers all five is ready for program use. One that answers fewer needs a revision before sign-off.

---

## Stress-testing the model card

Before sign-off, it's worth running a structured challenge on the analysis — not to find problems for their own sake, but to surface anything the data scientist may have optimized around without noticing. Use three parallel critics:

**The Skeptic** challenges the decision framing: "You're using 1990 census data to inform current program allocation — what's the assumption about how the geographic distribution of housing need has changed in 35 years? Has that been validated?"

**The Methodologist** checks the statistical choices: "You chose RMSE over MAE because large individual errors matter more. But for program allocation, you likely set a threshold — tracts above some predicted value get deprioritized. At a threshold, what matters is whether the model gets the ranking right, not the absolute error. Have you checked rank correlation?"

**The Equity Auditor** examines subgroup performance: "Coastal underprediction affects certain demographic groups disproportionately. Have you checked whether error patterns correlate with tract-level race or income composition?"

These three critics run in parallel — they don't debate each other, they each produce a punch list. The data scientist synthesizes the findings into model card updates before the program director signs off.

<div style="font-family:'JetBrains Mono','Courier New',monospace;font-size:0.82rem;line-height:1.6;background:#0d1b2e;border-radius:10px;padding:1.2rem 1.4rem;margin:1.5rem 0;border:1px solid #1a2f4a;">
<div style="color:#6c7a8d;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.06em;margin-bottom:0.8rem;">Copyable prompt — council of critics</div>
<div style="color:#f4a261;white-space:pre-wrap;">Review the model card and analysis plan for this regression model.
Run three parallel critics. Each works independently — no cross-debate.

Critic 1 — Skeptic: challenge the decision framing and temporal validity
of using 1990 data for current program allocation.

Critic 2 — Methodologist: challenge the metric choice (RMSE vs rank
correlation) given the threshold-based allocation decision.

Critic 3 — Equity Auditor: check whether coastal underprediction
correlates with demographic composition of affected tracts.

Each critic produces a numbered punch list of specific concerns.
Then synthesize: what are the top 2 fixes before sign-off?</div>
</div>

---

## Example synthesis output

<div style="font-family:'JetBrains Mono','Courier New',monospace;font-size:0.82rem;line-height:1.6;background:#0d1b2e;border-radius:10px;padding:1.2rem 1.4rem;margin:1.5rem 0;border:1px solid #1a2f4a;">
<div style="color:#6c7a8d;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.06em;margin-bottom:0.8rem;">Codex synthesis</div>
<div style="color:#a6e3a1;white-space:pre-wrap;">Top 2 fixes before sign-off:

1. Add temporal validity statement to problem_frame.md and model card
   executive summary. The 1990 data assumption is not documented anywhere
   visible to the program director. Add: "This model is trained on 1990
   census data. Using it for current allocation assumes the geographic
   distribution of housing cost burden has not changed substantially.
   This assumption has not been validated."

2. Add rank correlation (Spearman ρ) to evaluation metrics alongside RMSE.
   The allocation decision is threshold-based — rank accuracy matters more
   than absolute error for that use case. Current model card reports RMSE
   only. Add Spearman ρ by region (coastal, inland, valley) so the program
   director can see whether rank ordering is preserved even where RMSE
   is high.

Equity Auditor finding: coastal underprediction does correlate with
higher-income tracts (r ≈ 0.31), not with lower-income tracts — so
the systematic bias works against high-cost tracts, not against
disadvantaged populations. This is the opposite of the equity concern.
Document this finding explicitly in the model card to preempt the question.</div>
</div>

---

## Coordinating the data science team

If the data scientist is a direct report or collaborator, the manager review has a secondary purpose: calibrating effort on remaining open questions.

The execution lens identified two open questions: (1) geographic region features to address coastal underprediction, and (2) rank correlation as an alternative metric for threshold-based allocation. Before the next session begins, the manager should decide which of these is a priority:

If **coastal underprediction is operationally important** (coastal tracts are a significant share of the program's scope), the geographic feature engineering is worth the additional session. Assign it, set a clear acceptance criterion: "coastal RMSE should be within 20% of overall RMSE."

If **the current model is good enough for the program's purpose**, document the limitations, add the temporal validity statement, and close the project. Don't engineer features to address a limitation the program won't encounter in practice.

This is a manager decision, not a data science decision. The experiment log gives the manager the information to make it.

---

*Related: [Execution Lens](execution.md) · [Basic Classification — Manager Lens](../basic-classification/manager.md) · [Managing Data Science](../../workflows/managing-data-science/index.md)*
