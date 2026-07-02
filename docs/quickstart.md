---
description: Install Codex and run your first structured data science workflow. Complete in under ten minutes.
---

# Quickstart

Install Codex, verify it runs locally, and see what a structured workflow looks like — that's the full goal here. When you're done, pick the path that fits your role and follow one example end to end.

By the end of this page you'll have Codex installed, a clear mental model of how structured prompts work, and a concrete starting point for your role.

---

## Step 1 — Install Codex

<style>
.qs-tabs { display:flex; gap:0.5rem; margin-bottom:0.85rem; flex-wrap:wrap; }
.qs-tab {
  padding:0.35rem 1rem; border-radius:6px;
  border:1px solid var(--md-default-fg-color--lightest);
  background:transparent; color:var(--md-default-fg-color);
  cursor:pointer; font-family:inherit; font-size:0.88rem;
  transition:background 150ms ease, color 150ms ease, border-color 150ms ease;
}
.qs-tab:hover { border-color:var(--md-accent-fg-color); }
.qs-tab.qs-active {
  background:var(--md-accent-fg-color);
  color:#fff; border-color:var(--md-accent-fg-color);
}
.qs-panel { display:none; }
.qs-panel.qs-visible { display:block; }
.qs-cmd {
  font-family:'JetBrains Mono','Courier New',monospace;
  font-size:0.85rem; line-height:1.7;
  background:#0d1b2e; color:#e2e8f0;
  border-radius:9px; padding:1rem 1.2rem;
  margin:0.5rem 0 0.9rem; border:1px solid #1a2f4a;
  white-space:pre;
}
.qs-cmd .qs-prompt { color:#3bc9db; user-select:none; }
.qs-note { font-size:0.83rem; color:var(--md-default-fg-color--light); margin-top:0.2rem; }
</style>

<div>
  <div class="qs-tabs">
    <button class="qs-tab qs-active" onclick="qsOs('mac',this)">macOS</button>
    <button class="qs-tab" onclick="qsOs('win',this)">Windows</button>
    <button class="qs-tab" onclick="qsOs('linux',this)">Linux</button>
  </div>

  <div id="qs-mac" class="qs-panel qs-visible">
    <p style="font-size:0.9rem;margin-bottom:0.5rem;">Install via Homebrew (recommended):</p>
    <div class="qs-cmd"><span class="qs-prompt">$ </span>brew install codex</div>
    <p style="font-size:0.9rem;margin-bottom:0.5rem;">Or via npm if you don't have Homebrew:</p>
    <div class="qs-cmd"><span class="qs-prompt">$ </span>npm install -g @openai/codex</div>
    <p class="qs-note">The macOS desktop app (from the official Codex website) also includes CLI access — install and sign in, then run <code>codex --version</code> to confirm.</p>
  </div>

  <div id="qs-win" class="qs-panel">
    <p style="font-size:0.9rem;margin-bottom:0.5rem;">Install via npm in PowerShell:</p>
    <div class="qs-cmd"><span class="qs-prompt">PS> </span>npm install -g @openai/codex</div>
    <p class="qs-note">On Windows Subsystem for Linux, use the Linux steps instead. After install, run <code>codex --version</code> in a new terminal window to confirm.</p>
  </div>

  <div id="qs-linux" class="qs-panel">
    <p style="font-size:0.9rem;margin-bottom:0.5rem;">Install via npm:</p>
    <div class="qs-cmd"><span class="qs-prompt">$ </span>npm install -g @openai/codex</div>
    <p style="font-size:0.9rem;margin-bottom:0.5rem;">Or via apt on Debian/Ubuntu:</p>
    <div class="qs-cmd"><span class="qs-prompt">$ </span>sudo apt install codex</div>
    <p class="qs-note">Run <code>codex --version</code> in a new terminal window after install.</p>
  </div>
</div>

<script>
function qsOs(id, btn) {
  document.querySelectorAll('.qs-panel').forEach(p => p.classList.remove('qs-visible'));
  document.querySelectorAll('.qs-tab').forEach(b => b.classList.remove('qs-active'));
  document.getElementById('qs-' + id).classList.add('qs-visible');
  btn.classList.add('qs-active');
}
</script>

<p style="font-size:0.83rem;color:var(--md-default-fg-color--light);margin-top:0.75rem;">New to Terminal or never used npm? See the step-by-step guides: <a href="../toolkit/install-mac/">macOS install guide</a> · <a href="../toolkit/install-windows/">Windows install guide</a></p>

---

## Step 2 — Verify

Open a new terminal and run:

```bash
codex --version
```

You should see a version number. If you see a "command not found" error, check that your npm global bin directory is in your PATH — `npm bin -g` shows you where it is.

When you launch Codex it starts in **Default mode** — it proposes changes and waits for your confirmation before applying them. That's the right mode for learning. You can switch to Plan Mode (Codex explores before acting) or Auto-Accept (applies edits immediately) from the controls in your Codex environment.

---

## Step 3 — What a structured workflow looks like

Codex isn't a chatbot you prompt casually. It's a workflow executor — it runs structured prompt patterns (called **skills**) that enforce analysis gates and produce artifact outputs. Here's the difference:

<div style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:1.2rem 0 1.6rem;">
  <div>
    <div style="font-size:0.68rem;font-weight:700;letter-spacing:0.09em;text-transform:uppercase;color:var(--md-default-fg-color--light);margin-bottom:0.5rem;">Without structure</div>
    <pre style="margin:0;font-size:0.82rem;color:var(--md-default-fg-color--light);background:color-mix(in srgb,var(--md-default-bg-color) 96%,#888 4%);padding:0.85rem 1rem;border-radius:8px;border:1px solid var(--md-default-fg-color--lightest);white-space:pre-wrap;font-family:'JetBrains Mono','Courier New',monospace;">"Run a regression on this dataset."</pre>
    <div style="margin-top:0.55rem;font-size:0.81rem;color:var(--md-default-fg-color--light);">What you get: a generic "this dataset appears suitable for regression." No files written. No reproducibility. Nothing to hand off.</div>
  </div>
  <div>
    <div style="font-size:0.68rem;font-weight:700;letter-spacing:0.09em;text-transform:uppercase;color:var(--md-accent-fg-color);margin-bottom:0.5rem;">With structure</div>
    <pre style="margin:0;font-size:0.82rem;color:var(--md-default-fg-color);background:color-mix(in srgb,var(--md-default-bg-color) 95%,var(--md-accent-fg-color) 5%);padding:0.85rem 1rem;border-radius:8px;border:1px solid color-mix(in srgb,var(--md-accent-fg-color) 25%,transparent);white-space:pre-wrap;font-family:'JetBrains Mono','Courier New',monospace;">Run problem-framing skill.
Target: SalePrice
Metric: RMSE
Output: problem_frame.md</pre>
    <div style="margin-top:0.55rem;font-size:0.81rem;color:var(--md-default-fg-color);">What you get: a named file, an explicit metric, documented risks, and a defined next gate — something another session can pick up and continue.</div>
  </div>
</div>

Structure matters for three reasons: no explicit seed, environment, or output artifacts means the run isn't reproducible; no schema check means silent data quality problems; no required output structure means no handoff to the next session.

### Two interaction modes

Before you paste anything in, one thing to understand: Codex has two interaction styles, and the right one depends on what you're trying to get out of the session.

**Tutor mode** — Codex asks for your reasoning at each step before revealing the gate output. It coaches rather than executes: you attempt an answer, Codex builds on it or corrects it, and the artifact gets written once the reasoning is solid. This is the mode for building understanding alongside the artifact.

**Practitioner mode** — Codex runs the workflow gates directly and expects artifact-quality responses from you. No scaffolding, no pedagogical detours — just gates, outputs, and forward progress. This is the mode once you know the workflow.

For a first session, use tutor mode. The example below shows what that looks like.

### Your first session

The canonical example throughout this site is a housing-price prediction project on the [Ames dataset](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques). You can start it right now — paste this into Codex:

```text
Use tutor mode to guide me through the first steps of a housing price prediction project.

Dataset: Kaggle Housing Prices
(https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques)
Objective: predict SalePrice with low RMSE.

Start with the problem-framing skill.

Ask me questions instead of giving the full answer immediately.
```

Here's what that exchange looks like. Codex asks for your reasoning at each step before the gate completes — the goal is to build your understanding alongside the artifact.

<div style="font-family:'JetBrains Mono','Courier New',monospace;font-size:0.83rem;line-height:1.65;background:#0d1b2e;border-radius:10px;padding:1.25rem 1.4rem;margin:1.4rem 0;border:1px solid #1a2f4a;">
<div style="color:#6c7a8d;font-size:0.72rem;letter-spacing:0.06em;margin-bottom:1rem;text-transform:uppercase;">Tutor Mode · Problem-Framing Skill</div>

<div style="color:#3bc9db;font-size:0.76rem;font-weight:600;margin-bottom:0.25rem;">Codex</div>
<div style="color:#f4a261;margin-bottom:1rem;white-space:pre-wrap;">Your stated objective is "predict SalePrice with low RMSE."

Before we confirm that's the right metric — what decision would this prediction support? Will someone use this to price a house before listing, or to evaluate an automated offer?</div>

<div style="color:#94a3b8;font-size:0.76rem;font-weight:600;margin-bottom:0.25rem;">You</div>
<div style="color:#cbd5e1;margin-bottom:1rem;">To evaluate automated offers — checking whether the offer price is reasonable before accepting.</div>

<div style="color:#3bc9db;font-size:0.76rem;font-weight:600;margin-bottom:0.25rem;">Codex</div>
<div style="color:#f4a261;margin-bottom:1rem;white-space:pre-wrap;">Good — that context matters. Automated-offer evaluation has a symmetric error profile: overestimates and underestimates are both costly, so RMSE is the right call.

I'll log that as the decision context. Now: LotFrontage has about 17% missing values in this dataset. What's your first instinct — drop those rows, impute, or flag them separately?</div>

<div style="color:#94a3b8;font-size:0.76rem;font-weight:600;margin-bottom:0.25rem;">You</div>
<div style="color:#cbd5e1;margin-bottom:1rem;">Impute with the median — it should be roughly normal.</div>

<div style="color:#3bc9db;font-size:0.76rem;font-weight:600;margin-bottom:0.25rem;">Codex</div>
<div style="color:#f4a261;margin-bottom:1rem;white-space:pre-wrap;">Close — but first check whether LotFrontage has a cluster of structural zeros (no street frontage) versus true missing values. If it does, median imputation conflates two very different things. How would you separate those cases?</div>

<div style="color:#a6e3a1;border-top:1px solid #1a2f4a;margin-top:0.25rem;padding-top:1rem;">→ problem_frame.md written
→ Decision context: automated-offer evaluation · Metric: RMSE · LotFrontage risk flagged
→ Ready for data-audit gate</div>
</div>

The exchange continues the same way through data audit, split strategy, baseline, and evaluation. Each gate produces an artifact file. By the end of a session the repo is self-documenting — another person (or another session) can open it and immediately understand what's been decided and what comes next.

---

## Where to go from here

Pick the path that matches your role.

<div class="decision-grid" style="margin-top:1rem;">
  <a href="../examples/basic-classification/learning/" class="decision-card">
    <span class="decision-label">Student</span>
    <span class="decision-action">Attempt before answer</span>
    <span class="decision-desc">Tutor mode — Codex asks for your reasoning before revealing the output. Best for building intuition alongside the artifact. Includes an interactive demo at every gate.</span>
  </a>
  <a href="../examples/analytics-repo/execution/" class="decision-card">
    <span class="decision-label">Researcher / Data Scientist</span>
    <span class="decision-action">Direct execution</span>
    <span class="decision-desc">Practitioner mode — same gates, Codex executes directly and expects artifact-quality output. Faster, less hand-holding.</span>
  </a>
  <a href="../workflows/manager/lab-manager-agent/" class="decision-card">
    <span class="decision-label">Manager</span>
    <span class="decision-action">Coordinate and oversee</span>
    <span class="decision-desc">Lab manager mode — use Codex to track project state across a team, review gate artifacts, and flag when a project needs attention.</span>
  </a>
</div>

Not sure which fits you? [Choose Your Role →](roles/index.md) has a quick decision guide.
