# train.py

Source path: `src/ndae/cli/train.py`

## Role

This file belongs to the `src/ndae/cli` slice of the NDAE repository. Training CLI.

## Where This File Sits In The Pipeline

This file lives on the shell-facing edge of the repository. It translates command-line inputs into calls on the library runtime and keeps operational policy close to the CLI rather than spreading it across unrelated modules. In day-to-day execution it interacts most directly with neighboring modules such as `__init__.py`, `__init__.py`, `__init__.py`.

## Inputs, Outputs, And Tensor Shapes

- The main inputs are command-line arguments and file paths; outputs are usually files, checkpoints, logs, or process exit codes rather than just returned tensors.

## Implementation Walkthrough

Execution starts from shell-facing argument handling or a direct import, then hands control to the library runtime as quickly as possible.

Any logic kept here is operational rather than numerical: output path resolution, checkpoint selection, dry-run control, user-facing summaries, or failure surfacing.

## Function And Class Deep Dive

### build_argparser

Signature: `build_argparser()`

Purpose: Build the train CLI parser.

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

### run_train_cli

Signature: `run_train_cli(argv=None)`

Purpose: Run the train entry point.

Expected inputs and outputs:
- The callable boundary is `run_train_cli(argv=None)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `Path, VGG19Features, apply_overrides, build_argparser, build_trainer, create_workspace` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `Path, VGG19Features, apply_overrides, build_argparser, build_trainer` without redoing the same validation or reshaping work.

### apply_overrides

Signature: `apply_overrides(config, *, output_root, force_dry_run)`

Purpose: Apply CLI overrides to the config tree.

Expected inputs and outputs:
- The callable boundary is `apply_overrides(config, *, output_root, force_dry_run)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `replace` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `replace` without redoing the same validation or reshaping work.

### make_eval_checkpoint_callback

Signature: `make_eval_checkpoint_callback(workspace)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `make_eval_checkpoint_callback(workspace)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `save_checkpoint` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `save_checkpoint` without redoing the same validation or reshaping work.

## Formula Mapping

Formula mapping: not applicable. This file mainly defines command flow, delegation boundaries, and operational side effects rather than a standalone numerical transform.

## Design Decisions

- Separate argument parsing from runtime assembly so tests can call CLI helpers directly.
- Keep CLI modules close to the shell contract and delegate numerical work to the library.
- Keep shell-facing code thinner than numerical code so operational changes do not silently alter the math path.

## Common Failure Modes

- Most failures here come from delegated library calls, CLI argument misuse, or filesystem state rather than bespoke numerical checks.

## How This Connects To Neighboring Files

- [__init__.py](../config/__init__.md) supplies or consumes part of this file's contract.
- [__init__.py](../losses/__init__.md) supplies or consumes part of this file's contract.
- [__init__.py](../training/__init__.md) supplies or consumes part of this file's contract.
- [__init__.py](../utils/__init__.md) supplies or consumes part of this file's contract.

## Related Tests

- [test_smoke.py](../../../tests/test_smoke.md)
- [test_package_layout.py](../../../tests/test_package_layout.md)
- [test_trainer.py](../../../tests/test_trainer.md)
- [test_solver.py](../../../tests/test_solver.md)
- [test_schedule.py](../../../tests/test_schedule.md)
- [test_sample_cli.py](../../../tests/test_sample_cli.md)
