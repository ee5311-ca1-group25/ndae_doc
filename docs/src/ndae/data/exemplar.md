# exemplar.py

Source path: `src/ndae/data/exemplar.py`

## Role

This file belongs to the `src/ndae/data` slice of the NDAE repository. Exemplar image loading and preprocessing helpers.

## Where This File Sits In The Pipeline

This file is one focused step in the `src/ndae/data` slice of the NDAE runtime. In day-to-day execution it interacts most directly with neighboring modules such as `schema.py`, `validation.py`.

## Inputs, Outputs, And Tensor Shapes

- Sequence-style image tensors use `[N, 3, H, W]`, where `N` indexes exemplar frames or sampled outputs.

## Implementation Walkthrough

Most of the interesting behavior is in class methods, so the best reading strategy is constructor first, then the public methods in the order the rest of the runtime calls them.

This style keeps long-lived state explicit and avoids hiding state transitions in global variables or one-off closures.

## Function And Class Deep Dive

### ExemplarDataset

Role: Load an exemplar sequence into memory as a `[N, 3, H, W]` tensor.

Inheritance: `object`

Public methods:
- `from_config(cls, data_config, *, base_dir=None)`: Key method on this runtime object.

How the methods should be read:
- `from_config` is one stage in the class-level control flow. Read its guard clauses, then the helper calls `cls, resolve_data_root` to understand how state moves forward.

How to read this class:
- Start from construction or declared fields to see what long-lived state the object owns.
- Then read public methods in the order the rest of the runtime calls them; that is the real control flow.
- Treat private helpers as local refactoring aids rather than as a second independent API.

## Formula Mapping

Formula mapping: not applicable. This file mainly defines schema, orchestration, or utility behavior rather than a standalone equation.

## Design Decisions

- Represent sampling decisions as reusable specs so target extraction and rendering stay aligned.
- Keep exemplar loading deterministic once frame paths have been selected.

## Common Failure Modes

- There are no custom guard clauses in this file; failures mostly come from imported runtime code or invalid upstream tensors.

## How This Connects To Neighboring Files

- [schema.py](../config/schema.md) supplies or consumes part of this file's contract.
- [validation.py](../config/validation.md) supplies or consumes part of this file's contract.

## Related Tests

- [test_package_layout.py](../../../tests/test_package_layout.md)
- [test_dataset.py](../../../tests/test_dataset.md)
- [test_trainer.py](../../../tests/test_trainer.md)
- [test_smoke.py](../../../tests/test_smoke.md)
- [test_losses.py](../../../tests/test_losses.md)
- [test_config.py](../../../tests/test_config.md)
