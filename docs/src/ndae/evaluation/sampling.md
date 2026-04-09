# sampling.py

Source path: `src/ndae/evaluation/sampling.py`

## Role

This file belongs to the `src/ndae/evaluation` slice of the NDAE repository. Offline sampling helpers for evaluation and checkpoint export.

## Where This File Sits In The Pipeline

This file is one focused step in the `src/ndae/evaluation` slice of the NDAE runtime.

## Inputs, Outputs, And Tensor Shapes

- This file mostly moves structured Python objects or runtime state rather than introducing a new tensor convention of its own.

## Implementation Walkthrough

The file is built from focused helpers rather than one monolithic routine. That makes each contract easier to test and lets neighboring modules reuse only the pieces they need.

Branches in this file usually separate runtime modes or reject invalid inputs early so deeper numerical code can stay cleaner.

## Function And Class Deep Dive

### build_sample_timeline

Signature: `build_sample_timeline(timeline, *, dtype, synthesis_frames=50)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `build_sample_timeline(timeline, *, dtype, synthesis_frames=50)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `cat, linspace, log10, logspace` to see how this symbol sequences lower-level work.
2. Pay attention to layout changes; this is usually where the function adapts data for the next subsystem.
3. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- Tensor rearrangements are spelled out directly because later code depends on exact channel and batch semantics.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `cat, linspace, log10, logspace` without redoing the same validation or reshaping work.

### sample_sequence

Signature: `sample_sequence(system, timeline, *, sample_size, seed)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `sample_sequence(system, timeline, *, sample_size, seed)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `Generator, build_sample_timeline, eval, manual_seed, next, no_grad` to see how this symbol sequences lower-level work.
3. Track where stochastic values come from, because that determines reproducibility and how tests seed the behavior.
4. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.
- Randomness is explicit instead of hidden in module state, which makes training replay and tests reproducible.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `Generator, build_sample_timeline, eval, manual_seed, next` without redoing the same validation or reshaping work.

## Formula Mapping

- `build_sample_timeline` uses `logspace` for synthesis times and `linspace` for transition times, then concatenates them into one evaluation timeline.
- The synthesis branch computes `logspace(0, log10(1 + syn_t), synthesis_frames) - 1 - syn_t`, which keeps early warmup samples dense near `t_S`.
- `sample_sequence` draws `z0 ~ N(0, I)` and returns the whole latent trajectory plus the split point between synthesis and transition samples.

## Design Decisions

- Keep evaluation logic outside the training step so periodic inference does not blur the optimization path.
- Reuse the same rendering and loss stack for evaluation to avoid train/eval drift.

## Common Failure Modes

- Guard clause or surfaced failure: `ValueError('sample_size must be greater than 0')`

## How This Connects To Neighboring Files

- This file is relatively self-contained; its closest neighbors are package-level imports rather than one obvious sibling file.

## Related Tests

- [test_package_layout.py](../../../tests/test_package_layout.md)
- [test_trainer.py](../../../tests/test_trainer.md)
- [test_dataset.py](../../../tests/test_dataset.md)
