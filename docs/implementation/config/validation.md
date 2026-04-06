# Config Validation

## Purpose

`src/ndae/config/validation.py` enforces semantic constraints after YAML parsing.  
The current implementation extends validation in three directions:

- timeline semantics
- dataset layout and manifest-aware frame counting
- rendering metadata and camera/light parameter sanity

## Public API / key types

Important entry points:

- `validate_config(config, *, base_dir=None) -> None`
- `validate_rendering_config(config) -> None`
- `resolve_data_root(root, *, base_dir=None) -> Path`
- `resolve_available_images(exemplar_dir, *, exemplar) -> list[Path]`
- `load_manifest_images(manifest_path, *, exemplar_dir, exemplar) -> list[Path]`

## Behavior and invariants

Timeline rules:

- `t_I`, `t_S`, and `t_E` must be numeric
- the ordering must satisfy `t_I < t_S < t_E`

Dataset rules:

- `data.root` must exist and be a directory
- `data.exemplar` must resolve to a directory under `data.root`
- the effective frame set is determined by `_manifest.json` when present
- only if no manifest exists does validation fall back to scanning image files by extension
- `data.n_frames` must not exceed the number of effective images

Manifest behavior:

- `selected_files` entries must be strings
- entries must resolve inside the configured exemplar directory
- supported image suffixes are `.jpg`, `.jpeg`, and `.png`
- manifest order is preserved instead of being re-sorted

Path resolution:

- absolute `data.root` values are used as-is
- relative `data.root` values are resolved against `base_dir` when provided
- otherwise they resolve against the current working directory

Rendering rules:

- `rendering.renderer_type` must exist in `ndae.rendering.RENDERER_REGISTRY`
- `rendering.n_brdf_channels` must match the selected renderer metadata
- `rendering.n_normal_channels` must be greater than 0
- `rendering.n_aug_channels` must be greater than or equal to 0
- `rendering.camera_fov`, `rendering.camera_distance`, `rendering.height_scale`,
  and `rendering.gamma` must be positive
- `rendering.light_intensity` must be numeric
- `rendering.light_xy_position` must be a 2-tuple of finite floats

## Error handling

All validation failures raise `ConfigError`. Typical cases include:

- invalid timeline ordering
- missing dataset root or exemplar directory
- malformed manifest JSON
- missing files referenced by the manifest
- unsupported manifest file types
- requested frame count larger than the effective image count
- invalid renderer names
- mismatched BRDF channel counts
- malformed light positions

## Tests / validation

`tests/test_config.py` covers:

- invalid timeline ordering
- missing exemplar directories
- excessive requested frame count
- manifest precedence over raw directory count
- timeline default loading
- rendering default loading
- invalid renderer metadata
- legacy `model.n_aug_channels` rejection

## Related files

- `src/ndae/config/schema.py`
- `src/ndae/config/_parsing.py`
- `src/ndae/rendering/__init__.py`
- `src/ndae/data/exemplar.py`
