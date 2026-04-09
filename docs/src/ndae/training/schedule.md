# schedule.py

Source path: `src/ndae/training/schedule.py`

## Role

This file belongs to the `src/ndae/training` slice of the NDAE repository. Time-window configuration objects for NDAE training.

## Where This File Sits In The Pipeline

This file is one focused step in the `src/ndae/training` slice of the NDAE runtime.

## Inputs, Outputs, And Tensor Shapes

- This file mostly moves structured Python objects or runtime state rather than introducing a new tensor convention of its own.

## Implementation Walkthrough

Most of the interesting behavior is in class methods, so the best reading strategy is constructor first, then the public methods in the order the rest of the runtime calls them.

This style keeps long-lived state explicit and avoids hiding state transitions in global variables or one-off closures.

## Function And Class Deep Dive

### StageConfig

Role: Time boundaries and refresh rate for NDAE training.

Inheritance: `object`

Owned fields:
- `t_init`
- `t_start`
- `t_end`
- `refresh_rate`

How to read this class:
- Start from construction or declared fields to see what long-lived state the object owns.
- Then read public methods in the order the rest of the runtime calls them; that is the real control flow.
- Treat private helpers as local refactoring aids rather than as a second independent API.

### RolloutWindow

Role: Description of one rollout interval in the training cycle.

Inheritance: `object`

Owned fields:
- `kind`
- `t0`
- `t1`
- `refresh`

How to read this class:
- Start from construction or declared fields to see what long-lived state the object owns.
- Then read public methods in the order the rest of the runtime calls them; that is the real control flow.
- Treat private helpers as local refactoring aids rather than as a second independent API.

### RefreshSchedule

Role: Implements Algorithm 1's refresh cycle and stratified time sampling.

Inheritance: `object`

Public methods:
- `next(self, iteration, carry_time)`: Key method on this runtime object.

How the methods should be read:
- `next` is one stage in the class-level control flow. Read its guard clauses, then the helper calls `RolloutWindow, _sample_strata, item` to understand how state moves forward.

How to read this class:
- Start from construction or declared fields to see what long-lived state the object owns.
- Then read public methods in the order the rest of the runtime calls them; that is the real control flow.
- Treat private helpers as local refactoring aids rather than as a second independent API.

## Formula Mapping

- Each refresh cycle has one warmup window `[t_init, t_start]` followed by `refresh_rate - 1` generation windows.
- `_sample_strata` draws absolute times with `stratified_uniform`, then converts them into positive deltas so the trainer can march from one carry state to the next.
- `next` returns `RolloutWindow(kind, t0, t1, refresh)` where `refresh=True` only on the warmup step that seeds a new latent state.

## Design Decisions

- Keep immutable config containers separate from the stateful trainer runtime.
- Assemble train-time dependencies in a factory so stage resets can rebuild only what needs rebuilding.

## Common Failure Modes

- There are no custom guard clauses in this file; failures mostly come from imported runtime code or invalid upstream tensors.

## How This Connects To Neighboring Files

- This file is relatively self-contained; its closest neighbors are package-level imports rather than one obvious sibling file.

## Related Tests

- [test_schedule.py](../../../tests/test_schedule.md)
- [test_package_layout.py](../../../tests/test_package_layout.md)
- [test_trainer.py](../../../tests/test_trainer.md)
- [test_smoke.py](../../../tests/test_smoke.md)
- [test_config.py](../../../tests/test_config.md)
- [test_checkpoint.py](../../../tests/test_checkpoint.md)
