# Core Data Science Workflow

## Why Workflows Matter

AI tools make analysis easier and faster, but discipline and reproducibility still determine whether results are trustworthy.

AI can generate analysis. Workflows ensure the analysis is correct, reproducible, and interpretable.

This system encodes best practices as reusable workflow phases so teams can execute consistently across projects.

## The Canonical Workflow

1. problem framing
2. data audit
3. exploratory analysis
4. modeling
5. evaluation
6. experiment logging

```text
problem framing
↓
data audit
↓
EDA
↓
modeling
↓
evaluation
↓
experiment logging
```

## Skills as Workflow Execution

Each phase is executed through a Codex skill.

- `/problem-framing` -> [skills/data-science/problem-framing/](https://github.com/wdempsey/codexbatman/tree/main/skills/data-science/problem-framing)
- `/data-audit` -> [skills/data-science/data-audit/](https://github.com/wdempsey/codexbatman/tree/main/skills/data-science/data-audit)
- `/eda-plan` -> `skills/data-science/eda-plan/` (planned; not yet created)
- `/modeling` -> `skills/data-science/modeling/` (planned; not yet created)
- `/evaluation` -> `skills/data-science/model-evaluation/` (planned; not yet created)
- `/experiment-log` -> [skills/data-science/experiment-log/](https://github.com/wdempsey/codexbatman/tree/main/skills/data-science/experiment-log)

## Roles

- students -> learn the workflow
- data scientists -> execute the workflow
- managers -> review and coordinate the workflow
