# renderer.py

Source path: `src/ndae/rendering/renderer.py`

## Role

This file belongs to the `src/ndae/rendering` slice of the NDAE repository. Differentiable svBRDF renderer core for NDAE.

## Where This File Sits In The Pipeline

This file is the last numerical stage before losses see an image. It receives already-split BRDF and normal maps, applies geometry and BRDF evaluation, and returns linear-space renderings that other modules tone-map or compare. In day-to-day execution it interacts most directly with neighboring modules such as `brdf.py`, `geometry.py`, `postprocess.py`.

## Inputs, Outputs, And Tensor Shapes

- `brdf_maps` and `normal_map` are accepted as either `[C, H, W]` or `[B, C, H, W]`, but both inputs must agree on batch convention and spatial size.
- `positions`, when passed explicitly, must already be `[3, H, W]` and aligned with the current crop. Otherwise the file derives positions from camera geometry or from a requested region inside the full image.
- The returned rendering stays in linear RGB. Tone mapping is deliberately left to the caller when the surrounding path wants explicit control over where gamma correction happens.

## Implementation Walkthrough

The file first canonicalizes batch layout so the renderer has one consistent execution path. This keeps the rest of the code simple even though callers may render a single crop or a whole batch.

Geometry is then resolved: positions come either from an explicitly supplied crop-aligned grid or from camera parameters. From positions, the renderer computes incident and outgoing directions, localizes them with respect to the normal map, and unpacks BRDF parameters into the form expected by the selected BRDF callable.

Only after reflectance is computed does the file apply flash irradiance and invalid-angle masking. That ordering matters because the BRDF should operate on localized directions, while intensity falloff and angle validity are scene-level terms.

## Function And Class Deep Dive

### _ensure_image_batch

Signature: `_ensure_image_batch(tensor, *, name, expected_channels=None)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `_ensure_image_batch(tensor, *, name, expected_channels=None)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `unsqueeze` to see how this symbol sequences lower-level work.
3. Pay attention to layout changes; this is usually where the function adapts data for the next subsystem.
4. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.
- Tensor rearrangements are spelled out directly because later code depends on exact channel and batch semantics.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `unsqueeze` without redoing the same validation or reshaping work.

### render_svbrdf

Signature: `render_svbrdf(brdf_maps, normal_map, camera, flash_light, renderer_pp, unpack_fn, *, positions=None, full_height=None, full_width=None, region=None)`

Purpose: Render a linear-space svBRDF image from BRDF and normal maps.

Expected inputs and outputs:
- The callable boundary is `render_svbrdf(brdf_maps, normal_map, camera, flash_light, renderer_pp, unpack_fn, *, positions=None, full_height=None, full_width=None, region=None)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `_ensure_image_batch, _scalar_to_tensor, compute_directions, create_meshgrid, exp, expand` to see how this symbol sequences lower-level work.
3. Pay attention to layout changes; this is usually where the function adapts data for the next subsystem.
4. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.
- Tensor rearrangements are spelled out directly because later code depends on exact channel and batch semantics.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `compute_directions, create_meshgrid, exp, expand, light_decay` without redoing the same validation or reshaping work.

### _scalar_to_tensor

Signature: `_scalar_to_tensor(value, *, dtype, device)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `_scalar_to_tensor(value, *, dtype, device)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `isinstance, tensor, to` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `isinstance, tensor, to` without redoing the same validation or reshaping work.

## Formula Mapping

- The renderer computes reflectance from localized `wi` and `wo`, then scales it by flash irradiance before masking invalid back-facing pixels.
- `irradiance = exp(light_intensity) * light_decay(distance)` keeps light intensity in log space while preserving positive output energy.
- Final linear output is `reflectance * irradiance`, with any pixel where `wi_z < 0` or `wo_z < 0` zeroed out.

## Design Decisions

- Split geometry, BRDF terms, postprocess, and renderer assembly so each numerical layer can be validated independently.
- Prefer pure tensor helpers in the math-heavy path to keep gradients transparent.

## Common Failure Modes

- Guard clause or surfaced failure: `ValueError('brdf_maps and normal_map must both be batched or both be unbatched')`
- Guard clause or surfaced failure: `ValueError('brdf_maps and normal_map must share the same batch size')`
- Guard clause or surfaced failure: `ValueError('brdf_maps and normal_map must share the same spatial size')`
- Guard clause or surfaced failure: `ValueError('full_height and full_width are required when region is provided')`
- Guard clause or surfaced failure: `ValueError('positions cannot be combined with region or full image size')`
- Guard clause or surfaced failure: `ValueError('positions must be shaped [3, H, W] and match the input map size')`
- Guard clause or surfaced failure: `ValueError('region crop size must be greater than 0')`
- Guard clause or surfaced failure: `ValueError('region crop size must match the input map size')`
- Guard clause or surfaced failure: `ValueError('region must lie inside the full image extent')`
- Guard clause or surfaced failure: `ValueError(f'{name} expects a tensor shaped [C, H, W] or [B, C, H, W]')`

## How This Connects To Neighboring Files

- [brdf.py](brdf.md) supplies or consumes part of this file's contract.
- [geometry.py](geometry.md) supplies or consumes part of this file's contract.
- [postprocess.py](postprocess.md) supplies or consumes part of this file's contract.

## Related Tests

- [test_package_layout.py](../../../tests/test_package_layout.md)
- [test_trainer.py](../../../tests/test_trainer.md)
- [test_smoke.py](../../../tests/test_smoke.md)
- [test_config.py](../../../tests/test_config.md)
- [support.py](../../../tests/support.md)
