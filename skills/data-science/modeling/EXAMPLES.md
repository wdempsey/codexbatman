# Examples: Modeling

## Example 1

User request:

> Build a modeling plan for this binary classification project with a baseline and two candidate model families.

Expected behavior:

- define baseline model first
- define candidate set with rationale
- specify validation strategy before tuning

Expected artifacts:

- baseline model spec
- candidate model set
- validation approach
- feature/transform notes

## Example 2

User request:

> Run modeling with fixed splits and produce a training summary we can hand off to evaluation.

Expected behavior:

- train baseline and candidate models under comparable protocol
- record parameters and assumptions
- produce concise training/model summary

Expected artifacts:

- training log or model summary
- parameter summary
- evaluation handoff recommendation

## Example 3 (Bad Invocation)

User request:

> Auto-tune everything and give me the best model.

Expected Codex response:

- reject unbounded optimization request
- require baseline and candidate set definition
- require validation protocol before tuning

Expected artifacts after correction:

- baseline model spec
- constrained candidate set
- documented validation approach
