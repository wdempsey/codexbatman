# Model Card

_Gate 6 — Evaluation_
_Produced: tutor mode, evaluation skill_

---

## Model

Random Forest Classifier, n_estimators=100, default depth, random_state=42
Decision threshold: 0.38

## Intended Use

Cardiac referral triage — support a cardiologist's decision about whether to refer a patient
for further cardiac evaluation after a stress-test workup. Input: 13 clinical features
collected post-stress-test. Output: referral probability + binary recommendation.

**Not intended for**: diagnosis, severity staging, autonomous clinical decision-making.

## Population

Cleveland Clinic Foundation patients presenting with chest pain who completed a full
stress-test workup. Generalization to other populations unvalidated.

## Performance (held-out test set, n=61)

| Metric | Value |
|--------|-------|
| ROC-AUC | 0.891 |
| Sensitivity | 0.882 |
| Specificity | 0.778 |
| Accuracy | 0.836 |
| False negatives | 4 (patients with disease not flagged for referral) |
| False positives | 6 (patients without disease flagged for referral) |

## Confusion Matrix (threshold=0.38)

```
                Predicted 0    Predicted 1
Actual 0           21               6
Actual 1            4              30
```

## Feature Importances (top 5)

1. cp (chest pain type) — 0.14
2. thal (thalassemia type) — 0.13
3. ca (vessels on fluoroscopy) — 0.12
4. thalach (max heart rate) — 0.11
5. oldpeak (ST depression) — 0.10

## Known Limitations

- **Small test set**: 61 patients — confidence intervals on all metrics are wide
- **Single site**: trained and tested on Cleveland data only; may not generalize to different
  patient demographics or clinical protocols
- **Ceiling on ca and thal**: 6 missing values total — imputation introduces uncertainty
- **No temporal validation**: we don't know if 1989 Cleveland patient data reflects
  current clinical populations

## Clinical Risk

- False negative rate at threshold 0.38: ~12% (4/34 disease patients not referred)
- Clinicians should treat model output as a support tool, not a gate
- Any patient with high clinical suspicion should be referred regardless of model output

---

_Student note: Codex asked me to write the "intended use" section before looking at metrics.
I wanted to skip it. The reason it matters: without knowing what the model is for, you can't
know whether 0.882 sensitivity is good enough. Once I wrote "cardiac referral triage," it
was obvious that 12% missed disease is significant and a clinician needs to know that._
