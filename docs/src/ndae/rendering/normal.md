# normal.py

Source path: `src/ndae/rendering/normal.py`

## Role

This file belongs to the `src/ndae/rendering` slice of the NDAE repository. Height-to-normal conversion helpers for the rendering pipeline.

## Where This File Sits In The Pipeline

This file is one focused step in the `src/ndae/rendering` slice of the NDAE runtime.

## Inputs, Outputs, And Tensor Shapes

- This file mostly moves structured Python objects or runtime state rather than introducing a new tensor convention of its own.

## Implementation Walkthrough

The file is built from focused helpers rather than one monolithic routine. That makes each contract easier to test and lets neighboring modules reuse only the pieces they need.

Branches in this file usually separate runtime modes or reject invalid inputs early so deeper numerical code can stay cleaner.

## Function And Class Deep Dive

### height_to_normal

Signature: `height_to_normal(height, scale=1.0)`

Purpose: Convert height maps shaped [..., 1, H, W] into world-space normal maps.

Expected inputs and outputs:
- The callable boundary is `height_to_normal(height, scale=1.0)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `cat, norm, ones_like, pad, reshape` to see how this symbol sequences lower-level work.
3. Pay attention to layout changes; this is usually where the function adapts data for the next subsystem.
4. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.
- Tensor rearrangements are spelled out directly because later code depends on exact channel and batch semantics.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `cat, norm, ones_like, pad, reshape` without redoing the same validation or reshaping work.

## Formula Mapping

- The module estimates centered finite differences `gx = (h[x+1] - h[x-1]) / 2` and `gy = (h[y-1] - h[y+1]) / 2` after replicate padding.
- It then forms the unnormalized normal `[-gx, -gy, 1]` and divides by its L2 norm to obtain a unit-length normal map.

## Design Decisions

- Split geometry, BRDF terms, postprocess, and renderer assembly so each numerical layer can be validated independently.
- Prefer pure tensor helpers in the math-heavy path to keep gradients transparent.

## Common Failure Modes

- Guard clause or surfaced failure: `ValueError('height_to_normal expects a singleton channel dimension')`
- Guard clause or surfaced failure: `ValueError('height_to_normal expects a tensor shaped [..., 1, H, W]')`

## How This Connects To Neighboring Files

- This file is relatively self-contained; its closest neighbors are package-level imports rather than one obvious sibling file.

## Related Tests

- [test_package_layout.py](../../../tests/test_package_layout.md)
- [test_trainer.py](../../../tests/test_trainer.md)
- [test_smoke.py](../../../tests/test_smoke.md)
- [test_renderer.py](../../../tests/test_renderer.md)
- [test_losses.py](../../../tests/test_losses.md)
- [test_download_svbrdf_mini.py](../../../tests/test_download_svbrdf_mini.md)
