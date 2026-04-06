# Rendering Renderer

## Purpose

The core differentiable svBRDF renderer used by Lecture 3 is now split across:

- `src/ndae/rendering/geometry.py`
- `src/ndae/rendering/brdf.py`
- `src/ndae/rendering/postprocess.py`
- `src/ndae/rendering/renderer.py`

This keeps the public runtime entrypoint under `renderer.py`, while moving the
geometric setup and BRDF terms into smaller responsibility-focused modules.

- `geometry.py` contains `Camera`, `FlashLight`, normalization helpers,
  meshgrid generation, direction computation, and tangent-space projection.
- `brdf.py` contains Lambertian / GGX / Smith / Fresnel / Cook-Torrance terms
  plus BRDF-map unpack helpers.
- `postprocess.py` contains `light_decay`, `tonemapping`, and `reinhard`.
- `renderer.py` keeps `render_svbrdf`, batching checks, crop handling, and
  compatibility re-exports for the lower-level symbols.

## Public API / key types

The current renderer entry module exposes:

- `EPSILON`
- `Camera`
- `FlashLight`
- `normalize(v)`
- `channelwise_normalize(m)`
- `create_meshgrid(height, width, camera, device=None)`
- `compute_directions(positions, camera, flash_light)`
- `localize(vec, normal)`
- `localize_wiwo(wi, wo, normal)`
- `lambertian(wi, diffuse)`
- `distribution_ggx(h, alpha_u, alpha_v)`
- `smith_g1_ggx(v, alpha_u, alpha_v)`
- `geometry_smith(wi, wo, alpha_u, alpha_v)`
- `fresnel_schlick(cos_theta, f0)`
- `cook_torrance(wi, wo, specular, alpha_u, alpha_v)`
- `diffuse_cook_torrance(...)`
- `diffuse_iso_cook_torrance(...)`
- `unpack_brdf_diffuse_cook_torrance(brdf_maps)`
- `unpack_brdf_diffuse_iso_cook_torrance(brdf_maps)`
- `render_svbrdf(...)`
- `tonemapping(img, gamma=2.2, eps=EPSILON)`
- `light_decay(distance)`
- `reinhard(img)`

These symbols remain available from `ndae.rendering.renderer` and are now also
re-exported through the top-level `ndae.rendering` package.

## Behavior and invariants

The renderer currently targets the Lecture 3 svBRDF path:

- runtime inputs to `render_svbrdf` support `CHW` and `BCHW`
- crop rendering is supported through `region=(top, left, crop_h, crop_w)`
- crop mode always builds the meshgrid in full-image coordinates before slicing
- invalid local incident/outgoing directions are masked to zero
- `render_svbrdf` returns linear-space radiance; tone mapping stays explicit

Geometry conventions:

- the image plane lies on `z = 0`
- the camera is located at `(0, 0, distance)`
- the flash light is located at `(light_x, light_y, distance)`
- the `y` axis is flipped relative to image rows so world space remains
  right-handed

BRDF coverage in the current implementation:

- anisotropic diffuse + Cook-Torrance
- isotropic diffuse + Cook-Torrance via `alpha_u = alpha_v = alpha`

The registry still contains more renderer names for configuration purposes, but
their runtime branches are not wired up in this phase.

## Error handling

`render_svbrdf` raises `ValueError` when:

- BRDF maps or normal maps are not `CHW` or `BCHW`
- the normal map channel count is not 3
- batch sizes or spatial sizes do not match
- `region` is provided without `full_height` and `full_width`
- the crop shape is invalid or does not match the provided input map size

`create_meshgrid` also rejects non-positive spatial sizes.

## Tests / validation

`tests/test_renderer.py` verifies:

- `lambertian` matches the center-pixel `1 / pi` case
- `create_meshgrid` produces the expected axis orientation
- diffuse-only rendering matches the expected center-pixel value
- rougher specular lobes reduce center-pixel highlight intensity
- crop rendering matches slicing the full render
- gradients backpropagate from tone-mapped output to latent input

## Related files

- `src/ndae/rendering/maps.py`
- `src/ndae/rendering/normal.py`
- `src/ndae/rendering/geometry.py`
- `src/ndae/rendering/brdf.py`
- `src/ndae/rendering/postprocess.py`
- `src/ndae/rendering/renderer.py`
- `src/ndae/rendering/__init__.py`
- `tests/test_renderer.py`
- `course/lecture03.md`
