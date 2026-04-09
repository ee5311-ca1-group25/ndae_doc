# brdf.py

Source path: `src/ndae/rendering/brdf.py`

## Role

This file belongs to the `src/ndae/rendering` slice of the NDAE repository. Cook-Torrance BRDF terms and BRDF-map unpack helpers.

## Where This File Sits In The Pipeline

This file is one focused step in the `src/ndae/rendering` slice of the NDAE runtime. In day-to-day execution it interacts most directly with neighboring modules such as `geometry.py`.

## Inputs, Outputs, And Tensor Shapes

- This file mostly moves structured Python objects or runtime state rather than introducing a new tensor convention of its own.

## Implementation Walkthrough

The file is built from focused helpers rather than one monolithic routine. That makes each contract easier to test and lets neighboring modules reuse only the pieces they need.

Branches in this file usually separate runtime modes or reject invalid inputs early so deeper numerical code can stay cleaner.

## Function And Class Deep Dive

### _channel_dot

Signature: `_channel_dot(a, b)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `_channel_dot(a, b)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `sum` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `sum` without redoing the same validation or reshaping work.

### lambertian

Signature: `lambertian(wi, diffuse)`

Purpose: Lambertian diffuse term with the cosine factor included.

Expected inputs and outputs:
- The callable boundary is `lambertian(wi, diffuse)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `clamp, narrow` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- Clamping is used as a numerical guardrail so later formulas stay inside the domain they were designed for.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `clamp, narrow` without redoing the same validation or reshaping work.

### distribution_ggx

Signature: `distribution_ggx(h, alpha_u, alpha_v)`

Purpose: Anisotropic GGX normal distribution function.

Expected inputs and outputs:
- The callable boundary is `distribution_ggx(h, alpha_u, alpha_v)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `clamp, narrow` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- Clamping is used as a numerical guardrail so later formulas stay inside the domain they were designed for.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `clamp, narrow` without redoing the same validation or reshaping work.

### smith_g1_ggx

Signature: `smith_g1_ggx(v, alpha_u, alpha_v)`

Purpose: Anisotropic Smith G1 masking-shadowing term.

Expected inputs and outputs:
- The callable boundary is `smith_g1_ggx(v, alpha_u, alpha_v)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `clamp, narrow, sqrt` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- Clamping is used as a numerical guardrail so later formulas stay inside the domain they were designed for.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `clamp, narrow, sqrt` without redoing the same validation or reshaping work.

### geometry_smith

Signature: `geometry_smith(wi, wo, alpha_u, alpha_v)`

Purpose: Separable Smith masking-shadowing term.

Expected inputs and outputs:
- The callable boundary is `geometry_smith(wi, wo, alpha_u, alpha_v)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `smith_g1_ggx` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `smith_g1_ggx` without redoing the same validation or reshaping work.

### fresnel_schlick

Signature: `fresnel_schlick(cos_theta, f0)`

Purpose: Schlick Fresnel approximation.

Expected inputs and outputs:
- The callable boundary is `fresnel_schlick(cos_theta, f0)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `clamp, pow` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- Clamping is used as a numerical guardrail so later formulas stay inside the domain they were designed for.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `clamp, pow` without redoing the same validation or reshaping work.

### cook_torrance

Signature: `cook_torrance(wi, wo, specular, alpha_u, alpha_v)`

Purpose: Cosine-weighted anisotropic Cook-Torrance specular term.

Expected inputs and outputs:
- The callable boundary is `cook_torrance(wi, wo, specular, alpha_u, alpha_v)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `_channel_dot, channelwise_normalize, clamp, distribution_ggx, fresnel_schlick, geometry_smith` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- Clamping is used as a numerical guardrail so later formulas stay inside the domain they were designed for.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `channelwise_normalize, clamp, distribution_ggx, fresnel_schlick, geometry_smith` without redoing the same validation or reshaping work.

### diffuse_cook_torrance

Signature: `diffuse_cook_torrance(wi, wo, diffuse, specular, alpha_u, alpha_v)`

Purpose: Diffuse plus anisotropic Cook-Torrance specular.

Expected inputs and outputs:
- The callable boundary is `diffuse_cook_torrance(wi, wo, diffuse, specular, alpha_u, alpha_v)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `cook_torrance, lambertian` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `cook_torrance, lambertian` without redoing the same validation or reshaping work.

### diffuse_iso_cook_torrance

Signature: `diffuse_iso_cook_torrance(wi, wo, diffuse, specular, alpha)`

Purpose: Diffuse plus isotropic Cook-Torrance specular.

Expected inputs and outputs:
- The callable boundary is `diffuse_iso_cook_torrance(wi, wo, diffuse, specular, alpha)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `diffuse_cook_torrance` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `diffuse_cook_torrance` without redoing the same validation or reshaping work.

### unpack_brdf_diffuse_cook_torrance

Signature: `unpack_brdf_diffuse_cook_torrance(brdf_maps)`

Purpose: Unpack diffuse/specular/aniso-roughness parameters.

Expected inputs and outputs:
- The callable boundary is `unpack_brdf_diffuse_cook_torrance(brdf_maps)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `narrow` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `narrow` without redoing the same validation or reshaping work.

### unpack_brdf_diffuse_iso_cook_torrance

Signature: `unpack_brdf_diffuse_iso_cook_torrance(brdf_maps)`

Purpose: Unpack diffuse/specular/isotropic-roughness parameters.

Expected inputs and outputs:
- The callable boundary is `unpack_brdf_diffuse_iso_cook_torrance(brdf_maps)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `narrow` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `narrow` without redoing the same validation or reshaping work.

## Formula Mapping

- `lambertian = diffuse / pi * max(wi_z, 0)` includes the cosine term directly.
- `distribution_ggx` computes the anisotropic GGX normal distribution using `alpha_u`, `alpha_v`, and the half vector components.
- `geometry_smith = smith_g1_ggx(wi) * smith_g1_ggx(wo)` uses a separable masking-shadowing term.
- `fresnel_schlick = f0 + (1 - f0) * (1 - cos_theta)^5`.
- `cook_torrance = D * G * F / (4 * max(wo_z, eps))` after constructing `h = normalize(wi + wo)`.

## Design Decisions

- Split geometry, BRDF terms, postprocess, and renderer assembly so each numerical layer can be validated independently.
- Prefer pure tensor helpers in the math-heavy path to keep gradients transparent.

## Common Failure Modes

- There are no custom guard clauses in this file; failures mostly come from imported runtime code or invalid upstream tensors.

## How This Connects To Neighboring Files

- [geometry.py](geometry.md) supplies or consumes part of this file's contract.

## Related Tests

- [test_package_layout.py](../../../tests/test_package_layout.md)
- [test_trainer.py](../../../tests/test_trainer.md)
- [test_smoke.py](../../../tests/test_smoke.md)
- [test_renderer.py](../../../tests/test_renderer.md)
- [test_losses.py](../../../tests/test_losses.md)
- [test_download_svbrdf_mini.py](../../../tests/test_download_svbrdf_mini.md)
