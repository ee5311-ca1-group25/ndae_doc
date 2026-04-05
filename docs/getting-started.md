# Getting Started

## Prerequisites

- Python 3.11+
- uv package manager
- npx (for dataset helper fallback paths)

## Install dependencies

From the NDAE repository root:

```bash
uv sync
```

## Dry run command

```bash
uv run python main.py --config configs/base.yaml --dry-run
```

Alternative entry point:

```bash
uv run python scripts/train_svbrdf.py --config configs/base.yaml --dry-run
```

The dry run resolves configuration, creates an output directory, and exits before model training.
