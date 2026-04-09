# perceptual.py

Source path: `src/ndae/losses/perceptual.py`

## Role

This file belongs to the `src/ndae/losses` slice of the NDAE repository. Perceptual feature extractors used by texture-statistics losses.

## Where This File Sits In The Pipeline

This file sits between rendered RGB crops and the texture-statistics objectives. It turns images into a fixed stack of perceptual feature tensors that `gram_loss` and `slice_loss` can compare layer by layer.

## Inputs, Outputs, And Tensor Shapes

- Input to `VGG19Features.forward` must be `[B, 3, H, W]` in the same `[0, 1]` image range used elsewhere in the repository before normalization is applied.
- The return value is a Python list of tensors: the original image followed by five progressively deeper VGG feature maps. Spatial resolution shrinks after each average-pooling boundary.

## Implementation Walkthrough

The module first loads pretrained VGG-19 features and slices them into explicit block boundaries. That choice makes the feature hierarchy visible instead of hiding everything behind one opaque backbone call.

During the forward pass, the image is normalized with ImageNet mean and standard deviation, then pushed through each block in sequence. The code appends the original image before any VGG block output so later losses can mix image-space and feature-space statistics in one interface.

Average pooling is applied between blocks rather than relying on VGG's original max-pooling path. That keeps feature statistics smoother, which matters because the downstream losses compare distributions and correlations rather than class logits.

## Function And Class Deep Dive

### VGG19Features

Role: Frozen VGG-19 feature extractor with AvgPool block boundaries.

Inheritance: `nn.Module`

Public methods:
- `forward(self, x)`: Return the input image plus 5 pre-pooling VGG block activations.

How the methods should be read:
- `forward` is one stage in the class-level control flow. Read its guard clauses, then the helper calls `append, block, dim, pool, to` to understand how state moves forward.

How to read this class:
- Start from construction or declared fields to see what long-lived state the object owns.
- Then read public methods in the order the rest of the runtime calls them; that is the real control flow.
- Treat private helpers as local refactoring aids rather than as a second independent API.

## Formula Mapping

- Inputs are normalized channelwise as `(x - mean) / std` before entering VGG-19.
- The module returns `[x, block_0(x), ..., block_4(x)]`, so downstream losses can mix image-space and feature-space statistics.
- Between blocks it applies average pooling, matching the texture-statistics pipeline encoded in this repository.

## Design Decisions

- Separate feature extraction from objective composition so loss modes can share one perceptual frontend.
- Keep loss functions pure and batch-local so they are easy to unit test.

## Common Failure Modes

- There are no custom guard clauses in this file; failures mostly come from imported runtime code or invalid upstream tensors.

## How This Connects To Neighboring Files

- This file is relatively self-contained; its closest neighbors are package-level imports rather than one obvious sibling file.

## Related Tests

- [test_package_layout.py](../../../tests/test_package_layout.md)
- [test_losses.py](../../../tests/test_losses.md)
