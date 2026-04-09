# objectives.py

Source path: `src/ndae/losses/objectives.py`

## Role

This file belongs to the `src/ndae/losses` slice of the NDAE repository. Wrapper objectives built on top of texture-statistics losses.

## Where This File Sits In The Pipeline

This file is one focused step in the `src/ndae/losses` slice of the NDAE runtime.

## Inputs, Outputs, And Tensor Shapes

- This file mostly moves structured Python objects or runtime state rather than introducing a new tensor convention of its own.

## Implementation Walkthrough

The file is built from focused helpers rather than one monolithic routine. That makes each contract easier to test and lets neighboring modules reuse only the pieces they need.

Branches in this file usually separate runtime modes or reject invalid inputs early so deeper numerical code can stay cleaner.

## Function And Class Deep Dive

### overflow_loss

Signature: `overflow_loss(brdf_maps, eps=1e-06)`

Purpose: Penalize BRDF values outside the valid [eps, 1] interval.

Expected inputs and outputs:
- The callable boundary is `overflow_loss(brdf_maps, eps=1e-06)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `clamp, mean` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- Clamping is used as a numerical guardrail so later formulas stay inside the domain they were designed for.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `clamp, mean` without redoing the same validation or reshaping work.

### init_loss

Signature: `init_loss(rendered, target)`

Purpose: Compute the Init-stage per-pixel MSE objective.

Expected inputs and outputs:
- The callable boundary is `init_loss(rendered, target)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `mean` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `mean` without redoing the same validation or reshaping work.

### local_loss

Signature: `local_loss(vgg, rendered, target, loss_type='SW', generator=None)`

Purpose: Dispatch the Local-stage loss to SWD or Gram statistics.

Expected inputs and outputs:
- The callable boundary is `local_loss(vgg, rendered, target, loss_type='SW', generator=None)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `gram_loss, slice_loss, upper` to see how this symbol sequences lower-level work.
3. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `gram_loss, slice_loss, upper` without redoing the same validation or reshaping work.

## Formula Mapping

- `overflow_loss = mean((brdf_maps - clamp(brdf_maps, eps, 1))^2)` penalizes values outside the physically valid BRDF interval.
- `init_loss = mean((rendered - target)^2)` is plain per-pixel MSE on tone-mapped crops.
- `local_loss` is a dispatcher: it selects `slice_loss` for `SW` and `gram_loss` for `GRAM` while keeping the trainer-side call site uniform.

## Design Decisions

- Separate feature extraction from objective composition so loss modes can share one perceptual frontend.
- Keep loss functions pure and batch-local so they are easy to unit test.

## Common Failure Modes

- Guard clause or surfaced failure: `ValueError(f"Unknown loss_type: {loss_type!r}. Must be 'SW' or 'GRAM'.")`

## How This Connects To Neighboring Files

- This file is relatively self-contained; its closest neighbors are package-level imports rather than one obvious sibling file.

## Related Tests

- [test_package_layout.py](../../../tests/test_package_layout.md)
