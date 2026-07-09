# Interview Me Examples

## Ambiguous Artifact Request

Input:

```text
Build me a dashboard for experiment metrics.
```

Good response shape:

```text
Hypothesis: You need a personal experiment status view, and "dashboard" is the artifact name that came to mind.
Confidence: 35% - missing user, decision, success criterion, and out-of-scope boundary.

Question: Who needs to use this output to make a decision?
Guess: You personally, because the pain sounds like tracking active runs rather than reporting to leadership.
```

Do not propose chart libraries, page layout, or implementation tasks yet.

## Conventional Best-Practice Answer

Input:

```text
I should probably make this scalable before we show it to engineering.
```

Good response:

```text
Question: If you did not have to justify this as "best practice", what would you actually want to be true before engineering sees it?
Guess: You want the input and output contract to be stable, not a fully scalable system yet.
```

## Confirmed Restatement

Output before handoff:

```text
Outcome: A lightweight list of active experiments and their next required decision.
User: The experiment owner.
Why now: Runs are spread across docs and are getting lost.
Success: The owner can answer what is running, what is blocked, and what decision is next.
Constraint: Keep it local and simple; no new service.
Out of scope: Production dashboard, analytics warehouse, or executive reporting.
Recommended next skill: problem-framing if this becomes a formal analytical workflow; ml-feature-spec if it becomes an engineering-facing feature.
```
