# maps.py

Source path: `src/ndae/rendering/maps.py`

## Role

This file belongs to the `src/ndae/rendering` slice of the NDAE repository. Latent map extraction helpers for the rendering pipeline.

## Where This File Sits In The Pipeline

This file is one focused step in the `src/ndae/rendering` slice of the NDAE runtime.

## Inputs, Outputs, And Tensor Shapes

- This file mostly moves structured Python objects or runtime state rather than introducing a new tensor convention of its own.

## Implementation Walkthrough

The file is built from focused helpers rather than one monolithic routine. That makes each contract easier to test and lets neighboring modules reuse only the pieces they need.

Branches in this file usually separate runtime modes or reject invalid inputs early so deeper numerical code can stay cleaner.

## Function And Class Deep Dive

### l2i

Signature: `l2i(x)`

Purpose: Map latent-space values from [-1, 1] into [0, 1].

Expected inputs and outputs:
- The callable boundary is `l2i(x)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers assume the return value already matches the local conventions of the surrounding file and can be consumed directly.

### i2l

Signature: `i2l(x)`

Purpose: Map image-space values from [0, 1] into [-1, 1].

Expected inputs and outputs:
- The callable boundary is `i2l(x)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers assume the return value already matches the local conventions of the surrounding file and can be consumed directly.

### split_latent_maps

Signature: `split_latent_maps(z, n_brdf_channels, n_normal_channels=1)`

Purpose: Split latent maps into BRDF maps and height maps using ...CHW layout.

Expected inputs and outputs:
- The callable boundary is `split_latent_maps(z, n_brdf_channels, n_normal_channels=1)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `l2i, narrow` to see how this symbol sequences lower-level work.
3. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `l2i, narrow` without redoing the same validation or reshaping work.

### clip_maps

Signature: `clip_maps(maps, eps=1e-06)`

Purpose: Clamp BRDF maps into the physically valid [eps, 1] range.

Expected inputs and outputs:
- The callable boundary is `clip_maps(maps, eps=1e-06)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `clamp` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- Clamping is used as a numerical guardrail so later formulas stay inside the domain they were designed for.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `clamp` without redoing the same validation or reshaping work.

## Formula Mapping

- `l2i(x) = 0.5 * x + 0.5` maps latent channels from `[-1, 1]` into `[0, 1]`.
- `i2l(x) = 2 * (x - 0.5)` is the exact inverse mapping.
- `split_latent_maps` interprets the channel axis as `[..., C, H, W]`, exposes the BRDF channels in image space, and leaves the height channels in latent space.
- `clip_maps(maps) = clamp(maps, eps, 1)` is the last validity pass before rendering or overflow loss computation.

## Design Decisions

- Split geometry, BRDF terms, postprocess, and renderer assembly so each numerical layer can be validated independently.
- Prefer pure tensor helpers in the math-heavy path to keep gradients transparent.

## Common Failure Modes

- Guard clause or surfaced failure: `ValueError('latent channels must be greater than or equal to n_brdf_channels + n_normal_channels')`
- Guard clause or surfaced failure: `ValueError('n_brdf_channels must be greater than 0')`
- Guard clause or surfaced failure: `ValueError('n_normal_channels must be greater than 0')`
- Guard clause or surfaced failure: `ValueError('split_latent_maps expects a tensor shaped [..., C, H, W]')`

## How This Connects To Neighboring Files

- This file is relatively self-contained; its closest neighbors are package-level imports rather than one obvious sibling file.

## Related Tests

- [test_package_layout.py](../../../tests/test_package_layout.md)
- [test_trainer.py](../../../tests/test_trainer.md)
- [test_renderer.py](../../../tests/test_renderer.md)
- [test_losses.py](../../../tests/test_losses.md)
