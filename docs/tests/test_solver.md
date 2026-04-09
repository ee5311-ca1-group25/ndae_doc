# test_solver.py

Source path: `tests/test_solver.py`

## System Under Test

- [odefunc.py](../src/ndae/models/odefunc.md)
- [trajectory.py](../src/ndae/models/trajectory.md)
- [unet.py](../src/ndae/models/unet.md)
- [__init__.py](../src/ndae/training/__init__.md)
- [solver.py](../src/ndae/training/solver.md)

## Fixtures And Helpers

- `make_trajectory_model()`

## Test Groups

- `solver_config_defaults_match_runtime_defaults`: `test_solver_config_defaults_match_runtime_defaults`
- `solver_config`: `test_solver_config_is_frozen`, `test_solver_config_is_exported_from_training_package`
- `rollout_result_exposes_fields`: `test_rollout_result_exposes_fields`
- `rollout_result`: `test_rollout_result_is_exported_from_training_package`
- `solve_rollout`: `test_solve_rollout_returns_rollout_result_with_expected_shapes`, `test_solve_rollout_zero_init_vector_field_keeps_state_nearly_static`, `test_solve_rollout_gradients_flow_to_wrapped_unet_parameters`, `test_solve_rollout_supports_configured_solver_methods`
- `solve_rollout_preserves_initial_state_and_records_times`: `test_solve_rollout_preserves_initial_state_and_records_times`
- `solve_rollout_final_state`: `test_solve_rollout_final_state_matches_last_state`
- `rollout_warmup`: `test_rollout_warmup_uses_warmup_window_times`, `test_rollout_warmup_rejects_non_warmup_window`
- `rollout_generation`: `test_rollout_generation_uses_generation_window_times`, `test_rollout_generation_rejects_non_generation_window`
- `rollout_stage_wrappers_preserve`: `test_rollout_stage_wrappers_preserve_zero_init_static_behavior`
- `rollout_generation_allows`: `test_rollout_generation_allows_gradient_flow`

## What Each Group Proves

- `solver_config_defaults_match_runtime_defaults` proves that the implementation still satisfies the contract exercised by `test_solver_config_defaults_match_runtime_defaults`.
- `solver_config` proves that the implementation still satisfies the contract exercised by `test_solver_config_is_frozen`, `test_solver_config_is_exported_from_training_package`.
- `rollout_result_exposes_fields` proves that the implementation still satisfies the contract exercised by `test_rollout_result_exposes_fields`.
- `rollout_result` proves that the implementation still satisfies the contract exercised by `test_rollout_result_is_exported_from_training_package`.
- `solve_rollout` proves that the implementation still satisfies the contract exercised by `test_solve_rollout_returns_rollout_result_with_expected_shapes`, `test_solve_rollout_zero_init_vector_field_keeps_state_nearly_static`, `test_solve_rollout_gradients_flow_to_wrapped_unet_parameters`.
- `solve_rollout_preserves_initial_state_and_records_times` proves that the implementation still satisfies the contract exercised by `test_solve_rollout_preserves_initial_state_and_records_times`.
- `solve_rollout_final_state` proves that the implementation still satisfies the contract exercised by `test_solve_rollout_final_state_matches_last_state`.
- `rollout_warmup` proves that the implementation still satisfies the contract exercised by `test_rollout_warmup_uses_warmup_window_times`, `test_rollout_warmup_rejects_non_warmup_window`.
- `rollout_generation` proves that the implementation still satisfies the contract exercised by `test_rollout_generation_uses_generation_window_times`, `test_rollout_generation_rejects_non_generation_window`.
- `rollout_stage_wrappers_preserve` proves that the implementation still satisfies the contract exercised by `test_rollout_stage_wrappers_preserve_zero_init_static_behavior`.
- `rollout_generation_allows` proves that the implementation still satisfies the contract exercised by `test_rollout_generation_allows_gradient_flow`.

## Regression Intent

These tests are intended to catch behavior drift in the mirrored runtime paths, not just import-time failures.

## Remaining Gaps

The file only covers the explicit cases encoded in its test functions; full-sequence numerical drift still depends on broader smoke and integration coverage.

## Related Source Files

- [odefunc.py](../src/ndae/models/odefunc.md)
- [trajectory.py](../src/ndae/models/trajectory.md)
- [unet.py](../src/ndae/models/unet.md)
- [__init__.py](../src/ndae/training/__init__.md)
- [solver.py](../src/ndae/training/solver.md)
