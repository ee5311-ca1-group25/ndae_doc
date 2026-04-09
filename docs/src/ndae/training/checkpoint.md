# checkpoint.py

Source path: `src/ndae/training/checkpoint.py`

## Role

This file belongs to the `src/ndae/training` slice of the NDAE repository. Checkpoint helpers for training and sampling.

## Where This File Sits In The Pipeline

This file is one focused step in the `src/ndae/training` slice of the NDAE runtime.

## Inputs, Outputs, And Tensor Shapes

- This file mostly moves structured Python objects or runtime state rather than introducing a new tensor convention of its own.

## Implementation Walkthrough

The file is built from focused helpers rather than one monolithic routine. That makes each contract easier to test and lets neighboring modules reuse only the pieces they need.

Branches in this file usually separate runtime modes or reject invalid inputs early so deeper numerical code can stay cleaner.

## Function And Class Deep Dive

### resolve_checkpoint_dir

Signature: `resolve_checkpoint_dir(path)`

Purpose: Resolve and validate a concrete checkpoint directory.

Expected inputs and outputs:
- The callable boundary is `resolve_checkpoint_dir(path)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `FileNotFoundError, Path, exists, expanduser, is_dir, resolve` to see how this symbol sequences lower-level work.
3. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `FileNotFoundError, Path, exists, expanduser, is_dir` without redoing the same validation or reshaping work.

### save_checkpoint

Signature: `save_checkpoint(workspace, trainer, *, saved_during_eval)`

Purpose: Persist model, optimizer, trainer state, and metadata.

Expected inputs and outputs:
- The callable boundary is `save_checkpoint(workspace, trainer, *, saved_during_eval)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `_flashlight_payload, _trainer_state_payload, copytree, dumps, exists, mkdir` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `copytree, dumps, exists, mkdir, rmtree` without redoing the same validation or reshaping work.

### load_resume_checkpoint

Signature: `load_resume_checkpoint(checkpoint_dir, trainer)`

Purpose: Restore model, optimizer, and runtime state for boundary resume.

Expected inputs and outputs:
- The callable boundary is `load_resume_checkpoint(checkpoint_dir, trainer)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `RefreshSchedule, _load_flashlight_state, _load_meta, _load_trainer_state, get, load` to see how this symbol sequences lower-level work.
3. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `RefreshSchedule, get, load, load_state_dict, resolve_checkpoint_dir` without redoing the same validation or reshaping work.

### load_sample_checkpoint

Signature: `load_sample_checkpoint(checkpoint_dir, model, flash_light)`

Purpose: Restore model weights for sample-only inference and return checkpoint metadata.

Expected inputs and outputs:
- The callable boundary is `load_sample_checkpoint(checkpoint_dir, model, flash_light)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `_load_flashlight_state, _load_meta, load, load_state_dict, next, parameters` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `load, load_state_dict, next, parameters, resolve_checkpoint_dir` without redoing the same validation or reshaping work.

### _flashlight_payload

Signature: `_flashlight_payload(flash_light)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `_flashlight_payload(flash_light)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `cpu, detach, isinstance, tensor` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `cpu, detach, isinstance, tensor` without redoing the same validation or reshaping work.

### _trainer_state_payload

Signature: `_trainer_state_payload(state)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `_trainer_state_payload(state)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `cpu, detach` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `cpu, detach` without redoing the same validation or reshaping work.

### _load_trainer_state

Signature: `_load_trainer_state(trainer_state_path, *, device, dtype)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `_load_trainer_state(trainer_state_path, *, device, dtype)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `TrainerState, load, str, to` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `TrainerState, load, str, to` without redoing the same validation or reshaping work.

### _load_meta

Signature: `_load_meta(checkpoint_dir)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `_load_meta(checkpoint_dir)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `loads, read_text` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `loads, read_text` without redoing the same validation or reshaping work.

### _load_flashlight_state

Signature: `_load_flashlight_state(flashlight_path, flash_light, *, device, dtype)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `_load_flashlight_state(flashlight_path, flash_light, *, device, dtype)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `FileNotFoundError, copy_, is_file, isinstance, item, load` to see how this symbol sequences lower-level work.
3. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `FileNotFoundError, copy_, is_file, isinstance, item` without redoing the same validation or reshaping work.

## Formula Mapping

Formula mapping: not applicable. This file mainly defines schema, orchestration, or utility behavior rather than a standalone equation.

## Design Decisions

- Keep immutable config containers separate from the stateful trainer runtime.
- Assemble train-time dependencies in a factory so stage resets can rebuild only what needs rebuilding.

## Common Failure Modes

- Guard clause or surfaced failure: `FileNotFoundError(f'Checkpoint directory does not exist: {checkpoint_dir}')`
- Guard clause or surfaced failure: `FileNotFoundError(f'Checkpoint is missing flashlight state: {flashlight_path}')`
- Guard clause or surfaced failure: `ValueError(f"Checkpoint directory must be 'latest' or 'step_XXXXXX', got {checkpoint_dir.name!r}")`
- Guard clause or surfaced failure: `ValueError(f'Checkpoint is not resume-ready: {resolved_dir}')`
- Guard clause or surfaced failure: `ValueError(f'Checkpoint path must be a directory: {checkpoint_dir}')`
- Guard clause or surfaced failure: `ValueError(f'Checkpoint path must point inside a checkpoints directory, got {checkpoint_dir}')`
- Guard clause or surfaced failure: `ValueError(f'Resume-ready checkpoints must have trainer_state.cycle_step == 0, got {trainer_state.cycle_step}')`

## How This Connects To Neighboring Files

- This file is relatively self-contained; its closest neighbors are package-level imports rather than one obvious sibling file.

## Related Tests

- [test_package_layout.py](../../../tests/test_package_layout.md)
- [test_smoke.py](../../../tests/test_smoke.md)
- [test_sample_cli.py](../../../tests/test_sample_cli.md)
- [test_config.py](../../../tests/test_config.md)
- [test_checkpoint.py](../../../tests/test_checkpoint.md)
- [support.py](../../../tests/support.md)
