# train_svbrdf.py

Source path: `scripts/train_svbrdf.py`

## Role

This directory mirrors executable shell entry points from the main repository. Thin script entry point for training. The module also exposes a direct `__main__` execution path.

## Where This File Sits In The Pipeline

This file lives on the shell-facing edge of the repository. It translates command-line inputs into calls on the library runtime and keeps operational policy close to the CLI rather than spreading it across unrelated modules. In day-to-day execution it interacts most directly with neighboring modules such as `train.py`.

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

- [train.py](../src/ndae/cli/train.md) supplies or consumes part of this file's contract.

## Related Tests

- No direct test file was matched to this module by the documentation generator.
