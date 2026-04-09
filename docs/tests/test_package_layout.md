# test_package_layout.py

Source path: `tests/test_package_layout.py`

## System Under Test

- This test file exercises repository behavior through indirect imports or command execution paths.

## Fixtures And Helpers

- No file-local fixtures or helpers are declared; this file relies on inline test bodies or shared helpers.

## Test Groups

- `package_modules_import`: `test_package_modules_import`
- `data_package_exports_public_api`: `test_data_package_exports_public_api`
- `losses_package_exports_public_api`: `test_losses_package_exports_public_api`
- `models_package_exports_public_api`: `test_models_package_exports_public_api`
- `training_package_exports_public_api`: `test_training_package_exports_public_api`
- `evaluation_package_exports_public_api`: `test_evaluation_package_exports_public_api`
- `rendering_package_exports_renderer_metadata`: `test_rendering_package_exports_renderer_metadata`
- `rendering_normal_module_imports`: `test_rendering_normal_module_imports`
- `rendering_renderer_module_imports`: `test_rendering_renderer_module_imports`
- `rendering_geometry_module_imports`: `test_rendering_geometry_module_imports`
- `rendering_brdf_module_imports`: `test_rendering_brdf_module_imports`
- `rendering_postprocess_module_imports`: `test_rendering_postprocess_module_imports`
- `train_cli_stub`: `test_train_cli_stub_returns_success`
- `main_entrypoint_smoke`: `test_main_entrypoint_smoke`

## What Each Group Proves

- `package_modules_import` proves that the implementation still satisfies the contract exercised by `test_package_modules_import`.
- `data_package_exports_public_api` proves that the implementation still satisfies the contract exercised by `test_data_package_exports_public_api`.
- `losses_package_exports_public_api` proves that the implementation still satisfies the contract exercised by `test_losses_package_exports_public_api`.
- `models_package_exports_public_api` proves that the implementation still satisfies the contract exercised by `test_models_package_exports_public_api`.
- `training_package_exports_public_api` proves that the implementation still satisfies the contract exercised by `test_training_package_exports_public_api`.
- `evaluation_package_exports_public_api` proves that the implementation still satisfies the contract exercised by `test_evaluation_package_exports_public_api`.
- `rendering_package_exports_renderer_metadata` proves that the implementation still satisfies the contract exercised by `test_rendering_package_exports_renderer_metadata`.
- `rendering_normal_module_imports` proves that the implementation still satisfies the contract exercised by `test_rendering_normal_module_imports`.
- `rendering_renderer_module_imports` proves that the implementation still satisfies the contract exercised by `test_rendering_renderer_module_imports`.
- `rendering_geometry_module_imports` proves that the implementation still satisfies the contract exercised by `test_rendering_geometry_module_imports`.
- `rendering_brdf_module_imports` proves that the implementation still satisfies the contract exercised by `test_rendering_brdf_module_imports`.
- `rendering_postprocess_module_imports` proves that the implementation still satisfies the contract exercised by `test_rendering_postprocess_module_imports`.
- `train_cli_stub` proves that the implementation still satisfies the contract exercised by `test_train_cli_stub_returns_success`.
- `main_entrypoint_smoke` proves that the implementation still satisfies the contract exercised by `test_main_entrypoint_smoke`.

## Regression Intent

These tests are intended to catch behavior drift in the mirrored runtime paths, not just import-time failures.

## Remaining Gaps

The file only covers the explicit cases encoded in its test functions; full-sequence numerical drift still depends on broader smoke and integration coverage.

## Related Source Files

- No direct source file link was inferred automatically.
