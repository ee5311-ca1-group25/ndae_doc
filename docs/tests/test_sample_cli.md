# test_sample_cli.py

Source path: `tests/test_sample_cli.py`

## System Under Test

- [sample.py](../src/ndae/cli/sample.md)
- [__init__.py](../src/ndae/data/__init__.md)
- [__init__.py](../src/ndae/evaluation/__init__.md)
- [__init__.py](../src/ndae/training/__init__.md)
- [__init__.py](../src/ndae/utils/__init__.md)

## Fixtures And Helpers

- `_create_sample_checkpoint(tmp_path, *, n_frames=3)`

## Test Groups

- `sample_cli_writes_png_sequence_from_checkpoint`: `test_sample_cli_writes_png_sequence_from_checkpoint`
- `sample_cli_requires_explicit_sample_size`: `test_sample_cli_requires_explicit_sample_size`
- `sample_cli`: `test_sample_cli_uses_explicit_sample_size`
- `sample_cli_accepts_explicit_output_dir`: `test_sample_cli_accepts_explicit_output_dir`
- `sample_cli_requires_flashlight_checkpoint_state`: `test_sample_cli_requires_flashlight_checkpoint_state`
- `sample_cli_reads_non_resume_ready_checkpoint`: `test_sample_cli_reads_non_resume_ready_checkpoint`
- `build_sample_timeline`: `test_build_sample_timeline_uses_synthesis_and_transition_segments`
- `sample_sequence`: `test_sample_sequence_returns_synthesis_and_transition_states`

## What Each Group Proves

- `sample_cli_writes_png_sequence_from_checkpoint` proves that the implementation still satisfies the contract exercised by `test_sample_cli_writes_png_sequence_from_checkpoint`.
- `sample_cli_requires_explicit_sample_size` proves that the implementation still satisfies the contract exercised by `test_sample_cli_requires_explicit_sample_size`.
- `sample_cli` proves that the implementation still satisfies the contract exercised by `test_sample_cli_uses_explicit_sample_size`.
- `sample_cli_accepts_explicit_output_dir` proves that the implementation still satisfies the contract exercised by `test_sample_cli_accepts_explicit_output_dir`.
- `sample_cli_requires_flashlight_checkpoint_state` proves that the implementation still satisfies the contract exercised by `test_sample_cli_requires_flashlight_checkpoint_state`.
- `sample_cli_reads_non_resume_ready_checkpoint` proves that the implementation still satisfies the contract exercised by `test_sample_cli_reads_non_resume_ready_checkpoint`.
- `build_sample_timeline` proves that the implementation still satisfies the contract exercised by `test_build_sample_timeline_uses_synthesis_and_transition_segments`.
- `sample_sequence` proves that the implementation still satisfies the contract exercised by `test_sample_sequence_returns_synthesis_and_transition_states`.

## Regression Intent

These tests are intended to catch behavior drift in the mirrored runtime paths, not just import-time failures.

## Remaining Gaps

The file only covers the explicit cases encoded in its test functions; full-sequence numerical drift still depends on broader smoke and integration coverage.

## Related Source Files

- [sample.py](../src/ndae/cli/sample.md)
- [__init__.py](../src/ndae/data/__init__.md)
- [__init__.py](../src/ndae/evaluation/__init__.md)
- [__init__.py](../src/ndae/training/__init__.md)
- [__init__.py](../src/ndae/utils/__init__.md)
