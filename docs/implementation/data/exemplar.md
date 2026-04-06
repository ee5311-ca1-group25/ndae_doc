# Data Exemplar

## Purpose

`src/ndae/data/exemplar.py` implements `ExemplarDataset`, the in-memory loader for a single exemplar sequence.

The class is intentionally small. NDAE uses exemplar overfitting, so the dataset does not need a PyTorch `Dataset` or `DataLoader` abstraction at this stage.

## Public API / key types

Main entry points:

- `ExemplarDataset(root, exemplar, *, n_frames=100, image_size=256)`
- `ExemplarDataset.from_config(data_config, *, base_dir=None)`
- `__len__() -> int`
- `__getitem__(index) -> torch.Tensor`

Public state:

- `frames`: tensor shaped `[N, 3, H, W]`
- `n_frames`: number of selected frames
- `image_size`: stored as `(H, W)`
- `source_paths`: tuple of the actual image paths used

## Behavior and invariants

Frame discovery:

- effective image discovery is delegated to `resolve_available_images`
- this means `_manifest.json` is preferred over raw directory scanning
- when a manifest exists, its `selected_files` order is preserved

Frame selection:

- if `available == n_frames`, all effective images are used
- if `available > n_frames`, the loader uses uniform index selection that always keeps the first and last frames
- if `n_frames == 1`, the loader returns only the first frame

Preprocessing pipeline for each image:

1. open the file with PIL
2. convert to RGB
3. center-crop to the largest square
4. resize to `(image_size, image_size)`
5. convert to `numpy.float32`
6. normalize to `[0, 1]`
7. convert to `torch.float32` and permute to CHW

The final tensor is stacked as `[N, 3, image_size, image_size]`.

`from_config(..., base_dir=...)` resolves relative `data.root` the same way config validation does. This keeps runtime loading consistent with config checks.

## Error handling

The class raises `ValueError` when:

- `n_frames <= 0`
- `image_size <= 0`
- the requested frame count exceeds the effective image count

`__getitem__` follows Python sequence semantics:

- negative indices are allowed
- out-of-range indices raise `IndexError`

Manifest and path errors bubble up from the shared config-validation helpers as `ConfigError`.

## Tests / validation

`tests/test_dataset.py` verifies:

- loading from the real mini exemplar via `from_config`
- output tensor shape, dtype, and range
- manifest order preservation
- fallback sorting when no manifest exists
- uniform downsampling when more images are available than requested
- error handling for insufficient frames
- negative indexing and `base_dir` resolution

## Related files

- `src/ndae/config/validation.py`
- `configs/base.yaml`
- `tests/test_dataset.py`
