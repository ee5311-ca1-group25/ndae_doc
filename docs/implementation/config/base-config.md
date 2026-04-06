# Base Config

## Purpose

`configs/base.yaml` is the canonical small configuration used for smoke tests and early implementation phases.

For the current Lecture 3 config path it does three important jobs:

- it carries the new timeline fields
- it carries the default rendering metadata used by the svBRDF pipeline
- it points to the mini SVBRDF subset that is small enough for fast tests

## Public API / key types

Relevant `rendering` block:

```yaml
rendering:
  renderer_type: diffuse_cook_torrance
  n_normal_channels: 1
  n_aug_channels: 9
  camera_fov: 50.0
  camera_distance: 1.0
  light_intensity: 0.0
  light_xy_position: [0.0, 0.0]
  height_scale: 1.0
  gamma: 2.2
```

Relevant `data` block:

```yaml
data:
  root: data_local/svbrdf_mini
  exemplar: clay_solidifying
  image_size: 256
  crop_size: 128
  n_frames: 8
  t_I: -2.0
  t_S: 0.0
  t_E: 10.0
```

## Behavior and invariants

- `root` and `exemplar` point to the local mini dataset
- `n_frames: 8` matches the current `_manifest.json` selection for `clay_solidifying`
- `image_size: 256` defines the final exemplar tensor resolution
- `crop_size: 128` is the target crop size for later training steps
- `t_I`, `t_S`, and `t_E` encode the default ODE time domain used throughout the data pipeline
- `renderer_type: diffuse_cook_torrance` implies `n_brdf_channels = 8`
- `n_aug_channels: 9` now lives under `rendering`, not `model`
- `light_xy_position: [0.0, 0.0]` is parsed into `(0.0, 0.0)` in the resolved config
- the resolved rendering channel count is `8 + 1 + 9 = 18`

With `t_S = 0.0`, `t_E = 10.0`, and `n_frames = 8`, the implied frame spacing is:

```text
dt = (t_E - t_S) / n_frames = 1.25
```

## Error handling

This file does not contain logic, but its contents are checked by:

- `src/ndae/config/_parsing.py`
- `src/ndae/config/validation.py`

## Tests / validation

The base config is used directly by:

- `tests/test_config.py`
- `tests/test_smoke.py`
- `tests/test_dataset.py`
- `tests/test_package_layout.py`

## Related files

- `src/ndae/config/schema.py`
- `src/ndae/rendering/__init__.py`
- `src/ndae/data/exemplar.py`
- `src/ndae/data/timeline.py`
