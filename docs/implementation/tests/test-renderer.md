# Renderer Tests

## Purpose

`tests/test_renderer.py` is currently the executable specification for the
Lecture 3 Phase B/C rendering-helper layer.

At this stage the file covers latent map extraction helpers and
`height_to_normal`. It does not yet test `renderer.py`, because that module is
still planned for later phases.

## Public API / key types

The test file exercises:

- `l2i`
- `i2l`
- `split_latent_maps`
- `clip_maps`
- `height_to_normal`

It imports these through `ndae.rendering` so the tests also validate the package
re-export surface where applicable, while `height_to_normal` is imported through
`ndae.rendering.normal`.

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

## Error handling

The tests explicitly check for `ValueError` on malformed `split_latent_maps`
and `height_to_normal` inputs. This matches the style already used by the
data-layer helpers and keeps the failure mode explicit rather than silently
truncating or reshaping data.

## Tests / validation

The focused validation command for the current Phase B slice is:

```bash
uv run pytest tests/test_renderer.py tests/test_package_layout.py tests/test_config.py -q
```

This proves:

- rendering-helper behavior
- height-to-normal behavior and gradient flow
- package export wiring
- no regression in the rendering config introduced in Phase A

## Related files

- `src/ndae/rendering/maps.py`
- `src/ndae/rendering/normal.py`
- `src/ndae/rendering/__init__.py`
- `tests/test_package_layout.py`
