# EDA Hypothesis Journal Rubric

Score a use of this skill against these checks:

- Confirms problem framing, data audit, and EDA plan before exploration.
- Starts with sanity checks before interpreting plots.
- Records each exploratory question as a hypothesis entry.
- Logs null, rejected, and inconclusive hypotheses when they affect the next step.
- Checks target timing, feature availability, and split contamination during EDA.
- Keeps exploratory branches tied to evidence and plan revisions.
- Produces a proceed/revise/halt modeling handoff.
- Routes leakage or target-definition failures back to the owning gate.

Failure modes:

- Plotting without a stated question.
- Treating EDA as permission to train models.
- Ignoring data-audit conditions.
- Recording only interesting findings.
- Proceeding to modeling after a leakage finding without mitigation.
