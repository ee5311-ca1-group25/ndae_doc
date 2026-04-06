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

## Render a synthetic svBRDF example

```bash
uv run python scripts/render_svbrdf_example.py \
  --preset plastic \
  --output outputs/render_example/plastic.png \
  --image-size 256
```

Alternative coated-metal preset:

```bash
uv run python scripts/render_svbrdf_example.py \
  --preset coated_metal \
  --output outputs/render_example/coated_metal.png \
  --image-size 256
```

These commands synthesize smoother BRDF maps and a height map, run them through
the current Lecture 3 renderer, and save tone-mapped PNGs.
