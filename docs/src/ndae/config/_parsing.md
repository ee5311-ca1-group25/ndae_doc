# _parsing.py

Source path: `src/ndae/config/_parsing.py`

## Role

This file belongs to the `src/ndae/config` slice of the NDAE repository. Internal helpers for reading config payloads into dataclasses.

## Where This File Sits In The Pipeline

This file is one focused step in the `src/ndae/config` slice of the NDAE runtime. In day-to-day execution it interacts most directly with neighboring modules such as `__init__.py`.

## Inputs, Outputs, And Tensor Shapes

- This file mostly moves structured Python objects or runtime state rather than introducing a new tensor convention of its own.

## Implementation Walkthrough

The file is built from focused helpers rather than one monolithic routine. That makes each contract easier to test and lets neighboring modules reuse only the pieces they need.

Branches in this file usually separate runtime modes or reject invalid inputs early so deeper numerical code can stay cleaner.

## Function And Class Deep Dive

### config_from_mapping

Signature: `config_from_mapping(payload)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `config_from_mapping(payload)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `NDAEConfig, build_data_config, build_experiment_config, build_model_config, build_rendering_config, build_train_config` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `NDAEConfig, build_data_config, build_experiment_config, build_model_config, build_rendering_config` without redoing the same validation or reshaping work.

### build_experiment_config

Signature: `build_experiment_config(payload)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `build_experiment_config(payload)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `ExperimentConfig, expect_keys, read_int, read_str` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `ExperimentConfig, expect_keys, read_int, read_str` without redoing the same validation or reshaping work.

### build_data_config

Signature: `build_data_config(payload)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `build_data_config(payload)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `DataConfig, expect_keys, read_int, read_optional_float, read_str` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `DataConfig, expect_keys, read_int, read_optional_float, read_str` without redoing the same validation or reshaping work.

### build_model_config

Signature: `build_model_config(payload)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `build_model_config(payload)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `ModelConfig, expect_keys, read_int, read_str` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `ModelConfig, expect_keys, read_int, read_str` without redoing the same validation or reshaping work.

### build_rendering_config

Signature: `build_rendering_config(payload)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `build_rendering_config(payload)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `ConfigError, RenderingConfig, expect_keys, join, read_optional_float, read_optional_float_pair` to see how this symbol sequences lower-level work.
3. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `ConfigError, RenderingConfig, expect_keys, join, read_optional_float` without redoing the same validation or reshaping work.

### build_train_config

Signature: `build_train_config(payload)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `build_train_config(payload)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `TrainConfig, build_train_loss_config, build_train_runtime_config, build_train_scheduler_config, build_train_stage_config, expect_keys` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `TrainConfig, build_train_loss_config, build_train_runtime_config, build_train_scheduler_config, build_train_stage_config` without redoing the same validation or reshaping work.

### build_train_runtime_config

Signature: `build_train_runtime_config(payload)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `build_train_runtime_config(payload)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `TrainRuntimeConfig, expect_keys, read_bool, read_float, read_int, read_optional_int` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `TrainRuntimeConfig, expect_keys, read_bool, read_float, read_int` without redoing the same validation or reshaping work.

### build_train_stage_config

Signature: `build_train_stage_config(payload)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `build_train_stage_config(payload)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `TrainStageConfig, expect_keys, read_int, read_optional_int` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `TrainStageConfig, expect_keys, read_int, read_optional_int` without redoing the same validation or reshaping work.

### build_train_loss_config

Signature: `build_train_loss_config(payload)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `build_train_loss_config(payload)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `TrainLossConfig, expect_keys, read_optional_float, read_optional_int, read_optional_str, upper` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `TrainLossConfig, expect_keys, read_optional_float, read_optional_int, read_optional_str` without redoing the same validation or reshaping work.

### build_train_scheduler_config

Signature: `build_train_scheduler_config(payload)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `build_train_scheduler_config(payload)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `TrainSchedulerConfig, expect_keys, read_optional_float, read_optional_int` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `TrainSchedulerConfig, expect_keys, read_optional_float, read_optional_int` without redoing the same validation or reshaping work.

### expect_keys

Signature: `expect_keys(payload, section, required, *, optional=None)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `expect_keys(payload, section, required, *, optional=None)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `ConfigError, append, join, sorted` to see how this symbol sequences lower-level work.
3. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `ConfigError, append, join, sorted` without redoing the same validation or reshaping work.

### read_str

Signature: `read_str(payload, key, section)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `read_str(payload, key, section)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `ConfigError, isinstance` to see how this symbol sequences lower-level work.
3. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `ConfigError, isinstance` without redoing the same validation or reshaping work.

### read_int

Signature: `read_int(payload, key, section)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `read_int(payload, key, section)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `ConfigError, type` to see how this symbol sequences lower-level work.
3. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `ConfigError, type` without redoing the same validation or reshaping work.

### read_float

Signature: `read_float(payload, key, section)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `read_float(payload, key, section)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `ConfigError, type` to see how this symbol sequences lower-level work.
3. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `ConfigError, type` without redoing the same validation or reshaping work.

### read_optional_float

Signature: `read_optional_float(payload, key, section, *, default)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `read_optional_float(payload, key, section, *, default)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `read_float` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `read_float` without redoing the same validation or reshaping work.

### read_optional_str

Signature: `read_optional_str(payload, key, section, *, default)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `read_optional_str(payload, key, section, *, default)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `read_str` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `read_str` without redoing the same validation or reshaping work.

### read_optional_int

Signature: `read_optional_int(payload, key, section, *, default)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `read_optional_int(payload, key, section, *, default)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `read_int` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `read_int` without redoing the same validation or reshaping work.

### read_bool

Signature: `read_bool(payload, key, section)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `read_bool(payload, key, section)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `ConfigError, type` to see how this symbol sequences lower-level work.
3. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `ConfigError, type` without redoing the same validation or reshaping work.

### read_optional_float_pair

Signature: `read_optional_float_pair(payload, key, section, *, default)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `read_optional_float_pair(payload, key, section, *, default)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `ConfigError, isinstance, type` to see how this symbol sequences lower-level work.
3. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `ConfigError, isinstance, type` without redoing the same validation or reshaping work.

### require_mapping

Signature: `require_mapping(value, section)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `require_mapping(value, section)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `ConfigError, isinstance` to see how this symbol sequences lower-level work.
3. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `ConfigError, isinstance` without redoing the same validation or reshaping work.

## Formula Mapping

Formula mapping: not applicable. This file mainly defines schema, orchestration, or utility behavior rather than a standalone equation.

## Design Decisions

- Split schema, parsing, loading, and validation so configuration errors stay field-scoped and testable.
- Prefer explicit dataclasses over untyped dictionaries once the YAML payload has been parsed.

## Common Failure Modes

- Guard clause or surfaced failure: `ConfigError(f"Invalid {section} section: {'; '.join(problems)}")`
- Guard clause or surfaced failure: `ConfigError(f'rendering.renderer_type must be one of: {supported}')`
- Guard clause or surfaced failure: `ConfigError(f'{section} must be a mapping')`
- Guard clause or surfaced failure: `ConfigError(f'{section}.{key} must be a boolean')`
- Guard clause or surfaced failure: `ConfigError(f'{section}.{key} must be a float')`
- Guard clause or surfaced failure: `ConfigError(f'{section}.{key} must be a sequence of two floats')`
- Guard clause or surfaced failure: `ConfigError(f'{section}.{key} must be a string')`
- Guard clause or surfaced failure: `ConfigError(f'{section}.{key} must be an integer')`

## How This Connects To Neighboring Files

- [__init__.py](../rendering/__init__.md) supplies or consumes part of this file's contract.

## Related Tests

- No direct test file was matched to this module by the documentation generator.
