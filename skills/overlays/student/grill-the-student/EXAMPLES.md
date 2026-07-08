# grill-the-student Examples

## Vague Problem-Set Help

Input:

> I have to do a logistic regression problem set and I don't get it.

Good first question:

> Which part are you on right now: setting up the response/predictors, interpreting coefficients, fitting the model, or checking performance?

Expected behavior:

- ask one question
- do not explain logistic regression yet
- narrow the confusion boundary before handoff

## Notation Mismatch

Input:

> My notes use `X beta` but the textbook uses h_theta(x). Are those the same?

Good first question:

> Which notation does your professor expect you to use on this assignment?

Expected behavior:

- identify the course notation
- mirror the student's notation back
- avoid converting the answer into another convention too early

## Course Coverage Boundary

Input:

> Should I use cross-validation or AIC here?

Good first question:

> Which of those has your class covered so far, and does the prompt name either one?

Expected behavior:

- establish covered and allowed methods
- do not recommend a method before knowing the course boundary

## Misconception Handoff

Input:

> I think increasing lambda in lasso always increases test accuracy because it removes bad variables.

Good first question:

> What do you think lambda is directly controlling in the lasso objective?

Expected behavior:

- ask one diagnostic alignment question
- if the claim persists, route to `misconception-diagnosis`
