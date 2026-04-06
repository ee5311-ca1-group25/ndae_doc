# Renderer Tests

## Purpose

`tests/test_renderer.py` is currently the executable specification for the
Lecture 3 Phase B/C/D rendering stack.

At this stage the file covers latent map extraction helpers,
`height_to_normal`, and the first core renderer behaviors across
`geometry.py`, `brdf.py`, `postprocess.py`, and `renderer.py`. It does not yet
cover the entire final acceptance surface listed in the lecture plan.

## Public API / key types

The test file exercises:

- `l2i`
- `i2l`
- `split_latent_maps`
- `clip_maps`
- `height_to_normal`
- `lambertian`
- `create_meshgrid`
- `diffuse_cook_torrance`
- `render_svbrdf`
- `tonemapping`

It imports these through `ndae.rendering` so the tests also validate the package
re-export surface where applicable, while `height_to_normal` is imported through
`ndae.rendering.normal` and renderer runtime helpers are imported through
`ndae.rendering.renderer`.

## Behavior and invariants

The test groups verify:

- `l2i` and `i2l` invert each other on representative samples
- `split_latent_maps` returns the expected BRDF and height slices for `CHW`
  tensors
- `split_latent_maps` preserves leading batch dimensions under `...CHW`
  layouts
- augmentation channels do not leak into either returned tensor
- invalid rank and invalid channel-count arguments are rejected
- `clip_maps` clamps values into the requested `[eps, 1.0]` interval
- flat height maps produce `(0, 0, 1)` normals
- sloped height maps produce normals with the expected sign convention
- leading batch dimensions are preserved through normal conversion
- autograd can backpropagate through `height_to_normal`
- `lambertian` matches the center-pixel `1 / pi` reference case
- `create_meshgrid` preserves the expected world-space axis orientation
- diffuse-only rendering matches the manually computed center-pixel value
- crop rendering matches slicing the full rendered image
- roughness changes affect the specular highlight monotonically at the center pixel
- gradients backpropagate through the current render path

## Error handling

The tests explicitly check for `ValueError` on malformed `split_latent_maps`
and `height_to_normal` inputs. This matches the style already used by the
data-layer helpers and keeps the failure mode explicit rather than silently
truncating or reshaping data.

## Tests / validation

The focused validation command for the current Phase D slice is:

```bash
uv run pytest tests/test_renderer.py tests/test_package_layout.py tests/test_config.py -q
```

This proves:

- rendering-helper behavior
- height-to-normal behavior and gradient flow
- renderer core geometry and BRDF behavior
- package export wiring
- no regression in the rendering config introduced in Phase A

## Related files

- `src/ndae/rendering/maps.py`
- `src/ndae/rendering/normal.py`
- `src/ndae/rendering/geometry.py`
- `src/ndae/rendering/brdf.py`
- `src/ndae/rendering/postprocess.py`
- `src/ndae/rendering/renderer.py`
- `src/ndae/rendering/__init__.py`
- `tests/test_package_layout.py`
