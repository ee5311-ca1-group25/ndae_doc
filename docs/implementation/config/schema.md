# Config Schema

## Purpose

`src/ndae/config/schema.py` defines the dataclass tree used across the project.  
The current data-path implementation extends `DataConfig` so the data layer can carry timeline parameters in addition to dataset paths and image sizes.

## Public API / key types

The relevant type is `DataConfig`:

```python
@dataclass(slots=True)
class DataConfig:
    root: str
    exemplar: str
    image_size: int
    crop_size: int
    n_frames: int
    t_I: float = -2.0
    t_S: float = 0.0
    t_E: float = 10.0
```

`NDAEConfig` embeds this under `config.data`.

## Behavior and invariants

- `t_I`, `t_S`, and `t_E` are part of the dataclass shape, not ad hoc YAML fields.
- Default values are stored directly on the dataclass, which keeps older config payloads compatible.
- The schema itself does not enforce semantic ordering such as `t_I < t_S < t_E`; that belongs in validation.

## Error handling

This file does not raise schema-specific errors on its own. It only defines typed containers.

## Tests / validation

Behavior is exercised indirectly through:

- `tests/test_config.py`, which checks config loading and default timeline values
- `tests/test_dataset.py`, which uses `DataConfig` to construct `ExemplarDataset`

## Related files

- `src/ndae/config/_parsing.py`
- `src/ndae/config/validation.py`
- `configs/base.yaml`
