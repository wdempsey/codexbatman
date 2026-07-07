#!/usr/bin/env python3
"""Validate and optionally score Codex Batman skill eval task sets."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from tempfile import TemporaryDirectory


REQUIRED_TOP_LEVEL = {"schema_version", "skill", "split", "cases"}
REQUIRED_CASE_FIELDS = {
    "id",
    "input",
    "expected_route",
    "must_include",
    "must_not_include",
    "notes",
}
ALLOWED_SPLITS = {"improvement", "heldout"}


@dataclass
class EvalCase:
    file_path: Path
    skill: str
    split: str
    case_id: str
    must_include: list[str]
    must_not_include: list[str]


def normalize_case_id(case_id: str) -> str:
    return re.sub(r"[^a-zA-Z0-9_.-]+", "-", case_id).strip("-")


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text())
    except json.JSONDecodeError as exc:
        raise ValueError(f"{path}: invalid JSON: {exc}") from exc


def require_string_list(value: object, field: str, path: Path, case_id: str) -> None:
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        raise ValueError(f"{path}: case {case_id!r} field {field!r} must be a list of strings")


def validate_eval_file(path: Path) -> list[EvalCase]:
    data = load_json(path)
    missing = REQUIRED_TOP_LEVEL - set(data)
    if missing:
        raise ValueError(f"{path}: missing top-level fields: {', '.join(sorted(missing))}")

    if data["schema_version"] != 1:
        raise ValueError(f"{path}: schema_version must be 1")
    if data["split"] not in ALLOWED_SPLITS:
        raise ValueError(f"{path}: split must be one of {sorted(ALLOWED_SPLITS)}")
    if not isinstance(data["skill"], str) or not data["skill"]:
        raise ValueError(f"{path}: skill must be a non-empty string")
    if not isinstance(data["cases"], list) or not data["cases"]:
        raise ValueError(f"{path}: cases must be a non-empty list")

    parent_names = {parent.name for parent in path.parents}
    if data["split"] not in parent_names:
        raise ValueError(f"{path}: split {data['split']!r} must live under an {data['split']}/ directory")

    cases: list[EvalCase] = []
    seen_ids: set[str] = set()
    for case in data["cases"]:
        if not isinstance(case, dict):
            raise ValueError(f"{path}: each case must be an object")
        missing_case_fields = REQUIRED_CASE_FIELDS - set(case)
        if missing_case_fields:
            raise ValueError(
                f"{path}: case missing fields: {', '.join(sorted(missing_case_fields))}"
            )
        case_id = case["id"]
        if not isinstance(case_id, str) or not case_id:
            raise ValueError(f"{path}: case id must be a non-empty string")
        if case_id in seen_ids:
            raise ValueError(f"{path}: duplicate case id {case_id!r}")
        seen_ids.add(case_id)

        for field in ("expected_route", "must_include", "must_not_include"):
            require_string_list(case[field], field, path, case_id)
        if not isinstance(case["input"], str) or not case["input"]:
            raise ValueError(f"{path}: case {case_id!r} input must be a non-empty string")
        if not isinstance(case["notes"], str):
            raise ValueError(f"{path}: case {case_id!r} notes must be a string")

        cases.append(
            EvalCase(
                file_path=path,
                skill=data["skill"],
                split=data["split"],
                case_id=case_id,
                must_include=case["must_include"],
                must_not_include=case["must_not_include"],
            )
        )
    return cases


def discover_eval_files(root: Path) -> list[Path]:
    return sorted(path for path in root.rglob("*.json") if "schemas" not in path.parts)


def score_response(case: EvalCase, response_text: str) -> list[str]:
    response_lower = response_text.lower()
    failures: list[str] = []
    for required in case.must_include:
        if required.lower() not in response_lower:
            failures.append(f"{case.case_id}: missing required text {required!r}")
    for forbidden in case.must_not_include:
        if forbidden.lower() in response_lower:
            failures.append(f"{case.case_id}: includes forbidden text {forbidden!r}")
    return failures


def response_path_for(responses_dir: Path, case_id: str) -> Path:
    return responses_dir / f"{normalize_case_id(case_id)}.txt"


def run(root: Path, responses_dir: Path | None) -> int:
    eval_files = discover_eval_files(root)
    if not eval_files:
        print(f"No eval JSON files found under {root}")
        return 1

    all_cases: list[EvalCase] = []
    failures: list[str] = []
    seen_global_ids: set[str] = set()

    for path in eval_files:
        try:
            cases = validate_eval_file(path)
        except ValueError as exc:
            failures.append(str(exc))
            continue
        for case in cases:
            if case.case_id in seen_global_ids:
                failures.append(f"{path}: duplicate global case id {case.case_id!r}")
            seen_global_ids.add(case.case_id)
        all_cases.extend(cases)

    if responses_dir:
        for case in all_cases:
            path = response_path_for(responses_dir, case.case_id)
            if not path.exists():
                failures.append(f"{case.case_id}: missing response file {path}")
                continue
            failures.extend(score_response(case, path.read_text()))

    if failures:
        print("Skill eval check failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    split_counts: dict[str, int] = {}
    for case in all_cases:
        split_counts[case.split] = split_counts.get(case.split, 0) + 1

    print(
        "Skill eval check passed: "
        + ", ".join(f"{split}={count}" for split, count in sorted(split_counts.items()))
    )
    return 0


def run_self_test() -> None:
    with TemporaryDirectory() as tmp:
        root = Path(tmp) / "evals"
        eval_dir = root / "improvement" / "skills"
        eval_dir.mkdir(parents=True)
        eval_file = eval_dir / "example.json"
        eval_file.write_text(
            json.dumps(
                {
                    "schema_version": 1,
                    "skill": "example",
                    "split": "improvement",
                    "cases": [
                        {
                            "id": "example-case",
                            "input": "Route this.",
                            "expected_route": ["example"],
                            "must_include": ["example"],
                            "must_not_include": ["forbidden"],
                            "notes": "self-test",
                        }
                    ],
                }
            )
        )
        cases = validate_eval_file(eval_file)
        assert len(cases) == 1
        assert not score_response(cases[0], "Use example.")
        failures = score_response(cases[0], "Use forbidden.")
        assert len(failures) == 2


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        default="evals",
        help="Eval root directory. Defaults to evals.",
    )
    parser.add_argument(
        "--responses-dir",
        help="Optional directory of response text files named <case-id>.txt.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Validate eval files. This is the default when no responses directory is provided.",
    )
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="Run built-in checks for the eval runner.",
    )
    args = parser.parse_args()

    if args.self_test:
        run_self_test()
        print("Skill eval runner self-test passed.")
        return 0

    responses_dir = Path(args.responses_dir) if args.responses_dir else None
    return run(Path(args.root), responses_dir)


if __name__ == "__main__":
    sys.exit(main())
