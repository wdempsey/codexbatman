# Leakage Check

Use this check before trusting model performance.

## Questions

- Could any feature reveal future information at prediction time?
- Are labels or post-outcome fields leaking into inputs?
- Are there duplicated entities across train and test?
- Are preprocessing steps fitted using information from the full dataset?
- Is the split strategy aligned with time, person, group, or cluster structure?

## Minimum Output

- leakage risks identified
- mitigation actions
- proceed or halt recommendation
