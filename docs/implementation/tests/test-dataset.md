# Dataset Tests

## Purpose

`tests/test_dataset.py` is the executable specification for the current data-path implementation.

It does more than check shapes. The file encodes the behavior that the data pipeline must preserve as later phases extend the project.

Package-export, config, and CLI smoke regression are intentionally kept in separate files:

- `tests/test_package_layout.py`
- `tests/test_config.py`
- `tests/test_smoke.py`

## Public API / key types

The test file exercises:

- `Timeline`
- `ExemplarDataset`
- `random_crop`
- `random_take`
- `stratified_uniform`
- `sample_frame_indices`

It also uses `DataConfig` and `load_config` to test the integrated config-to-data path.

## Behavior and invariants

The test groups are organized around three layers.

### Timeline tests

These verify:

- construction from config
- `dt`, warm-up duration, and generation duration
- round-trip frame/time conversion
- clamping outside the valid time range
- constructor and index validation

### Exemplar dataset tests

These verify:

- loading the real mini exemplar from `configs/base.yaml`
- manifest order preservation
- fallback filename sorting when no manifest exists
- uniform downsampling when more frames are available than requested
- negative indexing and out-of-range access behavior
- path resolution with `base_dir`

### Sampling tests

These verify:

- deterministic `random_crop` and `random_take` under fixed seeds
- spatial continuity for `random_crop`
- value preservation for `random_take`
- ordered, in-range samples from `stratified_uniform`
- refresh-step and continuation-step behavior for `sample_frame_indices`

## Error handling

The tests explicitly check that invalid inputs raise the right exception families:

- `ValueError` for invalid dimensions, counts, and timeline semantics
- `IndexError` for invalid element access

This matters because later code can rely on these boundaries instead of silently clamping incorrect usage.

## Tests / validation

The recommended command is:

```bash
PYTHONPATH=src pytest tests/test_package_layout.py tests/test_dataset.py tests/test_config.py tests/test_smoke.py
```

This combines:

- the dataset and utility checks
- package export regression
- config regression coverage
- the dry-run smoke test

## Related files

- `src/ndae/data/exemplar.py`
- `src/ndae/data/timeline.py`
- `src/ndae/data/sampling.py`
- `src/ndae/config/validation.py`
