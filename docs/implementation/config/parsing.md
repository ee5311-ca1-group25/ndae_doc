# Config Parsing

## Purpose

`src/ndae/config/_parsing.py` converts raw YAML mappings into the dataclass tree defined in `src/ndae/config/schema.py`.

The current data-path implementation adds timeline-aware parsing for the `data` section and upgrades key validation so optional fields can be accepted without weakening unknown-key checks.

## Public API / key types

Key entry points:

- `config_from_mapping(payload) -> NDAEConfig`
- `build_data_config(payload) -> DataConfig`
- `expect_keys(payload, section, required, optional=None) -> None`

## Behavior and invariants

`build_data_config` now treats the following keys as required:

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

`expect_keys` enforces two separate sets:

- `required`, which must all be present
- `optional`, which are accepted but not mandatory

This preserves strict unknown-key rejection while allowing backward-compatible config files.

## Error handling

Parsing raises `ConfigError` when:

- a required key is missing
- an unknown key is present
- a field has the wrong scalar type
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

## Related files

- `src/ndae/config/schema.py`
- `src/ndae/config/loader.py`
- `src/ndae/config/validation.py`
