# test_smoke.py

Source path: `tests/test_smoke.py`

## System Under Test

- [render_example.py](../src/ndae/cli/render_example.md)
- [sample.py](../src/ndae/cli/sample.md)
- [train.py](../src/ndae/cli/train.md)

## Fixtures And Helpers

- No file-local fixtures or helpers are declared; this file relies on inline test bodies or shared helpers.

## Test Groups

- `dry_run_creates_workspace_and_resolved_config`: `test_dry_run_creates_workspace_and_resolved_config`
- `render_example_cli_writes_png`: `test_render_example_cli_writes_png`
- `non_dry_run_cli_executes_trainer_and_writes_metrics`: `test_non_dry_run_cli_executes_trainer_and_writes_metrics`
- `train_cli_writes_boundary_checkpoint`: `test_train_cli_writes_boundary_checkpoint`
- `train_cli`: `test_train_cli_saves_local_checkpoint_after_misaligned_stage_switch`
- `train_checkpoint_sample_closes_loop_on_toy_setup`: `test_train_checkpoint_sample_closes_loop_on_toy_setup`
- `resume_cli_appends_metrics_jsonl`: `test_resume_cli_appends_metrics_jsonl`

## What Each Group Proves

- `dry_run_creates_workspace_and_resolved_config` proves that the implementation still satisfies the contract exercised by `test_dry_run_creates_workspace_and_resolved_config`.
- `render_example_cli_writes_png` proves that the implementation still satisfies the contract exercised by `test_render_example_cli_writes_png`.
- `non_dry_run_cli_executes_trainer_and_writes_metrics` proves that the implementation still satisfies the contract exercised by `test_non_dry_run_cli_executes_trainer_and_writes_metrics`.
- `train_cli_writes_boundary_checkpoint` proves that the implementation still satisfies the contract exercised by `test_train_cli_writes_boundary_checkpoint`.
- `train_cli` proves that the implementation still satisfies the contract exercised by `test_train_cli_saves_local_checkpoint_after_misaligned_stage_switch`.
- `train_checkpoint_sample_closes_loop_on_toy_setup` proves that the implementation still satisfies the contract exercised by `test_train_checkpoint_sample_closes_loop_on_toy_setup`.
- `resume_cli_appends_metrics_jsonl` proves that the implementation still satisfies the contract exercised by `test_resume_cli_appends_metrics_jsonl`.

## Regression Intent

These tests are intended to catch behavior drift in the mirrored runtime paths, not just import-time failures.

## Remaining Gaps

The file only covers the explicit cases encoded in its test functions; full-sequence numerical drift still depends on broader smoke and integration coverage.

## Related Source Files

- [render_example.py](../src/ndae/cli/render_example.md)
- [sample.py](../src/ndae/cli/sample.md)
- [train.py](../src/ndae/cli/train.md)
