# unet.py

Source path: `src/ndae/models/unet.py`

## Role

This file belongs to the `src/ndae/models` slice of the NDAE repository. UNet assembly for NDAE models.

## Where This File Sits In The Pipeline

This file defines the learnable vector field backbone. The ODE adapter and trajectory wrapper treat it as `f_theta(t, x)`, but its internal job is multi-scale feature processing with explicit time modulation.

## Inputs, Outputs, And Tensor Shapes

- The main forward path expects `x` shaped `[B, C, H, W]` and time `t` shaped either `[]` or `[B]`.
- The output shape matches the input latent shape exactly because the module is used as a vector field inside an ODE solver: `f_theta(t, x)` must live in the same state space as `x`.
- Skip tensors preserve spatial detail across the downsampling and upsampling path, so intermediate channel widths change but the final output returns to the original spatial resolution.

## Implementation Walkthrough

Initialization builds one time MLP, an initial projection block, a mirrored down/up stack, and a final projection head. The structure is deliberately explicit so channel growth and skip usage are easy to inspect.

In the forward pass, scalar time is expanded to batch length when needed, then encoded once into `t_emb`. That embedding is reused at every conditioned block, so time information is global to the whole UNet pass rather than recomputed per layer.

The data path alternates between feature refinement and resolution changes. Down blocks push activations into a skip stack before resampling, the mid block processes the bottleneck representation, and up blocks recover resolution while concatenating the saved skips in reverse order.

## Function And Class Deep Dive

### NDAEUNet

Role: JAX-aligned UNet used as the NDAE vector field backbone.

Inheritance: `nn.Module`

Public methods:
- `forward(self, t, x)`: Evaluate the UNet as f(t, x) with scalar or batched time input.

How the methods should be read:
- `forward` is one stage in the class-level control flow. Read its guard clauses, then the helper calls `append, attn, block, cat, dim` to understand how state moves forward.

How to read this class:
- Start from construction or declared fields to see what long-lived state the object owns.
- Then read public methods in the order the rest of the runtime calls them; that is the real control flow.
- Treat private helpers as local refactoring aids rather than as a second independent API.

## Formula Mapping

- The model implements the vector field `f_theta(t, x)` used inside the ODE solver.
- Time conditioning is produced once as `t_emb = TimeMLP(t)` and injected into every residual block that accepts `emb_dim`.
- The data path is `init_conv -> downs -> mid -> ups -> final_conv`, with skip tensors concatenated during the up path.

## Design Decisions

- Use small modules with explicit shape validation instead of hiding tensor contracts inside one large model file.
- Keep the ODE adapter, trajectory wrapper, embeddings, and blocks independently testable.

## Common Failure Modes

- There are no custom guard clauses in this file; failures mostly come from imported runtime code or invalid upstream tensors.

## How This Connects To Neighboring Files

- This file is relatively self-contained; its closest neighbors are package-level imports rather than one obvious sibling file.

## Related Tests

- [test_solver.py](../../../tests/test_solver.md)
- [test_package_layout.py](../../../tests/test_package_layout.md)
- [test_models.py](../../../tests/test_models.md)
