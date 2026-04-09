# __init__.py

Source path: `src/ndae/cli/__init__.py`

## Role

This file belongs to the `src/ndae/cli` slice of the NDAE repository. Command-line entry points for NDAE.

## Where This File Sits In The Pipeline

This file lives on the shell-facing edge of the repository. It translates command-line inputs into calls on the library runtime and keeps operational policy close to the CLI rather than spreading it across unrelated modules.

## Inputs, Outputs, And Tensor Shapes

- The main inputs are command-line arguments and file paths; outputs are usually files, checkpoints, logs, or process exit codes rather than just returned tensors.

## Implementation Walkthrough

Execution starts from shell-facing argument handling or a direct import, then hands control to the library runtime as quickly as possible.

Any logic kept here is operational rather than numerical: output path resolution, checkpoint selection, dry-run control, user-facing summaries, or failure surfacing.

## Function And Class Deep Dive

This file is intentionally thin. Its value comes from the contract it exposes or the module it delegates into, not from a large amount of internal logic.

## Formula Mapping

Formula mapping: not applicable. This file mainly defines command flow, delegation boundaries, and operational side effects rather than a standalone numerical transform.

## Design Decisions

- Separate argument parsing from runtime assembly so tests can call CLI helpers directly.
- Keep CLI modules close to the shell contract and delegate numerical work to the library.
- Keep shell-facing code thinner than numerical code so operational changes do not silently alter the math path.

## Common Failure Modes

- Most failures here come from delegated library calls, CLI argument misuse, or filesystem state rather than bespoke numerical checks.

## How This Connects To Neighboring Files

- This file is relatively self-contained; its closest neighbors are package-level imports rather than one obvious sibling file.

## Related Tests

- [test_smoke.py](../../../tests/test_smoke.md)
- [test_sample_cli.py](../../../tests/test_sample_cli.md)
- [test_package_layout.py](../../../tests/test_package_layout.md)
