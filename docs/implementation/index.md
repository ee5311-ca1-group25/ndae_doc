# Implementation Overview

This section documents the files that implement the current NDAE data path.

The goal of this implementation slice is to make the data path concrete:

- parse timeline-aware configuration
- validate dataset layout and timeline parameters
- load exemplar frames into memory
- map between discrete frames and continuous ODE time
- provide crop, take, and frame-sampling utilities
- verify all of the above with focused tests

These pages are implementation references. They describe code behavior and invariants, not the full theory from the course notes.

## Data pipeline at a glance

This implementation slice connects the following modules:

- `src/ndae/config/schema.py`
- `src/ndae/config/_parsing.py`
- `src/ndae/config/validation.py`
- `configs/base.yaml`
- `src/ndae/data/exemplar.py`
- `src/ndae/data/timeline.py`
- `src/ndae/data/sampling.py`
- `tests/test_dataset.py`

The flow is:

1. Load `configs/base.yaml` into dataclasses.
2. Validate dataset paths, manifest contents, frame counts, and timeline ordering.
3. Load exemplar images into a `[N, 3, H, W]` tensor.
4. Build a `Timeline` object for frame/time conversion.
5. Use sampling helpers for local crops, shuffled pixel samples, and online-training frame selection.
6. Lock the behavior down with dataset and utility tests.

## Reading guide

- Start with [Config Schema](config/schema.md) and [Config Parsing](config/parsing.md) to understand how timeline fields enter the program.
- Read [Config Validation](config/validation.md) and [Base Config](config/base-config.md) to see how the mini dataset and timeline defaults are checked.
- Read [Data Exemplar](data/exemplar.md), [Data Timeline](data/timeline.md), and [Data Sampling](data/sampling.md) for the runtime data path.
- Finish with [Dataset Tests](tests/test-dataset.md) for the executable specification.
