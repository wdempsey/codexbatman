---
hide:
  - navigation
  - toc
description: Codex-native data science workflow system with structured workflow gates, reproducibility enforcement, and role-aware overlays.
social:
  cards_layout_options:
    title: Codex-Native Data Science Workflow
    description: Structured, reproducible workflow for disciplined applied data science.
---

<div class="hf-home">
  <section class="hf-section hf-hero" id="home-intro">
    <div class="hf-hero__backdrop" aria-hidden="true"></div>
    <div class="hf-shell">
      <h1>Codex-Native Data Science Workflow</h1>
      <p class="hf-lead">
        Codex Batman is a markdown-first, artifact-first operating system for reproducible data science. It gives
        students, practitioners, and managers one shared workflow backbone with clear gates, durable project memory,
        and role-aware execution.
      </p>
      <p class="hf-inline-cta">
        <a class="md-button md-button--primary" href="quickstart/">Start with Quickstart</a>
        <a class="md-button" href="roles/">Choose your role</a>
      </p>
    </div>
    <div class="hf-scroll-cue" aria-hidden="true">Scroll</div>
  </section>

  <section class="hf-section hf-section--dark" id="choose-your-path">
    <div class="hf-shell hf-reveal">
      <p class="hf-kicker">Choose Your Path</p>
      <h2>Start From The Role You Actually Have</h2>
      <p class="hf-summary">
        Students, researchers, data scientists, and managers all use the same workflow backbone. The role paths change
        the delivery style and first action so you do not have to learn the whole architecture before getting started.
      </p>

      <div class="hf-bubble-grid">
        <article class="hf-bubble">
          <h3>Students</h3>
          <p>Learn through guided practice, hints, and attempt-before-answer tutoring.</p>
          <p><a href="students/">Open student path</a></p>
        </article>
        <article class="hf-bubble">
          <h3>Researchers & Data Scientists</h3>
          <p>Run trustworthy analysis with gates, artifacts, and reproducible project memory.</p>
          <p><a href="data-scientists/">Open research path</a></p>
        </article>
        <article class="hf-bubble">
          <h3>Managers</h3>
          <p>Track project health, blockers, handoffs, decisions, and stakeholder updates.</p>
          <p><a href="managers/">Open manager path</a></p>
        </article>
      </div>

      <p class="hf-inline-cta">
        <a class="md-button md-button--primary" href="roles/">Compare role paths</a>
        <a class="md-button" href="examples/">See worked examples</a>
      </p>
    </div>
  </section>

  <section class="hf-section" id="how-it-works">
    <div class="hf-shell hf-reveal">
      <p class="hf-kicker">How It Works</p>
      <h2>One Backbone, Different Lenses</h2>
      <p class="hf-summary">
        Skills encode best practices, documentation pages explain the workflows, and role overlays adapt the same
        backbone to learning, execution, and management.
      </p>

      <div class="hf-media-list">
        <article class="hf-media-row hf-reveal">
          <div class="hf-media-image">
            <img src="assets/home/where-start-installation.png" alt="Cartoon installation scene for Codex setup" loading="lazy">
          </div>
          <div>
            <h3>Installation and Setup</h3>
            <p>Set up the base toolkit, environment, and local workflow checks.</p>
            <p><a href="setup/">Open setup</a></p>
          </div>
        </article>

        <article class="hf-media-row hf-media-row--alt hf-reveal">
          <div class="hf-media-image">
            <img src="assets/home/hero-workflow-bg-exit.png" alt="Codex Batman workflow visual" loading="lazy">
          </div>
          <div>
            <h3>Workflow Backbone</h3>
            <p>Move from project bootstrap through problem framing, data audit, modeling, evaluation, and experiment logging.</p>
            <p><a href="workflows/data-science/">Open workflow overview</a></p>
          </div>
        </article>

        <article class="hf-media-row hf-reveal">
          <div class="hf-media-image">
            <img src="assets/home/hero-workflow-bg.png" alt="Codex Batman project workflow backdrop" loading="lazy">
          </div>
          <div>
            <h3>Worked Examples</h3>
            <p>See the same system through learning, execution, and manager coordination lenses.</p>
            <p><a href="examples/">Open examples</a></p>
          </div>
        </article>
      </div>

      <p class="hf-inline-cta">
        <a class="md-button" href="quickstart/">Open the guided quickstart</a>
        <a class="md-button" href="backbone/">Explore the Backbone Protocol</a>
      </p>
    </div>
  </section>

  <section class="hf-section hf-section--dark" id="proof-of-utility">
    <div class="hf-shell hf-reveal">
      <p class="hf-kicker">Proof Of Utility</p>
      <h2>What The System Produces</h2>
      <p class="hf-summary">
        The point is not just to explain a workflow. The point is to leave behind durable artifacts that help the next analysis session, the next collaborator, or the next manager review start from real project state instead of chat memory.
      </p>

      <div class="hf-media-list">
        <article class="hf-media-row hf-reveal">
          <div class="hf-media-image">
            <div class="hf-proof-card">
              <p><strong>Student Artifact</strong></p>
              <pre><code>problem_frame.md
- target: SalePrice
- metric: RMSE
- prediction time: before sale
- first risks: missingness, leakage</code></pre>
            </div>
          </div>
          <div>
            <h3>Student Workflow Artifact</h3>
            <p>A beginner-facing artifact that proves the learner framed the problem before modeling and can resume from real project state.</p>
            <p><a href="examples/analytics-repo/student/">Open the student repo example</a></p>
          </div>
        </article>

        <article class="hf-media-row hf-media-row--alt hf-reveal">
          <div class="hf-media-image">
            <div class="hf-proof-card">
              <p><strong>Practitioner Artifact</strong></p>
              <pre><code>experiment_log.md
- baseline: linear regression
- candidate: random forest
- split: fixed validation set
- next action: inspect leakage risk</code></pre>
            </div>
          </div>
          <div>
            <h3>Practitioner Workflow Artifact</h3>
            <p>An execution-facing artifact that records what was tried, what won so far, and what needs to happen next.</p>
            <p><a href="examples/analytics-repo/practitioner/">Open the practitioner repo example</a></p>
          </div>
        </article>

        <article class="hf-media-row hf-reveal">
          <div class="hf-media-image">
            <img src="images/project-overview-dashboard-v1.png" alt="Example project overview dashboard showing project status, priorities, metrics, and tasks" loading="lazy">
          </div>
          <div>
            <h3>Project Dashboard Snapshot</h3>
            <p>A manager-facing artifact that surfaces status, priorities, owners, risks, deadlines, and next actions in one place.</p>
            <p><a href="workflows/examples/project-overview-example/">Open the example dashboard</a></p>
          </div>
        </article>
      </div>

      <p class="hf-inline-cta">
        <a class="md-button md-button--primary" href="examples/">See worked examples</a>
        <a class="md-button" href="examples/analytics-repo/">See repo artifacts</a>
        <a class="md-button" href="workflows/examples/project-overview-example/">See a manager artifact</a>
      </p>
    </div>
  </section>

  <section class="hf-section hf-section--connect" id="stay-in-the-loop">
    <div class="hf-shell hf-connect-grid hf-reveal">
      <div>
        <p class="hf-kicker">Next Step</p>
        <h2>Move Into A Concrete Workflow</h2>
        <p class="hf-summary">
          Start with setup, compare role paths, or review worked examples before changing your own project process.
        </p>

        <p class="hf-links">
          <a class="md-button md-button--primary" href="quickstart/">Start quickstart</a>
          <a class="md-button" href="roles/">Choose your role</a>
          <a class="md-button" href="examples/">See examples</a>
          <a class="md-button" href="https://github.com/wdempsey/codexbatman">GitHub</a>
        </p>
      </div>

      <figure class="hf-exit-figure hf-reveal-image">
        <img src="assets/home/hero-workflow-bg-exit.png" alt="Codex Batman workflow visual" loading="lazy">
      </figure>
    </div>
  </section>
</div>
