#!/usr/bin/env python3
"""Deterministic file-level guardrails for Codex Batman lifecycle events."""

from __future__ import annotations

import argparse
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


STUDENT_MEMORY_PREFIX = "memory/students/"
FLAGGED_SKILL_SUFFIX = "/flagged-skills.md"
SHARED_SKILL_PREFIXES = ("skills/", "evals/")
SHARED_SKILL_FILES = {
    "SKILL-STYLE.md",
    "CAPABILITY-MATRIX.md",
    "skills/METADATA.md",
}


@dataclass(frozen=True)
class Change:
    status: str
    paths: tuple[str, ...]


def parse_name_status(output: str) -> list[Change]:
    changes: list[Change] = []
    for raw_line in output.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        parts = line.split("\t")
        if len(parts) < 2:
            raise ValueError(f"Could not parse git name-status line: {raw_line!r}")
        changes.append(Change(status=parts[0], paths=tuple(parts[1:])))
    return changes


def is_student_memory(path: str) -> bool:
    return path.startswith(STUDENT_MEMORY_PREFIX)


def is_flagged_skill_file(path: str) -> bool:
    return is_student_memory(path) and path.endswith(FLAGGED_SKILL_SUFFIX)


def is_shared_skill_surface(path: str) -> bool:
    return path in SHARED_SKILL_FILES or path.startswith(SHARED_SKILL_PREFIXES)


def path_was_deleted(change: Change, path: str) -> bool:
    return change.status.startswith("D") and path == change.paths[0]


def evaluate(changes: list[Change]) -> list[str]:
    touched_paths = {path for change in changes for path in change.paths}
    flagged_skill_touched = any(is_flagged_skill_file(path) for path in touched_paths)
    shared_skill_touched = any(is_shared_skill_surface(path) for path in touched_paths)

    failures: list[str] = []

    if flagged_skill_touched and shared_skill_touched:
        failures.append(
            "Student flagged-skill PRs must not also modify shared skill surfaces. "
            "Keep the student flag PR separate from any maintainer draft skill PR."
        )

    for change in changes:
        for path in change.paths:
            if path_was_deleted(change, path) and is_student_memory(path):
                failures.append(
                    f"Student memory file deletion blocked: {path}. "
                    "Use an explicit maintainer cleanup PR for memory removal."
                )

    return failures


def run_git_name_status(base: str | None, head: str | None) -> str:
    if base and head:
        cmd = ["git", "diff", "--name-status", base, head]
    elif base or head:
        raise ValueError("--base and --head must be provided together")
    else:
        cmd = ["git", "diff", "--cached", "--name-status"]
    return subprocess.check_output(cmd, text=True)


def read_changes(args: argparse.Namespace) -> list[Change]:
    if args.from_file:
        return parse_name_status(Path(args.from_file).read_text())
    return parse_name_status(run_git_name_status(args.base, args.head))


def run_self_test() -> None:
    passing_cases = [
        [Change("M", ("memory/students/alex/flagged-skills.md",))],
        [Change("A", ("skills/methods/example/SKILL.md",))],
        [Change("M", ("docs/students/index.md",))],
    ]
    failing_cases = [
        [
            Change("M", ("memory/students/alex/flagged-skills.md",)),
            Change("A", ("skills/methods/example/SKILL.md",)),
        ],
        [Change("D", ("memory/students/alex/profile.md",))],
    ]

    for case in passing_cases:
        failures = evaluate(case)
        assert not failures, failures

    for case in failing_cases:
        failures = evaluate(case)
        assert failures, "Expected lifecycle gate failure"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check Codex Batman student-memory and skill-promotion guardrails."
    )
    parser.add_argument("--base", help="Base git ref for branch diff checks.")
    parser.add_argument("--head", help="Head git ref for branch diff checks.")
    parser.add_argument(
        "--from-file",
        help="Read git diff --name-status formatted lines from a file.",
    )
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="Run built-in unit checks for the lifecycle gate.",
    )
    args = parser.parse_args()

    if args.self_test:
        run_self_test()
        print("codexbatman lifecycle gate self-test passed.")
        return 0

    changes = read_changes(args)
    failures = evaluate(changes)

    if failures:
        print("codexbatman lifecycle gate failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("codexbatman lifecycle gate passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
