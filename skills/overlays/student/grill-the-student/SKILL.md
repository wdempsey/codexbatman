---
name: grill-the-student
description: Run a pre-answer alignment interview for a student before tutoring or solving begins. Use when a student asks for help but their notation, course coverage, assignment constraints, or exact confusion boundary is unclear; ask one question at a time until Codex can restate the student's mental model and the student confirms it. Do not use for ordinary tutor-mode scaffolding after the student's context is already clear, or for misconception repair after repeated wrong attempts.
category: overlays
status: active
stage: overlay
role_compatibility:
  - student
default_interaction: socratic
interaction_skill: socratic-tutor
runs_after:
  - identity-loader
recommended_next:
  - tutor-mode
  - misconception-diagnosis
inputs:
  - student question
  - known course context
  - assignment prompt or constraints
  - student attempt or partial reasoning
outputs:
  - confirmed mental-model restatement
  - notation notes
  - course-coverage boundary
  - confusion boundary
human_review_required: false
---

# Grill The Student

Run this before tutoring when the student's context is too blurry to teach safely.

This is not `tutor-mode`. It does not teach the topic, solve the problem, or diagnose a misconception. It asks focused alignment questions until the tutor knows the student's notation, course coverage, and confusion boundary well enough to begin.

## Use When

Use this skill when:

- the student asks for help but their notation or course vocabulary is unclear
- the student says "I don't know where I'm stuck" or gives a vague confusion report
- the assignment or professor's framing may constrain what methods are allowed
- Codex is tempted to explain a concept before knowing what the student has already covered
- the next tutoring step depends on whether the student is confused about setup, notation, method choice, algebra, code, or interpretation

## Inputs

- student's current question
- any visible attempt, notes, assignment prompt, or course reference
- identity-loader context, if available

## Outputs

Produce only:

- a confirmed restatement of the student's mental model
- notation and vocabulary notes
- what the course has and has not covered
- the narrow confusion boundary
- the recommended next skill

## Stop Conditions

Stop and ask before continuing when:

- the student has not confirmed the restatement
- the problem appears to be graded work and the student wants the answer
- the student asks to upload class notes; route to the future class-notes ingestion convention rather than inventing persistent files
- the interview reveals a repeated conceptual error; route to `misconception-diagnosis`
- the context is clear enough for ordinary `tutor-mode`

## Procedure

Ask one question at a time. Wait for the student's answer before asking the next question.

1. Start with the student's goal.
   - Ask what they are trying to do in one sentence.
   - If they shared an assignment prompt, ask which part they are working on now.

2. Extract notation.
   - Ask what symbols, variable names, or terms their class uses.
   - Mirror their notation back exactly; do not silently translate to another convention.

3. Establish course coverage.
   - Ask what methods or concepts the instructor has introduced so far.
   - Ask what methods are explicitly allowed or discouraged for this task.

4. Find the confusion boundary.
   - Ask what step felt solid immediately before the confusion began.
   - Ask what the first unclear word, equation, code line, or decision was.
   - Do not explain yet; keep narrowing.

5. Restate the mental model.
   - Summarize what the student seems to understand.
   - Summarize what they are uncertain about.
   - Ask: "Did I get your current model right?"

6. Hand off.
   - If the student confirms, route to `tutor-mode` with the confirmed notes.
   - If the student corrects the restatement, ask one more alignment question and restate again.
   - If the student has repeated a wrong causal or conceptual claim, route to `misconception-diagnosis`.

## Output Format

Use this format only after the student confirms the restatement:

```markdown
## Confirmed Alignment

### Student Goal
{one sentence}

### Notation And Vocabulary
{symbols, terms, variable names, and course-specific wording}

### Course Coverage
{covered, not covered, allowed, and off-limits methods}

### Confusion Boundary
{the first unclear step or concept}

### Confirmed Mental Model
{what the student understands and how they currently reason about the problem}

### Next Skill
{tutor-mode or misconception-diagnosis, with one sentence why}
```

## Guardrails

- Do not answer the substantive question during the grill.
- Do not ask a checklist all at once.
- Do not overwrite the student's notation with a standard notation unless they ask for translation.
- Do not assume the course has covered a method just because it is standard.
- Do not store new memory files; this skill only prepares the tutoring handoff.
