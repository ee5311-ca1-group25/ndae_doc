# target_sampling.py

Source path: `src/ndae/training/target_sampling.py`

## Role

This file belongs to the `src/ndae/training` slice of the NDAE repository. Training target sampling and rendering helpers.

## Where This File Sits In The Pipeline

This file bridges exemplar frames and rendered supervision crops. It is where stage-specific sampling policy becomes concrete target tensors that the trainer can feed into loss functions.

## Inputs, Outputs, And Tensor Shapes

- This file mostly moves structured Python objects or runtime state rather than introducing a new tensor convention of its own.

## Implementation Walkthrough

The file is built from focused helpers rather than one monolithic routine. That makes each contract easier to test and lets neighboring modules reuse only the pieces they need.

Branches in this file usually separate runtime modes or reject invalid inputs early so deeper numerical code can stay cleaner.

## Function And Class Deep Dive

### sample_target_batch

Signature: `sample_target_batch(trainer, target_index, *, current_stage, brdf_maps, height_map)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `sample_target_batch(trainer, target_index, *, current_stage, brdf_maps, height_map)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `append, apply_target_spec, height_to_normal, render_sample, sample_spec, stack` to see how this symbol sequences lower-level work.
2. Pay attention to layout changes; this is usually where the function adapts data for the next subsystem.
3. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- Tensor rearrangements are spelled out directly because later code depends on exact channel and batch semantics.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `append, apply_target_spec, height_to_normal, render_sample, sample_spec` without redoing the same validation or reshaping work.

### sample_spec

Signature: `sample_spec(trainer, target_frame, *, current_stage)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `sample_spec(trainer, target_frame, *, current_stage)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `sample_random_crop_spec, sample_random_take_spec` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `sample_random_crop_spec, sample_random_take_spec` without redoing the same validation or reshaping work.

### apply_target_spec

Signature: `apply_target_spec(target_frame, spec)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `apply_target_spec(target_frame, spec)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `apply_crop_spec, apply_take_spec` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `apply_crop_spec, apply_take_spec` without redoing the same validation or reshaping work.

### render_sample

Signature: `render_sample(trainer, brdf_maps, normal_map, spec, *, image_height, image_width)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `render_sample(trainer, brdf_maps, normal_map, spec, *, image_height, image_width)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `apply_crop_spec, apply_take_spec, clip_maps, create_meshgrid, render_svbrdf` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `apply_crop_spec, apply_take_spec, clip_maps, create_meshgrid, render_svbrdf` without redoing the same validation or reshaping work.

### region_origin_for

Signature: `region_origin_for(image, spec)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `region_origin_for(image, spec)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.

What downstream code assumes:
- Callers assume the return value already matches the local conventions of the surrounding file and can be consumed directly.

## Formula Mapping

- Init-stage supervision uses `sample_random_take_spec`, so target pixels and render positions are shuffled consistently through the same index set.
- Local-stage supervision uses `sample_random_crop_spec`, so target crops and render crops share one rectangular region.
- `sample_target_batch` renders each sampled region, tone-maps the rendered batch, and returns `{target, rendered}` for the trainer loss.
- Init-stage rendering forces `normal_map = height_to_normal(zeros_like(height_map))`, while local-stage rendering uses the true height-derived normals.

## Design Decisions

- Keep immutable config containers separate from the stateful trainer runtime.
- Assemble train-time dependencies in a factory so stage resets can rebuild only what needs rebuilding.

## Common Failure Modes

- Guard clause or surfaced failure: `ValueError('crop size must be less than or equal to image size')`
- Guard clause or surfaced failure: `ValueError('rect CropSampleSpec requires top/left or ratio fields')`

## How This Connects To Neighboring Files

- This file is relatively self-contained; its closest neighbors are package-level imports rather than one obvious sibling file.

## Related Tests

- [test_trainer.py](../../../tests/test_trainer.md)
