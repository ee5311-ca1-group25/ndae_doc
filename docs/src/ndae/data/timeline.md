# timeline.py

Source path: `src/ndae/data/timeline.py`

## Role

This file belongs to the `src/ndae/data` slice of the NDAE repository. Timeline helpers for mapping between frame indices and ODE time.

## Where This File Sits In The Pipeline

This file is one focused step in the `src/ndae/data` slice of the NDAE runtime. In day-to-day execution it interacts most directly with neighboring modules such as `schema.py`.

## Inputs, Outputs, And Tensor Shapes

- This file mostly moves structured Python objects or runtime state rather than introducing a new tensor convention of its own.

## Implementation Walkthrough

Most of the interesting behavior is in class methods, so the best reading strategy is constructor first, then the public methods in the order the rest of the runtime calls them.

This style keeps long-lived state explicit and avoids hiding state transitions in global variables or one-off closures.

## Function And Class Deep Dive

### Timeline

Role: Continuous-time view over exemplar frame indices.

Inheritance: `object`

Owned fields:
- `t_I`
- `t_S`
- `t_E`
- `n_frames`

Public methods:
- `dt(self)`: Key method on this runtime object.
- `warmup_duration(self)`: Key method on this runtime object.
- `generation_duration(self)`: Key method on this runtime object.
- `frame_to_time(self, k)`: Key method on this runtime object.
- `time_to_frame(self, t)`: Key method on this runtime object.
- `from_config(cls, data_config)`: Key method on this runtime object.

How the methods should be read:
- `dt` is one stage in the class-level control flow. Read its guard clauses, then the helper calls `inside this class` to understand how state moves forward.
- `warmup_duration` is one stage in the class-level control flow. Read its guard clauses, then the helper calls `inside this class` to understand how state moves forward.
- `generation_duration` is one stage in the class-level control flow. Read its guard clauses, then the helper calls `inside this class` to understand how state moves forward.
- `frame_to_time` is one stage in the class-level control flow. Read its guard clauses, then the helper calls `IndexError` to understand how state moves forward.
- `time_to_frame` is one stage in the class-level control flow. Read its guard clauses, then the helper calls `floor` to understand how state moves forward.
- `from_config` is one stage in the class-level control flow. Read its guard clauses, then the helper calls `cls` to understand how state moves forward.

How to read this class:
- Start from construction or declared fields to see what long-lived state the object owns.
- Then read public methods in the order the rest of the runtime calls them; that is the real control flow.
- Treat private helpers as local refactoring aids rather than as a second independent API.

## Formula Mapping

- `dt = (t_E - t_S) / n_frames` is the frame spacing used by both `frame_to_time` and `time_to_frame`.
- `frame_to_time(k) = t_S + k * dt` converts discrete supervision indices into continuous ODE time.
- `time_to_frame(t)` computes `floor(max(t - t_S, 0) / dt + 1e-9)` and clamps the result into `[0, n_frames - 1]`.

## Design Decisions

- Represent sampling decisions as reusable specs so target extraction and rendering stay aligned.
- Keep exemplar loading deterministic once frame paths have been selected.

## Common Failure Modes

- There are no custom guard clauses in this file; failures mostly come from imported runtime code or invalid upstream tensors.

## How This Connects To Neighboring Files

- [schema.py](../config/schema.md) supplies or consumes part of this file's contract.

## Related Tests

- [test_package_layout.py](../../../tests/test_package_layout.md)
- [test_dataset.py](../../../tests/test_dataset.md)
- [test_trainer.py](../../../tests/test_trainer.md)
- [test_sample_cli.py](../../../tests/test_sample_cli.md)
- [test_config.py](../../../tests/test_config.md)
- [support.py](../../../tests/support.md)
