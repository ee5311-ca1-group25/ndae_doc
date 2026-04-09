# __init__.py

Source path: `src/ndae/rendering/__init__.py`

## Role

This file belongs to the `src/ndae/rendering` slice of the NDAE repository. Public rendering API for NDAE. Its main job is to define the import surface for the surrounding package.

## Exported API Surface

- `EPSILON`
- `Camera`
- `FlashLight`
- `RENDERER_REGISTRY`
- `RendererSpec`
- `channelwise_normalize`
- `clip_maps`
- `compute_directions`
- `cook_torrance`
- `create_meshgrid`
- `diffuse_cook_torrance`
- `diffuse_iso_cook_torrance`
- `distribution_ggx`
- `fresnel_schlick`
- `geometry_smith`
- `height_to_normal`
- `i2l`
- `lambertian`
- `l2i`
- `light_decay`
- `localize`
- `localize_wiwo`
- `normalize`
- `reinhard`
- `render_svbrdf`
- `select_renderer`
- `smith_g1_ggx`
- `split_latent_maps`
- `tonemapping`
- `unpack_brdf_diffuse_cook_torrance`
- `unpack_brdf_diffuse_iso_cook_torrance`

## Re-export Design

This file centralizes symbols that the rest of the repository treats as package-level vocabulary. The goal is not to hide where implementations live, but to give callers one stable import surface even if internal files evolve over time.

## Import Side Effects

Importing this file re-exports symbols from child modules and may expose registries, dataclasses, or helper functions those modules define. It does not perform dataset loading, checkpoint I/O, or runtime mutation on import.

## How Downstream Code Uses These Exports

- Higher-level modules and tests use these exports to keep imports short and to avoid depending on every internal filename directly.
- The exported names usually define the package boundary that other slices of the runtime are expected to rely on.

## Formula Mapping

Formula mapping: not applicable. This file shapes import ergonomics and public package boundaries rather than introducing a numerical transform.

## Related Tests

- [test_trainer.py](../../../tests/test_trainer.md)
- [test_renderer.py](../../../tests/test_renderer.md)
- [test_package_layout.py](../../../tests/test_package_layout.md)
- [test_losses.py](../../../tests/test_losses.md)
- [test_config.py](../../../tests/test_config.md)
- [support.py](../../../tests/support.md)
