# test_models.py

Source path: `tests/test_models.py`

## System Under Test

- [blocks.py](../src/ndae/models/blocks.md)
- [odefunc.py](../src/ndae/models/odefunc.md)
- [time_embedding.py](../src/ndae/models/time_embedding.md)
- [trajectory.py](../src/ndae/models/trajectory.md)
- [unet.py](../src/ndae/models/unet.md)

## Fixtures And Helpers

- No file-local fixtures or helpers are declared; this file relies on inline test bodies or shared helpers.

## Test Groups

- `sinusoidal_time_embedding_scalar_shape_and_bounds`: `test_sinusoidal_time_embedding_scalar_shape_and_bounds`
- `sinusoidal_time_embedding_batch_shape_and_bounds`: `test_sinusoidal_time_embedding_batch_shape_and_bounds`
- `sinusoidal_time_embedding_distinguishes_different_times`: `test_sinusoidal_time_embedding_distinguishes_different_times`
- `sinusoidal_time_embedding`: `test_sinusoidal_time_embedding_is_smooth_for_nearby_times`
- `time_mlp_batch_output_shape`: `test_time_mlp_batch_output_shape`
- `time_mlp`: `test_time_mlp_gradient_flows_to_input_time`
- `time_embedding`: `test_time_embedding_rejects_invalid_dim`, `test_time_embedding_rejects_dim_smaller_than_four`, `test_time_embedding_rejects_invalid_input_rank`
- `zero_init_zeros_all_parameters`: `test_zero_init_zeros_all_parameters`
- `default_conv2d_preserves_spatial_shape`: `test_default_conv2d_preserves_spatial_shape`
- `default_conv2d`: `test_default_conv2d_uses_circular_padding`
- `spatial_linear_preserves_spatial_shape`: `test_spatial_linear_preserves_spatial_shape`
- `conv_block_kernel_size_3`: `test_conv_block_kernel_size_3_uses_default_conv2d`
- `conv_block_kernel_size_1`: `test_conv_block_kernel_size_1_uses_spatial_linear`
- `conv_block`: `test_conv_block_rejects_invalid_kernel_size`, `test_conv_block_with_zero_init_time_embedding_matches_no_embedding`, `test_conv_block_gradients_flow_to_input_and_embedding`
- `resample_downsample_shape`: `test_resample_downsample_shape`
- `resample_upsample_shape`: `test_resample_upsample_shape`
- `attention`: `test_attention_zero_init_output_is_near_zero`
- `residual_attention`: `test_residual_attention_matches_input_at_initialization`, `test_residual_attention_gradients_flow_to_input`
- `unet_forward_shape_default_config`: `test_unet_forward_shape_default_config`
- `unet_forward_shape`: `test_unet_forward_shape_with_deeper_dim_mults`
- `unet`: `test_unet_supports_attention_toggle`, `test_unet_supports_scalar_time_input`, `test_unet_zero_init_output_is_near_zero`, `test_unet_gradients_flow_when_final_layer_is_unfrozen_from_zero`, `test_unet_rejects_invalid_x_rank`, `test_unet_rejects_invalid_time_rank`, `test_unet_rejects_time_batch_mismatch`, `test_unet_rejects_dim_mults_without_leading_one`, `test_unet_rejects_empty_dim_mults`
- `odefunc_forward_shape_passthrough`: `test_odefunc_forward_shape_passthrough`
- `odefunc`: `test_odefunc_keeps_wrapped_module_identity`, `test_odefunc_gradients_flow_to_wrapped_unet_parameters`
- `odefunc_registers_the`: `test_odefunc_registers_the_same_parameters_as_wrapped_model`
- `odefunc_preserves_unet`: `test_odefunc_preserves_unet_zero_init_behavior`
- `trajectory_forward_shape`: `test_trajectory_forward_shape_is_time_major`
- `trajectory_preserves_initial_state`: `test_trajectory_preserves_initial_state`
- `trajectory`: `test_trajectory_zero_init_vector_field_keeps_state_nearly_static`, `test_trajectory_gradients_flow_to_wrapped_unet_parameters`, `test_trajectory_supports_solver_method_passthrough`, `test_trajectory_supports_augmentation_state_dimensions`, `test_trajectory_rejects_invalid_z0_rank`, `test_trajectory_rejects_invalid_t_eval_rank`, `test_trajectory_rejects_t_eval_with_fewer_than_two_points`
- `parameter_summary`: `test_parameter_summary`

## What Each Group Proves

- `sinusoidal_time_embedding_scalar_shape_and_bounds` proves that the implementation still satisfies the contract exercised by `test_sinusoidal_time_embedding_scalar_shape_and_bounds`.
- `sinusoidal_time_embedding_batch_shape_and_bounds` proves that the implementation still satisfies the contract exercised by `test_sinusoidal_time_embedding_batch_shape_and_bounds`.
- `sinusoidal_time_embedding_distinguishes_different_times` proves that the implementation still satisfies the contract exercised by `test_sinusoidal_time_embedding_distinguishes_different_times`.
- `sinusoidal_time_embedding` proves that the implementation still satisfies the contract exercised by `test_sinusoidal_time_embedding_is_smooth_for_nearby_times`.
- `time_mlp_batch_output_shape` proves that the implementation still satisfies the contract exercised by `test_time_mlp_batch_output_shape`.
- `time_mlp` proves that the implementation still satisfies the contract exercised by `test_time_mlp_gradient_flows_to_input_time`.
- `time_embedding` proves that the implementation still satisfies the contract exercised by `test_time_embedding_rejects_invalid_dim`, `test_time_embedding_rejects_dim_smaller_than_four`, `test_time_embedding_rejects_invalid_input_rank`.
- `zero_init_zeros_all_parameters` proves that the implementation still satisfies the contract exercised by `test_zero_init_zeros_all_parameters`.
- `default_conv2d_preserves_spatial_shape` proves that the implementation still satisfies the contract exercised by `test_default_conv2d_preserves_spatial_shape`.
- `default_conv2d` proves that the implementation still satisfies the contract exercised by `test_default_conv2d_uses_circular_padding`.
- `spatial_linear_preserves_spatial_shape` proves that the implementation still satisfies the contract exercised by `test_spatial_linear_preserves_spatial_shape`.
- `conv_block_kernel_size_3` proves that the implementation still satisfies the contract exercised by `test_conv_block_kernel_size_3_uses_default_conv2d`.
- `conv_block_kernel_size_1` proves that the implementation still satisfies the contract exercised by `test_conv_block_kernel_size_1_uses_spatial_linear`.
- `conv_block` proves that the implementation still satisfies the contract exercised by `test_conv_block_rejects_invalid_kernel_size`, `test_conv_block_with_zero_init_time_embedding_matches_no_embedding`, `test_conv_block_gradients_flow_to_input_and_embedding`.
- `resample_downsample_shape` proves that the implementation still satisfies the contract exercised by `test_resample_downsample_shape`.
- `resample_upsample_shape` proves that the implementation still satisfies the contract exercised by `test_resample_upsample_shape`.
- `attention` proves that the implementation still satisfies the contract exercised by `test_attention_zero_init_output_is_near_zero`.
- `residual_attention` proves that the implementation still satisfies the contract exercised by `test_residual_attention_matches_input_at_initialization`, `test_residual_attention_gradients_flow_to_input`.
- `unet_forward_shape_default_config` proves that the implementation still satisfies the contract exercised by `test_unet_forward_shape_default_config`.
- `unet_forward_shape` proves that the implementation still satisfies the contract exercised by `test_unet_forward_shape_with_deeper_dim_mults`.
- `unet` proves that the implementation still satisfies the contract exercised by `test_unet_supports_attention_toggle`, `test_unet_supports_scalar_time_input`, `test_unet_zero_init_output_is_near_zero`.
- `odefunc_forward_shape_passthrough` proves that the implementation still satisfies the contract exercised by `test_odefunc_forward_shape_passthrough`.
- `odefunc` proves that the implementation still satisfies the contract exercised by `test_odefunc_keeps_wrapped_module_identity`, `test_odefunc_gradients_flow_to_wrapped_unet_parameters`.
- `odefunc_registers_the` proves that the implementation still satisfies the contract exercised by `test_odefunc_registers_the_same_parameters_as_wrapped_model`.
- `odefunc_preserves_unet` proves that the implementation still satisfies the contract exercised by `test_odefunc_preserves_unet_zero_init_behavior`.
- `trajectory_forward_shape` proves that the implementation still satisfies the contract exercised by `test_trajectory_forward_shape_is_time_major`.
- `trajectory_preserves_initial_state` proves that the implementation still satisfies the contract exercised by `test_trajectory_preserves_initial_state`.
- `trajectory` proves that the implementation still satisfies the contract exercised by `test_trajectory_zero_init_vector_field_keeps_state_nearly_static`, `test_trajectory_gradients_flow_to_wrapped_unet_parameters`, `test_trajectory_supports_solver_method_passthrough`.
- `parameter_summary` proves that the implementation still satisfies the contract exercised by `test_parameter_summary`.

## Regression Intent

These tests are intended to catch behavior drift in the mirrored runtime paths, not just import-time failures.

## Remaining Gaps

The file only covers the explicit cases encoded in its test functions; full-sequence numerical drift still depends on broader smoke and integration coverage.

## Related Source Files

- [blocks.py](../src/ndae/models/blocks.md)
- [odefunc.py](../src/ndae/models/odefunc.md)
- [time_embedding.py](../src/ndae/models/time_embedding.md)
- [trajectory.py](../src/ndae/models/trajectory.md)
- [unet.py](../src/ndae/models/unet.md)
