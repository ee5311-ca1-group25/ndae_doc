# Rendering Postprocess

## Purpose

`src/ndae/rendering/postprocess.py` contains the small post-render helpers used
by the Lecture 3 svBRDF path.

These functions stay independent from BRDF evaluation so `renderer.py` can stay
focused on batching, geometry assembly, and the render entrypoint.

## Public API / key types

The module exposes:

- `tonemapping(img, gamma=2.2, eps=EPSILON)`
- `light_decay(distance)`
- `reinhard(img)`

These helpers are available from `ndae.rendering.postprocess`, the compatibility
layer `ndae.rendering.renderer`, and the top-level `ndae.rendering` package.

## Behavior and invariants

- `tonemapping` clamps into `[eps, 1.0]` and applies `pow(1 / gamma)`
- `light_decay` uses inverse-square falloff with the shared `EPSILON`
- `reinhard` provides the alternative `x / (1 + x)` mapping

The main renderer currently uses `light_decay` directly inside
`render_svbrdf`, while tests exercise `tonemapping` on rendered outputs.

## Related files

- `src/ndae/rendering/geometry.py`
- `src/ndae/rendering/__init__.py`
- `src/ndae/rendering/renderer.py`
- `tests/test_renderer.py`
