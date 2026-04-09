# test_losses.py

Source path: `tests/test_losses.py`

## System Under Test

- [__init__.py](../src/ndae/losses/__init__.md)
- [perceptual.py](../src/ndae/losses/perceptual.md)
- [__init__.py](../src/ndae/rendering/__init__.md)

## Fixtures And Helpers

- `patch_vgg19(monkeypatch)`

## Test Groups

- `vgg19_output_shapes`: `test_vgg19_output_shapes`
- `vgg19_frozen`: `test_vgg19_frozen`
- `vgg19`: `test_vgg19_gradient_to_input`, `test_vgg19_rejects_invalid_rank`, `test_vgg19_rejects_non_rgb_input`
- `gram_matrix_shape_and_symmetry`: `test_gram_matrix_shape_and_symmetry`
- `gram_matrix`: `test_gram_matrix_supports_batches`, `test_gram_matrix_rejects_invalid_rank`
- `gram_loss`: `test_gram_loss_same_input_zero`, `test_gram_loss_diff_input_positive`, `test_gram_loss_gradient_to_sample`
- `swd`: `test_swd_same_input_zero`, `test_swd_diff_input_positive`, `test_swd_reproducible`, `test_swd_rejects_invalid_rank`, `test_swd_rejects_channel_mismatch`
- `swd_resizes_exemplar_projection_length`: `test_swd_resizes_exemplar_projection_length`
- `slice_loss`: `test_slice_loss_gradient_backward`, `test_slice_loss_reproducible`, `test_slice_loss_rejects_invalid_weight_count`, `test_slice_loss_rejects_non_positive_weight_sum`
- `overflow_loss`: `test_overflow_loss_in_range_zero`, `test_overflow_loss_out_of_range_positive`
- `overflow_loss_proportional_to_excess`: `test_overflow_loss_proportional_to_excess`
- `init_loss`: `test_init_loss_same_input_zero`, `test_init_loss_matches_manual_mse`
- `local_loss_sw`: `test_local_loss_sw_same_input_zero`
- `local_loss_gram`: `test_local_loss_gram_same_input_zero`
- `local_loss_sw_and_gram_modes`: `test_local_loss_sw_and_gram_modes_positive`
- `local_loss`: `test_local_loss_rejects_unknown_mode`
- `full_pipeline`: `test_full_pipeline_gradient`

## What Each Group Proves

- `vgg19_output_shapes` proves that the implementation still satisfies the contract exercised by `test_vgg19_output_shapes`.
- `vgg19_frozen` proves that the implementation still satisfies the contract exercised by `test_vgg19_frozen`.
- `vgg19` proves that the implementation still satisfies the contract exercised by `test_vgg19_gradient_to_input`, `test_vgg19_rejects_invalid_rank`, `test_vgg19_rejects_non_rgb_input`.
- `gram_matrix_shape_and_symmetry` proves that the implementation still satisfies the contract exercised by `test_gram_matrix_shape_and_symmetry`.
- `gram_matrix` proves that the implementation still satisfies the contract exercised by `test_gram_matrix_supports_batches`, `test_gram_matrix_rejects_invalid_rank`.
- `gram_loss` proves that the implementation still satisfies the contract exercised by `test_gram_loss_same_input_zero`, `test_gram_loss_diff_input_positive`, `test_gram_loss_gradient_to_sample`.
- `swd` proves that the implementation still satisfies the contract exercised by `test_swd_same_input_zero`, `test_swd_diff_input_positive`, `test_swd_reproducible`.
- `swd_resizes_exemplar_projection_length` proves that the implementation still satisfies the contract exercised by `test_swd_resizes_exemplar_projection_length`.
- `slice_loss` proves that the implementation still satisfies the contract exercised by `test_slice_loss_gradient_backward`, `test_slice_loss_reproducible`, `test_slice_loss_rejects_invalid_weight_count`.
- `overflow_loss` proves that the implementation still satisfies the contract exercised by `test_overflow_loss_in_range_zero`, `test_overflow_loss_out_of_range_positive`.
- `overflow_loss_proportional_to_excess` proves that the implementation still satisfies the contract exercised by `test_overflow_loss_proportional_to_excess`.
- `init_loss` proves that the implementation still satisfies the contract exercised by `test_init_loss_same_input_zero`, `test_init_loss_matches_manual_mse`.
- `local_loss_sw` proves that the implementation still satisfies the contract exercised by `test_local_loss_sw_same_input_zero`.
- `local_loss_gram` proves that the implementation still satisfies the contract exercised by `test_local_loss_gram_same_input_zero`.
- `local_loss_sw_and_gram_modes` proves that the implementation still satisfies the contract exercised by `test_local_loss_sw_and_gram_modes_positive`.
- `local_loss` proves that the implementation still satisfies the contract exercised by `test_local_loss_rejects_unknown_mode`.
- `full_pipeline` proves that the implementation still satisfies the contract exercised by `test_full_pipeline_gradient`.

## Regression Intent

These tests are intended to catch behavior drift in the mirrored runtime paths, not just import-time failures.

## Remaining Gaps

The file only covers the explicit cases encoded in its test functions; full-sequence numerical drift still depends on broader smoke and integration coverage.

## Related Source Files

- [__init__.py](../src/ndae/losses/__init__.md)
- [perceptual.py](../src/ndae/losses/perceptual.md)
- [__init__.py](../src/ndae/rendering/__init__.md)
