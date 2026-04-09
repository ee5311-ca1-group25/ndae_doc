# solver.py

Source path: `src/ndae/training/solver.py`

## Role

This file belongs to the `src/ndae/training` slice of the NDAE repository. Solver configuration and rollout result containers for NDAE training.

## Where This File Sits In The Pipeline

This file is one focused step in the `src/ndae/training` slice of the NDAE runtime.

## Inputs, Outputs, And Tensor Shapes

- This file mostly moves structured Python objects or runtime state rather than introducing a new tensor convention of its own.

## Implementation Walkthrough

The file is built from focused helpers rather than one monolithic routine. That makes each contract easier to test and lets neighboring modules reuse only the pieces they need.

Branches in this file usually separate runtime modes or reject invalid inputs early so deeper numerical code can stay cleaner.

## Function And Class Deep Dive

### SolverConfig

Role: Numerical solver configuration for ODE integration.

Inheritance: `object`

Owned fields:
- `method`
- `rtol`
- `atol`
- `options`

How to read this class:
- Start from construction or declared fields to see what long-lived state the object owns.
- Then read public methods in the order the rest of the runtime calls them; that is the real control flow.
- Treat private helpers as local refactoring aids rather than as a second independent API.

### RolloutResult

Role: Result of a single rollout segment.

Inheritance: `object`

Owned fields:
- `states`
- `final_state`
- `t0`
- `t1`

How to read this class:
- Start from construction or declared fields to see what long-lived state the object owns.
- Then read public methods in the order the rest of the runtime calls them; that is the real control flow.
- Treat private helpers as local refactoring aids rather than as a second independent API.

### solve_rollout

Signature: `solve_rollout(trajectory_model, z0, t0, t1, config)`

Purpose: Integrate a single rollout segment between two times.

Expected inputs and outputs:
- The callable boundary is `solve_rollout(trajectory_model, z0, t0, t1, config)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `RolloutResult, tensor, trajectory_model` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `RolloutResult, tensor, trajectory_model` without redoing the same validation or reshaping work.

### rollout_warmup

Signature: `rollout_warmup(trajectory_model, z0, window, config)`

Purpose: Execute a warm-up rollout for a precomputed warm-up window.

Expected inputs and outputs:
- The callable boundary is `rollout_warmup(trajectory_model, z0, window, config)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `solve_rollout` to see how this symbol sequences lower-level work.
3. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `solve_rollout` without redoing the same validation or reshaping work.

### rollout_generation

Signature: `rollout_generation(trajectory_model, z0, window, config)`

Purpose: Execute a generation rollout for a precomputed generation window.

Expected inputs and outputs:
- The callable boundary is `rollout_generation(trajectory_model, z0, window, config)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `solve_rollout` to see how this symbol sequences lower-level work.
3. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `solve_rollout` without redoing the same validation or reshaping work.

## Formula Mapping

- `solve_rollout` always integrates exactly two time points, so the returned tensor contains the start state and the end state for one training segment.
- `rollout_warmup` and `rollout_generation` are guard wrappers around `solve_rollout` that enforce the schedule contract before integration begins.

## Design Decisions

- Keep immutable config containers separate from the stateful trainer runtime.
- Assemble train-time dependencies in a factory so stage resets can rebuild only what needs rebuilding.

## Common Failure Modes

- Guard clause or surfaced failure: `ValueError('rollout_generation expected a generation window with refresh=False')`
- Guard clause or surfaced failure: `ValueError('rollout_warmup expected a warmup window with refresh=True')`

## How This Connects To Neighboring Files

- This file is relatively self-contained; its closest neighbors are package-level imports rather than one obvious sibling file.

## Related Tests

- [test_solver.py](../../../tests/test_solver.md)
- [test_package_layout.py](../../../tests/test_package_layout.md)
- [test_trainer.py](../../../tests/test_trainer.md)
- [test_smoke.py](../../../tests/test_smoke.md)
- [test_models.py](../../../tests/test_models.md)
- [test_config.py](../../../tests/test_config.md)
