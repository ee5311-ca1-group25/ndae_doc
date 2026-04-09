# runtime.py

Source path: `src/ndae/evaluation/runtime.py`

## Role

This file belongs to the `src/ndae/evaluation` slice of the NDAE repository. Evaluation helpers used by the trainer runtime.

## Where This File Sits In The Pipeline

This file is one focused step in the `src/ndae/evaluation` slice of the NDAE runtime.

## Inputs, Outputs, And Tensor Shapes

- This file mostly moves structured Python objects or runtime state rather than introducing a new tensor convention of its own.

## Implementation Walkthrough

The file is built from focused helpers rather than one monolithic routine. That makes each contract easier to test and lets neighboring modules reuse only the pieces they need.

Branches in this file usually separate runtime modes or reject invalid inputs early so deeper numerical code can stay cleaner.

## Function And Class Deep Dive

### should_eval

Signature: `should_eval(trainer, iteration)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `should_eval(trainer, iteration)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers assume the return value already matches the local conventions of the surrounding file and can be consumed directly.

### run_eval

Signature: `run_eval(trainer, *, iteration)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `run_eval(trainer, *, iteration)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `compute_inference_loss, effective_lr, step` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `compute_inference_loss, effective_lr, step` without redoing the same validation or reshaping work.

### compute_inference_loss

Signature: `compute_inference_loss(trainer)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `compute_inference_loss(trainer)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `append, cat, detach, item, linspace, local_loss` to see how this symbol sequences lower-level work.
2. Track where stochastic values come from, because that determines reproducibility and how tests seed the behavior.
3. Pay attention to layout changes; this is usually where the function adapts data for the next subsystem.
4. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- Randomness is explicit instead of hidden in module state, which makes training replay and tests reproducible.
- Tensor rearrangements are spelled out directly because later code depends on exact channel and batch semantics.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `append, cat, detach, item, linspace` without redoing the same validation or reshaping work.

### effective_lr

Signature: `effective_lr(trainer)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `effective_lr(trainer)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers assume the return value already matches the local conventions of the surrounding file and can be consumed directly.

## Formula Mapping

- `should_eval` triggers on step `0`, every `eval_every` steps, and at the init-to-local watershed.
- `compute_inference_loss` samples `z0 ~ N(0, I)`, rolls out on `[t_I, linspace(t_S, t_E, n_frames)]`, renders every generated frame, and averages the local loss across the sequence.
- `effective_lr` reports the optimizer's current learning rate after any `ReduceLROnPlateau` update.

## Design Decisions

- Keep evaluation logic outside the training step so periodic inference does not blur the optimization path.
- Reuse the same rendering and loss stack for evaluation to avoid train/eval drift.

## Common Failure Modes

- There are no custom guard clauses in this file; failures mostly come from imported runtime code or invalid upstream tensors.

## How This Connects To Neighboring Files

- This file is relatively self-contained; its closest neighbors are package-level imports rather than one obvious sibling file.

## Related Tests

- [test_trainer.py](../../../tests/test_trainer.md)
- [test_package_layout.py](../../../tests/test_package_layout.md)
- [test_solver.py](../../../tests/test_solver.md)
- [test_smoke.py](../../../tests/test_smoke.md)
- [test_schedule.py](../../../tests/test_schedule.md)
- [test_config.py](../../../tests/test_config.md)
