# test_schedule.py

Source path: `tests/test_schedule.py`

## System Under Test

- [schedule.py](../src/ndae/training/schedule.md)

## Fixtures And Helpers

- No file-local fixtures or helpers are declared; this file relies on inline test bodies or shared helpers.

## Test Groups

- `stage_config_defaults_match_runtime_defaults`: `test_stage_config_defaults_match_runtime_defaults`
- `stage_config`: `test_stage_config_rejects_equal_t_init_and_t_start`, `test_stage_config_rejects_t_start_not_before_t_end`, `test_stage_config_rejects_refresh_rate_smaller_than_two`
- `rollout_window_exposes_fields`: `test_rollout_window_exposes_fields`
- `refresh_schedule`: `test_refresh_schedule_returns_warmup_window_on_cycle_start`, `test_refresh_schedule_returns_generation_window_between_refresh_steps`, `test_refresh_schedule_is_deterministic_with_seeded_generator`, `test_refresh_schedule_rejects_generation_before_warmup`
- `refresh_schedule_generation`: `test_refresh_schedule_generation_uses_carry_time_as_t0`
- `refresh_schedule_generation_t1`: `test_refresh_schedule_generation_t1_is_strictly_increasing_within_cycle`
- `refresh_schedule_generation_cycle_covers_generation_interval`: `test_refresh_schedule_generation_cycle_covers_generation_interval`
- `refresh_schedule_resamples`: `test_refresh_schedule_resamples_for_next_cycle`

## What Each Group Proves

- `stage_config_defaults_match_runtime_defaults` proves that the implementation still satisfies the contract exercised by `test_stage_config_defaults_match_runtime_defaults`.
- `stage_config` proves that the implementation still satisfies the contract exercised by `test_stage_config_rejects_equal_t_init_and_t_start`, `test_stage_config_rejects_t_start_not_before_t_end`, `test_stage_config_rejects_refresh_rate_smaller_than_two`.
- `rollout_window_exposes_fields` proves that the implementation still satisfies the contract exercised by `test_rollout_window_exposes_fields`.
- `refresh_schedule` proves that the implementation still satisfies the contract exercised by `test_refresh_schedule_returns_warmup_window_on_cycle_start`, `test_refresh_schedule_returns_generation_window_between_refresh_steps`, `test_refresh_schedule_is_deterministic_with_seeded_generator`.
- `refresh_schedule_generation` proves that the implementation still satisfies the contract exercised by `test_refresh_schedule_generation_uses_carry_time_as_t0`.
- `refresh_schedule_generation_t1` proves that the implementation still satisfies the contract exercised by `test_refresh_schedule_generation_t1_is_strictly_increasing_within_cycle`.
- `refresh_schedule_generation_cycle_covers_generation_interval` proves that the implementation still satisfies the contract exercised by `test_refresh_schedule_generation_cycle_covers_generation_interval`.
- `refresh_schedule_resamples` proves that the implementation still satisfies the contract exercised by `test_refresh_schedule_resamples_for_next_cycle`.

## Regression Intent

These tests are intended to catch behavior drift in the mirrored runtime paths, not just import-time failures.

## Remaining Gaps

The file only covers the explicit cases encoded in its test functions; full-sequence numerical drift still depends on broader smoke and integration coverage.

## Related Source Files

- [schedule.py](../src/ndae/training/schedule.md)
