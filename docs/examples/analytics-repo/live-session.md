---
description: A real student-Codex coaching exchange across the first two workflow gates — problem framing and data audit — including a wrong answer, a hint, and the correction.
---

# Live Session Example — Student Mode

This page shows what an actual student-Codex exchange looks like using tutor mode on the housing-price project.

It covers the first two workflow gates: **problem framing** and **data audit**. The student gets one answer wrong, asks for a hint on a follow-up, and the session ends with two real backbone artifacts written to disk.

This isn't a polished demo — it's the texture of an actual coaching conversation.

---

<div style="font-family:'JetBrains Mono','Courier New',monospace;font-size:0.84rem;line-height:1.6;margin:2rem 0;">

<!-- ── Gate 1: Problem Framing ── -->

<div style="color:#3bc9db;margin-bottom:1.2rem;">
$ codex run problem_frame.md --skill tutor-mode
</div>

<div style="background:#0d1b2e;border-left:3px solid #f4a261;border-radius:0 8px 8px 0;padding:0.9rem 1.1rem;margin-bottom:0.85rem;">
<div style="font-size:0.68rem;color:#4a6885;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:0.4rem;">Codex</div>
Before we write the problem frame — what do you think the prediction target is for this project, and should we use accuracy or RMSE as the metric? Tell me your reasoning.
</div>

<div style="background:#091422;border-left:3px solid #6b7fa3;border-radius:0 8px 8px 0;padding:0.9rem 1.1rem;margin-bottom:0.85rem;">
<div style="font-size:0.68rem;color:#4a6885;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:0.4rem;">Student</div>
The target is SalePrice. I'd use accuracy since we want to get it right.
</div>

<div style="background:#0d1b2e;border-left:3px solid #f4a261;border-radius:0 8px 8px 0;padding:0.9rem 1.1rem;margin-bottom:0.85rem;">
<div style="font-size:0.68rem;color:#4a6885;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:0.4rem;">Codex</div>
You're right that SalePrice is the target — that part is solid. But accuracy isn't the right metric here. Accuracy measures whether a classification is correct or not — like "did we predict the right label?" SalePrice is a continuous number, not a category. There's no single "correct" price to predict; a house selling for $182,000 when you predicted $185,000 is different from being off by $50,000.<br><br>
What kind of error metric would make sense for a continuous prediction where large errors matter more than small ones?
</div>

<div style="background:#091422;border-left:3px solid #6b7fa3;border-radius:0 8px 8px 0;padding:0.9rem 1.1rem;margin-bottom:0.85rem;">
<div style="font-size:0.68rem;color:#4a6885;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:0.4rem;">Student</div>
Something that measures distance from the real price? Like mean absolute error?
</div>

<div style="background:#0d1b2e;border-left:3px solid #f4a261;border-radius:0 8px 8px 0;padding:0.9rem 1.1rem;margin-bottom:0.85rem;">
<div style="font-size:0.68rem;color:#4a6885;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:0.4rem;">Codex</div>
MAE works, and it's easier to interpret — "on average we're $X off." But Kaggle uses RMSE for this competition. Do you know why RMSE is often preferred over MAE when large prediction errors are especially bad?
</div>

<div style="background:#091422;border-left:3px solid #6b7fa3;border-radius:0 8px 8px 0;padding:0.9rem 1.1rem;margin-bottom:0.85rem;">
<div style="font-size:0.68rem;color:#4a6885;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:0.4rem;">Student</div>
I'm not sure. Can I get a hint?
</div>

<div style="background:#0d1b2e;border-left:3px solid #f4a261;border-radius:0 8px 8px 0;padding:0.9rem 1.1rem;margin-bottom:0.85rem;">
<div style="font-size:0.68rem;color:#4a6885;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:0.4rem;">Codex — hint</div>
Think about what "squaring" the errors before averaging them does to large errors versus small ones. If you're off by $1,000, squaring gives 1,000,000. If you're off by $10,000, squaring gives 100,000,000 — a hundred times larger, not ten times larger. What does that tell you about how RMSE treats big mistakes?
</div>

<div style="background:#091422;border-left:3px solid #6b7fa3;border-radius:0 8px 8px 0;padding:0.9rem 1.1rem;margin-bottom:0.85rem;">
<div style="font-size:0.68rem;color:#4a6885;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:0.4rem;">Student</div>
Oh — it punishes big errors way more than small ones. So RMSE is better when being really wrong matters more than being slightly wrong.
</div>

<div style="background:#0d1b2e;border-left:3px solid #f4a261;border-radius:0 8px 8px 0;padding:0.9rem 1.1rem;margin-bottom:0.85rem;">
<div style="font-size:0.68rem;color:#4a6885;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:0.4rem;">Codex</div>
Exactly right. In a real estate context, being off by $100,000 is a much bigger problem than being off by $5,000 — RMSE captures that asymmetry. Two more things before we write the frame: who would use this prediction and when? And what risks do you see before we even touch the model?
</div>

<div style="background:#091422;border-left:3px solid #6b7fa3;border-radius:0 8px 8px 0;padding:0.9rem 1.1rem;margin-bottom:0.85rem;">
<div style="font-size:0.68rem;color:#4a6885;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:0.4rem;">Student</div>
A buyer or agent would use it before listing the house. Risks — maybe missing values? And some features might leak the price, like if there's a column that's basically just SalePrice in disguise.
</div>

<div style="background:#0d1b2e;border-left:3px solid #f4a261;border-radius:0 8px 8px 0;padding:0.9rem 1.1rem;margin-bottom:1.4rem;">
<div style="font-size:0.68rem;color:#4a6885;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:0.4rem;">Codex</div>
Both are real concerns. "Pre-listing" is important — it tells us that features only known after a sale (like MoSold, YrSold) shouldn't be in the model. Let me write the problem frame.
</div>

<div style="background:#0f2137;border:1px solid #3bc9db;border-radius:8px;padding:0.9rem 1.1rem;margin-bottom:1.8rem;color:#3bc9db;">
<div style="font-size:0.68rem;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:0.55rem;opacity:0.7;">artifact written</div>
<pre style="margin:0;color:#a6e3a1;font-size:0.8rem;line-height:1.6;">problem_frame.md
─────────────────────────────────────
target:           SalePrice
metric:           RMSE
prediction time:  before listing — no post-sale features allowed
decision context: estimate likely sale price from structured housing features
first risks:
  - missing values in LotFrontage, GarageYrBlt
  - leakage from sale-date features (MoSold, YrSold)
  - overfitting to Kaggle leaderboard patterns</pre>
</div>

<!-- ── Gate 2: Data Audit ── -->

<div style="color:#3bc9db;margin-bottom:1.2rem;">
$ codex run data_audit.md --skill tutor-mode
</div>

<div style="background:#0d1b2e;border-left:3px solid #f4a261;border-radius:0 8px 8px 0;padding:0.9rem 1.1rem;margin-bottom:0.85rem;">
<div style="font-size:0.68rem;color:#4a6885;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:0.4rem;">Codex</div>
Before I run the audit — don't look at the data yet. Just from domain knowledge: which columns do you expect to have missing values, and what's your instinct on how to handle them?
</div>

<div style="background:#091422;border-left:3px solid #6b7fa3;border-radius:0 8px 8px 0;padding:0.9rem 1.1rem;margin-bottom:0.85rem;">
<div style="font-size:0.68rem;color:#4a6885;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:0.4rem;">Student</div>
LotFrontage seems like it could be missing for some houses. Maybe garage columns too — some houses might not have a garage. I'd probably use median for everything.
</div>

<div style="background:#0d1b2e;border-left:3px solid #f4a261;border-radius:0 8px 8px 0;padding:0.9rem 1.1rem;margin-bottom:0.85rem;">
<div style="font-size:0.68rem;color:#4a6885;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:0.4rem;">Codex</div>
Good instinct on LotFrontage — it's about 17% missing, one of the worst in the dataset. And yes, all the Garage columns cluster together: if there's no garage, GarageYrBlt, GarageCars, GarageArea, GarageType are all NaN at the same time.<br><br>
But "median for everything" is too simple. Here's a question: if a house has no garage and GarageYrBlt is NaN — does the NaN mean "unknown" or does it mean "there is no garage"? Does that change how you'd impute it?
</div>

<div style="background:#091422;border-left:3px solid #6b7fa3;border-radius:0 8px 8px 0;padding:0.9rem 1.1rem;margin-bottom:0.85rem;">
<div style="font-size:0.68rem;color:#4a6885;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:0.4rem;">Student</div>
Oh — the NaN means "there is no garage," not that the year is unknown. So imputing the median year would be wrong — it would make the model think there's a garage when there isn't.
</div>

<div style="background:#0d1b2e;border-left:3px solid #f4a261;border-radius:0 8px 8px 0;padding:0.9rem 1.1rem;margin-bottom:0.85rem;">
<div style="font-size:0.68rem;color:#4a6885;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:0.4rem;">Codex</div>
Exactly. For GarageYrBlt and other Garage numerics: impute with 0 — "no garage" is a meaningful value, not an unknown one. For GarageCond, GarageType and similar categoricals: fill with the string 'None' so the model treats it as its own category. For LotFrontage, on the other hand, NaN really does mean "we don't know" — so median is the right call there. Let me write the data card.
</div>

<div style="background:#0f2137;border:1px solid #3bc9db;border-radius:8px;padding:0.9rem 1.1rem;margin-bottom:1.8rem;color:#3bc9db;">
<div style="font-size:0.68rem;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:0.55rem;opacity:0.7;">artifact written</div>
<pre style="margin:0;color:#a6e3a1;font-size:0.8rem;line-height:1.6;">data_card.md
─────────────────────────────────────
dataset:      Ames Housing / Kaggle House Prices
rows:         1,460 train / 1,459 test
target:       SalePrice (continuous)

high-missingness columns:
  LotFrontage:  17.7% — impute with median (truly unknown)
  GarageYrBlt:   5.5% — impute with 0 (no garage)
  MasVnrType:    0.5% — impute with 'None'

imputation plan:
  numeric garage cols → 0
  categorical garage cols → 'None'
  LotFrontage → column median

leakage watch:
  MoSold, YrSold — sale timing known only after sale
  remove or treat carefully in production deployment</pre>
</div>

</div>

---

## What This Session Demonstrates

Two gates, two artifacts, one wrong answer that got corrected without just being given the answer. That's student mode working as intended.

A few things worth noticing about the exchange:

**The wrong answer got a follow-up question, not a correction.** When the student said "accuracy," Codex didn't say "that's wrong, use RMSE." It asked a question that surfaced why accuracy doesn't apply. The student arrived at the right concept themselves.

**The hint was specific, not a spoiler.** When the student asked for a hint on RMSE vs MAE, Codex gave a concrete mathematical frame (what squaring does to large errors) rather than just stating the answer.

**The missingness question had a real conceptual trap.** "Median for everything" is a common first instinct and it's wrong for structured missingness. Codex pushed on the distinction between "unknown" and "absent" — a distinction that matters in real data work, not just in this exercise.

**Both artifacts are real backbone artifacts.** The `problem_frame.md` and `data_card.md` produced here follow the same standard as the practitioner path. Student mode changes the coaching style, not what gets written to disk.

---

## Try It Yourself

This session was run using:

```text
Use tutor mode to guide me through a housing-price prediction project using the Codex Batman workflow.

Dataset: Kaggle House Prices
(https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques)
Objective: predict SalePrice with low RMSE.

Start with the problem-framing skill.
At each step, ask for my reasoning before giving the answer.
```

Your conversation will differ — Codex responds to what you actually type, not a script.

---

## Where To Go Next

- [Interactive Demo](student.md) — work through the 8-step sequence yourself, one gate at a time
- [For Students](../../students/index.md) — the full student role page with recommended sequence
- [Practitioner Path](practitioner.md) — the same project without the coaching scaffolding
