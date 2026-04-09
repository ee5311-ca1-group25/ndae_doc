# geometry.py

Source path: `src/ndae/rendering/geometry.py`

## Role

This file belongs to the `src/ndae/rendering` slice of the NDAE repository. Geometry helpers for the differentiable svBRDF renderer.

## Where This File Sits In The Pipeline

This file is one focused step in the `src/ndae/rendering` slice of the NDAE runtime.

## Inputs, Outputs, And Tensor Shapes

- This file mostly moves structured Python objects or runtime state rather than introducing a new tensor convention of its own.

## Implementation Walkthrough

The file is built from focused helpers rather than one monolithic routine. That makes each contract easier to test and lets neighboring modules reuse only the pieces they need.

Branches in this file usually separate runtime modes or reject invalid inputs early so deeper numerical code can stay cleaner.

## Function And Class Deep Dive

### Camera

Role: This class owns one stateful runtime component.

Inheritance: `object`

Owned fields:
- `fov`
- `distance`

How to read this class:
- Start from construction or declared fields to see what long-lived state the object owns.
- Then read public methods in the order the rest of the runtime calls them; that is the real control flow.
- Treat private helpers as local refactoring aids rather than as a second independent API.

### FlashLight

Role: This class owns one stateful runtime component.

Inheritance: `object`

Owned fields:
- `intensity`
- `xy_position`

How to read this class:
- Start from construction or declared fields to see what long-lived state the object owns.
- Then read public methods in the order the rest of the runtime calls them; that is the real control flow.
- Treat private helpers as local refactoring aids rather than as a second independent API.

### normalize

Signature: `normalize(v)`

Purpose: Normalize vectors along the last dimension.

Expected inputs and outputs:
- The callable boundary is `normalize(v)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `norm` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `norm` without redoing the same validation or reshaping work.

### channelwise_normalize

Signature: `channelwise_normalize(m)`

Purpose: Normalize vector maps along the channel dimension.

Expected inputs and outputs:
- The callable boundary is `channelwise_normalize(m)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `norm` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `norm` without redoing the same validation or reshaping work.

### create_meshgrid

Signature: `create_meshgrid(height, width, camera, device=None)`

Purpose: Create a physical-space position grid for an image plane at z=0.

Expected inputs and outputs:
- The callable boundary is `create_meshgrid(height, width, camera, device=None)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `linspace, meshgrid, radians, stack, tan, zeros_like` to see how this symbol sequences lower-level work.
3. Pay attention to layout changes; this is usually where the function adapts data for the next subsystem.
4. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.
- Tensor rearrangements are spelled out directly because later code depends on exact channel and batch semantics.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `linspace, meshgrid, radians, stack, tan` without redoing the same validation or reshaping work.

### compute_directions

Signature: `compute_directions(positions, camera, flash_light)`

Purpose: Compute per-pixel incident and outgoing directions in world space.

Expected inputs and outputs:
- The callable boundary is `compute_directions(positions, camera, flash_light)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `channelwise_normalize, tensor, view` to see how this symbol sequences lower-level work.
2. Pay attention to layout changes; this is usually where the function adapts data for the next subsystem.
3. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- Tensor rearrangements are spelled out directly because later code depends on exact channel and batch semantics.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `channelwise_normalize, tensor, view` without redoing the same validation or reshaping work.

### _channel_dot

Signature: `_channel_dot(a, b)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `_channel_dot(a, b)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `sum` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `sum` without redoing the same validation or reshaping work.

### localize

Signature: `localize(vec, normal)`

Purpose: Project world-space vectors into the local tangent frame of a normal map.

Expected inputs and outputs:
- The callable boundary is `localize(vec, normal)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `_channel_dot, cat, channelwise_normalize, cross, fill_, select` to see how this symbol sequences lower-level work.
2. Pay attention to layout changes; this is usually where the function adapts data for the next subsystem.
3. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- Tensor rearrangements are spelled out directly because later code depends on exact channel and batch semantics.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `cat, channelwise_normalize, cross, fill_, select` without redoing the same validation or reshaping work.

### localize_wiwo

Signature: `localize_wiwo(wi, wo, normal)`

Purpose: Project incident and outgoing directions into local tangent space.

Expected inputs and outputs:
- The callable boundary is `localize_wiwo(wi, wo, normal)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `localize` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `localize` without redoing the same validation or reshaping work.

## Formula Mapping

- `normalize(v) = v / (||v|| + eps)` and `channelwise_normalize(m) = m / (||m||_channel + eps)`.
- `create_meshgrid` maps normalized image coordinates into a physical image plane using `half_width = distance * tan(fov / 2)` and the image aspect ratio.
- `compute_directions` constructs world-space incident and outgoing vectors from the light/camera positions to every surface point.
- `localize` builds tangent and bitangent vectors orthogonal to the normal map, then projects a world-space vector onto that local basis with channelwise dot products.

## Design Decisions

- Split geometry, BRDF terms, postprocess, and renderer assembly so each numerical layer can be validated independently.
- Prefer pure tensor helpers in the math-heavy path to keep gradients transparent.

## Common Failure Modes

- Guard clause or surfaced failure: `ValueError('height and width must be greater than 0')`

## How This Connects To Neighboring Files

- This file is relatively self-contained; its closest neighbors are package-level imports rather than one obvious sibling file.

## Related Tests

- [test_package_layout.py](../../../tests/test_package_layout.md)
