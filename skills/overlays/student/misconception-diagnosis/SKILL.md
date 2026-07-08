---
name: misconception-diagnosis
description: Diagnose and repair a persistent student misconception after hints, tutoring, or pre-answer alignment reveal repeated wrong reasoning. Use when the student has shown an attempt and the same conceptual error recurs across prompts, examples, workflow steps, or corrections; reproduce the reasoning, localize the broken step, offer a minimal counterexample, verify repair Socratically, and emit a mastery evidence record for session-wrap. Do not use for vague context, missing prerequisites, one-off slips, or ordinary tutor-mode scaffolding.
category: overlays
status: active
stage: overlay
role_compatibility:
  - student
default_interaction: socratic
interaction_skill: socratic-tutor
runs_after:
  - identity-loader
  - grill-the-student
overlays:
  - problem-framing
  - data-audit
  - eda-plan
  - modeling
  - model-evaluation
  - experiment-log
recommended_next:
  - tutor-mode
  - exercise-generator
  - session-wrap
inputs:
  - student attempt or repeated claim
  - prior hints or tutor-mode turns
  - underlying workflow step
  - class notation and course context
outputs:
  - reproduced student reasoning
  - localized broken step
  - minimal counterexample
  - Socratic repair check
  - mastery evidence record
human_review_required: false
---

# Misconception Diagnosis

Diagnose the smallest conceptual gap that explains a student's repeated error.

This is not `hint-ladder` and not ordinary `tutor-mode`. Use it only after the student has shown enough reasoning to distinguish a misconception from missing context, missing prerequisite knowledge, or a one-off slip.

## Use When

Use this overlay when:

- the student repeats the same type of error after one or more hints
- the student's attempt reveals a plausible but wrong mental model
- the wrong answer would propagate through later workflow steps
- `grill-the-student` has already found the confusion boundary and the issue is not just vague context
- a repaired understanding should be recorded for `session-wrap`

## Inputs

- the student's exact claim, attempt, or explanation
- the relevant underlying skill or workflow step
- prior hint or tutor-mode turns, if available
- `NOTATION.md` and `COURSE-CONTEXT.md`, if identity-loader loaded them

## Outputs

Produce:

- a faithful reproduction of the student's reasoning
- the earliest broken step
- a minimal counterexample or contrast case
- one Socratic repair prompt
- an evidence record for `session-wrap`

## Stop Conditions

Stop and route elsewhere when:

- the student has not shown an attempt or reasoning; use `grill-the-student` or `tutor-mode`
- the issue is unfamiliar prerequisite material; route to the relevant method skill or `tutor-mode`
- the issue is a one-off arithmetic, syntax, or transcription slip; use `hint-ladder` or a small correction prompt
- the task is graded work and the student wants the finished answer
- you cannot reproduce the student's reasoning; ask one clarifying question first

## How It Wraps Existing Skills

Choose the relevant base skill, then inspect the student's attempt against the logic of that workflow.

Focus on diagnosing:

- what they misunderstood
- why that misunderstanding is plausible
- what contrast or correction would repair it

## Procedure

Ask one question at a time. Do not lecture over the student's reasoning.

1. Ground the context.
   - Name the underlying skill or workflow step.
   - Use the student's documented notation and course coverage when present.
   - Quote or paraphrase the student's exact reasoning before diagnosing.

2. Reproduce the student reasoning.
   - Restate the chain as the student seems to see it.
   - If the chain is uncertain, ask: "Is this the reasoning you were using?"
   - Do not continue until the reasoning is clear enough to test.

3. Localize the broken step.
   - Identify the earliest step where valid reasoning becomes invalid.
   - Name the misconception as a claim about the concept, not a flaw in the student.
   - Explain why the misconception was plausible from the course context.

4. Give a minimal counterexample.
   - Use the smallest example, number, diagram, pseudo-dataset, or symbolic contrast that breaks the misconception.
   - Keep the counterexample focused on the misconception, not the whole assignment.
   - Avoid replacing the student's full work with a complete solution.

5. Verify repair Socratically.
   - Ask the student to revise the broken step or explain the counterexample back.
   - If the repair succeeds, mark the evidence record status as `resolved`.
   - If the repair is partial, mark it as `needs_practice` and route to `exercise-generator` or `tutor-mode`.

6. Hand off to session memory.
   - Emit an evidence record, but do not edit `mastery.json` directly.
   - Tell `session-wrap` to append the confirmed record to `misconceptions_resolved` at `/wrap`.

## Output Format

Use this format:

````markdown
## Misconception Diagnosis

### Underlying Skill Or Workflow
{skill or workflow step}

### Student Reasoning Reproduced
{student's reasoning in their notation}

### Broken Step
{earliest step where the reasoning fails}

### Minimal Counterexample
{small contrast case that exposes the misconception}

### Repair Check
{one Socratic prompt asking the student to revise or explain}

### Evidence Record For Session Wrap
```json
{
  "date": "YYYY-MM-DD",
  "domain": "domain key from mastery.json, if known",
  "topic": "topic key from mastery.json, if known",
  "misconception": "plain-language misconception",
  "student_reasoning_evidence": "short evidence from the student's attempt",
  "broken_step": "earliest invalid step",
  "counterexample": "minimal counterexample used",
  "repair_check": "student's repair result or pending prompt",
  "status": "resolved | needs_practice",
  "recommended_mastery_update": "none | introduced | practiced"
}
```
````

## Evidence Record Rules

- Use existing `mastery.json` domain and topic keys when they fit.
- Use `topic: "unmapped"` when no current key fits; do not invent a new key during diagnosis.
- Set `status: "resolved"` only after the student repairs the reasoning in their own words.
- Set `recommended_mastery_update: "none"` unless the repair includes enough practice for `session-wrap` to propose a conservative update.
- Never write the evidence record directly; `session-wrap` handles confirmed memory writes.

## Guardrails

- Do not label the student as confused without naming the actual confusion.
- Do not give only the right answer or a full worked solution.
- Do not diagnose when the issue is just incomplete effort or missing information.
- Do not use textbook notation when `NOTATION.md` says the course uses something else.
- Do not silently correct possible errors in class notes; flag them and ask.
- Do not mark a misconception as resolved until the student passes the repair check.

## Escalation Conditions

If the student lacks prerequisite knowledge entirely, say so directly and recommend stepping back to `tutor-mode` or a simpler exercise.
