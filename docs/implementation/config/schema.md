# Config Schema

## Purpose

`src/ndae/config/schema.py` defines the dataclass tree used across the project.
The current Lecture 3 configuration layout separates model architecture settings
from rendering settings so svBRDF projection parameters have an explicit home.

## Public API / key types

The relevant types are `ModelConfig`, `RenderingConfig`, and `NDAEConfig`:

```python
@dataclass(slots=True)
class ModelConfig:
    dim: int
    solver: str
```

```python
@dataclass(slots=True)
class RenderingConfig:
    renderer_type: str = "diffuse_cook_torrance"
    n_brdf_channels: int = 8
    n_normal_channels: int = 1
    n_aug_channels: int = 9
    camera_fov: float = 50.0
    camera_distance: float = 1.0
    light_intensity: float = 0.0
    light_xy_position: tuple[float, float] = (0.0, 0.0)
    height_scale: float = 1.0
    gamma: float = 2.2

    @property
    def total_channels(self) -> int: ...
```

`NDAEConfig` now embeds both `config.model` and `config.rendering`.

## Behavior and invariants

- `ModelConfig` no longer carries `n_aug_channels`; augmentation channels are
  part of the rendering projection shape.
- `RenderingConfig` stores all renderer metadata and camera/light defaults in
  one place.
- `total_channels` is derived state, not a serialized YAML field.
- The schema itself does not enforce semantic rules such as renderer validity
  or positive camera distance; that belongs in validation.

## Error handling

This file does not raise schema-specific errors on its own. It only defines typed containers.

## Tests / validation

Behavior is exercised indirectly through:

- `tests/test_config.py`, which checks dataclass loading, rendering defaults,
  and serialization
- `tests/test_smoke.py`, which checks dry-run output and resolved config
- `tests/test_package_layout.py`, which checks the rendering metadata exports

## Related files

- `src/ndae/config/_parsing.py`
- `src/ndae/config/validation.py`
- `src/ndae/rendering/__init__.py`
- `configs/base.yaml`
