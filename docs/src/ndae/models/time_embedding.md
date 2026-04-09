# time_embedding.py

Source path: `src/ndae/models/time_embedding.py`

## Role

This file belongs to the `src/ndae/models` slice of the NDAE repository. Time embedding modules for NDAE models.

## Where This File Sits In The Pipeline

This file is the time-conditioning frontend for the model stack. Every later block that depends on time receives a learned embedding produced here rather than raw scalar time.

## Inputs, Outputs, And Tensor Shapes

- This file mostly moves structured Python objects or runtime state rather than introducing a new tensor convention of its own.

## Implementation Walkthrough

Most of the interesting behavior is in class methods, so the best reading strategy is constructor first, then the public methods in the order the rest of the runtime calls them.

This style keeps long-lived state explicit and avoids hiding state transitions in global variables or one-off closures.

## Function And Class Deep Dive

### SinusoidalTimeEmbedding

Role: Map a scalar time value to a fixed sinusoidal embedding.

Inheritance: `nn.Module`

Public methods:
- `forward(self, t)`: Encode scalar `[]` or batched `[B]` times as sinusoidal features.

How the methods should be read:
- `forward` is one stage in the class-level control flow. Read its guard clauses, then the helper calls `cat, cos, dim, sin, to` to understand how state moves forward.

How to read this class:
- Start from construction or declared fields to see what long-lived state the object owns.
- Then read public methods in the order the rest of the runtime calls them; that is the real control flow.
- Treat private helpers as local refactoring aids rather than as a second independent API.

### TimeMLP

Role: Project sinusoidal time features to the UNet time-conditioning width.

Inheritance: `nn.Module`

Public methods:
- `forward(self, t)`: Return a learned time embedding for scalar `[]` or batched `[B]` times.

How the methods should be read:
- `forward` is one stage in the class-level control flow. Read its guard clauses, then the helper calls `mlp, sinusoidal_emb` to understand how state moves forward.

How to read this class:
- Start from construction or declared fields to see what long-lived state the object owns.
- Then read public methods in the order the rest of the runtime calls them; that is the real control flow.
- Treat private helpers as local refactoring aids rather than as a second independent API.

## Formula Mapping

- `SinusoidalTimeEmbedding` builds frequencies `freqs_i = exp(-i * log(10000) / (half_dim - 1))`.
- The forward pass returns `[sin(t * freqs), cos(t * freqs)]`, so every scalar time is embedded into a deterministic periodic basis.
- `TimeMLP` then applies `Linear -> SiLU -> Linear` to project the sinusoidal basis into the wider conditioning dimension used by the UNet.

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
