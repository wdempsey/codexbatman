# misconception-diagnosis Examples

## Descriptive Versus Predictive Framing

User request:

> I keep treating descriptive questions like predictive ones. Diagnose what I’m getting wrong.

Expected behavior:

- wrap `problem-framing`
- reproduce the student's objective-switch reasoning
- localize the broken step where "describe this population" becomes "predict future cases"
- use a minimal contrast between a summary question and a prediction question
- ask for a revised problem-frame sentence
- emit an evidence record for `session-wrap`

## Lasso Lambda Misconception

User request:

> I keep saying that increasing lambda in lasso always improves test accuracy because it removes bad variables.

Expected behavior:

- wrap the relevant modeling or method-teaching skill
- reproduce the reasoning: larger lambda -> fewer variables -> fewer bad variables -> better test accuracy
- localize the broken step: simpler models can underfit and test error can increase
- offer a tiny train/test contrast or U-shaped error sketch
- ask the student to explain when a larger lambda could hurt

## One-Off Slip Boundary

User request:

> I accidentally typed `X_test` where I meant `X_train`. Diagnose my misconception.

Expected behavior:

- do not over-diagnose
- say this looks like a one-off implementation slip unless it repeats
- route to `hint-ladder` or a small debugging prompt
- do not emit a misconception evidence record

## Course Notation Boundary

User request:

> My notes use `lambda(t | Z)` for the hazard, and I keep interpreting it like the survival probability.

Expected behavior:

- use the course notation from `NOTATION.md` if available
- reproduce the student's mapping between hazard and survival
- localize the broken step: instantaneous risk is not cumulative survival probability
- use a minimal contrast case
- ask the student to restate the difference in the course notation
