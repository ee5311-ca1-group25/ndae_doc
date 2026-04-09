# swd.py

Source path: `src/ndae/losses/swd.py`

## Role

This file belongs to the `src/ndae/losses` slice of the NDAE repository. Gram-based texture statistics losses.

## Where This File Sits In The Pipeline

This file is the core comparison layer for local texture supervision. The trainer never uses it directly; it calls `local_loss`, which dispatches here when the configured mode is `SW` or `GRAM`.

## Inputs, Outputs, And Tensor Shapes

- `gram_matrix` accepts either `[C, H, W]` or `[B, C, H, W]` and flattens spatial positions into one axis before forming channel-channel correlations.
- `sliced_wasserstein_loss` expects exemplar and sample tensors with matching rank and channel count. It projects along randomly sampled channel directions, so the last dimension after reshaping is the number of spatial samples being compared.
- `slice_loss` consumes the feature lists returned by `VGG19Features`, so its effective inputs are not raw images alone but a stack of multi-scale perceptual activations.

## Implementation Walkthrough

The file implements two related ideas: Gram-matrix comparison for second-order feature correlations, and sliced Wasserstein comparison for distribution alignment along random directions.

The SWD path reshapes features so channel directions can be sampled in feature space, not in pixel space. After projection, it sorts exemplar and sample activations before comparing them, which is what makes the metric insensitive to spatial ordering and sensitive to the empirical distribution instead.

The weighted `slice_loss` wrapper exists because the trainer wants one scalar local loss even though the perceptual frontend emits a stack of feature tensors at different scales.

## Function And Class Deep Dive

### gram_matrix

Signature: `gram_matrix(f)`

Purpose: Compute a Gram matrix normalized by the number of spatial samples.

Expected inputs and outputs:
- The callable boundary is `gram_matrix(f)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `dim, reshape, transpose` to see how this symbol sequences lower-level work.
3. Pay attention to layout changes; this is usually where the function adapts data for the next subsystem.
4. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.
- Tensor rearrangements are spelled out directly because later code depends on exact channel and batch semantics.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `dim, reshape, transpose` without redoing the same validation or reshaping work.

### gram_loss

Signature: `gram_loss(features, exemplar, sample, generator=None)`

Purpose: Compute the summed per-layer Gram-matrix MSE across VGG features.

Expected inputs and outputs:
- The callable boundary is `gram_loss(features, exemplar, sample, generator=None)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `features, gram_matrix, mean, zeros` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `features, gram_matrix, mean, zeros` without redoing the same validation or reshaping work.

### sliced_wasserstein_loss

Signature: `sliced_wasserstein_loss(fe, fs, generator=None)`

Purpose: Compute sliced Wasserstein loss between one pair of feature tensors.

Expected inputs and outputs:
- The callable boundary is `sliced_wasserstein_loss(fe, fs, generator=None)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `clamp_min, dim, interpolate, matmul, mean, norm` to see how this symbol sequences lower-level work.
3. Track where stochastic values come from, because that determines reproducibility and how tests seed the behavior.
4. Pay attention to layout changes; this is usually where the function adapts data for the next subsystem.
5. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.
- Randomness is explicit instead of hidden in module state, which makes training replay and tests reproducible.
- Tensor rearrangements are spelled out directly because later code depends on exact channel and batch semantics.
- Clamping is used as a numerical guardrail so later formulas stay inside the domain they were designed for.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `clamp_min, dim, interpolate, matmul, mean` without redoing the same validation or reshaping work.

### slice_loss

Signature: `slice_loss(features, exemplar, sample, generator=None, weights=None)`

Purpose: Compute the weighted multi-layer sliced Wasserstein loss.

Expected inputs and outputs:
- The callable boundary is `slice_loss(features, exemplar, sample, generator=None, weights=None)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `features, new_tensor, sliced_wasserstein_loss, zeros` to see how this symbol sequences lower-level work.
3. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `features, new_tensor, sliced_wasserstein_loss, zeros` without redoing the same validation or reshaping work.

## Formula Mapping

- `gram_matrix(f)` reshapes spatial positions into one axis and computes `(F F^T) / N`, where `N` is the number of spatial samples.
- `gram_loss` sums mean-squared errors between exemplar and sample Gram matrices across all returned VGG feature blocks.
- `sliced_wasserstein_loss` draws random normalized directions, projects exemplar and sample features onto those directions, sorts the projections, and averages squared distances between the sorted projections.
- `slice_loss` normalizes user weights so their average stays `1`, then accumulates weighted sliced-Wasserstein losses across VGG blocks.

## Design Decisions

- Separate feature extraction from objective composition so loss modes can share one perceptual frontend.
- Keep loss functions pure and batch-local so they are easy to unit test.

## Common Failure Modes

- Guard clause or surfaced failure: `ValueError('slice_loss expects weights with a positive sum.')`
- Guard clause or surfaced failure: `ValueError(f'gram_matrix expects input shaped (C, H, W) or (B, C, H, W), got {tuple(f.shape)}.')`
- Guard clause or surfaced failure: `ValueError(f'slice_loss expects {len(sample_features)} weights, got {len(weights)}.')`
- Guard clause or surfaced failure: `ValueError(f'sliced_wasserstein_loss expects exemplar and sample to have the same rank, got {fe.dim()} and {fs.dim()}.')`
- Guard clause or surfaced failure: `ValueError(f'sliced_wasserstein_loss expects inputs shaped (C, H, W) or (B, C, H, W), got {tuple(fe.shape)} and {tuple(fs.shape)}.')`
- Guard clause or surfaced failure: `ValueError(f'sliced_wasserstein_loss expects matching channel counts, got {fe.shape[-3]} and {fs.shape[-3]}.')`

## How This Connects To Neighboring Files

- This file is relatively self-contained; its closest neighbors are package-level imports rather than one obvious sibling file.

## Related Tests

- [test_package_layout.py](../../../tests/test_package_layout.md)
- [test_losses.py](../../../tests/test_losses.md)
