# Reproducibility Capture Examples

## Modeling Run

Good capsule:

```markdown
## Reproducibility Capsule

Result: Logistic regression baseline ROC-AUC 0.842 in 5-fold stratified CV.
Data version: `data/processed/churn_2026-07-01.parquet`; 18,204 rows; customer-month unit.
Code version: branch `churn-baseline`, commit `abc1234`, dirty worktree: no.
Command or notebook path: `python scripts/train_baseline.py --config configs/churn.yaml`.
Environment: Python 3.12; packages from `requirements.txt`; sklearn 1.5.2.
Seed strategy: global seed 20260709; split seed 20260709; model random_state 20260709.
Randomness caveats: none expected beyond floating-point tolerance.
Known gaps: data checksum not recorded; add before final report.
Handoff: copy into experiment-log entry `run-004`.
```

## Dirty Notebook Result

Good response:

```markdown
Known gaps:
- Worktree has uncommitted notebook and helper changes.
- Data extract date is unknown.
- No seed was set for the train/test split.

Decision: Do not report this number as reproducible. Record it as exploratory and rerun after closing the gaps.
```
