# postprocess.py

Source path: `src/ndae/rendering/postprocess.py`

## Role

This file belongs to the `src/ndae/rendering` slice of the NDAE repository. Post-processing helpers for the differentiable svBRDF renderer.

## Where This File Sits In The Pipeline

This file is one focused step in the `src/ndae/rendering` slice of the NDAE runtime. In day-to-day execution it interacts most directly with neighboring modules such as `geometry.py`.

## Inputs, Outputs, And Tensor Shapes

- This file mostly moves structured Python objects or runtime state rather than introducing a new tensor convention of its own.

## Implementation Walkthrough

The file is built from focused helpers rather than one monolithic routine. That makes each contract easier to test and lets neighboring modules reuse only the pieces they need.

Branches in this file usually separate runtime modes or reject invalid inputs early so deeper numerical code can stay cleaner.

## Function And Class Deep Dive

### tonemapping

Signature: `tonemapping(img, gamma=2.2, eps=EPSILON)`

Purpose: Convert linear HDR values into the [0, 1] sRGB range.

Expected inputs and outputs:
- The callable boundary is `tonemapping(img, gamma=2.2, eps=EPSILON)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `clamp, pow` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- Clamping is used as a numerical guardrail so later formulas stay inside the domain they were designed for.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `clamp, pow` without redoing the same validation or reshaping work.

### light_decay

Signature: `light_decay(distance)`

Purpose: Inverse-square distance falloff.

Expected inputs and outputs:
- The callable boundary is `light_decay(distance)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers assume the return value already matches the local conventions of the surrounding file and can be consumed directly.

### reinhard

Signature: `reinhard(img)`

Purpose: Alternative Reinhard tone mapping.

Expected inputs and outputs:
- The callable boundary is `reinhard(img)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers assume the return value already matches the local conventions of the surrounding file and can be consumed directly.

## Formula Mapping

- `tonemapping(img) = clamp(img, eps, 1)^(1 / gamma)` is the default gamma-space output transform.
- `light_decay(distance) = 1 / (distance^2 + eps)` models inverse-square flash falloff.
- `reinhard(img) = img / (1 + img)` is the alternative compressive tone map kept as a helper.

## Design Decisions

- Split geometry, BRDF terms, postprocess, and renderer assembly so each numerical layer can be validated independently.
- Prefer pure tensor helpers in the math-heavy path to keep gradients transparent.

## Common Failure Modes

- There are no custom guard clauses in this file; failures mostly come from imported runtime code or invalid upstream tensors.

## How This Connects To Neighboring Files

- [geometry.py](geometry.md) supplies or consumes part of this file's contract.

## Related Tests

- [test_package_layout.py](../../../tests/test_package_layout.md)
