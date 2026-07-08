---
description: Worked student case studies showing class-note ingestion, pre-answer alignment, misconception diagnosis, and tutor-mode together.
---

# Student Class Notes Case Studies

These case studies show what happens after a student brings course notes into the system.

They are examples, not new skills. The routing stays the same:

1. `identity-loader` resolves the student context.
2. `class-notes-ingestion` persists confirmed notation and course boundaries when the student wants future sessions to remember them.
3. `grill-the-student` narrows the immediate confusion boundary before tutoring.
4. `tutor-mode` teaches without giving away the whole answer.
5. `misconception-diagnosis` runs only when repeated reasoning shows a real conceptual error.
6. `session-wrap` records confirmed learning and evidence.

## Case 1: Survival Notes Reconciled With RAG

**Student input**

> I uploaded my survival notes. My professor writes the Cox model as
> `lambda(t | Z) = lambda_0(t) exp(gamma'Z)`. The RAG demo keeps talking
> about `h(t | x)`. Are these the same thing? Also, what does the lung
> dataset's `status` variable mean?

**Route**

```text
identity-loader
class-notes-ingestion
Survival RAG query
grill-the-student if the exact confusion remains unclear
tutor-mode
```

**Durable context written after confirmation**

`memory/students/{name}/NOTATION.md`:

```markdown
| Symbol or term | Professor/course meaning | Standard equivalent | Source | Notes |
| --- | --- | --- | --- | --- |
| `lambda(t | Z)` | hazard at time `t` conditional on covariates `Z` | `h(t | x)` | survival notes, Cox unit | Use professor notation first. |
| `lambda_0(t)` | baseline hazard | `h_0(t)` | survival notes, Cox unit | Do not call this baseline survival. |
| `gamma'Z` | linear predictor in the Cox model | `beta'x` | survival notes, Cox unit | Translate only if asked. |
```

`memory/students/{name}/COURSE-CONTEXT.md`:

```markdown
## Covered So Far

- Kaplan-Meier estimator: covered conceptually and in R.
- Log-rank test: covered for comparing two survival curves.
- Cox model: introduced with professor notation `lambda(t | Z)`.

## Not Yet Covered Or Off Limits

- Time-varying covariates: not covered yet.
- Proportional hazards diagnostics: mentioned but not assigned.
```

**RAG grounding**

The [Survival RAG example](survival-rag/index.md) retrieves from two sources:

- textbook chunks for conceptual terms such as hazard and survival
- dataset codebook entries for `time`, `status`, and clinical covariates

For this question, Codex should say where the answer is coming from:

```text
From your course notes: use `lambda(t | Z)` for the hazard.
From the RAG codebook: `status` is 1 = censored, 2 = dead in the lung dataset.
```

**Safe tutor move**

Codex should not jump straight to a Cox-model lecture. It should ask:

> In your professor's notation, what part of `lambda(t | Z)` tells us the
> patient has already survived up to time `t`, and what part changes with `Z`?

That question reconciles the RAG vocabulary with the student's course notation
without replacing one with the other.

## Case 2: Problem Set Routed Through `/grill-the-student`

**Student input**

> My stats problem set asks us to compare two models. I found an online example
> using cross-validation and random forests, but our class just covered AIC and
> likelihood ratio tests. Which should I use?

**Route**

```text
identity-loader
grill-the-student
tutor-mode
```

Use `class-notes-ingestion` only if the student wants those course constraints
remembered for future sessions. If this is a one-off problem set, the alignment
can stay in the current tutoring handoff.

**Grill sequence**

Ask one question at a time:

```text
Which methods does the prompt explicitly allow or name?
```

Then:

```text
What did your instructor say AIC and likelihood ratio tests are for?
```

Then:

```text
Where does your current attempt get stuck: choosing the comparison,
writing the hypotheses, computing the criterion, or interpreting the result?
```

**Confirmed alignment**

```markdown
## Confirmed Alignment

### Student Goal
Choose the model-comparison method for the assigned problem set.

### Notation And Vocabulary
The class says "full model" and "reduced model"; it has not introduced
train/test language for this unit.

### Course Coverage
Covered: likelihood ratio tests and AIC.
Not covered: cross-validation, random forests.
Allowed: methods in the current unit.

### Confusion Boundary
The student is unsure whether a method found online is allowed when the class
has not covered it.

### Next Skill
`tutor-mode`, because the route is clear and the student now needs scaffolded
help applying the allowed comparison.
```

**Safe tutor move**

Codex should guide the student to choose between AIC and likelihood ratio tests
using the course's full/reduced-model framing. It should not recommend random
forests or cross-validation just because those are standard tools elsewhere.

## Case 3: Notes Containing A Seeded Error

**Student input**

> My lecture notes say: "Increasing lambda in lasso always increases test
> accuracy because it removes bad variables." Can you add this to my course
> context and help me use it?

**Route**

```text
identity-loader
class-notes-ingestion
misconception-diagnosis if the student repeats the claim
tutor-mode or exercise-generator after repair
session-wrap
```

**Class-note ingestion behavior**

Codex should not silently rewrite the notes. It should propose:

```markdown
## Possible Issues In Notes

- Lasso lambda statement: notes say "Increasing lambda in lasso always
  increases test accuracy because it removes bad variables."
  Evidence: uploaded lecture note excerpt.
  Status: unconfirmed possible issue.
```

Then it should ask:

> This looks like a possible overstatement. Should I record it as a possible
> issue in `COURSE-CONTEXT.md` rather than treating it as confirmed course
> guidance?

**Misconception diagnosis**

If the student repeats the claim after a hint, route to `misconception-diagnosis`.

```markdown
### Student Reasoning Reproduced
Larger `lambda` -> more shrinkage -> fewer variables -> fewer bad variables
-> higher test accuracy.

### Broken Step
The broken step is "fewer variables always means better test accuracy."
Removing variance can help, but too much shrinkage can underfit.

### Minimal Counterexample
Imagine the only truly predictive variable is shrunk almost to zero. The model
is simpler, but it now misses real signal, so test error can rise.

### Repair Check
Can you explain one situation where increasing `lambda` helps, and one where it hurts?
```

**Evidence record for `/wrap`**

```json
{
  "date": "YYYY-MM-DD",
  "domain": "regression_and_modeling",
  "topic": "regularization_lasso_ridge",
  "misconception": "Increasing lasso lambda always improves test accuracy because it removes bad variables.",
  "student_reasoning_evidence": "Student repeated the lecture-note claim after an initial hint.",
  "broken_step": "Equated simpler model with universally better generalization.",
  "counterexample": "If lambda shrinks a truly predictive coefficient too far, the model underfits and test error can rise.",
  "repair_check": "Student explained one help case and one hurt case in their own words.",
  "status": "resolved",
  "recommended_mastery_update": "introduced"
}
```

## Case 4: Simulation-Design Notes

There is no committed simulation-campaign findings artifact in the repository
right now. The available anchor is the [Methods / Code Project](methods-code-project/index.md),
which describes simulation studies and model-comparison experiments at the
design level.

**Student input**

> My methods class notes say the estimator with the lowest average RMSE is
> automatically the best. We are reading a simulation study, and I am not sure
> how to think about bias, variance, and failure cases.

**Route**

```text
identity-loader
class-notes-ingestion if the notes should persist
grill-the-student
tutor-mode with model-evaluation or experiment-log
misconception-diagnosis if "lowest average RMSE is automatically best" persists
```

**Course context**

```markdown
## Covered So Far

- Bias, variance, and RMSE definitions.
- Simulation summaries by scenario.

## Possible Issues In Notes

- "Lowest average RMSE is automatically best" may be incomplete.
  Evidence: course note excerpt.
  Status: unconfirmed; ask whether the instructor later covers failure modes,
  tail behavior, or scenario-specific performance.
```

**Safe tutor move**

Codex should ask:

> Which scenario matters for the decision your simulation study is trying to
> support: average performance across all settings, or performance in the
> high-risk setting where the estimator can fail badly?

That keeps the lesson tied to simulation design without inventing results that
are not in the repo.

## What These Cases Prove

- Persistent course context belongs in `NOTATION.md` and `COURSE-CONTEXT.md`.
- Immediate confusion belongs in `grill-the-student`.
- Teaching the next step belongs in `tutor-mode`.
- Repeated wrong reasoning belongs in `misconception-diagnosis`.
- Durable learning evidence belongs in `session-wrap`, after student confirmation.

The skills stay separate, but the student experience feels continuous.
