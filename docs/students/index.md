# For Students

## What This System Teaches

This system teaches data science as a workflow, not as isolated techniques.

Students use AI as a coach rather than an answer generator. The goal is to build durable reasoning habits through explicit workflow steps, required artifacts, and iterative revision.

Students train on the same backbone used in professional projects. The difference is delivery style: learning is scaffolded, feedback-oriented, and attempt-first.

## How Learning Works

The tutoring architecture is:

Canonical Skill  
↓  
Tutor Overlay  
↓  
Guided Practice  
↓  
Feedback

Canonical skills define workflow logic and artifact requirements. The tutor overlay changes how Codex teaches that logic.

In student mode:

- Codex asks for an attempt before giving full answers.
- Hints and checks come before full solutions.
- Exercises adapt to current skill level and recent errors.
- Feedback focuses on reasoning quality and workflow discipline.

## Learning Path

1. `problem-framing`  
   Learn to convert a broad question into a precise analytical objective, constraints, and success criteria.

2. `data-audit`  
   Learn to inspect data quality, scope, assumptions, and readiness before analysis.

3. `eda-plan`  
   Learn to design exploratory steps that are hypothesis-linked, bounded, and reproducible.

4. `experiment-log`  
   Learn to document each modeling iteration with decisions, parameters, outcomes, and next actions.

This path is sequential: framing before audit, audit before exploration, and logging throughout execution.

## Example Session

Student: help me learn difference-in-differences

Codex (student overlay):

- asks conceptual questions to test baseline understanding
- proposes a small dataset for guided practice
- checks intermediate reasoning before continuing
- gives hints before showing a full worked solution

## Key Skills for Students

- `problem-framing`
- `data-audit`
- `eda-plan`
- `experiment-log`
- `causal-design-check`

## Skill Links

- [skills/data-science/problem-framing](https://github.com/wdempsey/codexbatman/tree/main/skills/data-science/problem-framing)
- [skills/data-science/data-audit](https://github.com/wdempsey/codexbatman/tree/main/skills/data-science/data-audit)
- [skills/data-science/experiment-log](https://github.com/wdempsey/codexbatman/tree/main/skills/data-science/experiment-log)
- [skills/overlays/student/tutor-mode](https://github.com/wdempsey/codexbatman/tree/main/skills/overlays/student/tutor-mode)
