# test_dataset.py

Source path: `tests/test_dataset.py`

## System Under Test

- [__init__.py](../src/ndae/config/__init__.md)
- [exemplar.py](../src/ndae/data/exemplar.md)
- [sampling.py](../src/ndae/data/sampling.md)
- [timeline.py](../src/ndae/data/timeline.md)

## Fixtures And Helpers

- `write_image(path, *, size, color)`

## Test Groups

- `timeline_from_config`: `test_timeline_from_config`
- `timeline_properties`: `test_timeline_properties`
- `timeline_round_trip_default_config`: `test_timeline_round_trip_default_config`
- `timeline_round_trip_nonzero_t_start`: `test_timeline_round_trip_nonzero_t_start`
- `timeline_time_to_frame_clamps_before_start_and_after_end`: `test_timeline_time_to_frame_clamps_before_start_and_after_end`
- `timeline_frame_to_time`: `test_timeline_frame_to_time_rejects_out_of_range_index`
- `timeline`: `test_timeline_rejects_invalid_constructor_args`
- `exemplar_dataset_from_config`: `test_exemplar_dataset_from_config_loads_manifest_selected_frames`, `test_exemplar_dataset_from_config_resolves_relative_root_with_base_dir`
- `exemplar_dataset`: `test_exemplar_dataset_returns_expected_shape_dtype_and_range`, `test_exemplar_dataset_without_manifest_falls_back_to_sorted_filenames`, `test_exemplar_dataset_rejects_insufficient_available_frames`, `test_exemplar_dataset_supports_negative_index_and_rejects_out_of_range_index`
- `exemplar_dataset_preserves_manifest_order`: `test_exemplar_dataset_preserves_manifest_order`
- `exemplar_dataset_uniformly_samples`: `test_exemplar_dataset_uniformly_samples_when_more_images_than_requested`
- `exemplar_dataset_single_frame_path`: `test_exemplar_dataset_single_frame_path_uses_first_frame`
- `random_crop_shape_and_determinism`: `test_random_crop_shape_and_determinism`
- `random_crop_preserves_spatial_continuity`: `test_random_crop_preserves_spatial_continuity`
- `random_crop`: `test_random_crop_rejects_invalid_shape_or_size`
- `random_take_shape_and_determinism`: `test_random_take_shape_and_determinism`
- `random_take_preserves_values`: `test_random_take_preserves_values`
- `random_take_destroys_spatial_structure`: `test_random_take_destroys_spatial_structure`
- `random_take`: `test_random_take_rejects_invalid_shape_or_sample_size`
- `sample_random_crop_spec_and_apply_are_deterministic`: `test_sample_random_crop_spec_and_apply_are_deterministic`
- `sample_random_take_spec_and_apply_are_deterministic`: `test_sample_random_take_spec_and_apply_are_deterministic`
- `sample_random_take_spec`: `test_sample_random_take_spec_uses_full_image_randperm_prefix`
- `apply_take_spec`: `test_apply_take_spec_uses_indices_directly`
- `stratified_uniform`: `test_stratified_uniform_returns_in_range_ordered_samples`, `test_stratified_uniform_is_deterministic_with_seed`, `test_stratified_uniform_rejects_invalid_arguments`
- `sample_frame_indices`: `test_sample_frame_indices_returns_zero_for_refresh_step`, `test_sample_frame_indices_is_deterministic_with_seed`, `test_sample_frame_indices_rejects_invalid_arguments`
- `sample_frame_indices_samples_within_expected_stratum`: `test_sample_frame_indices_samples_within_expected_stratum`

## What Each Group Proves

- `timeline_from_config` proves that the implementation still satisfies the contract exercised by `test_timeline_from_config`.
- `timeline_properties` proves that the implementation still satisfies the contract exercised by `test_timeline_properties`.
- `timeline_round_trip_default_config` proves that the implementation still satisfies the contract exercised by `test_timeline_round_trip_default_config`.
- `timeline_round_trip_nonzero_t_start` proves that the implementation still satisfies the contract exercised by `test_timeline_round_trip_nonzero_t_start`.
- `timeline_time_to_frame_clamps_before_start_and_after_end` proves that the implementation still satisfies the contract exercised by `test_timeline_time_to_frame_clamps_before_start_and_after_end`.
- `timeline_frame_to_time` proves that the implementation still satisfies the contract exercised by `test_timeline_frame_to_time_rejects_out_of_range_index`.
- `timeline` proves that the implementation still satisfies the contract exercised by `test_timeline_rejects_invalid_constructor_args`.
- `exemplar_dataset_from_config` proves that the implementation still satisfies the contract exercised by `test_exemplar_dataset_from_config_loads_manifest_selected_frames`, `test_exemplar_dataset_from_config_resolves_relative_root_with_base_dir`.
- `exemplar_dataset` proves that the implementation still satisfies the contract exercised by `test_exemplar_dataset_returns_expected_shape_dtype_and_range`, `test_exemplar_dataset_without_manifest_falls_back_to_sorted_filenames`, `test_exemplar_dataset_rejects_insufficient_available_frames`.
- `exemplar_dataset_preserves_manifest_order` proves that the implementation still satisfies the contract exercised by `test_exemplar_dataset_preserves_manifest_order`.
- `exemplar_dataset_uniformly_samples` proves that the implementation still satisfies the contract exercised by `test_exemplar_dataset_uniformly_samples_when_more_images_than_requested`.
- `exemplar_dataset_single_frame_path` proves that the implementation still satisfies the contract exercised by `test_exemplar_dataset_single_frame_path_uses_first_frame`.
- `random_crop_shape_and_determinism` proves that the implementation still satisfies the contract exercised by `test_random_crop_shape_and_determinism`.
- `random_crop_preserves_spatial_continuity` proves that the implementation still satisfies the contract exercised by `test_random_crop_preserves_spatial_continuity`.
- `random_crop` proves that the implementation still satisfies the contract exercised by `test_random_crop_rejects_invalid_shape_or_size`.
- `random_take_shape_and_determinism` proves that the implementation still satisfies the contract exercised by `test_random_take_shape_and_determinism`.
- `random_take_preserves_values` proves that the implementation still satisfies the contract exercised by `test_random_take_preserves_values`.
- `random_take_destroys_spatial_structure` proves that the implementation still satisfies the contract exercised by `test_random_take_destroys_spatial_structure`.
- `random_take` proves that the implementation still satisfies the contract exercised by `test_random_take_rejects_invalid_shape_or_sample_size`.
- `sample_random_crop_spec_and_apply_are_deterministic` proves that the implementation still satisfies the contract exercised by `test_sample_random_crop_spec_and_apply_are_deterministic`.
- `sample_random_take_spec_and_apply_are_deterministic` proves that the implementation still satisfies the contract exercised by `test_sample_random_take_spec_and_apply_are_deterministic`.
- `sample_random_take_spec` proves that the implementation still satisfies the contract exercised by `test_sample_random_take_spec_uses_full_image_randperm_prefix`.
- `apply_take_spec` proves that the implementation still satisfies the contract exercised by `test_apply_take_spec_uses_indices_directly`.
- `stratified_uniform` proves that the implementation still satisfies the contract exercised by `test_stratified_uniform_returns_in_range_ordered_samples`, `test_stratified_uniform_is_deterministic_with_seed`, `test_stratified_uniform_rejects_invalid_arguments`.
- `sample_frame_indices` proves that the implementation still satisfies the contract exercised by `test_sample_frame_indices_returns_zero_for_refresh_step`, `test_sample_frame_indices_is_deterministic_with_seed`, `test_sample_frame_indices_rejects_invalid_arguments`.
- `sample_frame_indices_samples_within_expected_stratum` proves that the implementation still satisfies the contract exercised by `test_sample_frame_indices_samples_within_expected_stratum`.

## Regression Intent

These tests are intended to catch behavior drift in the mirrored runtime paths, not just import-time failures.

## Remaining Gaps

The file only covers the explicit cases encoded in its test functions; full-sequence numerical drift still depends on broader smoke and integration coverage.

## Related Source Files

- [__init__.py](../src/ndae/config/__init__.md)
- [exemplar.py](../src/ndae/data/exemplar.md)
- [sampling.py](../src/ndae/data/sampling.md)
- [timeline.py](../src/ndae/data/timeline.md)
