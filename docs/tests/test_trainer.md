# test_trainer.py

Source path: `tests/test_trainer.py`

## System Under Test

- [__init__.py](../src/ndae/config/__init__.md)
- [__init__.py](../src/ndae/data/__init__.md)
- [runtime.py](../src/ndae/evaluation/runtime.md)
- [__init__.py](../src/ndae/models/__init__.md)
- [__init__.py](../src/ndae/rendering/__init__.md)
- [__init__.py](../src/ndae/training/__init__.md)
- [target_sampling.py](../src/ndae/training/target_sampling.md)
- [trainer.py](../src/ndae/training/trainer.md)

## Fixtures And Helpers

- `make_trainer(tmp_path, *, batch_size=1, n_iter=3, n_init_iter=1, log_every=1, loss_type='SW', n_loss_crops=2, overflow_weight=100.0, init_height_weight=1.0, eval_every=500, scheduler_factor=0.5, scheduler_patience_evals=5, scheduler_min_lr=0.0001)`

## Test Groups

- `trainer_single_step_updates_parameters`: `test_trainer_single_step_updates_parameters`
- `trainer_switches_stage_after_n_init_iter`: `test_trainer_switches_stage_after_n_init_iter`
- `trainer`: `test_trainer_uses_distinct_init_and_local_stage_configs`
- `trainer_detaches_and_advances_carry_state`: `test_trainer_detaches_and_advances_carry_state`
- `trainer_run_writes_metrics_jsonl`: `test_trainer_run_writes_metrics_jsonl`
- `trainer_init_stage`: `test_trainer_init_stage_uses_random_take_specs`
- `trainer_local_stage`: `test_trainer_local_stage_uses_random_crop_specs`, `test_trainer_local_stage_supports_gram_loss`
- `trainer_multicrop`: `test_trainer_multicrop_uses_all_samples`
- `render_sample`: `test_render_sample_uses_exemplar_image_size_for_positions`
- `trainer_init_loss_includes_height_and_weighted_overflow`: `test_trainer_init_loss_includes_height_and_weighted_overflow`
- `normalize`: `test_normalize_gradients_scales_nonzero_grads_and_keeps_zero_grads_finite`
- `run_triggers_eval_at_iteration`: `test_run_triggers_eval_at_iteration_zero_watershed_and_period`
- `init_eval_does_not_step_scheduler`: `test_init_eval_does_not_step_scheduler`
- `local_eval_steps_scheduler_and_reports_inference_loss`: `test_local_eval_steps_scheduler_and_reports_inference_loss`
- `enter_local_stage_resets_scheduler`: `test_enter_local_stage_resets_scheduler`
- `run_invokes_eval_callback_only_on_eval_steps`: `test_run_invokes_eval_callback_only_on_eval_steps`

## What Each Group Proves

- `trainer_single_step_updates_parameters` proves that the implementation still satisfies the contract exercised by `test_trainer_single_step_updates_parameters`.
- `trainer_switches_stage_after_n_init_iter` proves that the implementation still satisfies the contract exercised by `test_trainer_switches_stage_after_n_init_iter`.
- `trainer` proves that the implementation still satisfies the contract exercised by `test_trainer_uses_distinct_init_and_local_stage_configs`.
- `trainer_detaches_and_advances_carry_state` proves that the implementation still satisfies the contract exercised by `test_trainer_detaches_and_advances_carry_state`.
- `trainer_run_writes_metrics_jsonl` proves that the implementation still satisfies the contract exercised by `test_trainer_run_writes_metrics_jsonl`.
- `trainer_init_stage` proves that the implementation still satisfies the contract exercised by `test_trainer_init_stage_uses_random_take_specs`.
- `trainer_local_stage` proves that the implementation still satisfies the contract exercised by `test_trainer_local_stage_uses_random_crop_specs`, `test_trainer_local_stage_supports_gram_loss`.
- `trainer_multicrop` proves that the implementation still satisfies the contract exercised by `test_trainer_multicrop_uses_all_samples`.
- `render_sample` proves that the implementation still satisfies the contract exercised by `test_render_sample_uses_exemplar_image_size_for_positions`.
- `trainer_init_loss_includes_height_and_weighted_overflow` proves that the implementation still satisfies the contract exercised by `test_trainer_init_loss_includes_height_and_weighted_overflow`.
- `normalize` proves that the implementation still satisfies the contract exercised by `test_normalize_gradients_scales_nonzero_grads_and_keeps_zero_grads_finite`.
- `run_triggers_eval_at_iteration` proves that the implementation still satisfies the contract exercised by `test_run_triggers_eval_at_iteration_zero_watershed_and_period`.
- `init_eval_does_not_step_scheduler` proves that the implementation still satisfies the contract exercised by `test_init_eval_does_not_step_scheduler`.
- `local_eval_steps_scheduler_and_reports_inference_loss` proves that the implementation still satisfies the contract exercised by `test_local_eval_steps_scheduler_and_reports_inference_loss`.
- `enter_local_stage_resets_scheduler` proves that the implementation still satisfies the contract exercised by `test_enter_local_stage_resets_scheduler`.
- `run_invokes_eval_callback_only_on_eval_steps` proves that the implementation still satisfies the contract exercised by `test_run_invokes_eval_callback_only_on_eval_steps`.

## Regression Intent

These tests are intended to catch behavior drift in the mirrored runtime paths, not just import-time failures.

## Remaining Gaps

The file only covers the explicit cases encoded in its test functions; full-sequence numerical drift still depends on broader smoke and integration coverage.

## Related Source Files

- [__init__.py](../src/ndae/config/__init__.md)
- [__init__.py](../src/ndae/data/__init__.md)
- [runtime.py](../src/ndae/evaluation/runtime.md)
- [__init__.py](../src/ndae/models/__init__.md)
- [__init__.py](../src/ndae/rendering/__init__.md)
- [__init__.py](../src/ndae/training/__init__.md)
- [target_sampling.py](../src/ndae/training/target_sampling.md)
- [trainer.py](../src/ndae/training/trainer.md)
