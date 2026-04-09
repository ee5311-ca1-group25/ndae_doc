#!/usr/bin/env python3

from __future__ import annotations

import argparse
import ast
from dataclasses import dataclass
from pathlib import Path
import shutil
import textwrap

from repo_docs_common import (
    ROOT_FILE,
    expected_doc_directories,
    list_target_sources,
    markdown_link,
    normalize_whitespace,
    page_rules_for,
    source_to_doc,
    title_for_directory,
    title_for_source,
)


MATH_OVERRIDES: dict[str, str] = {
    "src/ndae/data/sampling.py": """
- `random_crop` samples integer offsets `top ~ U{0, H-crop_h}` and `left ~ U{0, W-crop_w}` and returns `image[:, top:top+crop_h, left:left+crop_w]`.
- `random_take` samples `new_h * new_w` unique flattened positions with `torch.randperm(H * W)` and reshapes the gather result back to `[C, new_h, new_w]`.
- `stratified_uniform` divides `[minval, maxval)` into `n` equal bins and draws one sample per bin, so returned times stay monotonic by construction.
- `sample_frame_indices` maps cycle step `k` to the interval `[segment * (k-1), segment * k)` where `segment = n_frames / (refresh_rate - 1)`, then floors the sampled point to a frame index.
""",
    "src/ndae/data/timeline.py": """
- `dt = (t_E - t_S) / n_frames` is the frame spacing used by both `frame_to_time` and `time_to_frame`.
- `frame_to_time(k) = t_S + k * dt` converts discrete supervision indices into continuous ODE time.
- `time_to_frame(t)` computes `floor(max(t - t_S, 0) / dt + 1e-9)` and clamps the result into `[0, n_frames - 1]`.
""",
    "src/ndae/evaluation/runtime.py": """
- `should_eval` triggers on step `0`, every `eval_every` steps, and at the init-to-local watershed.
- `compute_inference_loss` samples `z0 ~ N(0, I)`, rolls out on `[t_I, linspace(t_S, t_E, n_frames)]`, renders every generated frame, and averages the local loss across the sequence.
- `effective_lr` reports the optimizer's current learning rate after any `ReduceLROnPlateau` update.
""",
    "src/ndae/evaluation/sampling.py": """
- `build_sample_timeline` uses `logspace` for synthesis times and `linspace` for transition times, then concatenates them into one evaluation timeline.
- The synthesis branch computes `logspace(0, log10(1 + syn_t), synthesis_frames) - 1 - syn_t`, which keeps early warmup samples dense near `t_S`.
- `sample_sequence` draws `z0 ~ N(0, I)` and returns the whole latent trajectory plus the split point between synthesis and transition samples.
""",
    "src/ndae/losses/objectives.py": """
- `overflow_loss = mean((brdf_maps - clamp(brdf_maps, eps, 1))^2)` penalizes values outside the physically valid BRDF interval.
- `init_loss = mean((rendered - target)^2)` is plain per-pixel MSE on tone-mapped crops.
- `local_loss` is a dispatcher: it selects `slice_loss` for `SW` and `gram_loss` for `GRAM` while keeping the trainer-side call site uniform.
""",
    "src/ndae/losses/perceptual.py": """
- Inputs are normalized channelwise as `(x - mean) / std` before entering VGG-19.
- The module returns `[x, block_0(x), ..., block_4(x)]`, so downstream losses can mix image-space and feature-space statistics.
- Between blocks it applies average pooling, matching the texture-statistics pipeline encoded in this repository.
""",
    "src/ndae/losses/swd.py": """
- `gram_matrix(f)` reshapes spatial positions into one axis and computes `(F F^T) / N`, where `N` is the number of spatial samples.
- `gram_loss` sums mean-squared errors between exemplar and sample Gram matrices across all returned VGG feature blocks.
- `sliced_wasserstein_loss` draws random normalized directions, projects exemplar and sample features onto those directions, sorts the projections, and averages squared distances between the sorted projections.
- `slice_loss` normalizes user weights so their average stays `1`, then accumulates weighted sliced-Wasserstein losses across VGG blocks.
""",
    "src/ndae/models/blocks.py": """
- `ConvBlock` applies `proj -> norm -> optional (scale, shift) from time embedding -> activation`.
- When an embedding is present, the block computes `x = x * (scale + 1) + shift`, which is the time-conditioned affine modulation used throughout the UNet.
- `LinearTimeSelfAttention` forms `q`, `k`, and `v`, normalizes `k` with `softmax`, computes `context = einsum(k, v)`, then projects `context` back with `einsum(context, q)`.
""",
    "src/ndae/models/odefunc.py": """
- The module is the explicit ODE adapter `dz/dt = f_theta(t, z)`.
- `ODEFunction.forward(t, state)` forwards directly to the wrapped vector field so `torchdiffeq.odeint` can call it with the solver signature it expects.
""",
    "src/ndae/models/time_embedding.py": """
- `SinusoidalTimeEmbedding` builds frequencies `freqs_i = exp(-i * log(10000) / (half_dim - 1))`.
- The forward pass returns `[sin(t * freqs), cos(t * freqs)]`, so every scalar time is embedded into a deterministic periodic basis.
- `TimeMLP` then applies `Linear -> SiLU -> Linear` to project the sinusoidal basis into the wider conditioning dimension used by the UNet.
""",
    "src/ndae/models/trajectory.py": """
- `TrajectoryModel.forward` computes `states = odeint(odefunc, z0, t_eval, **solver_kwargs)`.
- Input validation enforces `z0.shape == [B, C, H, W]` and `t_eval.shape == [T]` with `T >= 2` before the numerical solver is called.
""",
    "src/ndae/models/unet.py": """
- The model implements the vector field `f_theta(t, x)` used inside the ODE solver.
- Time conditioning is produced once as `t_emb = TimeMLP(t)` and injected into every residual block that accepts `emb_dim`.
- The data path is `init_conv -> downs -> mid -> ups -> final_conv`, with skip tensors concatenated during the up path.
""",
    "src/ndae/rendering/brdf.py": """
- `lambertian = diffuse / pi * max(wi_z, 0)` includes the cosine term directly.
- `distribution_ggx` computes the anisotropic GGX normal distribution using `alpha_u`, `alpha_v`, and the half vector components.
- `geometry_smith = smith_g1_ggx(wi) * smith_g1_ggx(wo)` uses a separable masking-shadowing term.
- `fresnel_schlick = f0 + (1 - f0) * (1 - cos_theta)^5`.
- `cook_torrance = D * G * F / (4 * max(wo_z, eps))` after constructing `h = normalize(wi + wo)`.
""",
    "src/ndae/rendering/geometry.py": """
- `normalize(v) = v / (||v|| + eps)` and `channelwise_normalize(m) = m / (||m||_channel + eps)`.
- `create_meshgrid` maps normalized image coordinates into a physical image plane using `half_width = distance * tan(fov / 2)` and the image aspect ratio.
- `compute_directions` constructs world-space incident and outgoing vectors from the light/camera positions to every surface point.
- `localize` builds tangent and bitangent vectors orthogonal to the normal map, then projects a world-space vector onto that local basis with channelwise dot products.
""",
    "src/ndae/rendering/maps.py": """
- `l2i(x) = 0.5 * x + 0.5` maps latent channels from `[-1, 1]` into `[0, 1]`.
- `i2l(x) = 2 * (x - 0.5)` is the exact inverse mapping.
- `split_latent_maps` interprets the channel axis as `[..., C, H, W]`, exposes the BRDF channels in image space, and leaves the height channels in latent space.
- `clip_maps(maps) = clamp(maps, eps, 1)` is the last validity pass before rendering or overflow loss computation.
""",
    "src/ndae/rendering/normal.py": """
- The module estimates centered finite differences `gx = (h[x+1] - h[x-1]) / 2` and `gy = (h[y-1] - h[y+1]) / 2` after replicate padding.
- It then forms the unnormalized normal `[-gx, -gy, 1]` and divides by its L2 norm to obtain a unit-length normal map.
""",
    "src/ndae/rendering/postprocess.py": """
- `tonemapping(img) = clamp(img, eps, 1)^(1 / gamma)` is the default gamma-space output transform.
- `light_decay(distance) = 1 / (distance^2 + eps)` models inverse-square flash falloff.
- `reinhard(img) = img / (1 + img)` is the alternative compressive tone map kept as a helper.
""",
    "src/ndae/rendering/renderer.py": """
- The renderer computes reflectance from localized `wi` and `wo`, then scales it by flash irradiance before masking invalid back-facing pixels.
- `irradiance = exp(light_intensity) * light_decay(distance)` keeps light intensity in log space while preserving positive output energy.
- Final linear output is `reflectance * irradiance`, with any pixel where `wi_z < 0` or `wo_z < 0` zeroed out.
""",
    "src/ndae/training/schedule.py": """
- Each refresh cycle has one warmup window `[t_init, t_start]` followed by `refresh_rate - 1` generation windows.
- `_sample_strata` draws absolute times with `stratified_uniform`, then converts them into positive deltas so the trainer can march from one carry state to the next.
- `next` returns `RolloutWindow(kind, t0, t1, refresh)` where `refresh=True` only on the warmup step that seeds a new latent state.
""",
    "src/ndae/training/solver.py": """
- `solve_rollout` always integrates exactly two time points, so the returned tensor contains the start state and the end state for one training segment.
- `rollout_warmup` and `rollout_generation` are guard wrappers around `solve_rollout` that enforce the schedule contract before integration begins.
""",
    "src/ndae/training/system.py": """
- `build_svbrdf_system` assembles the vector field, ODE wrapper, trajectory model, solver configuration, camera, light, and renderer choice into one runtime object.
- `render_latent_state` applies `split_latent_maps -> height_to_normal -> clip_maps -> render_svbrdf -> tonemapping`.
- The flashlight intensity is stored as a learnable scalar parameter, which keeps the renderer differentiable with respect to exposure.
""",
    "src/ndae/training/target_sampling.py": """
- Init-stage supervision uses `sample_random_take_spec`, so target pixels and render positions are shuffled consistently through the same index set.
- Local-stage supervision uses `sample_random_crop_spec`, so target crops and render crops share one rectangular region.
- `sample_target_batch` renders each sampled region, tone-maps the rendered batch, and returns `{target, rendered}` for the trainer loss.
- Init-stage rendering forces `normal_map = height_to_normal(zeros_like(height_map))`, while local-stage rendering uses the true height-derived normals.
""",
    "src/ndae/training/trainer.py": """
- Init-stage total loss is `loss_total = init_loss(rendered, target) + init_height_weight * mean(height_map^2) + overflow_weight * overflow_loss(brdf_maps)`.
- Local-stage total loss is `loss_total = local_loss(vgg, rendered, target, loss_type) + overflow_weight * overflow_loss(brdf_maps)`.
- Gradient normalization divides each parameter gradient by `||g|| + 1e-8` before the optimizer step.
- Stage transition resets the optimizer, scheduler, schedule state, carry state, carry time, and cycle index when training crosses from init to local.
""",
}


FAMILY_DESIGN_NOTES: dict[str, tuple[str, ...]] = {
    "scripts": (
        "Keep executable scripts thin so operational behavior lives in importable library code.",
        "Use script wrappers as stable shell entry points without duplicating training logic.",
    ),
    "src/ndae/cli": (
        "Separate argument parsing from runtime assembly so tests can call CLI helpers directly.",
        "Keep CLI modules close to the shell contract and delegate numerical work to the library.",
    ),
    "src/ndae/config": (
        "Split schema, parsing, loading, and validation so configuration errors stay field-scoped and testable.",
        "Prefer explicit dataclasses over untyped dictionaries once the YAML payload has been parsed.",
    ),
    "src/ndae/data": (
        "Represent sampling decisions as reusable specs so target extraction and rendering stay aligned.",
        "Keep exemplar loading deterministic once frame paths have been selected.",
    ),
    "src/ndae/evaluation": (
        "Keep evaluation logic outside the training step so periodic inference does not blur the optimization path.",
        "Reuse the same rendering and loss stack for evaluation to avoid train/eval drift.",
    ),
    "src/ndae/losses": (
        "Separate feature extraction from objective composition so loss modes can share one perceptual frontend.",
        "Keep loss functions pure and batch-local so they are easy to unit test.",
    ),
    "src/ndae/models": (
        "Use small modules with explicit shape validation instead of hiding tensor contracts inside one large model file.",
        "Keep the ODE adapter, trajectory wrapper, embeddings, and blocks independently testable.",
    ),
    "src/ndae/rendering": (
        "Split geometry, BRDF terms, postprocess, and renderer assembly so each numerical layer can be validated independently.",
        "Prefer pure tensor helpers in the math-heavy path to keep gradients transparent.",
    ),
    "src/ndae/training": (
        "Keep immutable config containers separate from the stateful trainer runtime.",
        "Assemble train-time dependencies in a factory so stage resets can rebuild only what needs rebuilding.",
    ),
    "src/ndae/utils": (
        "Isolate workspace and image I/O helpers from the core numerical path.",
    ),
    "tests": (
        "Favor narrow regression tests that lock individual invariants instead of relying only on end-to-end smoke coverage.",
    ),
}


DIRECTORY_ROLE_NOTES: dict[str, str] = {
    "scripts": "This directory mirrors executable shell entry points from the main repository.",
    "src": "This directory mirrors the importable NDAE library tree.",
    "src/ndae": "This package holds the NDAE runtime, rendering stack, losses, training loop, and helper utilities.",
    "tests": "This directory mirrors the repository's regression and smoke test suite.",
}

PIPELINE_OVERRIDES: dict[str, str] = {
    "main.py": "This is the outermost shell-facing training entrypoint. It exists above the package tree and immediately hands control to the CLI layer.",
    "src/ndae/losses/perceptual.py": "This file sits between rendered RGB crops and the texture-statistics objectives. It turns images into a fixed stack of perceptual feature tensors that `gram_loss` and `slice_loss` can compare layer by layer.",
    "src/ndae/losses/swd.py": "This file is the core comparison layer for local texture supervision. The trainer never uses it directly; it calls `local_loss`, which dispatches here when the configured mode is `SW` or `GRAM`.",
    "src/ndae/rendering/renderer.py": "This file is the last numerical stage before losses see an image. It receives already-split BRDF and normal maps, applies geometry and BRDF evaluation, and returns linear-space renderings that other modules tone-map or compare.",
    "src/ndae/training/trainer.py": "This file is the orchestration center of the train-time runtime. It sits above schedule, solver, target sampling, rendering, losses, and evaluation, and it is the place where one optimization step becomes a repeatable state machine.",
    "src/ndae/training/target_sampling.py": "This file bridges exemplar frames and rendered supervision crops. It is where stage-specific sampling policy becomes concrete target tensors that the trainer can feed into loss functions.",
    "src/ndae/models/unet.py": "This file defines the learnable vector field backbone. The ODE adapter and trajectory wrapper treat it as `f_theta(t, x)`, but its internal job is multi-scale feature processing with explicit time modulation.",
    "src/ndae/models/time_embedding.py": "This file is the time-conditioning frontend for the model stack. Every later block that depends on time receives a learned embedding produced here rather than raw scalar time.",
}

TENSOR_OVERRIDES: dict[str, list[str]] = {
    "src/ndae/losses/perceptual.py": [
        "Input to `VGG19Features.forward` must be `[B, 3, H, W]` in the same `[0, 1]` image range used elsewhere in the repository before normalization is applied.",
        "The return value is a Python list of tensors: the original image followed by five progressively deeper VGG feature maps. Spatial resolution shrinks after each average-pooling boundary.",
    ],
    "src/ndae/losses/swd.py": [
        "`gram_matrix` accepts either `[C, H, W]` or `[B, C, H, W]` and flattens spatial positions into one axis before forming channel-channel correlations.",
        "`sliced_wasserstein_loss` expects exemplar and sample tensors with matching rank and channel count. It projects along randomly sampled channel directions, so the last dimension after reshaping is the number of spatial samples being compared.",
        "`slice_loss` consumes the feature lists returned by `VGG19Features`, so its effective inputs are not raw images alone but a stack of multi-scale perceptual activations.",
    ],
    "src/ndae/models/unet.py": [
        "The main forward path expects `x` shaped `[B, C, H, W]` and time `t` shaped either `[]` or `[B]`.",
        "The output shape matches the input latent shape exactly because the module is used as a vector field inside an ODE solver: `f_theta(t, x)` must live in the same state space as `x`.",
        "Skip tensors preserve spatial detail across the downsampling and upsampling path, so intermediate channel widths change but the final output returns to the original spatial resolution.",
    ],
    "src/ndae/rendering/renderer.py": [
        "`brdf_maps` and `normal_map` are accepted as either `[C, H, W]` or `[B, C, H, W]`, but both inputs must agree on batch convention and spatial size.",
        "`positions`, when passed explicitly, must already be `[3, H, W]` and aligned with the current crop. Otherwise the file derives positions from camera geometry or from a requested region inside the full image.",
        "The returned rendering stays in linear RGB. Tone mapping is deliberately left to the caller when the surrounding path wants explicit control over where gamma correction happens.",
    ],
    "src/ndae/training/trainer.py": [
        "`exemplar_frames` are stored as `[N, 3, H, W]`, while latent states and rendered crops are batch-first tensors produced during each training step.",
        "The trainer keeps a carried latent state between continuation windows, so the effective state machine is not just optimizer state but also ODE state, carry time, and cycle position.",
        "Loss tensors are always reduced to scalars before backward, which is why the trainer can normalize gradients parameter by parameter after `loss_total.backward()`.",
    ],
}

WALKTHROUGH_OVERRIDES: dict[str, list[str]] = {
    "src/ndae/losses/perceptual.py": [
        "The module first loads pretrained VGG-19 features and slices them into explicit block boundaries. That choice makes the feature hierarchy visible instead of hiding everything behind one opaque backbone call.",
        "During the forward pass, the image is normalized with ImageNet mean and standard deviation, then pushed through each block in sequence. The code appends the original image before any VGG block output so later losses can mix image-space and feature-space statistics in one interface.",
        "Average pooling is applied between blocks rather than relying on VGG's original max-pooling path. That keeps feature statistics smoother, which matters because the downstream losses compare distributions and correlations rather than class logits.",
    ],
    "src/ndae/losses/swd.py": [
        "The file implements two related ideas: Gram-matrix comparison for second-order feature correlations, and sliced Wasserstein comparison for distribution alignment along random directions.",
        "The SWD path reshapes features so channel directions can be sampled in feature space, not in pixel space. After projection, it sorts exemplar and sample activations before comparing them, which is what makes the metric insensitive to spatial ordering and sensitive to the empirical distribution instead.",
        "The weighted `slice_loss` wrapper exists because the trainer wants one scalar local loss even though the perceptual frontend emits a stack of feature tensors at different scales.",
    ],
    "src/ndae/models/unet.py": [
        "Initialization builds one time MLP, an initial projection block, a mirrored down/up stack, and a final projection head. The structure is deliberately explicit so channel growth and skip usage are easy to inspect.",
        "In the forward pass, scalar time is expanded to batch length when needed, then encoded once into `t_emb`. That embedding is reused at every conditioned block, so time information is global to the whole UNet pass rather than recomputed per layer.",
        "The data path alternates between feature refinement and resolution changes. Down blocks push activations into a skip stack before resampling, the mid block processes the bottleneck representation, and up blocks recover resolution while concatenating the saved skips in reverse order.",
    ],
    "src/ndae/rendering/renderer.py": [
        "The file first canonicalizes batch layout so the renderer has one consistent execution path. This keeps the rest of the code simple even though callers may render a single crop or a whole batch.",
        "Geometry is then resolved: positions come either from an explicitly supplied crop-aligned grid or from camera parameters. From positions, the renderer computes incident and outgoing directions, localizes them with respect to the normal map, and unpacks BRDF parameters into the form expected by the selected BRDF callable.",
        "Only after reflectance is computed does the file apply flash irradiance and invalid-angle masking. That ordering matters because the BRDF should operate on localized directions, while intensity falloff and angle validity are scene-level terms.",
    ],
    "src/ndae/training/trainer.py": [
        "Construction wires together long-lived runtime objects and creates the mutable training state. The trainer deliberately owns optimizer, scheduler, carry state, and metric logging because those pieces evolve step by step.",
        "A single `step()` call chooses the active stage, asks the refresh schedule for the next rollout window, integrates the latent state, projects it into renderable maps, samples the correct target batch for the stage, computes the scalar loss, normalizes gradients, and advances the state machine.",
        "The outer `run()` loop stays thin on purpose. It repeatedly calls `step()`, logs metrics, and triggers evaluation through a separate helper, keeping optimization and evaluation boundaries readable.",
    ],
}


@dataclass
class FunctionInfo:
    name: str
    signature: str
    docstring: str
    calls: list[str]
    raises: list[str]
    source: str


@dataclass
class ClassInfo:
    name: str
    docstring: str
    bases: list[str]
    methods: list[FunctionInfo]
    fields: list[str]


@dataclass
class ModuleInfo:
    rel_path: Path
    docstring: str
    functions: list[FunctionInfo]
    classes: list[ClassInfo]
    imports: list[str]
    imported_ndae_modules: list[str]
    exports: list[str]
    has_main_guard: bool
    source_text: str


PREDICATE_TOKENS = {
    "returns",
    "supports",
    "rejects",
    "reproducible",
    "same",
    "diff",
    "gradient",
    "gradients",
    "zero",
    "positive",
    "negative",
    "range",
    "matches",
    "center",
    "backward",
    "fails",
    "raises",
    "loads",
    "saves",
    "resolves",
    "counts",
    "builds",
    "runs",
    "renders",
    "uses",
    "keeps",
    "can",
    "is",
    "for",
    "when",
    "with",
    "without",
    "in",
    "out",
}

IGNORED_CALL_NAMES = {
    "ValueError",
    "RuntimeError",
    "TypeError",
    "AssertionError",
    "bool",
    "dict",
    "enumerate",
    "float",
    "int",
    "item",
    "len",
    "list",
    "max",
    "min",
    "print",
    "range",
    "round",
    "set",
    "sum",
    "tuple",
    "zip",
}


def first_sentence(text: str) -> str:
    cleaned = normalize_whitespace(text)
    if not cleaned:
        return ""
    if ". " in cleaned:
        return cleaned.split(". ", 1)[0].rstrip(".") + "."
    return cleaned


def format_signature(node: ast.FunctionDef | ast.AsyncFunctionDef) -> str:
    args: list[str] = []
    positional = list(node.args.posonlyargs) + list(node.args.args)
    defaults = [None] * (len(positional) - len(node.args.defaults)) + list(node.args.defaults)
    for index, arg in enumerate(positional):
        rendered = arg.arg
        if index < len(node.args.posonlyargs):
            rendered += ""
        default = defaults[index]
        if default is not None:
            rendered += f"={ast.unparse(default)}"
        args.append(rendered)
        if index + 1 == len(node.args.posonlyargs) and node.args.posonlyargs:
            args[-1] += " /"
    if node.args.vararg is not None:
        args.append(f"*{node.args.vararg.arg}")
    elif node.args.kwonlyargs:
        args.append("*")
    for kwarg, default in zip(node.args.kwonlyargs, node.args.kw_defaults):
        rendered = kwarg.arg
        if default is not None:
            rendered += f"={ast.unparse(default)}"
        args.append(rendered)
    if node.args.kwarg is not None:
        args.append(f"**{node.args.kwarg.arg}")
    return f"{node.name}({', '.join(args)})"


def resolve_import_from(rel_path: Path, module_name: str, level: int) -> str:
    if level == 0:
        return module_name
    package_parts = list(rel_path.with_suffix("").parts[:-1])
    if package_parts and package_parts[-1] == "__init__":
        package_parts = package_parts[:-1]
    if level > len(package_parts):
        return module_name
    base_parts = package_parts[: len(package_parts) - level]
    if module_name:
        base_parts.extend(module_name.split("."))
    return ".".join(base_parts)


def collect_calls(node: ast.AST) -> list[str]:
    names: set[str] = set()
    for child in ast.walk(node):
        if isinstance(child, ast.Call):
            func = child.func
            if isinstance(func, ast.Name):
                if func.id not in IGNORED_CALL_NAMES:
                    names.add(func.id)
            elif isinstance(func, ast.Attribute):
                names.add(func.attr)
    return sorted(names)


def collect_raises(node: ast.AST) -> list[str]:
    messages: list[str] = []
    for child in ast.walk(node):
        if isinstance(child, ast.Raise) and child.exc is not None:
            try:
                rendered = ast.unparse(child.exc)
            except Exception:
                continue
            messages.append(normalize_whitespace(rendered))
    return messages


def parse_module(repo_root: Path, rel_path: Path) -> ModuleInfo:
    source_text = (repo_root / rel_path).read_text(encoding="utf-8")
    tree = ast.parse(source_text)
    functions: list[FunctionInfo] = []
    classes: list[ClassInfo] = []
    imports: list[str] = []
    imported_ndae_modules: set[str] = set()
    exports: list[str] = []
    has_main_guard = '__name__ == "__main__"' in source_text or "__name__ == '__main__'" in source_text

    for node in tree.body:
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.append(alias.name)
                    if alias.name.startswith("ndae"):
                        imported_ndae_modules.add(alias.name)
            else:
                module_name = resolve_import_from(rel_path, node.module or "", node.level)
                imports.append(module_name)
                if module_name.startswith("ndae"):
                    imported_ndae_modules.add(module_name)
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            functions.append(
                FunctionInfo(
                    name=node.name,
                    signature=format_signature(node),
                    docstring=ast.get_docstring(node) or "",
                    calls=collect_calls(node),
                    raises=collect_raises(node),
                    source=ast.get_source_segment(source_text, node) or "",
                )
            )
        elif isinstance(node, ast.ClassDef):
            methods: list[FunctionInfo] = []
            fields: list[str] = []
            for child in node.body:
                if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    methods.append(
                        FunctionInfo(
                            name=child.name,
                            signature=format_signature(child),
                            docstring=ast.get_docstring(child) or "",
                            calls=collect_calls(child),
                            raises=collect_raises(child),
                            source=ast.get_source_segment(source_text, child) or "",
                        )
                    )
                elif isinstance(child, ast.AnnAssign) and isinstance(child.target, ast.Name):
                    fields.append(child.target.id)
            classes.append(
                ClassInfo(
                    name=node.name,
                    docstring=ast.get_docstring(node) or "",
                    bases=[ast.unparse(base) for base in node.bases],
                    methods=methods,
                    fields=fields,
                )
            )
        elif isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "__all__":
                    try:
                        value = ast.literal_eval(node.value)
                    except Exception:
                        value = []
                    if isinstance(value, list):
                        exports.extend(str(item) for item in value if isinstance(item, str))

    return ModuleInfo(
        rel_path=rel_path,
        docstring=ast.get_docstring(tree) or "",
        functions=functions,
        classes=classes,
        imports=sorted({item for item in imports if item}),
        imported_ndae_modules=sorted(imported_ndae_modules),
        exports=exports,
        has_main_guard=has_main_guard,
        source_text=source_text,
    )


def module_path_for(rel_path: Path) -> str:
    if rel_path.parts[:2] == ("src", "ndae"):
        if rel_path.name == "__init__.py":
            return ".".join(rel_path.parts[1:-1])
        return ".".join(rel_path.with_suffix("").parts[1:])
    return ""


def family_key_for(rel_path: Path) -> str:
    parts = rel_path.parts
    if rel_path == ROOT_FILE or parts[0] == "scripts":
        return "scripts"
    if parts[:3] == ("src", "ndae", "cli"):
        return "src/ndae/cli"
    if len(parts) >= 3 and parts[:2] == ("src", "ndae"):
        return "/".join(parts[:3])
    if parts[0] == "tests":
        return "tests"
    return parts[0]


def role_text(module: ModuleInfo, kind: str) -> str:
    family = family_key_for(module.rel_path)
    notes = []
    if family in DIRECTORY_ROLE_NOTES:
        notes.append(DIRECTORY_ROLE_NOTES[family])
    elif family in FAMILY_DESIGN_NOTES:
        notes.append(f"This file belongs to the `{family}` slice of the NDAE repository.")
    if module.docstring:
        notes.append(first_sentence(module.docstring))
    if kind in {"script", "cli"} and module.has_main_guard:
        notes.append("The module also exposes a direct `__main__` execution path.")
    if kind == "init":
        notes.append("Its main job is to define the import surface for the surrounding package.")
    return " ".join(notes) if notes else "This file is part of the NDAE repository implementation."


def module_display_name(module: ModuleInfo) -> str:
    if module.rel_path.parts[:2] == ("src", "ndae"):
        return module.rel_path.with_suffix("").as_posix()
    return module.rel_path.as_posix()


def neighbor_source_paths(module: ModuleInfo, all_modules: dict[Path, ModuleInfo]) -> list[Path]:
    neighbors: list[Path] = []
    source_set = set(all_modules)
    for imported in module.imported_ndae_modules:
        if imported == "ndae":
            candidate = Path("src/ndae/__init__.py")
        else:
            candidate = Path("src") / Path(*imported.split("."))
            if candidate.with_suffix(".py") in source_set:
                candidate = candidate.with_suffix(".py")
            else:
                candidate = candidate / "__init__.py"
        if candidate in source_set and candidate != module.rel_path and candidate not in neighbors:
            neighbors.append(candidate)
    return neighbors[:6]


def file_pipeline_text(module: ModuleInfo, kind: str, neighbors: list[Path]) -> str:
    override = PIPELINE_OVERRIDES.get(module.rel_path.as_posix())
    if override is not None:
        base = override
    elif kind in {"script", "cli"}:
        base = (
            "This file lives on the shell-facing edge of the repository. It translates command-line inputs into calls on the library runtime and keeps operational policy close to the CLI rather than spreading it across unrelated modules."
        )
    elif kind == "test":
        base = "This file sits on the regression boundary of the repository and encodes observable behavior that surrounding implementation files are expected to preserve."
    else:
        base = f"This file is one focused step in the `{family_key_for(module.rel_path)}` slice of the NDAE runtime."
    if neighbors:
        names = ", ".join(f"`{path.name}`" for path in neighbors[:3])
        return base + f" In day-to-day execution it interacts most directly with neighboring modules such as {names}."
    return base


def tensor_shape_notes(module: ModuleInfo, kind: str) -> list[str]:
    override = TENSOR_OVERRIDES.get(module.rel_path.as_posix())
    if override is not None:
        return override
    notes: list[str] = []
    source = module.source_text
    if "[B, C, H, W]" in source or "(B, C, H, W)" in source:
        notes.append("The canonical batched tensor layout in this file is `[B, C, H, W]`, which matches the rest of the image-like runtime.")
    if "[C, H, W]" in source or "(C, H, W)" in source:
        notes.append("Some helpers also accept single-image tensors in `[C, H, W]` format and normalize them internally.")
    if "[N, 3, H, W]" in source:
        notes.append("Sequence-style image tensors use `[N, 3, H, W]`, where `N` indexes exemplar frames or sampled outputs.")
    if kind in {"script", "cli"} or "argparse" in source:
        notes.append("The main inputs are command-line arguments and file paths; outputs are usually files, checkpoints, logs, or process exit codes rather than just returned tensors.")
    if not notes:
        notes.append("This file mostly moves structured Python objects or runtime state rather than introducing a new tensor convention of its own.")
    return notes


def implementation_walkthrough(module: ModuleInfo, kind: str) -> list[str]:
    override = WALKTHROUGH_OVERRIDES.get(module.rel_path.as_posix())
    if override is not None:
        return override
    if kind == "init":
        return [
            "The file gathers selected symbols from neighboring modules so callers can import a stable package surface instead of chasing the internal directory layout.",
            "Most maintenance effort here is about choosing what belongs in the public package contract and what should stay as a deep import.",
        ]
    if kind == "test":
        return [
            "The file is organized around externally observable behavior. Each test group isolates one contract so failures point at a specific regression instead of a vague end-to-end mismatch.",
            "Local helpers stay small because the point of the file is to preserve behavior, not to introduce a second layer of abstraction.",
        ]
    if kind in {"script", "cli"}:
        return [
            "Execution starts from shell-facing argument handling or a direct import, then hands control to the library runtime as quickly as possible.",
            "Any logic kept here is operational rather than numerical: output path resolution, checkpoint selection, dry-run control, user-facing summaries, or failure surfacing.",
        ]
    if module.classes and not module.functions:
        return [
            "Most of the interesting behavior is in class methods, so the best reading strategy is constructor first, then the public methods in the order the rest of the runtime calls them.",
            "This style keeps long-lived state explicit and avoids hiding state transitions in global variables or one-off closures.",
        ]
    return [
        "The file is built from focused helpers rather than one monolithic routine. That makes each contract easier to test and lets neighboring modules reuse only the pieces they need.",
        "Branches in this file usually separate runtime modes or reject invalid inputs early so deeper numerical code can stay cleaner.",
    ]


def why_written_this_way(symbol: FunctionInfo) -> list[str]:
    notes: list[str] = []
    source = symbol.source
    if symbol.raises:
        notes.append("The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.")
    if any(name in source for name in ("torch.rand", "torch.randn", "torch.randint", "torch.randperm")):
        notes.append("Randomness is explicit instead of hidden in module state, which makes training replay and tests reproducible.")
    if any(name in source for name in (".reshape(", ".view(", ".permute(", ".unsqueeze(", ".squeeze(", "torch.stack", "torch.cat")):
        notes.append("Tensor rearrangements are spelled out directly because later code depends on exact channel and batch semantics.")
    if "clamp(" in source or "clamp_min" in source:
        notes.append("Clamping is used as a numerical guardrail so later formulas stay inside the domain they were designed for.")
    if not notes:
        notes.append("The implementation stays intentionally small so the surrounding pipeline can compose it predictably.")
    return notes


def downstream_assumptions(symbol: FunctionInfo) -> list[str]:
    calls = [name for name in symbol.calls if not name.startswith("_")]
    if calls:
        return [f"Callers rely on this symbol to prepare clean inputs for `{', '.join(calls[:5])}` without redoing the same validation or reshaping work."]
    return ["Callers assume the return value already matches the local conventions of the surrounding file and can be consumed directly."]


def deep_dive_for_function(function: FunctionInfo) -> list[str]:
    lines = [
        f"### {function.name}",
        "",
        f"Signature: `{function.signature}`",
        "",
        f"Purpose: {first_sentence(function.docstring) or 'This symbol implements one focused step in the surrounding file.'}",
        "",
        "Expected inputs and outputs:",
        f"- The callable boundary is `{function.signature}`, so the argument order and optional parameters are part of the contract other files depend on.",
        "- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.",
        "",
        "Step-by-step implementation reading guide:",
    ]
    step = 1
    if function.raises:
        lines.append(f"{step}. Read the guard clauses first; they define the cases the rest of the function refuses to handle.")
        step += 1
    if function.calls:
        lines.append(f"{step}. Follow the delegated helpers `{', '.join(function.calls[:6])}` to see how this symbol sequences lower-level work.")
        step += 1
    if any(name in function.source for name in ("torch.rand", "torch.randn", "torch.randint", "torch.randperm")):
        lines.append(f"{step}. Track where stochastic values come from, because that determines reproducibility and how tests seed the behavior.")
        step += 1
    if any(name in function.source for name in (".reshape(", ".view(", ".permute(", ".unsqueeze(", ".squeeze(", "torch.stack", "torch.cat")):
        lines.append(f"{step}. Pay attention to layout changes; this is usually where the function adapts data for the next subsystem.")
        step += 1
    lines.append(f"{step}. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.")
    lines.extend(
        [
            "",
            "Why it is implemented this way:",
        ]
    )
    for note in why_written_this_way(function):
        lines.append(f"- {note}")
    lines.extend(
        [
            "",
            "What downstream code assumes:",
        ]
    )
    for note in downstream_assumptions(function):
        lines.append(f"- {note}")
    lines.append("")
    return lines


def deep_dive_for_class(cls: ClassInfo) -> list[str]:
    lines = [
        f"### {cls.name}",
        "",
        f"Role: {first_sentence(cls.docstring) or 'This class owns one stateful runtime component.'}",
        "",
        f"Inheritance: `{', '.join(cls.bases) if cls.bases else 'object'}`",
        "",
    ]
    if cls.fields:
        lines.append("Owned fields:")
        for field in cls.fields:
            lines.append(f"- `{field}`")
        lines.append("")
    public_methods = [method for method in cls.methods if not method.name.startswith("_")]
    if public_methods:
        lines.append("Public methods:")
        for method in public_methods:
            lines.append(f"- `{method.signature}`: {first_sentence(method.docstring) or 'Key method on this runtime object.'}")
        lines.append("")
        lines.append("How the methods should be read:")
        for method in public_methods:
            lines.append(f"- `{method.name}` is one stage in the class-level control flow. Read its guard clauses, then the helper calls `{', '.join(method.calls[:5]) or 'inside this class'}` to understand how state moves forward.")
        lines.append("")
    lines.extend(
        [
            "How to read this class:",
            "- Start from construction or declared fields to see what long-lived state the object owns.",
            "- Then read public methods in the order the rest of the runtime calls them; that is the real control flow.",
            "- Treat private helpers as local refactoring aids rather than as a second independent API.",
            "",
        ]
    )
    return lines


def related_tests_for(rel_path: Path, modules: dict[Path, ModuleInfo]) -> list[Path]:
    if rel_path.parts and rel_path.parts[0] == "tests":
        return []
    module_name = module_path_for(rel_path)
    stem = rel_path.stem
    candidates: list[tuple[int, Path]] = []
    for path, module in modules.items():
        if not path.parts or path.parts[0] != "tests":
            continue
        score = 0
        if module_name and module_name in module.source_text:
            score += 8
        if stem in module.source_text:
            score += 3
        if rel_path.name in module.source_text:
            score += 4
        if rel_path == ROOT_FILE and "run_train_cli" in module.source_text:
            score += 2
        if rel_path.parts and rel_path.parts[0] == "scripts" and stem in path.stem:
            score += 5
        if score > 0:
            candidates.append((score, path))
    return [path for _, path in sorted(candidates, reverse=True)[:6]]


def related_sources_for_test(rel_path: Path, module: ModuleInfo, target_sources: list[Path]) -> list[Path]:
    if rel_path.parts[0] != "tests":
        return []
    source_set = set(target_sources)
    results: list[Path] = []
    for imported in module.imported_ndae_modules:
        if imported == "ndae":
            candidate = Path("src/ndae/__init__.py")
        else:
            candidate = Path("src") / Path(*imported.split("."))
            if candidate.with_suffix(".py") in source_set:
                candidate = candidate.with_suffix(".py")
            else:
                candidate = candidate / "__init__.py"
        if candidate in source_set and candidate not in results:
            results.append(candidate)
    if results:
        return results
    heuristic = rel_path.stem.removeprefix("test_")
    for candidate in target_sources:
        if candidate.parts[0] != "src":
            continue
        if heuristic in candidate.stem or heuristic in candidate.as_posix():
            results.append(candidate)
    return results[:6]


def test_groups(module: ModuleInfo) -> dict[str, list[str]]:
    groups: dict[str, list[str]] = {}
    for function in module.functions:
        if not function.name.startswith("test_"):
            continue
        tokens = function.name.removeprefix("test_").split("_")
        subject: list[str] = []
        for token in tokens:
            if token in PREDICATE_TOKENS and subject:
                break
            subject.append(token)
        key = "_".join(subject) if subject else function.name
        groups.setdefault(key, []).append(function.name)
    return groups


def doc_path_for(rel_path: Path) -> Path:
    return source_to_doc(rel_path)


def link_list(current_doc: Path, rel_paths: list[Path]) -> list[str]:
    return [f"- {markdown_link(path.name, current_doc, doc_path_for(path))}" for path in rel_paths]


def render_init_page(module: ModuleInfo, related_tests: list[Path]) -> str:
    current_doc = doc_path_for(module.rel_path)
    lines = [
        f"# {title_for_source(module.rel_path)}",
        "",
        f"Source path: `{module.rel_path.as_posix()}`",
        "",
        "## Role",
        "",
        role_text(module, "init"),
        "",
        "## Exported API Surface",
        "",
    ]
    if module.exports:
        lines.extend(f"- `{name}`" for name in module.exports)
    else:
        lines.append("- No explicit `__all__` export list is declared in this file.")
    lines.extend(
        [
            "",
            "## Re-export Design",
            "",
            "This file centralizes symbols that the rest of the repository treats as package-level vocabulary. The goal is not to hide where implementations live, but to give callers one stable import surface even if internal files evolve over time.",
            "",
            "## Import Side Effects",
            "",
            "Importing this file re-exports symbols from child modules and may expose registries, dataclasses, or helper functions those modules define. It does not perform dataset loading, checkpoint I/O, or runtime mutation on import.",
            "",
            "## How Downstream Code Uses These Exports",
            "",
        ]
    )
    if module.exports:
        lines.append("- Higher-level modules and tests use these exports to keep imports short and to avoid depending on every internal filename directly.")
        lines.append("- The exported names usually define the package boundary that other slices of the runtime are expected to rely on.")
    else:
        lines.append("- Downstream code currently treats this file more as a namespace anchor than as a heavily curated export list.")
    lines.extend(
        [
            "",
            "## Formula Mapping",
            "",
            "Formula mapping: not applicable. This file shapes import ergonomics and public package boundaries rather than introducing a numerical transform.",
            "",
            "## Related Tests",
            "",
        ]
    )
    if related_tests:
        lines.extend(link_list(current_doc, related_tests))
    else:
        lines.append("- No direct test file imports this package entrypoint explicitly.")
    lines.append("")
    return "\n".join(lines)


def render_source_page(module: ModuleInfo, related_tests: list[Path], kind: str, all_modules: dict[Path, ModuleInfo]) -> str:
    current_doc = doc_path_for(module.rel_path)
    neighbors = neighbor_source_paths(module, all_modules)
    lines = [
        f"# {title_for_source(module.rel_path)}",
        "",
        f"Source path: `{module.rel_path.as_posix()}`",
        "",
        "## Role",
        "",
        role_text(module, kind),
        "",
        "## Where This File Sits In The Pipeline",
        "",
        file_pipeline_text(module, kind, neighbors),
        "",
        "## Inputs, Outputs, And Tensor Shapes",
        "",
    ]
    for note in tensor_shape_notes(module, kind):
        lines.append(f"- {note}")
    lines.extend(
        [
            "",
            "## Implementation Walkthrough",
            "",
        ]
    )
    for paragraph in implementation_walkthrough(module, kind):
        lines.append(paragraph)
        lines.append("")
    lines.extend(
        [
            "## Function And Class Deep Dive",
            "",
        ]
    )
    if not module.functions and not module.classes:
        lines.append("This file is intentionally thin. Its value comes from the contract it exposes or the module it delegates into, not from a large amount of internal logic.")
        lines.append("")
    for cls in module.classes:
        lines.extend(deep_dive_for_class(cls))
    for function in module.functions:
        lines.extend(deep_dive_for_function(function))
    lines.extend(
        [
            "## Formula Mapping",
            "",
        ]
    )
    override = MATH_OVERRIDES.get(module.rel_path.as_posix())
    if override is None:
        if kind in {"script", "cli"}:
            lines.append("Formula mapping: not applicable. This file mainly defines command flow, delegation boundaries, and operational side effects rather than a standalone numerical transform.")
        else:
            lines.append("Formula mapping: not applicable. This file mainly defines schema, orchestration, or utility behavior rather than a standalone equation.")
    else:
        lines.extend(textwrap.dedent(override).strip().splitlines())
    lines.extend(
        [
            "",
            "## Design Decisions",
            "",
        ]
    )
    family_notes = FAMILY_DESIGN_NOTES.get(family_key_for(module.rel_path), ())
    if family_notes:
        for note in family_notes:
            lines.append(f"- {note}")
    else:
        lines.append("- Keep this file narrowly scoped so the surrounding runtime can compose it without hidden state.")
    if kind in {"script", "cli"}:
        lines.append("- Keep shell-facing code thinner than numerical code so operational changes do not silently alter the math path.")
    lines.extend(
        [
            "",
            "## Common Failure Modes",
            "",
        ]
    )
    raise_lines = sorted({raise_text for function in module.functions for raise_text in function.raises})
    if raise_lines:
        for raise_text in raise_lines[:10]:
            lines.append(f"- Guard clause or surfaced failure: `{raise_text}`")
    elif kind in {"script", "cli"}:
        lines.append("- Most failures here come from delegated library calls, CLI argument misuse, or filesystem state rather than bespoke numerical checks.")
    else:
        lines.append("- There are no custom guard clauses in this file; failures mostly come from imported runtime code or invalid upstream tensors.")
    lines.extend(
        [
            "",
            "## How This Connects To Neighboring Files",
            "",
        ]
    )
    if neighbors:
        for path in neighbors:
            lines.append(f"- {markdown_link(path.name, current_doc, doc_path_for(path))} supplies or consumes part of this file's contract.")
    else:
        lines.append("- This file is relatively self-contained; its closest neighbors are package-level imports rather than one obvious sibling file.")
    lines.extend(
        [
            "",
            "## Related Tests",
            "",
        ]
    )
    if related_tests:
        lines.extend(link_list(current_doc, related_tests))
    else:
        lines.append("- No direct test file was matched to this module by the documentation generator.")
    lines.append("")
    return "\n".join(lines)


def render_test_page(module: ModuleInfo, related_sources: list[Path]) -> str:
    current_doc = doc_path_for(module.rel_path)
    groups = test_groups(module)
    lines = [
        f"# {title_for_source(module.rel_path)}",
        "",
        f"Source path: `{module.rel_path.as_posix()}`",
        "",
        "## System Under Test",
        "",
    ]
    if related_sources:
        lines.extend(link_list(current_doc, related_sources))
    else:
        lines.append("- This test file exercises repository behavior through indirect imports or command execution paths.")
    lines.extend(
        [
            "",
            "## Fixtures And Helpers",
            "",
        ]
    )
    helper_functions = [function for function in module.functions if not function.name.startswith("test_")]
    if helper_functions:
        for function in helper_functions:
            lines.append(f"- `{function.signature}`")
    else:
        lines.append("- No file-local fixtures or helpers are declared; this file relies on inline test bodies or shared helpers.")
    lines.extend(
        [
            "",
            "## Test Groups",
            "",
        ]
    )
    if groups:
        for subject, names in groups.items():
            lines.append(f"- `{subject}`: {', '.join(f'`{name}`' for name in names)}")
    else:
        lines.append("- This file does not declare `test_*` functions.")
    lines.extend(
        [
            "",
            "## What Each Group Proves",
            "",
        ]
    )
    if groups:
        for subject, names in groups.items():
            lines.append(f"- `{subject}` proves that the implementation still satisfies the contract exercised by {', '.join(f'`{name}`' for name in names[:3])}.")
    else:
        lines.append("- Protects whichever runtime path is imported by this file.")
    lines.extend(
        [
            "",
            "## Regression Intent",
            "",
            "These tests are intended to catch behavior drift in the mirrored runtime paths, not just import-time failures.",
            "",
            "## Remaining Gaps",
            "",
            "The file only covers the explicit cases encoded in its test functions; full-sequence numerical drift still depends on broader smoke and integration coverage.",
            "",
            "## Related Source Files",
            "",
        ]
    )
    if related_sources:
        lines.extend(link_list(current_doc, related_sources))
    else:
        lines.append("- No direct source file link was inferred automatically.")
    lines.append("")
    return "\n".join(lines)


def render_directory_index(rel_dir: Path, child_dirs: list[Path], child_files: list[Path]) -> str:
    lines = [
        f"# {title_for_directory(rel_dir)}",
        "",
    ]
    if rel_dir != Path():
        lines.append(f"Source directory: `{rel_dir.as_posix()}/`")
        lines.append("")
    lines.extend(
        [
            "## Role",
            "",
            DIRECTORY_ROLE_NOTES.get(rel_dir.as_posix(), "This page mirrors a source directory from the main NDAE repository so navigation follows the repository layout."),
            "",
            "## Contents",
            "",
        ]
    )
    current_doc = rel_dir / "index.md" if rel_dir != Path() else Path("index.md")
    for child_dir in child_dirs:
        target = child_dir / "index.md"
        lines.append(f"- {markdown_link(f'{child_dir.name}/', current_doc, target)}")
    for child_file in child_files:
        target = source_to_doc(child_file)
        lines.append(f"- {markdown_link(child_file.name, current_doc, target)}")
    lines.extend(
        [
            "",
            "## Notes",
            "",
            "This section is repository-structured reference material. The page exists to keep MkDocs navigation aligned with the source tree.",
            "",
        ]
    )
    return "\n".join(lines)


def render_home_page(target_sources: list[Path]) -> str:
    lines = [
        "# Home",
        "",
        "This site is a repository-mirrored reference for the `ndae` implementation. Every tracked implementation file under `main.py`, `scripts/`, `src/`, and `tests/` has a matching page, and the navigation order follows the source tree instead of a tutorial sequence.",
        "",
        "## Coverage",
        "",
        f"- Documented implementation files: `{len(target_sources)}`",
        "- Mirrored roots: `main.py`, `scripts/`, `src/`, `tests/`",
        "- Generated pages use fixed templates so source files, CLI modules, package entrypoints, and tests stay consistent.",
        "",
        "## Navigation",
        "",
        "- Top-level navigation keeps the repository order: `Home`, `main.py`, `scripts/`, `src/`, `tests/`.",
        "- Every mirrored directory has its own `index.md`, so sections remain clickable without a custom MkDocs navigation plugin.",
        "- Leaf pages use the literal source filename as the page title, including `__init__.py`.",
        "",
        "## Maintenance",
        "",
        "- Regenerate the mirrored docs with `python3 scripts/generate_repo_docs.py --repo-root ../ndae --docs-root docs`.",
        "- Validate coverage, section headings, source-path headers, and banned wording with `python3 scripts/validate_repo_docs.py --repo-root ../ndae --docs-root docs --fail-on-extra`.",
        "- Build locally with `mkdocs build --strict`.",
        "",
    ]
    return "\n".join(lines)


def generate_docs(repo_root: Path, docs_root: Path) -> None:
    target_sources = list_target_sources(repo_root)
    modules = {path: parse_module(repo_root, path) for path in target_sources}

    if docs_root.exists():
        shutil.rmtree(docs_root)
    docs_root.mkdir(parents=True, exist_ok=True)

    (docs_root / "index.md").write_text(render_home_page(target_sources), encoding="utf-8")

    for directory in expected_doc_directories(repo_root):
        if directory == Path():
            continue
        child_dirs = sorted(
            candidate
            for candidate in expected_doc_directories(repo_root)
            if candidate.parent == directory and candidate != directory
        )
        child_files = sorted(path for path in target_sources if path.parent == directory)
        target = docs_root / directory / "index.md"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(
            render_directory_index(directory, child_dirs, child_files),
            encoding="utf-8",
        )

    for path, module in modules.items():
        rules = page_rules_for(path)
        related_tests = related_tests_for(path, modules)
        related_sources = related_sources_for_test(path, module, target_sources)
        target = docs_root / source_to_doc(path)
        target.parent.mkdir(parents=True, exist_ok=True)
        if rules.kind == "test":
            content = render_test_page(module, related_sources)
        elif rules.kind == "init":
            content = render_init_page(module, related_tests)
        else:
            content = render_source_page(module, related_tests, rules.kind, modules)
        target.write_text(content, encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate repository-mirrored NDAE docs.")
    parser.add_argument("--repo-root", type=Path, default=Path("../ndae"))
    parser.add_argument("--docs-root", type=Path, default=Path("docs"))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    generate_docs(args.repo_root.resolve(), args.docs_root.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
