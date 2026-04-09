# test_renderer.py

Source path: `tests/test_renderer.py`

## System Under Test

- [__init__.py](../src/ndae/rendering/__init__.md)

## Fixtures And Helpers

- No file-local fixtures or helpers are declared; this file relies on inline test bodies or shared helpers.

## Test Groups

- `l2i_i2l_inverse`: `test_l2i_i2l_inverse`
- `split_latent_maps`: `test_split_latent_maps_returns_brdf_and_height_for_chw`, `test_split_latent_maps_supports_leading_batch_dims`, `test_split_latent_maps_rejects_invalid_rank`, `test_split_latent_maps_rejects_non_positive_channel_counts`, `test_split_latent_maps_rejects_insufficient_channels`
- `split_latent_maps_discards_aug_channels`: `test_split_latent_maps_discards_aug_channels`
- `clip_maps`: `test_clip_maps_range`
- `height_to_normal_flat`: `test_height_to_normal_flat`
- `height_to_normal`: `test_height_to_normal_gradient_x`, `test_height_to_normal_supports_leading_batch_dims`, `test_height_to_normal_rejects_invalid_rank`, `test_height_to_normal_rejects_non_singleton_channel_dim`, `test_height_to_normal_backward`
- `lambertian`: `test_lambertian_center_pixel`
- `create_meshgrid`: `test_create_meshgrid_center_and_axes`
- `render_diffuse_only`: `test_render_diffuse_only_center_pixel`
- `diffuse_cook_torrance_roughness_monotonicity`: `test_diffuse_cook_torrance_roughness_monotonicity`
- `render_svbrdf_crop`: `test_render_svbrdf_crop_matches_full`
- `render_svbrdf_explicit_positions_match_region_crop`: `test_render_svbrdf_explicit_positions_match_region_crop`
- `render_svbrdf`: `test_render_svbrdf_backward_smoke`

## What Each Group Proves

- `l2i_i2l_inverse` proves that the implementation still satisfies the contract exercised by `test_l2i_i2l_inverse`.
- `split_latent_maps` proves that the implementation still satisfies the contract exercised by `test_split_latent_maps_returns_brdf_and_height_for_chw`, `test_split_latent_maps_supports_leading_batch_dims`, `test_split_latent_maps_rejects_invalid_rank`.
- `split_latent_maps_discards_aug_channels` proves that the implementation still satisfies the contract exercised by `test_split_latent_maps_discards_aug_channels`.
- `clip_maps` proves that the implementation still satisfies the contract exercised by `test_clip_maps_range`.
- `height_to_normal_flat` proves that the implementation still satisfies the contract exercised by `test_height_to_normal_flat`.
- `height_to_normal` proves that the implementation still satisfies the contract exercised by `test_height_to_normal_gradient_x`, `test_height_to_normal_supports_leading_batch_dims`, `test_height_to_normal_rejects_invalid_rank`.
- `lambertian` proves that the implementation still satisfies the contract exercised by `test_lambertian_center_pixel`.
- `create_meshgrid` proves that the implementation still satisfies the contract exercised by `test_create_meshgrid_center_and_axes`.
- `render_diffuse_only` proves that the implementation still satisfies the contract exercised by `test_render_diffuse_only_center_pixel`.
- `diffuse_cook_torrance_roughness_monotonicity` proves that the implementation still satisfies the contract exercised by `test_diffuse_cook_torrance_roughness_monotonicity`.
- `render_svbrdf_crop` proves that the implementation still satisfies the contract exercised by `test_render_svbrdf_crop_matches_full`.
- `render_svbrdf_explicit_positions_match_region_crop` proves that the implementation still satisfies the contract exercised by `test_render_svbrdf_explicit_positions_match_region_crop`.
- `render_svbrdf` proves that the implementation still satisfies the contract exercised by `test_render_svbrdf_backward_smoke`.

## Regression Intent

These tests are intended to catch behavior drift in the mirrored runtime paths, not just import-time failures.

## Remaining Gaps

The file only covers the explicit cases encoded in its test functions; full-sequence numerical drift still depends on broader smoke and integration coverage.

## Related Source Files

- [__init__.py](../src/ndae/rendering/__init__.md)
