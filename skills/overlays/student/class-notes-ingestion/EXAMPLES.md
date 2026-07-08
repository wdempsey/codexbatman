# class-notes-ingestion Examples

## OCR-Damaged Lecture Notes

Input:

> I uploaded screenshots from lecture 4. The OCR says `I(beta) = XTX / s^2`, but it might have dropped the transpose symbol.

Expected behavior:

- ask whether to persist the course notation for future sessions
- mark uncertain OCR as `[unclear]`
- record the suspected notation issue under possible issues
- do not silently rewrite the expression as a textbook formula

## Professor-Specific Survival Notation

Input:

> My class writes the Cox model as `lambda(t | Z) = lambda_0(t) exp(gamma'Z)`. Please use that instead of the textbook's `h(t|x)`.

Expected behavior:

- write `lambda(t | Z)` and `lambda_0(t) exp(gamma'Z)` as the preferred notation
- record `h(t|x)` as an optional standard equivalent only if helpful
- tell future tutor-mode to mirror the professor's notation

## Course Coverage Boundary

Input:

> These notes cover AIC and likelihood ratio tests but not cross-validation yet.

Expected behavior:

- record AIC and likelihood ratio tests as covered
- record cross-validation as not yet covered
- route future method advice through the course coverage boundary

## Seeded Error In Notes

Input:

> The notes say increasing lambda in lasso always increases test accuracy.

Expected behavior:

- flag the statement as a possible issue
- cite the source line or excerpt
- ask the student to confirm before treating it as an error
- do not overwrite the notes with the corrected claim during ingestion
