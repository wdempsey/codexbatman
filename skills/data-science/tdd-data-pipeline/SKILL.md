---
name: tdd-data-pipeline
description: Test-driven development for data science code on a software team. Use when building or fixing data pipelines, feature engineering functions, model inference wrappers, or any data transformation that ships as production code. Triggers on "red-green-refactor", "write tests first", "pipeline tests", "test my feature transform", or any request to build data science code with a test-first approach. Adapted from Matt Pocock's tdd skill (github.com/mattpocock/skills).
category: data-science
status: active
role_compatibility:
  - data scientist
prerequisites:
  - problem-framing
  - data-audit
---

# Skill: TDD for Data Pipelines

## Credit

Adapted from Matt Pocock's [`/tdd`](https://github.com/mattpocock/skills/blob/main/skills/engineering/tdd/SKILL.md) skill. Core philosophy (behavior-not-implementation, vertical slices, red-green-refactor) is his. Data science adaptations — what "public interface" means for transforms, what makes a good vs. bad pipeline test, model inference patterns — are specific to this repo.

## When to use this

This skill is for data science code that ships as part of a software product:

- Feature engineering functions (transform raw data → model-ready features)
- Data validation and schema checks
- Model inference wrappers (the function that takes inputs and returns predictions)
- Pipeline steps (ingestion, cleaning, encoding, splitting)

It is NOT for:
- Evaluating model performance (that belongs in `model-evaluation`)
- Exploratory notebooks (use `modeling` or `model-prototype`)
- One-off analysis scripts

## The core principle

Tests should verify **behavior through public interfaces**, not implementation details. For data science code, the public interface is the function signature — inputs in, outputs out. Tests verify that a given input produces the expected output shape, type, or statistical property. They do not test internal variable names, intermediate steps, or sklearn internals.

**A good pipeline test**: `assert transform(df).shape[1] == expected_n_features` — verifies the output contract.

**A bad pipeline test**: `assert pipeline.steps[0][1].strategy == 'median'` — verifies an implementation detail. If you swap imputation strategies, this fails even though behavior may be identical.

## The anti-pattern: horizontal slicing

Do NOT write all tests first, then all implementation. This is the most common mistake when adopting TDD for data science.

```
WRONG (horizontal):
  RED:   test_imputation, test_encoding, test_scaling, test_output_shape
  GREEN: write all transforms

RIGHT (vertical):
  RED → GREEN: test_output_schema → implement schema contract
  RED → GREEN: test_no_nulls_after_impute → implement imputation step
  RED → GREEN: test_inference_returns_probability → implement inference wrapper
```

Horizontal slicing produces tests that check imagined behavior. They pass when things break and fail when you refactor. Vertical slices keep you honest.

## Workflow

### 1. Plan the interface

Before writing any code:

- What does this function take as input? (DataFrame? dict? array?)
- What does it return? (transformed DataFrame? prediction array? dict with schema?)
- Which behaviors matter most to test? (output schema, null handling, value range, inference output type)

Check with the practitioner which behaviors to prioritize. You can't test everything. Focus on contracts that are invisible at the call site — the things that break silently.

**Ask**: "What should the public interface look like? Which failure modes are most dangerous?"

### 2. Tracer bullet

Write ONE test that verifies ONE contract end-to-end:

```python
# Red: write the test first
def test_feature_pipeline_output_schema():
    raw = pd.DataFrame({"age": [25, None, 40], "income": [50000, 80000, None]})
    result = feature_pipeline.transform(raw)
    assert list(result.columns) == ["age_imputed", "income_log", "income_scaled"]
    assert result.shape[0] == 3
```

Run it — it should fail. Then write the minimal code to make it pass. That's your tracer bullet: the path from input to output works.

### 3. Incremental loop

For each remaining behavior:

```
RED:   Write test for next contract → fails
GREEN: Minimal code to pass → passes
```

One test at a time. Only enough code to pass the current test. Do not anticipate future tests.

**Common contracts to test for data science code:**

- **Schema**: output columns, dtypes, shape
- **Null handling**: no nulls leak through after imputation; nulls in unexpected places raise, not silently propagate
- **Value range**: log-transformed values are non-negative; scaled values are in [0,1]; probabilities sum to 1
- **Inference contract**: model wrapper returns a dict with keys `prediction` and `probability`; probability is float in [0,1]
- **Idempotency**: running the pipeline twice on the same input gives the same result
- **Pipeline leakage**: fitting the pipeline on test data raises an error or is architecturally impossible (enforce with sklearn Pipeline, not with tests)

### 4. Refactor

After all tests pass:

- Extract shared setup into pytest fixtures
- Replace magic numbers with named constants
- Deepen modules: if the pipeline has five steps that are each tested separately, consider whether they belong behind a single `transform()` interface
- Run tests after each refactor step

**Never refactor while RED. Get to GREEN first.**

## What a good test looks like for data science

```python
# Good: tests behavior through the public interface
def test_inference_returns_probability_in_unit_interval():
    model = CardiacRiskModel.load("model_card.json")
    result = model.predict(sample_patient_features)
    assert 0.0 <= result["probability"] <= 1.0
    assert result["prediction"] in {0, 1}

# Good: tests the schema contract, not the internal steps
def test_feature_transform_drops_no_rows():
    raw = load_test_fixture("patients_with_missing.csv")
    transformed = feature_pipeline.fit_transform(raw)
    assert len(transformed) == len(raw)

# Bad: tests implementation detail
def test_imputer_uses_median():
    assert pipeline.named_steps["imputer"].strategy == "median"

# Bad: tests model accuracy (belongs in model-evaluation, not unit tests)
def test_model_achieves_roc_auc_above_0_85():
    ...
```

## Checklist per cycle

```
[ ] Test describes a behavioral contract, not an implementation detail
[ ] Test uses the public interface only (function signature, not internals)
[ ] Test would survive an internal refactor that preserves behavior
[ ] Code is minimal — only enough to pass this test
[ ] No speculative features added ahead of the current test
```
