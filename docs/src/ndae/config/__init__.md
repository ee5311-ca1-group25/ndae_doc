# __init__.py

Source path: `src/ndae/config/__init__.py`

## Role

This file belongs to the `src/ndae/config` slice of the NDAE repository. Configuration schema and loading helpers for NDAE. Its main job is to define the import surface for the surrounding package.

## Exported API Surface

- `ConfigError`
- `DataConfig`
- `ExperimentConfig`
- `ModelConfig`
- `NDAEConfig`
- `RenderingConfig`
- `TrainConfig`
- `TrainRuntimeConfig`
- `TrainStageConfig`
- `TrainLossConfig`
- `TrainSchedulerConfig`
- `load_config`
- `to_dict`
- `validate_config`

## Re-export Design

This file centralizes symbols that the rest of the repository treats as package-level vocabulary. The goal is not to hide where implementations live, but to give callers one stable import surface even if internal files evolve over time.

## Import Side Effects

Importing this file re-exports symbols from child modules and may expose registries, dataclasses, or helper functions those modules define. It does not perform dataset loading, checkpoint I/O, or runtime mutation on import.

## How Downstream Code Uses These Exports

- Higher-level modules and tests use these exports to keep imports short and to avoid depending on every internal filename directly.
- The exported names usually define the package boundary that other slices of the runtime are expected to rely on.

## Formula Mapping

Formula mapping: not applicable. This file shapes import ergonomics and public package boundaries rather than introducing a numerical transform.

## Related Tests

- [test_trainer.py](../../../tests/test_trainer.md)
- [test_package_layout.py](../../../tests/test_package_layout.md)
- [test_dataset.py](../../../tests/test_dataset.md)
- [test_config.py](../../../tests/test_config.md)
- [support.py](../../../tests/support.md)
