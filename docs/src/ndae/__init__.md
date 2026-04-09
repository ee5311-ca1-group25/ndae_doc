# __init__.py

Source path: `src/ndae/__init__.py`

## Role

NDAE package. Its main job is to define the import surface for the surrounding package.

## Exported API Surface

- No explicit `__all__` export list is declared in this file.

## Re-export Design

This file centralizes symbols that the rest of the repository treats as package-level vocabulary. The goal is not to hide where implementations live, but to give callers one stable import surface even if internal files evolve over time.

## Import Side Effects

Importing this file re-exports symbols from child modules and may expose registries, dataclasses, or helper functions those modules define. It does not perform dataset loading, checkpoint I/O, or runtime mutation on import.

## How Downstream Code Uses These Exports

- Downstream code currently treats this file more as a namespace anchor than as a heavily curated export list.

## Formula Mapping

Formula mapping: not applicable. This file shapes import ergonomics and public package boundaries rather than introducing a numerical transform.

## Related Tests

- [test_trainer.py](../../tests/test_trainer.md)
- [test_solver.py](../../tests/test_solver.md)
- [test_smoke.py](../../tests/test_smoke.md)
- [test_schedule.py](../../tests/test_schedule.md)
- [test_sample_cli.py](../../tests/test_sample_cli.md)
- [test_renderer.py](../../tests/test_renderer.md)
