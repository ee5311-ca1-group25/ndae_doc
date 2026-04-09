# errors.py

Source path: `src/ndae/config/errors.py`

## Role

This file belongs to the `src/ndae/config` slice of the NDAE repository. Configuration-specific errors.

## Where This File Sits In The Pipeline

This file is one focused step in the `src/ndae/config` slice of the NDAE runtime.

## Inputs, Outputs, And Tensor Shapes

- This file mostly moves structured Python objects or runtime state rather than introducing a new tensor convention of its own.

## Implementation Walkthrough

Most of the interesting behavior is in class methods, so the best reading strategy is constructor first, then the public methods in the order the rest of the runtime calls them.

This style keeps long-lived state explicit and avoids hiding state transitions in global variables or one-off closures.

## Function And Class Deep Dive

### ConfigError

Role: Raised when an NDAE configuration is malformed.

Inheritance: `ValueError`

How to read this class:
- Start from construction or declared fields to see what long-lived state the object owns.
- Then read public methods in the order the rest of the runtime calls them; that is the real control flow.
- Treat private helpers as local refactoring aids rather than as a second independent API.

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

- No direct test file was matched to this module by the documentation generator.
