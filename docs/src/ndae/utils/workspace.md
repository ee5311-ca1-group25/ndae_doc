# workspace.py

Source path: `src/ndae/utils/workspace.py`

## Role

This file belongs to the `src/ndae/utils` slice of the NDAE repository. Workspace helpers for NDAE train and debug runs.

## Where This File Sits In The Pipeline

This file is one focused step in the `src/ndae/utils` slice of the NDAE runtime. In day-to-day execution it interacts most directly with neighboring modules such as `__init__.py`.

## Inputs, Outputs, And Tensor Shapes

- This file mostly moves structured Python objects or runtime state rather than introducing a new tensor convention of its own.

## Implementation Walkthrough

The file is built from focused helpers rather than one monolithic routine. That makes each contract easier to test and lets neighboring modules reuse only the pieces they need.

Branches in this file usually separate runtime modes or reject invalid inputs early so deeper numerical code can stay cleaner.

## Function And Class Deep Dive

### create_workspace

Signature: `create_workspace(config)`

Purpose: Create the experiment workspace directory and return its path.

Expected inputs and outputs:
- The callable boundary is `create_workspace(config)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `Path, mkdir` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `Path, mkdir` without redoing the same validation or reshaping work.

### save_resolved_config

Signature: `save_resolved_config(config, workspace)`

Purpose: Persist the resolved config under the workspace directory.

Expected inputs and outputs:
- The callable boundary is `save_resolved_config(config, workspace)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `safe_dump, to_dict, write_text` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `safe_dump, to_dict, write_text` without redoing the same validation or reshaping work.

### format_run_summary

Signature: `format_run_summary(config, workspace)`

Purpose: Return a concise run summary for the current config.

Expected inputs and outputs:
- The callable boundary is `format_run_summary(config, workspace)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `join` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `join` without redoing the same validation or reshaping work.

## Formula Mapping

Formula mapping: not applicable. This file mainly defines schema, orchestration, or utility behavior rather than a standalone equation.

## Design Decisions

- Isolate workspace and image I/O helpers from the core numerical path.

## Common Failure Modes

- There are no custom guard clauses in this file; failures mostly come from imported runtime code or invalid upstream tensors.

## How This Connects To Neighboring Files

- [__init__.py](../config/__init__.md) supplies or consumes part of this file's contract.

## Related Tests

- [test_trainer.py](../../../tests/test_trainer.md)
- [test_smoke.py](../../../tests/test_smoke.md)
- [test_sample_cli.py](../../../tests/test_sample_cli.md)
- [test_checkpoint.py](../../../tests/test_checkpoint.md)
- [support.py](../../../tests/support.md)
