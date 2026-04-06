# Rendering Maps

## Purpose

`src/ndae/rendering/maps.py` implements the first rendering-side helpers for
Lecture 3. It converts latent-state channels into BRDF maps and height maps and
provides the value-range mapping helpers that later rendering stages depend on.

## Public API / key types

The public helpers are:

- `l2i(x) -> torch.Tensor`
- `i2l(x) -> torch.Tensor`
- `split_latent_maps(z, n_brdf_channels, n_normal_channels=1) -> tuple[torch.Tensor, torch.Tensor]`
- `clip_maps(maps, eps=1e-6) -> torch.Tensor`

These helpers are available both from `ndae.rendering.maps` and the package
entrypoint `ndae.rendering`.

## Behavior and invariants

`l2i` and `i2l` are simple affine mappings:

- `l2i(x) = x * 0.5 + 0.5`
- `i2l(x) = (x - 0.5) * 2.0`

`split_latent_maps` assumes `...CHW` layout:

- the channel dimension is fixed at `-3`
- the input rank must be at least 3
- `n_brdf_channels` must be greater than 0
- `n_normal_channels` must be greater than 0
- the latent tensor must have at least `n_brdf_channels + n_normal_channels` channels

The split behavior is:

- BRDF maps come from the first `n_brdf_channels` channels and are passed
  through `l2i`
- height maps come from the next `n_normal_channels` channels and are left in
  latent space
- any remaining augmentation channels are silently discarded

`clip_maps` is intentionally independent from `split_latent_maps`:

- it clamps BRDF values into `[eps, 1.0]`
- it does not modify height channels because it operates only on the BRDF map
  tensor passed to it

## Error handling

`split_latent_maps` raises `ValueError` when:

- the tensor rank is below 3
- either channel-count argument is non-positive
- the tensor does not contain enough channels for the requested BRDF and height slices

`clip_maps`, `l2i`, and `i2l` do not add extra validation; they rely on PyTorch
tensor semantics.

## Tests / validation

`tests/test_renderer.py` verifies:

- `l2i` and `i2l` are inverse mappings on representative values
- `split_latent_maps` works for plain `CHW` tensors
- `split_latent_maps` supports leading batch dimensions
- augmentation channels are discarded
- invalid rank and invalid channel counts fail with `ValueError`
- `clip_maps` enforces the expected numeric range

## Related files

- `src/ndae/rendering/__init__.py`
- `tests/test_renderer.py`
- `course/lecture03.md`
