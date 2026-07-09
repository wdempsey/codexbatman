# Plan As Guidance Examples

## Exploratory Analysis With Uncertainty

Input:

```text
We have a messy customer dataset and need a plan for EDA before deciding whether churn prediction is viable.
```

Good output shape:

```markdown
## Loop Contract

Outcome: Decide whether churn prediction is viable enough to proceed past EDA.
Acceptance evidence: data-audit status, target definition check, leakage notes, baseline feasibility note.
Non-goals: train production models or tune algorithms.
Allowed revisions: reorder EDA checks if data quality blocks feature exploration; pause if the target cannot be defined.
Must ask before: changing the prediction target or relaxing data-audit conditions.
Stop conditions: missing target event, temporal leakage, or unapproved data source.

### Step 1: Confirm Target And Prediction Time
Intent: Make the EDA questions answer the actual decision.
Acceptance criteria:
- Target event is named.
- Prediction time is stated.
- Unavailable-at-prediction variables are flagged.
Verification: target notes added to the analysis plan.
Permitted revision: if target is ambiguous, pause and route back to problem-framing.
```

The plan can change as EDA reveals constraints, but each change should be logged.

## Mid-Flight Discovery

Input:

```text
The plan says to build the baseline next, but while checking features I found a column that leaks the outcome.
```

Good response:

```markdown
## Deviation Log

- Planned: Build baseline after feature sanity checks.
  Changed: Pause modeling and return to leakage review.
  Evidence: `resolved_at` is populated only after churn event resolution.
  Reason: The original step order assumed no target-timing leak.
  Next action: update the data audit and revise the plan before modeling.
```

Do not force the original sequence when it would violate workflow gates.

## Implementation Handoff

Input:

```text
The ML feature spec is approved. Turn it into a flexible work plan.
```

Good response:

```markdown
### Step 1: Define Inference Contract Tests
Intent: Make the downstream implementation safe to slice.
Acceptance criteria:
- Required input schema is represented in a failing test.
- Missing required columns fail clearly.
Verification: targeted test fails before implementation.
Dependencies: approved ML feature spec.
Permitted revision: split schema and output-contract tests if the fixture grows too large.
```

Then hand executable slices to `incremental-implementation`.
