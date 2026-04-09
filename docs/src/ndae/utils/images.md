# images.py

Source path: `src/ndae/utils/images.py`

## Role

This file belongs to the `src/ndae/utils` slice of the NDAE repository. Image writing helpers for NDAE CLIs.

## Where This File Sits In The Pipeline

This file is one focused step in the `src/ndae/utils` slice of the NDAE runtime.

## Inputs, Outputs, And Tensor Shapes

- This file mostly moves structured Python objects or runtime state rather than introducing a new tensor convention of its own.

## Implementation Walkthrough

The file is built from focused helpers rather than one monolithic routine. That makes each contract easier to test and lets neighboring modules reuse only the pieces they need.

Branches in this file usually separate runtime modes or reject invalid inputs early so deeper numerical code can stay cleaner.

## Function And Class Deep Dive

### save_png_image

Signature: `save_png_image(path, image)`

Purpose: Save a CHW image tensor as an RGB PNG.

Expected inputs and outputs:
- The callable boundary is `save_png_image(path, image)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `Path, clamp, cpu, detach, imsave, mkdir` to see how this symbol sequences lower-level work.
2. Pay attention to layout changes; this is usually where the function adapts data for the next subsystem.
3. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- Tensor rearrangements are spelled out directly because later code depends on exact channel and batch semantics.
- Clamping is used as a numerical guardrail so later formulas stay inside the domain they were designed for.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `Path, clamp, cpu, detach, imsave` without redoing the same validation or reshaping work.

## Formula Mapping

Formula mapping: not applicable. This file mainly defines schema, orchestration, or utility behavior rather than a standalone equation.

## Design Decisions

- Isolate workspace and image I/O helpers from the core numerical path.

## Common Failure Modes

- There are no custom guard clauses in this file; failures mostly come from imported runtime code or invalid upstream tensors.

## How This Connects To Neighboring Files

- This file is relatively self-contained; its closest neighbors are package-level imports rather than one obvious sibling file.

## Related Tests

- [test_dataset.py](../../../tests/test_dataset.md)
- [test_config.py](../../../tests/test_config.md)
