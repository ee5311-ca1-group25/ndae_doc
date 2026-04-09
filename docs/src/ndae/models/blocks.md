# blocks.py

Source path: `src/ndae/models/blocks.py`

## Role

This file belongs to the `src/ndae/models` slice of the NDAE repository. Building blocks for NDAE models.

## Where This File Sits In The Pipeline

This file is one focused step in the `src/ndae/models` slice of the NDAE runtime.

## Inputs, Outputs, And Tensor Shapes

- This file mostly moves structured Python objects or runtime state rather than introducing a new tensor convention of its own.

## Implementation Walkthrough

The file is built from focused helpers rather than one monolithic routine. That makes each contract easier to test and lets neighboring modules reuse only the pieces they need.

Branches in this file usually separate runtime modes or reject invalid inputs early so deeper numerical code can stay cleaner.

## Function And Class Deep Dive

### DefaultConv2d

Role: 3x3 convolution with explicit circular padding.

Inheritance: `nn.Module`

Public methods:
- `forward(self, x)`: Key method on this runtime object.

How the methods should be read:
- `forward` is one stage in the class-level control flow. Read its guard clauses, then the helper calls `conv, pad` to understand how state moves forward.

How to read this class:
- Start from construction or declared fields to see what long-lived state the object owns.
- Then read public methods in the order the rest of the runtime calls them; that is the real control flow.
- Treat private helpers as local refactoring aids rather than as a second independent API.

### SpatialLinear

Role: 1x1 convolution used where the JAX code applies SpatialLinear.

Inheritance: `nn.Module`

Public methods:
- `forward(self, x)`: Key method on this runtime object.

How the methods should be read:
- `forward` is one stage in the class-level control flow. Read its guard clauses, then the helper calls `conv` to understand how state moves forward.

How to read this class:
- Start from construction or declared fields to see what long-lived state the object owns.
- Then read public methods in the order the rest of the runtime calls them; that is the real control flow.
- Treat private helpers as local refactoring aids rather than as a second independent API.

### ConvBlock

Role: Convolution, GroupNorm, optional time scale-shift, then activation.

Inheritance: `nn.Module`

Public methods:
- `forward(self, x, emb=None)`: Key method on this runtime object.

How the methods should be read:
- `forward` is one stage in the class-level control flow. Read its guard clauses, then the helper calls `act, chunk, mlp, norm, proj` to understand how state moves forward.

How to read this class:
- Start from construction or declared fields to see what long-lived state the object owns.
- Then read public methods in the order the rest of the runtime calls them; that is the real control flow.
- Treat private helpers as local refactoring aids rather than as a second independent API.

### Resample

Role: Resize with bilinear interpolation followed by DefaultConv2d.

Inheritance: `nn.Module`

Public methods:
- `forward(self, x)`: Key method on this runtime object.

How the methods should be read:
- `forward` is one stage in the class-level control flow. Read its guard clauses, then the helper calls `conv, interpolate` to understand how state moves forward.

How to read this class:
- Start from construction or declared fields to see what long-lived state the object owns.
- Then read public methods in the order the rest of the runtime calls them; that is the real control flow.
- Treat private helpers as local refactoring aids rather than as a second independent API.

### LinearTimeSelfAttention

Role: JAX-aligned multi-head linear attention with zero-initialized output.

Inheritance: `nn.Module`

Public methods:
- `forward(self, x)`: Key method on this runtime object.

How the methods should be read:
- `forward` is one stage in the class-level control flow. Read its guard clauses, then the helper calls `einsum, group_norm, reshape, softmax, to_out` to understand how state moves forward.

How to read this class:
- Start from construction or declared fields to see what long-lived state the object owns.
- Then read public methods in the order the rest of the runtime calls them; that is the real control flow.
- Treat private helpers as local refactoring aids rather than as a second independent API.

### Residual

Role: Add a module's output back to its input.

Inheritance: `nn.Module`

Public methods:
- `forward(self, x)`: Key method on this runtime object.

How the methods should be read:
- `forward` is one stage in the class-level control flow. Read its guard clauses, then the helper calls `fn` to understand how state moves forward.

How to read this class:
- Start from construction or declared fields to see what long-lived state the object owns.
- Then read public methods in the order the rest of the runtime calls them; that is the real control flow.
- Treat private helpers as local refactoring aids rather than as a second independent API.

### zero_init

Signature: `zero_init(module)`

Purpose: Zero-initialize all learnable parameters in-place.

Expected inputs and outputs:
- The callable boundary is `zero_init(module)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `parameters, zeros_` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `parameters, zeros_` without redoing the same validation or reshaping work.

## Formula Mapping

- `ConvBlock` applies `proj -> norm -> optional (scale, shift) from time embedding -> activation`.
- When an embedding is present, the block computes `x = x * (scale + 1) + shift`, which is the time-conditioned affine modulation used throughout the UNet.
- `LinearTimeSelfAttention` forms `q`, `k`, and `v`, normalizes `k` with `softmax`, computes `context = einsum(k, v)`, then projects `context` back with `einsum(context, q)`.

## Design Decisions

- Use small modules with explicit shape validation instead of hiding tensor contracts inside one large model file.
- Keep the ODE adapter, trajectory wrapper, embeddings, and blocks independently testable.

## Common Failure Modes

- There are no custom guard clauses in this file; failures mostly come from imported runtime code or invalid upstream tensors.

## How This Connects To Neighboring Files

- This file is relatively self-contained; its closest neighbors are package-level imports rather than one obvious sibling file.

## Related Tests

- [test_package_layout.py](../../../tests/test_package_layout.md)
- [test_models.py](../../../tests/test_models.md)
