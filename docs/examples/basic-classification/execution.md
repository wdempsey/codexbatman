# Basic Classification — Execution Lens

Use this lens when the goal is to complete the work reproducibly.

## Gates Completed

- problem framed
- data audited
- plan defined

## Concise Workflow

1. Define the positive class:
   missed advising appointment.
2. Confirm the prediction time:
   one week before the appointment.
3. Exclude features that would only be known after the appointment date.
4. Fit a simple baseline classifier.
5. Compare one or two justified candidate models.
6. Record the run in `experiment_log.md`.
7. Produce a short `model_card.md`.

## Reproducibility Checklist

- target defined
- prediction time defined
- leakage review documented
- split strategy documented
- baseline model recorded
- metrics recorded
- experiment log updated
- model card drafted

## Final Deliverables

- classification comparison summary
- experiment log entry
- model card
- workflow trace
