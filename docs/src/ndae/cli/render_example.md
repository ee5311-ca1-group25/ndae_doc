# render_example.py

Source path: `src/ndae/cli/render_example.py`

## Role

This file belongs to the `src/ndae/cli` slice of the NDAE repository. Render a synthetic svBRDF example image.

## Where This File Sits In The Pipeline

This file lives on the shell-facing edge of the repository. It translates command-line inputs into calls on the library runtime and keeps operational policy close to the CLI rather than spreading it across unrelated modules. In day-to-day execution it interacts most directly with neighboring modules such as `__init__.py`, `__init__.py`.

## Inputs, Outputs, And Tensor Shapes

- The main inputs are command-line arguments and file paths; outputs are usually files, checkpoints, logs, or process exit codes rather than just returned tensors.

## Implementation Walkthrough

Execution starts from shell-facing argument handling or a direct import, then hands control to the library runtime as quickly as possible.

Any logic kept here is operational rather than numerical: output path resolution, checkpoint selection, dry-run control, user-facing summaries, or failure surfacing.

## Function And Class Deep Dive

### build_argparser

Signature: `build_argparser()`

Purpose: Build the synthetic svBRDF example parser.

Expected inputs and outputs:
- The callable boundary is `build_argparser()`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `ArgumentParser, add_argument` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `ArgumentParser, add_argument` without redoing the same validation or reshaping work.

### run_render_example_cli

Signature: `run_render_example_cli(argv=None)`

Purpose: Render a synthetic svBRDF image and save it as PNG.

Expected inputs and outputs:
- The callable boundary is `run_render_example_cli(argv=None)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `Camera, FlashLight, build_argparser, build_example_svbrdf_maps, clip_maps, error` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `Camera, FlashLight, build_argparser, build_example_svbrdf_maps, clip_maps` without redoing the same validation or reshaping work.

### resolve_output_path

Signature: `resolve_output_path(output, *, preset)`

Purpose: Resolve the output path for the selected preset.

Expected inputs and outputs:
- The callable boundary is `resolve_output_path(output, *, preset)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `Path` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `Path` without redoing the same validation or reshaping work.

### build_example_svbrdf_maps

Signature: `build_example_svbrdf_maps(image_size, *, preset='plastic')`

Purpose: Build a deterministic synthetic svBRDF and height map.

Expected inputs and outputs:
- The callable boundary is `build_example_svbrdf_maps(image_size, *, preset='plastic')`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `build_checkerboard, build_coated_metal_preset, build_plastic_preset, cat, clamp, linspace` to see how this symbol sequences lower-level work.
3. Pay attention to layout changes; this is usually where the function adapts data for the next subsystem.
4. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.
- Tensor rearrangements are spelled out directly because later code depends on exact channel and batch semantics.
- Clamping is used as a numerical guardrail so later formulas stay inside the domain they were designed for.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `build_checkerboard, build_coated_metal_preset, build_plastic_preset, cat, clamp` without redoing the same validation or reshaping work.

### build_checkerboard

Signature: `build_checkerboard(xx, yy, *, frequency=3.0)`

Purpose: Build a tiled checkerboard mask in [0, 1].

Expected inputs and outputs:
- The callable boundary is `build_checkerboard(xx, yy, *, frequency=3.0)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `sin, to` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `sin, to` without redoing the same validation or reshaping work.

### build_plastic_preset

Signature: `build_plastic_preset(xx, yy, radial, checker)`

Purpose: Build a smooth painted-plastic material with a broad isotropic highlight.

Expected inputs and outputs:
- The callable boundary is `build_plastic_preset(xx, yy, radial, checker)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `clamp, exp, sin, square, stack, unsqueeze` to see how this symbol sequences lower-level work.
2. Pay attention to layout changes; this is usually where the function adapts data for the next subsystem.
3. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- Tensor rearrangements are spelled out directly because later code depends on exact channel and batch semantics.
- Clamping is used as a numerical guardrail so later formulas stay inside the domain they were designed for.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `clamp, exp, sin, square, stack` without redoing the same validation or reshaping work.

### build_coated_metal_preset

Signature: `build_coated_metal_preset(xx, yy, radial, checker)`

Purpose: Build a dark coated-metal material with a tighter isotropic highlight.

Expected inputs and outputs:
- The callable boundary is `build_coated_metal_preset(xx, yy, radial, checker)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `clamp, cos, exp, sin, square, stack` to see how this symbol sequences lower-level work.
2. Pay attention to layout changes; this is usually where the function adapts data for the next subsystem.
3. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- Tensor rearrangements are spelled out directly because later code depends on exact channel and batch semantics.
- Clamping is used as a numerical guardrail so later formulas stay inside the domain they were designed for.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `clamp, cos, exp, sin, square` without redoing the same validation or reshaping work.

### save_image

Signature: `save_image(path, image)`

Purpose: Save a CHW tensor as an RGB PNG.

Expected inputs and outputs:
- The callable boundary is `save_image(path, image)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `save_png_image` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `save_png_image` without redoing the same validation or reshaping work.

## Formula Mapping

Formula mapping: not applicable. This file mainly defines command flow, delegation boundaries, and operational side effects rather than a standalone numerical transform.

## Design Decisions

- Separate argument parsing from runtime assembly so tests can call CLI helpers directly.
- Keep CLI modules close to the shell contract and delegate numerical work to the library.
- Keep shell-facing code thinner than numerical code so operational changes do not silently alter the math path.

## Common Failure Modes

- Guard clause or surfaced failure: `ValueError(f'Unknown preset: {preset}')`

## How This Connects To Neighboring Files

- [__init__.py](../rendering/__init__.md) supplies or consumes part of this file's contract.
- [__init__.py](../utils/__init__.md) supplies or consumes part of this file's contract.

## Related Tests

- [test_smoke.py](../../../tests/test_smoke.md)
