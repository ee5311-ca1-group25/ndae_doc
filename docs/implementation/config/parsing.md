# Config Parsing

## Purpose

`src/ndae/config/_parsing.py` converts raw YAML mappings into the dataclass tree defined in `src/ndae/config/schema.py`.

The current Lecture 3 implementation adds parsing for an optional top-level
`rendering` section while keeping strict unknown-key rejection.

## Public API / key types

Key entry points:

- `config_from_mapping(payload) -> NDAEConfig`
- `build_data_config(payload) -> DataConfig`
- `build_rendering_config(payload) -> RenderingConfig`
- `expect_keys(payload, section, required, optional=None) -> None`

## Behavior and invariants

Top-level `config` keys now behave as follows:

- required: `experiment`, `data`, `model`, `train`
- optional: `rendering`

`build_data_config` treats the following keys as required:

- `root`
- `exemplar`
- `image_size`
- `crop_size`
- `n_frames`

And the following keys as optional:

- `t_I`
- `t_S`
- `t_E`

If a timeline field is omitted, parsing supplies the default:

- `t_I = -2.0`
- `t_S = 0.0`
- `t_E = 10.0`

`build_rendering_config` accepts only optional keys:

- `renderer_type`
- `n_normal_channels`
- `n_aug_channels`
- `camera_fov`
- `camera_distance`
- `light_intensity`
- `light_xy_position`
- `height_scale`
- `gamma`

If the entire `rendering` block is omitted, parsing supplies a default
`RenderingConfig`.

`n_brdf_channels` is never read from YAML. It is derived from
`renderer_type` through `ndae.rendering.select_renderer(...)`.

`expect_keys` enforces two separate sets:

- `required`, which must all be present
- `optional`, which are accepted but not mandatory

This preserves strict unknown-key rejection while allowing backward-compatible config files.

## Error handling

Parsing raises `ConfigError` when:

- a required key is missing
- an unknown key is present
- a field has the wrong scalar type
- `renderer_type` is unsupported
- `light_xy_position` is not a two-element numeric sequence
- a section expected to be a mapping is not a mapping

Type readers are intentionally strict:

- `read_int` requires `type(value) is int`
- `read_bool` requires `type(value) is bool`
- `read_float` accepts both `int` and `float`, then casts to `float`

## Tests / validation

`tests/test_config.py` verifies:

- the base config loads into dataclasses
- unknown keys are rejected
- timeline defaults are supplied when omitted
- the rendering block defaults correctly when omitted
- legacy `model.n_aug_channels` is rejected
- invalid renderer metadata is rejected

## Related files

- `src/ndae/config/schema.py`
- `src/ndae/config/loader.py`
- `src/ndae/config/validation.py`
- `src/ndae/rendering/__init__.py`
