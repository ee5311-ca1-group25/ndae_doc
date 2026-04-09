# test_config.py

Source path: `tests/test_config.py`

## System Under Test

- [__init__.py](../src/ndae/config/__init__.md)
- [__init__.py](../src/ndae/rendering/__init__.md)

## Fixtures And Helpers

- `make_rendering_config(**overrides)`
- `make_config(*, root, exemplar='clay_solidifying', image_size=256, crop_size=128, n_frames=1, t_S=0.0, t_E=10.0, rendering=None)`
- `write_frame(path)`

## Test Groups

- `base_config`: `test_base_config_loads_into_dataclasses`
- `debug_config`: `test_debug_config_loads_without_dataset_validation`
- `to_dict`: `test_to_dict_returns_plain_dictionary_tree`
- `full_clay_config`: `test_full_clay_config_loads_without_dataset_validation`
- `full_clay_official_like_config`: `test_full_clay_official_like_config_loads_without_dataset_validation`
- `load_config`: `test_load_config_supports_default_rendering_block`, `test_load_config_rejects_unknown_keys`, `test_load_config_rejects_legacy_model_n_aug_channels`, `test_load_config_rejects_invalid_renderer_type`, `test_load_config_rejects_invalid_light_xy_position`, `test_load_config_rejects_unknown_train_keys`, `test_load_config_rejects_explicit_data_t_i_key`
- `validate_config`: `test_validate_config_rejects_invalid_semantics`, `test_validate_config_rejects_missing_exemplar_directory`, `test_validate_config_rejects_excessive_frame_count`, `test_validate_config_rejects_invalid_rendering_channel_count`, `test_validate_config_rejects_non_finite_light_xy_position`, `test_validate_config_rejects_invalid_timeline_ordering`, `test_validate_config_rejects_n_init_iter_greater_than_n_iter`, `test_validate_config_rejects_non_positive_train_runtime_fields`, `test_validate_config_rejects_empty_resume_from`, `test_validate_config_rejects_invalid_phase1_fields`, `test_validate_config_rejects_scheduler_min_lr_above_lr`
- `validate_config_prefers_manifest_selected_files_over_directory_count`: `test_validate_config_prefers_manifest_selected_files_over_directory_count`
- `load_config_canonicalizes_uppercase_loss_type`: `test_load_config_canonicalizes_uppercase_loss_type`

## What Each Group Proves

- `base_config` proves that the implementation still satisfies the contract exercised by `test_base_config_loads_into_dataclasses`.
- `debug_config` proves that the implementation still satisfies the contract exercised by `test_debug_config_loads_without_dataset_validation`.
- `to_dict` proves that the implementation still satisfies the contract exercised by `test_to_dict_returns_plain_dictionary_tree`.
- `full_clay_config` proves that the implementation still satisfies the contract exercised by `test_full_clay_config_loads_without_dataset_validation`.
- `full_clay_official_like_config` proves that the implementation still satisfies the contract exercised by `test_full_clay_official_like_config_loads_without_dataset_validation`.
- `load_config` proves that the implementation still satisfies the contract exercised by `test_load_config_supports_default_rendering_block`, `test_load_config_rejects_unknown_keys`, `test_load_config_rejects_legacy_model_n_aug_channels`.
- `validate_config` proves that the implementation still satisfies the contract exercised by `test_validate_config_rejects_invalid_semantics`, `test_validate_config_rejects_missing_exemplar_directory`, `test_validate_config_rejects_excessive_frame_count`.
- `validate_config_prefers_manifest_selected_files_over_directory_count` proves that the implementation still satisfies the contract exercised by `test_validate_config_prefers_manifest_selected_files_over_directory_count`.
- `load_config_canonicalizes_uppercase_loss_type` proves that the implementation still satisfies the contract exercised by `test_load_config_canonicalizes_uppercase_loss_type`.

## Regression Intent

These tests are intended to catch behavior drift in the mirrored runtime paths, not just import-time failures.

## Remaining Gaps

The file only covers the explicit cases encoded in its test functions; full-sequence numerical drift still depends on broader smoke and integration coverage.

## Related Source Files

- [__init__.py](../src/ndae/config/__init__.md)
- [__init__.py](../src/ndae/rendering/__init__.md)
