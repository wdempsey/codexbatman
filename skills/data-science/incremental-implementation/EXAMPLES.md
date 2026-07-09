# Incremental Implementation Examples

## ML Feature Delivery

Input:

```text
Implement the approved risk-score feature. It touches feature generation, model serialization, and the inference wrapper.
```

Good slice plan:

```text
Slice 1: Add the input/output contract test for the inference wrapper.
Verify: targeted test fails for the missing contract.

Slice 2: Implement the smallest wrapper behavior that satisfies the contract.
Verify: targeted test passes.

Slice 3: Wire serialized model loading behind the existing interface.
Verify: wrapper contract test plus smoke prediction.

Slice 4: Add feature generation path for the approved schema.
Verify: feature schema test plus full wrapper smoke test.
```

If the user asks for tests first, hand the test-writing portion to `tdd-data-pipeline`.

## Documentation Tooling Change

Input:

```text
Add a docs check that validates skill eval JSON files and include it in CI.
```

Good slice plan:

```text
Slice 1: Add the validator script and a self-test.
Slice 2: Add a minimal eval fixture and run the validator locally.
Slice 3: Wire the script into the existing CI job.
Slice 4: Update docs with the exact command.
```

Do not combine script creation, CI wiring, docs, and unrelated cleanup in one increment.
