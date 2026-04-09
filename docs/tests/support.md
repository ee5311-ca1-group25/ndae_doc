# support.py

Source path: `tests/support.py`

## System Under Test

- [__init__.py](../src/ndae/config/__init__.md)
- [__init__.py](../src/ndae/data/__init__.md)
- [__init__.py](../src/ndae/models/__init__.md)
- [__init__.py](../src/ndae/rendering/__init__.md)
- [__init__.py](../src/ndae/training/__init__.md)
- [system.py](../src/ndae/training/system.md)

## Fixtures And Helpers

- `write_image(path, *, size, color)`
- `make_config(*, output_root, name='demo', data_root='unused_data_root', exemplar='example', image_size=16, crop_size=8, n_frames=4, t_S=0.0, t_E=2.0, dry_run=False, n_iter=3, n_init_iter=1, log_every=1, checkpoint_every=1, loss_type='SW', refresh_rate_init=2, refresh_rate_local=6, eval_every=500, n_loss_crops=32, overflow_weight=100.0, init_height_weight=1.0, scheduler_factor=0.5, scheduler_patience_evals=5, scheduler_min_lr=0.0001, resume_from=None)`
- `make_trainer(workspace, *, config=None, refresh_rate=3)`

## Test Groups

- This file does not declare `test_*` functions.

## What Each Group Proves

- Protects whichever runtime path is imported by this file.

## Regression Intent

These tests are intended to catch behavior drift in the mirrored runtime paths, not just import-time failures.

## Remaining Gaps

The file only covers the explicit cases encoded in its test functions; full-sequence numerical drift still depends on broader smoke and integration coverage.

## Related Source Files

- [__init__.py](../src/ndae/config/__init__.md)
- [__init__.py](../src/ndae/data/__init__.md)
- [__init__.py](../src/ndae/models/__init__.md)
- [__init__.py](../src/ndae/rendering/__init__.md)
- [__init__.py](../src/ndae/training/__init__.md)
- [system.py](../src/ndae/training/system.md)
