# Data

## Mini SVBRDF subset

Use the helper script to fetch a small local subset:

```bash
uv run python scripts/download_svbrdf_mini.py --exemplar clay_solidifying --count 4
```

Data is written under:

```text
data_local/svbrdf_mini/<exemplar>/
```

## Fallback options

If the source website blocks automated requests, use one of the fallback modes:

- Pass a `--cookie-header`
- Pass a `--signed-url`
- Use `--semi-auto` and paste request metadata from your browser

## Versioning guidance

Large datasets should not be committed to git. Keep generated data under ignored local directories.
