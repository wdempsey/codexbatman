# Problem Frame

_Gate 1 — Problem Framing_
_Produced: tutor mode, problem-framing skill_

---

## Decision

Should this patient be referred for further cardiac evaluation?

This is a **clinical triage decision** — a cardiologist uses the model output as one input
among several, not as the sole arbiter. False negatives (missing disease) are worse than
false positives (unnecessary referral), so we'll need to revisit the decision threshold.

## Modeling Objective

- **Task**: binary classification
- **Target**: `target` — 0 = no disease, 1+ = disease present (we binarize to 0/1)
- **Metric**: ROC-AUC (threshold-independent; captures both sensitivity and specificity)
- **Secondary metric**: sensitivity at clinical threshold (to be set after baseline)

## Prediction Time

All 13 features are collected post-stress-test. The model runs at the end of the clinical
workup, after thalach, exang, oldpeak, slope, and thal are already known. No leakage risk.

## Scope and Constraints

- Population: patients presenting with chest pain who undergo full stress-test workup
- No deployment timeline given; treat as offline batch scoring for now
- Model must be interpretable enough for a clinician to audit a recommendation

## First-Pass Risk Register

| Risk | Severity | Notes |
|------|----------|-------|
| Leakage (stress-test features) | Low | Prediction time confirmed post-stress-test |
| Missingness (ca, thal) | Medium | ca: 4 missing, thal: 2 missing — needs imputation plan |
| Class balance | Low | ~54% positive — balanced enough for standard splits |
| Threshold choice | High | Default 0.5 may not match clinical cost asymmetry |

---

_Student note: I almost forgot to check whether the stress-test features would be available
at prediction time. Codex asked me about it before I moved on. The key question was whether
the model would be used before or after the stress test — since it's after, no leakage._

Next step: `data-audit`
