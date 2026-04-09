# config.py

Source path: `src/ndae/training/config.py`

## Role

This file belongs to the `src/ndae/training` slice of the NDAE repository. Trainer-side config dataclasses.

## Where This File Sits In The Pipeline

This file is one focused step in the `src/ndae/training` slice of the NDAE runtime.

## Inputs, Outputs, And Tensor Shapes

- This file mostly moves structured Python objects or runtime state rather than introducing a new tensor convention of its own.

## Implementation Walkthrough

Most of the interesting behavior is in class methods, so the best reading strategy is constructor first, then the public methods in the order the rest of the runtime calls them.

This style keeps long-lived state explicit and avoids hiding state transitions in global variables or one-off closures.

## Function And Class Deep Dive

### TrainerRuntimeConfig

Role: Runtime controls for one trainer instance.

Inheritance: `object`

Owned fields:
- `batch_size`
- `workspace`
- `n_iter`
- `log_every`
- `gamma`
- `generator`
- `device`

How to read this class:
- Start from construction or declared fields to see what long-lived state the object owns.
- Then read public methods in the order the rest of the runtime calls them; that is the real control flow.
- Treat private helpers as local refactoring aids rather than as a second independent API.

### TrainerStageConfig

Role: Stage controls mirrored from the repo config schema.

Inheritance: `object`

Owned fields:
- `n_init_iter`
- `refresh_rate_init`
- `refresh_rate_local`

How to read this class:
- Start from construction or declared fields to see what long-lived state the object owns.
- Then read public methods in the order the rest of the runtime calls them; that is the real control flow.
- Treat private helpers as local refactoring aids rather than as a second independent API.

### TrainerLossConfig

Role: Loss controls mirrored from the repo config schema.

Inheritance: `object`

Owned fields:
- `loss_type`
- `n_loss_crops`
- `overflow_weight`
- `init_height_weight`

How to read this class:
- Start from construction or declared fields to see what long-lived state the object owns.
- Then read public methods in the order the rest of the runtime calls them; that is the real control flow.
- Treat private helpers as local refactoring aids rather than as a second independent API.

### TrainerSchedulerConfig

Role: Scheduler/eval controls mirrored from the repo config schema.

Inheritance: `object`

Owned fields:
- `eval_every`
- `scheduler_factor`
- `scheduler_patience_evals`
- `scheduler_min_lr`

How to read this class:
- Start from construction or declared fields to see what long-lived state the object owns.
- Then read public methods in the order the rest of the runtime calls them; that is the real control flow.
- Treat private helpers as local refactoring aids rather than as a second independent API.

### TrainerConfig

Role: Config and data inputs for one trainer instance.

Inheritance: `object`

Owned fields:
- `exemplar_frames`
- `timeline`
- `crop_size`
- `runtime`
- `stage`
- `loss`
- `scheduler`

How to read this class:
- Start from construction or declared fields to see what long-lived state the object owns.
- Then read public methods in the order the rest of the runtime calls them; that is the real control flow.
- Treat private helpers as local refactoring aids rather than as a second independent API.

## Formula Mapping

Formula mapping: not applicable. This file mainly defines schema, orchestration, or utility behavior rather than a standalone equation.

## Design Decisions

- Keep immutable config containers separate from the stateful trainer runtime.
- Assemble train-time dependencies in a factory so stage resets can rebuild only what needs rebuilding.

## Common Failure Modes

- There are no custom guard clauses in this file; failures mostly come from imported runtime code or invalid upstream tensors.

## How This Connects To Neighboring Files

- This file is relatively self-contained; its closest neighbors are package-level imports rather than one obvious sibling file.

## Related Tests

- [test_package_layout.py](../../../tests/test_package_layout.md)
- [test_trainer.py](../../../tests/test_trainer.md)
- [test_solver.py](../../../tests/test_solver.md)
- [test_smoke.py](../../../tests/test_smoke.md)
- [test_schedule.py](../../../tests/test_schedule.md)
- [test_sample_cli.py](../../../tests/test_sample_cli.md)
