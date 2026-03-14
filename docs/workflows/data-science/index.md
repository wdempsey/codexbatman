# Core Data Science Workflow

## Why Workflows Matter

AI tools make analysis easier and faster, but discipline and reproducibility still determine whether results are trustworthy.

AI can generate analysis. Workflows ensure the analysis is correct, reproducible, and interpretable.

This system encodes best practices as reusable workflow phases so teams can execute consistently across projects.

## The Canonical Workflow

1. project bootstrap
2. problem framing
3. data audit
4. exploratory analysis
5. modeling
6. evaluation
7. experiment logging

```text
project bootstrap
↓
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

- `/project-bootstrap` -> [skills/data-science/project-bootstrap/](https://github.com/wdempsey/codexbatman/tree/main/skills/data-science/project-bootstrap)
- `/problem-framing` -> [skills/data-science/problem-framing/](https://github.com/wdempsey/codexbatman/tree/main/skills/data-science/problem-framing)
- `/data-audit` -> [skills/data-science/data-audit/](https://github.com/wdempsey/codexbatman/tree/main/skills/data-science/data-audit)
- `/eda-plan` -> [skills/data-science/eda-plan/](https://github.com/wdempsey/codexbatman/tree/main/skills/data-science/eda-plan)
- `/modeling` -> [skills/data-science/modeling/](https://github.com/wdempsey/codexbatman/tree/main/skills/data-science/modeling)
- `/evaluation` -> [skills/data-science/model-evaluation/](https://github.com/wdempsey/codexbatman/tree/main/skills/data-science/model-evaluation)
- `/experiment-log` -> [skills/data-science/experiment-log/](https://github.com/wdempsey/codexbatman/tree/main/skills/data-science/experiment-log)

## Roles

- students -> learn the workflow
- data scientists -> execute the workflow
- managers -> review and coordinate the workflow
