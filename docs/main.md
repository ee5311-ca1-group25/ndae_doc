# main.py

Source path: `main.py`

## Role

This directory mirrors executable shell entry points from the main repository. The module also exposes a direct `__main__` execution path.

## Where This File Sits In The Pipeline

This is the outermost shell-facing training entrypoint. It exists above the package tree and immediately hands control to the CLI layer. In day-to-day execution it interacts most directly with neighboring modules such as `train.py`.

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

- Keep executable scripts thin so operational behavior lives in importable library code.
- Use script wrappers as stable shell entry points without duplicating training logic.
- Keep shell-facing code thinner than numerical code so operational changes do not silently alter the math path.

## Common Failure Modes

- Most failures here come from delegated library calls, CLI argument misuse, or filesystem state rather than bespoke numerical checks.

## How This Connects To Neighboring Files

- [train.py](src/ndae/cli/train.md) supplies or consumes part of this file's contract.

## Related Tests

- [test_package_layout.py](tests/test_package_layout.md)
- [test_smoke.py](tests/test_smoke.md)
