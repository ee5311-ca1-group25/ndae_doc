# sampling.py

Source path: `src/ndae/data/sampling.py`

## Role

This file belongs to the `src/ndae/data` slice of the NDAE repository. Sampling utilities for crops, pixel shuffles, and frame selection.

## Where This File Sits In The Pipeline

This file is one focused step in the `src/ndae/data` slice of the NDAE runtime.

## Inputs, Outputs, And Tensor Shapes

- Some helpers also accept single-image tensors in `[C, H, W]` format and normalize them internally.

## Implementation Walkthrough

The file is built from focused helpers rather than one monolithic routine. That makes each contract easier to test and lets neighboring modules reuse only the pieces they need.

Branches in this file usually separate runtime modes or reject invalid inputs early so deeper numerical code can stay cleaner.

## Function And Class Deep Dive

### CropSampleSpec

Role: Describe one training-space sample shared by target and rendering paths.

Inheritance: `object`

Owned fields:
- `kind`
- `height`
- `width`
- `top`
- `left`
- `top_ratio`
- `left_ratio`
- `indices`

How to read this class:
- Start from construction or declared fields to see what long-lived state the object owns.
- Then read public methods in the order the rest of the runtime calls them; that is the real control flow.
- Treat private helpers as local refactoring aids rather than as a second independent API.

### _validate_image_tensor

Signature: `_validate_image_tensor(image, *, fn_name)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `_validate_image_tensor(image, *, fn_name)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.

What downstream code assumes:
- Callers assume the return value already matches the local conventions of the surrounding file and can be consumed directly.

### random_crop

Signature: `random_crop(image, crop_h, crop_w, *, generator=None)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `random_crop(image, crop_h, crop_w, *, generator=None)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `_validate_image_tensor, item, randint` to see how this symbol sequences lower-level work.
3. Track where stochastic values come from, because that determines reproducibility and how tests seed the behavior.
4. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.
- Randomness is explicit instead of hidden in module state, which makes training replay and tests reproducible.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `item, randint` without redoing the same validation or reshaping work.

### sample_random_crop_spec

Signature: `sample_random_crop_spec(image, crop_h, crop_w, *, generator=None)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `sample_random_crop_spec(image, crop_h, crop_w, *, generator=None)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `CropSampleSpec, _validate_image_tensor, item, randint` to see how this symbol sequences lower-level work.
3. Track where stochastic values come from, because that determines reproducibility and how tests seed the behavior.
4. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.
- Randomness is explicit instead of hidden in module state, which makes training replay and tests reproducible.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `CropSampleSpec, item, randint` without redoing the same validation or reshaping work.

### apply_crop_spec

Signature: `apply_crop_spec(image, spec)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `apply_crop_spec(image, spec)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `_validate_image_tensor` to see how this symbol sequences lower-level work.
3. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.

What downstream code assumes:
- Callers assume the return value already matches the local conventions of the surrounding file and can be consumed directly.

### random_take

Signature: `random_take(image, new_h, new_w, *, generator=None)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `random_take(image, new_h, new_w, *, generator=None)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `_validate_image_tensor, apply_take_spec, sample_random_take_spec` to see how this symbol sequences lower-level work.
3. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `apply_take_spec, sample_random_take_spec` without redoing the same validation or reshaping work.

### sample_random_take_spec

Signature: `sample_random_take_spec(image, new_h, new_w, *, generator=None)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `sample_random_take_spec(image, new_h, new_w, *, generator=None)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `CropSampleSpec, _validate_image_tensor, randperm` to see how this symbol sequences lower-level work.
3. Track where stochastic values come from, because that determines reproducibility and how tests seed the behavior.
4. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.
- Randomness is explicit instead of hidden in module state, which makes training replay and tests reproducible.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `CropSampleSpec, randperm` without redoing the same validation or reshaping work.

### apply_take_spec

Signature: `apply_take_spec(image, spec)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `apply_take_spec(image, spec)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `_validate_image_tensor, any, numel, reshape, to` to see how this symbol sequences lower-level work.
3. Pay attention to layout changes; this is usually where the function adapts data for the next subsystem.
4. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.
- Tensor rearrangements are spelled out directly because later code depends on exact channel and batch semantics.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `any, numel, reshape, to` without redoing the same validation or reshaping work.

### stratified_uniform

Signature: `stratified_uniform(n, minval, maxval, *, generator=None, device=None)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `stratified_uniform(n, minval, maxval, *, generator=None, device=None)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `arange, rand` to see how this symbol sequences lower-level work.
3. Track where stochastic values come from, because that determines reproducibility and how tests seed the behavior.
4. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.
- Randomness is explicit instead of hidden in module state, which makes training replay and tests reproducible.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `arange, rand` without redoing the same validation or reshaping work.

### sample_frame_indices

Signature: `sample_frame_indices(n_frames, refresh_rate, step_in_cycle, *, generator=None)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `sample_frame_indices(n_frames, refresh_rate, step_in_cycle, *, generator=None)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `item, rand` to see how this symbol sequences lower-level work.
3. Track where stochastic values come from, because that determines reproducibility and how tests seed the behavior.
4. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.
- Randomness is explicit instead of hidden in module state, which makes training replay and tests reproducible.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `item, rand` without redoing the same validation or reshaping work.

## Formula Mapping

- `random_crop` samples integer offsets `top ~ U{0, H-crop_h}` and `left ~ U{0, W-crop_w}` and returns `image[:, top:top+crop_h, left:left+crop_w]`.
- `random_take` samples `new_h * new_w` unique flattened positions with `torch.randperm(H * W)` and reshapes the gather result back to `[C, new_h, new_w]`.
- `stratified_uniform` divides `[minval, maxval)` into `n` equal bins and draws one sample per bin, so returned times stay monotonic by construction.
- `sample_frame_indices` maps cycle step `k` to the interval `[segment * (k-1), segment * k)` where `segment = n_frames / (refresh_rate - 1)`, then floors the sampled point to a frame index.

## Design Decisions

- Represent sampling decisions as reusable specs so target extraction and rendering stay aligned.
- Keep exemplar loading deterministic once frame paths have been selected.

## Common Failure Modes

- Guard clause or surfaced failure: `ValueError('apply_crop_spec expects a rect CropSampleSpec')`
- Guard clause or surfaced failure: `ValueError('apply_take_spec expects a take CropSampleSpec')`
- Guard clause or surfaced failure: `ValueError('crop size must be less than or equal to image size')`
- Guard clause or surfaced failure: `ValueError('crop_h and crop_w must be greater than 0')`
- Guard clause or surfaced failure: `ValueError('minval must be less than maxval')`
- Guard clause or surfaced failure: `ValueError('n must be greater than 0')`
- Guard clause or surfaced failure: `ValueError('n_frames must be greater than 0')`
- Guard clause or surfaced failure: `ValueError('new_h * new_w must be less than or equal to H * W')`
- Guard clause or surfaced failure: `ValueError('new_h and new_w must be greater than 0')`
- Guard clause or surfaced failure: `ValueError('rect CropSampleSpec requires top/left or ratio fields')`

## How This Connects To Neighboring Files

- This file is relatively self-contained; its closest neighbors are package-level imports rather than one obvious sibling file.

## Related Tests

- [test_package_layout.py](../../../tests/test_package_layout.md)
- [test_dataset.py](../../../tests/test_dataset.md)
- [test_trainer.py](../../../tests/test_trainer.md)
