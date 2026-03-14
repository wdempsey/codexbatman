# Skill Testing Protocol

A lightweight validation protocol for new and updated skills.

This page exists as a reference target for the testing guidance cited in [Skill Patterns & Conventions](skill-patterns.md).

## What To Test

Check four things before treating a skill as ready:

1. Trigger accuracy
2. Execution correctness
3. Graceful degradation
4. Performance and usability

## Trigger Accuracy

Confirm that the skill activates on natural user phrasing.

- Test 2-3 realistic requests that should trigger the skill.
- Test nearby requests that should not trigger the skill.
- Check whether the description is specific enough to avoid false positives.

## Execution Correctness

Confirm that the skill performs the intended workflow.

- Run one representative happy-path case.
- Verify the expected artifacts, outputs, or edits are produced.
- Check that required inputs are requested or validated.
- Confirm that stop conditions and safety rules are followed.

## Graceful Degradation

Confirm that partial failure does not collapse the whole workflow.

- Simulate one unavailable tool, file, or dependency.
- Verify the skill reports what failed and what continued.
- Check that fallback behavior matches the skill's stated contract.

## Performance And Usability

Confirm that the skill is practical in real use.

- Check whether the steps are easy to follow in one session.
- Look for unnecessary tool calls or repeated work.
- Note any latency, confusion, or confirmation overload.
- Record whether the skill is meaningfully better than handling the task without the skill.

## Exit Criteria

A skill is ready to share when:

- it triggers reliably on intended requests
- it avoids obvious false positives
- it completes a representative task correctly
- it handles at least one failure mode without breaking down
- its instructions and outputs are clear enough for repeated use
