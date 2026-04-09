# __init__.py

Source path: `src/ndae/data/__init__.py`

## Role

This file belongs to the `src/ndae/data` slice of the NDAE repository. Data module for NDAE: exemplar loading, timeline, and sampling. Its main job is to define the import surface for the surrounding package.

## Exported API Surface

- `ExemplarDataset`
- `Timeline`
- `CropSampleSpec`
- `random_crop`
- `random_take`
- `sample_random_crop_spec`
- `sample_random_take_spec`
- `apply_crop_spec`
- `apply_take_spec`
- `stratified_uniform`
- `sample_frame_indices`

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
- [test_sample_cli.py](../../../tests/test_sample_cli.md)
- [test_package_layout.py](../../../tests/test_package_layout.md)
- [test_dataset.py](../../../tests/test_dataset.md)
- [support.py](../../../tests/support.md)
