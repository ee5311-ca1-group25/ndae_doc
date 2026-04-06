# Implementation Overview

This section documents the files that implement the current NDAE slice:
configuration, data loading, and the early rendering helper layers from Lecture 3.

The goal of the current implementation is to make three paths concrete:

- parse and validate the config tree, including rendering metadata
- load exemplar frames and map between discrete frames and continuous ODE time
- split latent states into BRDF maps and height maps, then convert height maps
  into world-space normals before later rendering phases

These pages are implementation references. They describe code behavior and invariants, not the full theory from the course notes.

## Current implementation slice

This slice connects the following modules:

- `src/ndae/config/schema.py`
- `src/ndae/config/_parsing.py`
- `src/ndae/config/validation.py`
- `configs/base.yaml`
- `src/ndae/rendering/__init__.py`
- `src/ndae/rendering/maps.py`
- `src/ndae/rendering/normal.py`
- `src/ndae/data/exemplar.py`
- `src/ndae/data/timeline.py`
- `src/ndae/data/sampling.py`
- `tests/test_renderer.py`
- `tests/test_dataset.py`

The flow is:

1. Load `configs/base.yaml` into dataclasses, including `RenderingConfig`.
2. Validate dataset paths, manifest contents, frame counts, timeline ordering, and renderer metadata.
3. Load exemplar images into a `[N, 3, H, W]` tensor.
4. Build a `Timeline` object for frame/time conversion.
5. Use sampling helpers for local crops, shuffled pixel samples, and online-training frame selection.
6. Use `split_latent_maps` and `clip_maps` to prepare latent states for rendering.
7. Use `height_to_normal` to convert height channels into `(..., 3, H, W)` normal maps.
8. Re-export data and rendering helpers through their package entrypoints where applicable.
9. Lock the behavior down with focused config, dataset, package, smoke, and renderer-helper tests.

## Reading guide

- Start with [Config Schema](config/schema.md) and [Config Parsing](config/parsing.md) to understand how rendering and timeline fields enter the program.
- Read [Config Validation](config/validation.md) and [Base Config](config/base-config.md) to see how the mini dataset defaults and rendering metadata are checked.
- Read [Rendering Maps](rendering/maps.md) for the latent split/value-mapping layer introduced in Lecture 3.
- Read [Rendering Normal](rendering/normal.md) for the height-to-normal conversion layer.
- Read [Data Exemplar](data/exemplar.md), [Data Timeline](data/timeline.md), and [Data Sampling](data/sampling.md) for the runtime data path.
- Finish with [Renderer Tests](tests/test-renderer.md) and [Dataset Tests](tests/test-dataset.md) for the executable specifications.
