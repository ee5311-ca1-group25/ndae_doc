# system.py

Source path: `src/ndae/training/system.py`

## Role

This file belongs to the `src/ndae/training` slice of the NDAE repository. Shared svBRDF runtime assembly for training and sampling.

## Where This File Sits In The Pipeline

This file is one focused step in the `src/ndae/training` slice of the NDAE runtime. In day-to-day execution it interacts most directly with neighboring modules such as `__init__.py`, `__init__.py`, `__init__.py`.

## Inputs, Outputs, And Tensor Shapes

- This file mostly moves structured Python objects or runtime state rather than introducing a new tensor convention of its own.

## Implementation Walkthrough

The file is built from focused helpers rather than one monolithic routine. That makes each contract easier to test and lets neighboring modules reuse only the pieces they need.

Branches in this file usually separate runtime modes or reject invalid inputs early so deeper numerical code can stay cleaner.

## Function And Class Deep Dive

### SVBRDFSystem

Role: Shared runtime components for svBRDF train/sample entry points.

Inheritance: `object`

Owned fields:
- `trajectory_model`
- `solver_config`
- `camera`
- `flash_light`
- `renderer_pp`
- `unpack_fn`
- `total_channels`
- `n_brdf_channels`
- `n_normal_channels`
- `height_scale`
- `gamma`

How to read this class:
- Start from construction or declared fields to see what long-lived state the object owns.
- Then read public methods in the order the rest of the runtime calls them; that is the real control flow.
- Treat private helpers as local refactoring aids rather than as a second independent API.

### build_svbrdf_system

Signature: `build_svbrdf_system(config)`

Purpose: Build the model, solver, and rendering runtime from config.

Expected inputs and outputs:
- The callable boundary is `build_svbrdf_system(config)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `Camera, FlashLight, NDAEUNet, ODEFunction, Parameter, SVBRDFSystem` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `Camera, FlashLight, NDAEUNet, ODEFunction, Parameter` without redoing the same validation or reshaping work.

### resolve_solver_method

Signature: `resolve_solver_method(solver)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `resolve_solver_method(solver)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.

What downstream code assumes:
- Callers assume the return value already matches the local conventions of the surrounding file and can be consumed directly.

### resolve_renderer_runtime

Signature: `resolve_renderer_runtime(config)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `resolve_renderer_runtime(config)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.

What downstream code assumes:
- Callers assume the return value already matches the local conventions of the surrounding file and can be consumed directly.

### render_latent_state

Signature: `render_latent_state(system, state)`

Purpose: Project one latent svBRDF state into a tone-mapped RGB image.

Expected inputs and outputs:
- The callable boundary is `render_latent_state(system, state)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `clip_maps, height_to_normal, render_svbrdf, split_latent_maps, tonemapping` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `clip_maps, height_to_normal, render_svbrdf, split_latent_maps, tonemapping` without redoing the same validation or reshaping work.

## Formula Mapping

- `build_svbrdf_system` assembles the vector field, ODE wrapper, trajectory model, solver configuration, camera, light, and renderer choice into one runtime object.
- `render_latent_state` applies `split_latent_maps -> height_to_normal -> clip_maps -> render_svbrdf -> tonemapping`.
- The flashlight intensity is stored as a learnable scalar parameter, which keeps the renderer differentiable with respect to exposure.

## Design Decisions

- Keep immutable config containers separate from the stateful trainer runtime.
- Assemble train-time dependencies in a factory so stage resets can rebuild only what needs rebuilding.

## Common Failure Modes

- Guard clause or surfaced failure: `ValueError(f"Non-dry-run training only supports renderer_type 'diffuse_cook_torrance' and 'diffuse_iso_cook_torrance', got {renderer_type!r}.")`
- Guard clause or surfaced failure: `ValueError(f"Unsupported model.solver for the training runtime: {solver!r}. Expected 'heun' or 'euler'.")`

## How This Connects To Neighboring Files

- [__init__.py](../config/__init__.md) supplies or consumes part of this file's contract.
- [__init__.py](../models/__init__.md) supplies or consumes part of this file's contract.
- [__init__.py](../rendering/__init__.md) supplies or consumes part of this file's contract.

## Related Tests

- [test_package_layout.py](../../../tests/test_package_layout.md)
- [support.py](../../../tests/support.md)
- [test_trainer.py](../../../tests/test_trainer.md)
- [test_sample_cli.py](../../../tests/test_sample_cli.md)
- [test_checkpoint.py](../../../tests/test_checkpoint.md)
