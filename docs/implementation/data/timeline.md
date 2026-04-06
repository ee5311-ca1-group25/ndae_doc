# Data Timeline

## Purpose

`src/ndae/data/timeline.py` defines the `Timeline` dataclass that maps between discrete frame indices and continuous ODE time.

It isolates time arithmetic from the rest of the data path, which keeps later training code cleaner.

## Public API / key types

The main type is:

```python
@dataclass(slots=True)
class Timeline:
    t_I: float
    t_S: float
    t_E: float
    n_frames: int
```

Key members:

- `dt`
- `warmup_duration`
- `generation_duration`
- `frame_to_time(k)`
- `time_to_frame(t)`
- `from_config(data_config)`

## Behavior and invariants

Derived quantities:

- `dt = (t_E - t_S) / n_frames`
- `warmup_duration = t_S - t_I`
- `generation_duration = t_E - t_S`

Frame-to-time mapping:

```text
frame_to_time(k) = t_S + k * dt
```

This means the last valid frame maps to `t_E - dt`, not `t_E`.

Time-to-frame mapping:

```text
time_to_frame(t) = clamp(floor((t - t_S) / dt), 0, n_frames - 1)
```

Implementation notes:

- times before `t_S` map to frame `0`
- times after the end of the generation window map to the last frame
- a small numeric tolerance is used to preserve `frame_to_time(k)` / `time_to_frame(...)` round-trips under floating-point error

## Error handling

`__post_init__` raises `ValueError` when:

- `n_frames <= 0`
- `t_I < t_S < t_E` does not hold

`frame_to_time(k)` is strict:

- negative or too-large indices raise `IndexError`

`time_to_frame(t)` is permissive:

- any real time is accepted and clamped into the valid frame range

## Tests / validation

`tests/test_dataset.py` checks:

- construction from `DataConfig`
- derived properties
- round-trip behavior for default and non-zero `t_S`
- clamp behavior before the start and after the end
- constructor errors and invalid frame indices

## Related files

- `src/ndae/config/schema.py`
- `configs/base.yaml`
- `tests/test_dataset.py`
