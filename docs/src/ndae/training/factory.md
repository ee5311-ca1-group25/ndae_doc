# factory.py

Source path: `src/ndae/training/factory.py`

## Role

This file belongs to the `src/ndae/training` slice of the NDAE repository. Factory helpers for assembling the training runtime.

## Where This File Sits In The Pipeline

This file is one focused step in the `src/ndae/training` slice of the NDAE runtime. In day-to-day execution it interacts most directly with neighboring modules such as `__init__.py`, `__init__.py`, `__init__.py`.

## Inputs, Outputs, And Tensor Shapes

- This file mostly moves structured Python objects or runtime state rather than introducing a new tensor convention of its own.

## Implementation Walkthrough

The file is built from focused helpers rather than one monolithic routine. That makes each contract easier to test and lets neighboring modules reuse only the pieces they need.

Branches in this file usually separate runtime modes or reject invalid inputs early so deeper numerical code can stay cleaner.

## Function And Class Deep Dive

### build_trainer

Signature: `build_trainer(config, workspace, *, dataset_base_dir=None, vgg_features=None, generator=None)`

Purpose: Build a Trainer from repo-level config and runtime defaults.

Expected inputs and outputs:
- The callable boundary is `build_trainer(config, workspace, *, dataset_base_dir=None, vgg_features=None, generator=None)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `Adam, Generator, RefreshSchedule, StageConfig, Trainer, TrainerComponents` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `Adam, Generator, RefreshSchedule, StageConfig, Trainer` without redoing the same validation or reshaping work.

## Formula Mapping

Formula mapping: not applicable. This file mainly defines schema, orchestration, or utility behavior rather than a standalone equation.

## Design Decisions

- Keep immutable config containers separate from the stateful trainer runtime.
- Assemble train-time dependencies in a factory so stage resets can rebuild only what needs rebuilding.

## Common Failure Modes

- There are no custom guard clauses in this file; failures mostly come from imported runtime code or invalid upstream tensors.

## How This Connects To Neighboring Files

- [__init__.py](../config/__init__.md) supplies or consumes part of this file's contract.
- [__init__.py](../data/__init__.md) supplies or consumes part of this file's contract.
- [__init__.py](../losses/__init__.md) supplies or consumes part of this file's contract.

## Related Tests

- [test_package_layout.py](../../../tests/test_package_layout.md)
- [test_trainer.py](../../../tests/test_trainer.md)
- [support.py](../../../tests/support.md)
