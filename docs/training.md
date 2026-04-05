# Training

## Current status

The repository is in incremental implementation phases. The current CLI supports a dry-run mode and workspace initialization.

## Typical command

```bash
uv run python scripts/train_svbrdf.py --config configs/base.yaml --dry-run
```

## Output structure

The command writes results under:

```text
outputs/<experiment_name>/
```

Expected artifacts include:

- `config.resolved.yaml`
- Run summary logs

## Next steps

As training modules are implemented, this page will be expanded with reproducible experiment recipes.
