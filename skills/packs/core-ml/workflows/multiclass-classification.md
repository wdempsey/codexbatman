# Multiclass Classification Workflow

Use this workflow when the target has more than two classes and the project needs a reproducible class-prediction workflow.

## Focus

- define the class system clearly
- confirm whether class imbalance matters
- choose metrics that reflect class-level performance, not only aggregate accuracy
- compare models under consistent splits

## Minimum Workflow

1. Define the class labels and their practical meaning.
2. Check data coverage across classes.
3. Confirm split validity and leakage boundaries.
4. Fit a simple baseline first.
5. Compare candidate models using aligned metrics.
6. Review per-class performance and confusion patterns.
7. Produce evaluation and model-card artifacts.

## Minimum Checks

- class labels are clear
- rare classes are acknowledged
- split strategy preserves valid comparison
- baseline exists
- per-class behavior is reviewed

## Recommended Outputs

- multiclass comparison summary
- evaluation report
- model card
- experiment log entry
