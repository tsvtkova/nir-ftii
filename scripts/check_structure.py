from pathlib import Path

REQUIRED = [
    "README.md",
    "docs/FULL_CRITERIA.md",
    "docs/ARTIFACT_REQUIREMENTS.md",
    "docs/GITHUB_STEP_BY_STEP.md",
    "rubrics/GENERAL_MATRIX.md",
    "rubrics/PROJECT_TYPES/RESEARCH.md",
    "rubrics/PROJECT_TYPES/TECHNOLOGICAL.md",
    "rubrics/PROJECT_TYPES/INDUSTRIAL.md",
    "rubrics/PROJECT_TYPES/COLLABORATIVE.md",
    "rubrics/PROJECT_TYPES/GROUP.md",
    "commission/QUICK_CHECKLIST.md",
    "commission/SCORING_FLOW.md",
]

root = Path(__file__).resolve().parents[1]
missing = [p for p in REQUIRED if not (root / p).exists()]

if missing:
    print("Не хватает файлов:")
    for p in missing:
        print(" -", p)
    raise SystemExit(1)

print("Структура репозитория проверена: OK")
