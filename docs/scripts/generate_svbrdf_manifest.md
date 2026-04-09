# generate_svbrdf_manifest.py

Source path: `scripts/generate_svbrdf_manifest.py`

## Role

This directory mirrors executable shell entry points from the main repository. Generate an NDAE exemplar manifest from an existing local image directory. The module also exposes a direct `__main__` execution path.

## Where This File Sits In The Pipeline

This file lives on the shell-facing edge of the repository. It translates command-line inputs into calls on the library runtime and keeps operational policy close to the CLI rather than spreading it across unrelated modules.

## Inputs, Outputs, And Tensor Shapes

- The main inputs are command-line arguments and file paths; outputs are usually files, checkpoints, logs, or process exit codes rather than just returned tensors.

## Implementation Walkthrough

Execution starts from shell-facing argument handling or a direct import, then hands control to the library runtime as quickly as possible.

Any logic kept here is operational rather than numerical: output path resolution, checkpoint selection, dry-run control, user-facing summaries, or failure surfacing.

## Function And Class Deep Dive

### build_parser

Signature: `build_parser()`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `build_parser()`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `ArgumentParser, add_argument` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `ArgumentParser, add_argument` without redoing the same validation or reshaping work.

### resolve_selected_files

Signature: `resolve_selected_files(exemplar_dir, exemplar)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `resolve_selected_files(exemplar_dir, exemplar)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `is_file, iterdir, lower, sorted` to see how this symbol sequences lower-level work.
3. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `is_file, iterdir, lower, sorted` without redoing the same validation or reshaping work.

### main

Signature: `main()`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `main()`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `Path, build_parser, error, exists, expanduser, is_dir` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `Path, build_parser, error, exists, expanduser` without redoing the same validation or reshaping work.

## Formula Mapping

Formula mapping: not applicable. This file mainly defines command flow, delegation boundaries, and operational side effects rather than a standalone numerical transform.

## Design Decisions

- Keep executable scripts thin so operational behavior lives in importable library code.
- Use script wrappers as stable shell entry points without duplicating training logic.
- Keep shell-facing code thinner than numerical code so operational changes do not silently alter the math path.

## Common Failure Modes

- Guard clause or surfaced failure: `ValueError(f'No image files found under {exemplar_dir}')`

## How This Connects To Neighboring Files

- This file is relatively self-contained; its closest neighbors are package-level imports rather than one obvious sibling file.

## Related Tests

- No direct test file was matched to this module by the documentation generator.
