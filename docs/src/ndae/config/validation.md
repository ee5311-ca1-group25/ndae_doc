# validation.py

Source path: `src/ndae/config/validation.py`

## Role

This file belongs to the `src/ndae/config` slice of the NDAE repository. Validation helpers for NDAE configuration.

## Where This File Sits In The Pipeline

This file is one focused step in the `src/ndae/config` slice of the NDAE runtime. In day-to-day execution it interacts most directly with neighboring modules such as `__init__.py`.

## Inputs, Outputs, And Tensor Shapes

- This file mostly moves structured Python objects or runtime state rather than introducing a new tensor convention of its own.

## Implementation Walkthrough

The file is built from focused helpers rather than one monolithic routine. That makes each contract easier to test and lets neighboring modules reuse only the pieces they need.

Branches in this file usually separate runtime modes or reject invalid inputs early so deeper numerical code can stay cleaner.

## Function And Class Deep Dive

### validate_config

Signature: `validate_config(config, *, base_dir=None, validate_dataset=True)`

Purpose: Validate structural and semantic constraints for an NDAE config.

Expected inputs and outputs:
- The callable boundary is `validate_config(config, *, base_dir=None, validate_dataset=True)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `ConfigError, ensure_bool, ensure_float, ensure_int, ensure_non_empty_string, ensure_non_negative_float` to see how this symbol sequences lower-level work.
3. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `ConfigError, ensure_bool, ensure_float, ensure_int, ensure_non_empty_string` without redoing the same validation or reshaping work.

### validate_rendering_config

Signature: `validate_rendering_config(config)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `validate_rendering_config(config)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `ConfigError, ensure_float, ensure_non_empty_string, ensure_non_negative_int, ensure_positive_float, ensure_positive_int` to see how this symbol sequences lower-level work.
3. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `ConfigError, ensure_float, ensure_non_empty_string, ensure_non_negative_int, ensure_positive_float` without redoing the same validation or reshaping work.

### ensure_non_empty_string

Signature: `ensure_non_empty_string(value, field_name)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `ensure_non_empty_string(value, field_name)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `ConfigError, isinstance, strip` to see how this symbol sequences lower-level work.
3. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `ConfigError, isinstance, strip` without redoing the same validation or reshaping work.

### ensure_int

Signature: `ensure_int(value, field_name)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `ensure_int(value, field_name)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `ConfigError, type` to see how this symbol sequences lower-level work.
3. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `ConfigError, type` without redoing the same validation or reshaping work.

### ensure_positive_int

Signature: `ensure_positive_int(value, field_name)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `ensure_positive_int(value, field_name)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `ConfigError, ensure_int` to see how this symbol sequences lower-level work.
3. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `ConfigError, ensure_int` without redoing the same validation or reshaping work.

### ensure_non_negative_int

Signature: `ensure_non_negative_int(value, field_name)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `ensure_non_negative_int(value, field_name)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `ConfigError, ensure_int` to see how this symbol sequences lower-level work.
3. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `ConfigError, ensure_int` without redoing the same validation or reshaping work.

### ensure_positive_float

Signature: `ensure_positive_float(value, field_name)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `ensure_positive_float(value, field_name)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `ConfigError, type` to see how this symbol sequences lower-level work.
3. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `ConfigError, type` without redoing the same validation or reshaping work.

### ensure_float

Signature: `ensure_float(value, field_name)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `ensure_float(value, field_name)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `ConfigError, type` to see how this symbol sequences lower-level work.
3. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `ConfigError, type` without redoing the same validation or reshaping work.

### ensure_non_negative_float

Signature: `ensure_non_negative_float(value, field_name)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `ensure_non_negative_float(value, field_name)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `ConfigError, ensure_float` to see how this symbol sequences lower-level work.
3. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `ConfigError, ensure_float` without redoing the same validation or reshaping work.

### ensure_bool

Signature: `ensure_bool(value, field_name)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `ensure_bool(value, field_name)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `ConfigError, type` to see how this symbol sequences lower-level work.
3. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `ConfigError, type` without redoing the same validation or reshaping work.

### validate_dataset_layout

Signature: `validate_dataset_layout(config, *, base_dir)`

Purpose: Validate dataset root/exemplar presence and image-count constraints.

Expected inputs and outputs:
- The callable boundary is `validate_dataset_layout(config, *, base_dir)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `ConfigError, exists, is_dir, resolve_available_images, resolve_data_root` to see how this symbol sequences lower-level work.
3. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `ConfigError, exists, is_dir, resolve_available_images, resolve_data_root` without redoing the same validation or reshaping work.

### resolve_data_root

Signature: `resolve_data_root(root, *, base_dir)`

Purpose: Resolve a data root against an optional base directory.

Expected inputs and outputs:
- The callable boundary is `resolve_data_root(root, *, base_dir)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `Path, cwd, is_absolute, resolve` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `Path, cwd, is_absolute, resolve` without redoing the same validation or reshaping work.

### count_image_files

Signature: `count_image_files(directory)`

Purpose: Count image files directly under the given exemplar directory.

Expected inputs and outputs:
- The callable boundary is `count_image_files(directory)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `is_file, iterdir, lower` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `is_file, iterdir, lower` without redoing the same validation or reshaping work.

### resolve_available_images

Signature: `resolve_available_images(exemplar_dir, *, exemplar)`

Purpose: Resolve available exemplar images, preferring _manifest.json when present.

Expected inputs and outputs:
- The callable boundary is `resolve_available_images(exemplar_dir, *, exemplar)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `exists, is_file, iterdir, load_manifest_images, lower, sorted` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `exists, is_file, iterdir, load_manifest_images, lower` without redoing the same validation or reshaping work.

### load_manifest_images

Signature: `load_manifest_images(manifest_path, *, exemplar_dir, exemplar)`

Purpose: Load the manifest-declared image set for an exemplar directory.

Expected inputs and outputs:
- The callable boundary is `load_manifest_images(manifest_path, *, exemplar_dir, exemplar)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `ConfigError, Path, append, exists, get, is_file` to see how this symbol sequences lower-level work.
3. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `ConfigError, Path, append, exists, get` without redoing the same validation or reshaping work.

## Formula Mapping

Formula mapping: not applicable. This file mainly defines schema, orchestration, or utility behavior rather than a standalone equation.

## Design Decisions

- Split schema, parsing, loading, and validation so configuration errors stay field-scoped and testable.
- Prefer explicit dataclasses over untyped dictionaries once the YAML payload has been parsed.

## Common Failure Modes

- Guard clause or surfaced failure: `ConfigError('data timeline must satisfy t_I < t_S < t_E')`
- Guard clause or surfaced failure: `ConfigError('data.crop_size must be less than or equal to data.image_size')`
- Guard clause or surfaced failure: `ConfigError('rendering.light_xy_position must be a tuple of two finite floats')`
- Guard clause or surfaced failure: `ConfigError('train.loss.loss_type must be one of: SW, GRAM')`
- Guard clause or surfaced failure: `ConfigError('train.scheduler.scheduler_factor must be between 0 and 1')`
- Guard clause or surfaced failure: `ConfigError('train.scheduler.scheduler_min_lr must be less than or equal to train.runtime.lr')`
- Guard clause or surfaced failure: `ConfigError('train.stage.n_init_iter must be less than or equal to train.runtime.n_iter')`
- Guard clause or surfaced failure: `ConfigError('train.stage.refresh_rate_init must be greater than or equal to 2')`
- Guard clause or surfaced failure: `ConfigError('train.stage.refresh_rate_local must be greater than or equal to 2')`
- Guard clause or surfaced failure: `ConfigError(f'Invalid manifest JSON: {manifest_path}')`

## How This Connects To Neighboring Files

- [__init__.py](../rendering/__init__.md) supplies or consumes part of this file's contract.

## Related Tests

- [test_config.py](../../../tests/test_config.md)
