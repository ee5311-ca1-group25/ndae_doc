# trajectory.py

Source path: `src/ndae/models/trajectory.py`

## Role

This file belongs to the `src/ndae/models` slice of the NDAE repository. Trajectory integration wrapper for NDAE models.

## Where This File Sits In The Pipeline

This file is one focused step in the `src/ndae/models` slice of the NDAE runtime.

## Inputs, Outputs, And Tensor Shapes

- The canonical batched tensor layout in this file is `[B, C, H, W]`, which matches the rest of the image-like runtime.

## Implementation Walkthrough

Most of the interesting behavior is in class methods, so the best reading strategy is constructor first, then the public methods in the order the rest of the runtime calls them.

This style keeps long-lived state explicit and avoids hiding state transitions in global variables or one-off closures.

## Function And Class Deep Dive

### TrajectoryModel

Role: Integrate an ODE function over evaluation times.

Inheritance: `nn.Module`

Public methods:
- `forward(self, z0, t_eval, **solver_kwargs)`: Key method on this runtime object.

How the methods should be read:
- `forward` is one stage in the class-level control flow. Read its guard clauses, then the helper calls `dim, numel, odeint` to understand how state moves forward.

How to read this class:
- Start from construction or declared fields to see what long-lived state the object owns.
- Then read public methods in the order the rest of the runtime calls them; that is the real control flow.
- Treat private helpers as local refactoring aids rather than as a second independent API.

## Formula Mapping

- `TrajectoryModel.forward` computes `states = odeint(odefunc, z0, t_eval, **solver_kwargs)`.
- Input validation enforces `z0.shape == [B, C, H, W]` and `t_eval.shape == [T]` with `T >= 2` before the numerical solver is called.

## Design Decisions

- Use small modules with explicit shape validation instead of hiding tensor contracts inside one large model file.
- Keep the ODE adapter, trajectory wrapper, embeddings, and blocks independently testable.

## Common Failure Modes

- There are no custom guard clauses in this file; failures mostly come from imported runtime code or invalid upstream tensors.

## How This Connects To Neighboring Files

- This file is relatively self-contained; its closest neighbors are package-level imports rather than one obvious sibling file.

## Related Tests

- [test_solver.py](../../../tests/test_solver.md)
- [test_package_layout.py](../../../tests/test_package_layout.md)
- [test_models.py](../../../tests/test_models.md)
- [test_trainer.py](../../../tests/test_trainer.md)
- [test_checkpoint.py](../../../tests/test_checkpoint.md)
- [support.py](../../../tests/support.md)
