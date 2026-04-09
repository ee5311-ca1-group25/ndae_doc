# test_checkpoint.py

Source path: `tests/test_checkpoint.py`

## System Under Test

- [__init__.py](../src/ndae/training/__init__.md)

## Fixtures And Helpers

- `_advance_to_boundary(trainer, *, n_steps=3)`

## Test Groups

- `save_checkpoint_writes_step_and_latest_layout`: `test_save_checkpoint_writes_step_and_latest_layout`
- `resume_checkpoint_round_trip_restores_model_optimizer_and_trainer_state`: `test_resume_checkpoint_round_trip_restores_model_optimizer_and_trainer_state`
- `load_resume_checkpoint`: `test_load_resume_checkpoint_rejects_non_resume_ready_meta`
- `load_resume_checkpoint_requires_flashlight_state`: `test_load_resume_checkpoint_requires_flashlight_state`
- `load_sample_checkpoint_accepts_non_resume_ready_checkpoint`: `test_load_sample_checkpoint_accepts_non_resume_ready_checkpoint`

## What Each Group Proves

- `save_checkpoint_writes_step_and_latest_layout` proves that the implementation still satisfies the contract exercised by `test_save_checkpoint_writes_step_and_latest_layout`.
- `resume_checkpoint_round_trip_restores_model_optimizer_and_trainer_state` proves that the implementation still satisfies the contract exercised by `test_resume_checkpoint_round_trip_restores_model_optimizer_and_trainer_state`.
- `load_resume_checkpoint` proves that the implementation still satisfies the contract exercised by `test_load_resume_checkpoint_rejects_non_resume_ready_meta`.
- `load_resume_checkpoint_requires_flashlight_state` proves that the implementation still satisfies the contract exercised by `test_load_resume_checkpoint_requires_flashlight_state`.
- `load_sample_checkpoint_accepts_non_resume_ready_checkpoint` proves that the implementation still satisfies the contract exercised by `test_load_sample_checkpoint_accepts_non_resume_ready_checkpoint`.

## Regression Intent

These tests are intended to catch behavior drift in the mirrored runtime paths, not just import-time failures.

## Remaining Gaps

The file only covers the explicit cases encoded in its test functions; full-sequence numerical drift still depends on broader smoke and integration coverage.

## Related Source Files

- [__init__.py](../src/ndae/training/__init__.md)
