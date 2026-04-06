# Data Sampling

## Purpose

`src/ndae/data/sampling.py` provides the small sampling primitives used by the NDAE data path and later training logic.

The current implementation provides four helpers:

- `random_crop`
- `random_take`
- `stratified_uniform`
- `sample_frame_indices`

## Public API / key types

All functions are stateless and operate on a single image or a single training-step request.

Randomized functions accept `torch.Generator | None` so callers can keep reproducibility local instead of mutating global RNG state.

## Behavior and invariants

### `random_crop`

- expects a 3D tensor shaped `[C, H, W]`
- samples `top` and `left` with `torch.randint`
- returns a contiguous spatial subregion `image[:, top:top+crop_h, left:left+crop_w]`
- preserves dtype, device, and value range

This mirrors the official JAX `random_crop` helper in `rendering_utils.py`.

### `random_take`

- expects a 3D tensor shaped `[C, H, W]`
- samples `new_h * new_w` flattened spatial indices without replacement
- reshapes the gathered values back to `[C, new_h, new_w]`
- preserves channel identity but destroys spatial locality

This mirrors the official JAX `random_take` behavior and is meant for the Init-stage statistic-matching loss.

### `stratified_uniform`

- splits `[minval, maxval)` into `n` equal subintervals
- draws one uniform sample from each subinterval
- returns a monotonic 1D `float32` tensor because each later sample comes from a later stratum

This is the PyTorch version of the JAX helper used by the online training schedule.

### `sample_frame_indices`

- validates `n_frames`, `refresh_rate`, and `step_in_cycle`
- returns `0` for `step_in_cycle == 0`, matching the refresh step supervision of frame 0
- for continuation steps, samples one scalar from the corresponding stratum of the frame domain and converts it to an integer frame index

This function is intentionally step-local:

- it decides which target frame to supervise for one training step
- it does not manage whole refresh cycles
- it does not depend on `Timeline`

## Error handling

`random_crop` raises `ValueError` when:

- the input is not 3D
- crop dimensions are non-positive
- crop dimensions exceed the image dimensions

`random_take` raises `ValueError` when:

- the input is not 3D
- target dimensions are non-positive
- the requested sample size exceeds `H * W`

`stratified_uniform` raises `ValueError` when:

- `n <= 0`
- `minval >= maxval`

`sample_frame_indices` raises `ValueError` when:

- `n_frames <= 0`
- `refresh_rate <= 1`
- `step_in_cycle` is outside `[0, refresh_rate)`

## Tests / validation

`tests/test_dataset.py` covers:

- crop shape and deterministic replay under fixed seeds
- proof that `random_crop` returns a true spatial submatrix
- proof that `random_take` only returns source pixel values
- stratified range and ordering checks for `stratified_uniform`
- deterministic and stratum-bounded behavior for `sample_frame_indices`

## Related files

- `src/ndae/data/timeline.py`
- `tests/test_dataset.py`
- `course/ode-appearance/rendering_utils.py` in the reference course materials
