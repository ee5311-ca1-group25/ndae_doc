# Rendering Normal

## Purpose

`src/ndae/rendering/normal.py` converts height maps into world-space normal
maps for the svBRDF rendering pipeline.

This is the second rendering helper layer after `maps.py`: latent states are
first split into BRDF maps and height maps, then the height channel is turned
into a normalized 3-channel normal map.

## Public API / key types

The public helper is:

- `height_to_normal(height, scale=1.0) -> torch.Tensor`

This helper is available from both `ndae.rendering.normal` and the top-level
`ndae.rendering` package.

## Behavior and invariants

`height_to_normal` assumes `...CHW` layout:

- input rank must be at least 3
- the channel dimension is fixed at `-3`
- the input channel count must be exactly `1`

The implementation supports arbitrary leading batch dimensions by flattening the
input to `NCHW`, applying `replicate` padding in 4D, and reshaping the result
back to `(..., 3, H, W)`.

The numeric steps are:

1. multiply the height tensor by `scale`
2. replicate-pad the spatial dimensions by 1 pixel on all sides
3. compute centered finite differences
4. build raw normals as `(-gx, -gy, 1)`
5. normalize each pixel with a small internal epsilon

The returned normals are in world space:

- flat height maps produce `(0, 0, 1)`
- a positive height slope along `x` produces a negative `x` normal component
- the `z` component stays positive because the surface faces the viewer

## Error handling

`height_to_normal` raises `ValueError` when:

- the input rank is below 3
- the channel dimension is not singleton

The helper does not enforce that `scale` is positive; that responsibility stays
in configuration validation.

## Tests / validation

`tests/test_renderer.py` verifies:

- flat height maps map to `(0, 0, 1)`
- linear height ramps along `x` produce the expected normal direction
- leading batch dimensions are preserved
- malformed inputs raise `ValueError`
- autograd works through the conversion

## Related files

- `src/ndae/rendering/maps.py`
- `src/ndae/rendering/__init__.py`
- `tests/test_renderer.py`
- `course/lecture03.md`
