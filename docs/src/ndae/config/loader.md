# loader.py

Source path: `src/ndae/config/loader.py`

## Role

This file belongs to the `src/ndae/config` slice of the NDAE repository. Public config loading and serialization helpers.

## Where This File Sits In The Pipeline

This file is one focused step in the `src/ndae/config` slice of the NDAE runtime.

## Inputs, Outputs, And Tensor Shapes

- This file mostly moves structured Python objects or runtime state rather than introducing a new tensor convention of its own.

## Implementation Walkthrough

The file is built from focused helpers rather than one monolithic routine. That makes each contract easier to test and lets neighboring modules reuse only the pieces they need.

Branches in this file usually separate runtime modes or reject invalid inputs early so deeper numerical code can stay cleaner.

## Function And Class Deep Dive

### load_config

Signature: `load_config(path, *, base_dir=None, validate_dataset=True)`

Purpose: Load and validate an NDAE config from a YAML file.

Expected inputs and outputs:
- The callable boundary is `load_config(path, *, base_dir=None, validate_dataset=True)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `Path, config_from_mapping, cwd, issubset, read_text, require_mapping` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `Path, config_from_mapping, cwd, issubset, read_text` without redoing the same validation or reshaping work.

### to_dict

Signature: `to_dict(config)`

Purpose: Convert a config dataclass tree back to plain dictionaries.

Expected inputs and outputs:
- The callable boundary is `to_dict(config)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers assume the return value already matches the local conventions of the surrounding file and can be consumed directly.

## Formula Mapping

Formula mapping: not applicable. This file mainly defines schema, orchestration, or utility behavior rather than a standalone equation.

## Design Decisions

- Split schema, parsing, loading, and validation so configuration errors stay field-scoped and testable.
- Prefer explicit dataclasses over untyped dictionaries once the YAML payload has been parsed.

## Common Failure Modes

- There are no custom guard clauses in this file; failures mostly come from imported runtime code or invalid upstream tensors.

## How This Connects To Neighboring Files

- This file is relatively self-contained; its closest neighbors are package-level imports rather than one obvious sibling file.

## Related Tests

- [test_download_svbrdf_mini.py](../../../tests/test_download_svbrdf_mini.md)
