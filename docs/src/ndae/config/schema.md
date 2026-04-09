# schema.py

Source path: `src/ndae/config/schema.py`

## Role

This file belongs to the `src/ndae/config` slice of the NDAE repository. Dataclass schemas for NDAE configuration.

## Where This File Sits In The Pipeline

This file is one focused step in the `src/ndae/config` slice of the NDAE runtime.

## Inputs, Outputs, And Tensor Shapes

- This file mostly moves structured Python objects or runtime state rather than introducing a new tensor convention of its own.

## Implementation Walkthrough

Most of the interesting behavior is in class methods, so the best reading strategy is constructor first, then the public methods in the order the rest of the runtime calls them.

This style keeps long-lived state explicit and avoids hiding state transitions in global variables or one-off closures.

## Function And Class Deep Dive

### ExperimentConfig

Role: This class owns one stateful runtime component.

Inheritance: `object`

Owned fields:
- `name`
- `output_root`
- `seed`

How to read this class:
- Start from construction or declared fields to see what long-lived state the object owns.
- Then read public methods in the order the rest of the runtime calls them; that is the real control flow.
- Treat private helpers as local refactoring aids rather than as a second independent API.

### DataConfig

Role: This class owns one stateful runtime component.

Inheritance: `object`

Owned fields:
- `root`
- `exemplar`
- `image_size`
- `crop_size`
- `n_frames`
- `t_S`
- `t_E`

Public methods:
- `t_I(self)`: Key method on this runtime object.

How the methods should be read:
- `t_I` is one stage in the class-level control flow. Read its guard clauses, then the helper calls `inside this class` to understand how state moves forward.

How to read this class:
- Start from construction or declared fields to see what long-lived state the object owns.
- Then read public methods in the order the rest of the runtime calls them; that is the real control flow.
- Treat private helpers as local refactoring aids rather than as a second independent API.

### ModelConfig

Role: This class owns one stateful runtime component.

Inheritance: `object`

Owned fields:
- `dim`
- `solver`

How to read this class:
- Start from construction or declared fields to see what long-lived state the object owns.
- Then read public methods in the order the rest of the runtime calls them; that is the real control flow.
- Treat private helpers as local refactoring aids rather than as a second independent API.

### RenderingConfig

Role: This class owns one stateful runtime component.

Inheritance: `object`

Owned fields:
- `renderer_type`
- `n_brdf_channels`
- `n_normal_channels`
- `n_aug_channels`
- `camera_fov`
- `camera_distance`
- `light_intensity`
- `light_xy_position`
- `height_scale`
- `gamma`

Public methods:
- `total_channels(self)`: Key method on this runtime object.

How the methods should be read:
- `total_channels` is one stage in the class-level control flow. Read its guard clauses, then the helper calls `inside this class` to understand how state moves forward.

How to read this class:
- Start from construction or declared fields to see what long-lived state the object owns.
- Then read public methods in the order the rest of the runtime calls them; that is the real control flow.
- Treat private helpers as local refactoring aids rather than as a second independent API.

### TrainRuntimeConfig

Role: This class owns one stateful runtime component.

Inheritance: `object`

Owned fields:
- `batch_size`
- `lr`
- `dry_run`
- `n_iter`
- `log_every`
- `checkpoint_every`
- `resume_from`

How to read this class:
- Start from construction or declared fields to see what long-lived state the object owns.
- Then read public methods in the order the rest of the runtime calls them; that is the real control flow.
- Treat private helpers as local refactoring aids rather than as a second independent API.

### TrainStageConfig

Role: This class owns one stateful runtime component.

Inheritance: `object`

Owned fields:
- `n_init_iter`
- `refresh_rate_init`
- `refresh_rate_local`

How to read this class:
- Start from construction or declared fields to see what long-lived state the object owns.
- Then read public methods in the order the rest of the runtime calls them; that is the real control flow.
- Treat private helpers as local refactoring aids rather than as a second independent API.

### TrainLossConfig

Role: This class owns one stateful runtime component.

Inheritance: `object`

Owned fields:
- `loss_type`
- `n_loss_crops`
- `overflow_weight`
- `init_height_weight`

How to read this class:
- Start from construction or declared fields to see what long-lived state the object owns.
- Then read public methods in the order the rest of the runtime calls them; that is the real control flow.
- Treat private helpers as local refactoring aids rather than as a second independent API.

### TrainSchedulerConfig

Role: This class owns one stateful runtime component.

Inheritance: `object`

Owned fields:
- `eval_every`
- `scheduler_factor`
- `scheduler_patience_evals`
- `scheduler_min_lr`

How to read this class:
- Start from construction or declared fields to see what long-lived state the object owns.
- Then read public methods in the order the rest of the runtime calls them; that is the real control flow.
- Treat private helpers as local refactoring aids rather than as a second independent API.

### TrainConfig

Role: This class owns one stateful runtime component.

Inheritance: `object`

Owned fields:
- `runtime`
- `stage`
- `loss`
- `scheduler`

How to read this class:
- Start from construction or declared fields to see what long-lived state the object owns.
- Then read public methods in the order the rest of the runtime calls them; that is the real control flow.
- Treat private helpers as local refactoring aids rather than as a second independent API.

### NDAEConfig

Role: This class owns one stateful runtime component.

Inheritance: `object`

Owned fields:
- `experiment`
- `data`
- `model`
- `rendering`
- `train`

How to read this class:
- Start from construction or declared fields to see what long-lived state the object owns.
- Then read public methods in the order the rest of the runtime calls them; that is the real control flow.
- Treat private helpers as local refactoring aids rather than as a second independent API.

## Formula Mapping

Formula mapping: not applicable. This file mainly defines schema, orchestration, or utility behavior rather than a standalone equation.

## Design Decisions

- Split schema, parsing, loading, and validation so configuration errors stay field-scoped and testable.
- Prefer explicit dataclasses over untyped dictionaries once the YAML payload has been parsed.

## Common Failure Modes

- There are no custom guard clauses in this file; failures mostly come from imported runtime code or invalid upstream tensors.

## How This Connects To Neighboring Files

- This file is relatively self-contained; its closest neighbors are package-level imports rather than one obvious sibling file.

## Related Tests

- No direct test file was matched to this module by the documentation generator.
