# trainer.py

Source path: `src/ndae/training/trainer.py`

## Role

This file belongs to the `src/ndae/training` slice of the NDAE repository. Trainer orchestration runtime.

## Where This File Sits In The Pipeline

This file is the orchestration center of the train-time runtime. It sits above schedule, solver, target sampling, rendering, losses, and evaluation, and it is the place where one optimization step becomes a repeatable state machine.

## Inputs, Outputs, And Tensor Shapes

- `exemplar_frames` are stored as `[N, 3, H, W]`, while latent states and rendered crops are batch-first tensors produced during each training step.
- The trainer keeps a carried latent state between continuation windows, so the effective state machine is not just optimizer state but also ODE state, carry time, and cycle position.
- Loss tensors are always reduced to scalars before backward, which is why the trainer can normalize gradients parameter by parameter after `loss_total.backward()`.

## Implementation Walkthrough

Construction wires together long-lived runtime objects and creates the mutable training state. The trainer deliberately owns optimizer, scheduler, carry state, and metric logging because those pieces evolve step by step.

A single `step()` call chooses the active stage, asks the refresh schedule for the next rollout window, integrates the latent state, projects it into renderable maps, samples the correct target batch for the stage, computes the scalar loss, normalizes gradients, and advances the state machine.

The outer `run()` loop stays thin on purpose. It repeatedly calls `step()`, logs metrics, and triggers evaluation through a separate helper, keeping optimization and evaluation boundaries readable.

## Function And Class Deep Dive

### TrainerComponents

Role: Long-lived runtime objects injected into the trainer.

Inheritance: `object`

Owned fields:
- `system`
- `optimizer_factory`
- `schedule`
- `init_stage_config`
- `local_stage_config`
- `vgg_features`

How to read this class:
- Start from construction or declared fields to see what long-lived state the object owns.
- Then read public methods in the order the rest of the runtime calls them; that is the real control flow.
- Treat private helpers as local refactoring aids rather than as a second independent API.

### Trainer

Role: Coordinate schedule, rollout, rendering, loss, and optimization.

Inheritance: `object`

Public methods:
- `batch_size(self)`: Key method on this runtime object.
- `workspace(self)`: Key method on this runtime object.
- `generator(self)`: Key method on this runtime object.
- `n_init_iter(self)`: Key method on this runtime object.
- `step(self)`: Run one optimization step and update the trainer state.
- `run(self, eval_callback=None)`: Run the configured number of training steps.

How the methods should be read:
- `batch_size` is one stage in the class-level control flow. Read its guard clauses, then the helper calls `inside this class` to understand how state moves forward.
- `workspace` is one stage in the class-level control flow. Read its guard clauses, then the helper calls `inside this class` to understand how state moves forward.
- `generator` is one stage in the class-level control flow. Read its guard clauses, then the helper calls `inside this class` to understand how state moves forward.
- `n_init_iter` is one stage in the class-level control flow. Read its guard clauses, then the helper calls `inside this class` to understand how state moves forward.
- `step` is one stage in the class-level control flow. Read its guard clauses, then the helper calls `_current_stage, _enter_local_stage, _normalize_gradients, _project_state, _resolve_initial_state` to understand how state moves forward.
- `run` is one stage in the class-level control flow. Read its guard clauses, then the helper calls `_log_metrics, eval_callback, run_eval, should_eval, step` to understand how state moves forward.

How to read this class:
- Start from construction or declared fields to see what long-lived state the object owns.
- Then read public methods in the order the rest of the runtime calls them; that is the real control flow.
- Treat private helpers as local refactoring aids rather than as a second independent API.

## Formula Mapping

- Init-stage total loss is `loss_total = init_loss(rendered, target) + init_height_weight * mean(height_map^2) + overflow_weight * overflow_loss(brdf_maps)`.
- Local-stage total loss is `loss_total = local_loss(vgg, rendered, target, loss_type) + overflow_weight * overflow_loss(brdf_maps)`.
- Gradient normalization divides each parameter gradient by `||g|| + 1e-8` before the optimizer step.
- Stage transition resets the optimizer, scheduler, schedule state, carry state, carry time, and cycle index when training crosses from init to local.

## Design Decisions

- Keep immutable config containers separate from the stateful trainer runtime.
- Assemble train-time dependencies in a factory so stage resets can rebuild only what needs rebuilding.

## Common Failure Modes

- There are no custom guard clauses in this file; failures mostly come from imported runtime code or invalid upstream tensors.

## How This Connects To Neighboring Files

- This file is relatively self-contained; its closest neighbors are package-level imports rather than one obvious sibling file.

## Related Tests

- [test_trainer.py](../../../tests/test_trainer.md)
- [test_package_layout.py](../../../tests/test_package_layout.md)
- [test_smoke.py](../../../tests/test_smoke.md)
- [test_sample_cli.py](../../../tests/test_sample_cli.md)
- [test_checkpoint.py](../../../tests/test_checkpoint.md)
- [support.py](../../../tests/support.md)
