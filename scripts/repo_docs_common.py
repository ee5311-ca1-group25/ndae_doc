#!/usr/bin/env python3

from __future__ import annotations

from dataclasses import dataclass
import os
from pathlib import Path
import re
import subprocess


TARGET_ROOTS = ("scripts", "src", "tests")
ROOT_FILE = Path("main.py")

BANNED_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("lecture wording", re.compile(r"\blecture\b", re.IGNORECASE)),
    ("course wording", re.compile(r"\bcourse\b", re.IGNORECASE)),
    ("course materials wording", re.compile(r"course materials", re.IGNORECASE)),
    ("lecture plan wording", re.compile(r"lecture plan", re.IGNORECASE)),
    ("train_plan wording", re.compile(r"train_plan", re.IGNORECASE)),
    ("course lecture link", re.compile(r"course/lecture[^)\s`]*", re.IGNORECASE)),
)


@dataclass(frozen=True)
class PageRules:
    kind: str
    required_sections: tuple[str, ...]


SCRIPT_RULES = PageRules(
    kind="script",
    required_sections=(
        "Role",
        "Where This File Sits In The Pipeline",
        "Inputs, Outputs, And Tensor Shapes",
        "Implementation Walkthrough",
        "Function And Class Deep Dive",
        "Formula Mapping",
        "Design Decisions",
        "Common Failure Modes",
        "How This Connects To Neighboring Files",
        "Related Tests",
    ),
)

CLI_RULES = PageRules(
    kind="cli",
    required_sections=(
        "Role",
        "Where This File Sits In The Pipeline",
        "Inputs, Outputs, And Tensor Shapes",
        "Implementation Walkthrough",
        "Function And Class Deep Dive",
        "Formula Mapping",
        "Design Decisions",
        "Common Failure Modes",
        "How This Connects To Neighboring Files",
        "Related Tests",
    ),
)

INIT_RULES = PageRules(
    kind="init",
    required_sections=(
        "Role",
        "Exported API Surface",
        "Re-export Design",
        "Import Side Effects",
        "How Downstream Code Uses These Exports",
        "Formula Mapping",
        "Related Tests",
    ),
)

TEST_RULES = PageRules(
    kind="test",
    required_sections=(
        "System Under Test",
        "Fixtures And Helpers",
        "Test Groups",
        "What Each Group Proves",
        "Regression Intent",
        "Remaining Gaps",
        "Related Source Files",
    ),
)

SOURCE_RULES = PageRules(
    kind="source",
    required_sections=(
        "Role",
        "Where This File Sits In The Pipeline",
        "Inputs, Outputs, And Tensor Shapes",
        "Implementation Walkthrough",
        "Function And Class Deep Dive",
        "Formula Mapping",
        "Design Decisions",
        "Common Failure Modes",
        "How This Connects To Neighboring Files",
        "Related Tests",
    ),
)


def list_tracked_files(repo_root: Path) -> list[Path]:
    output = subprocess.check_output(
        ["git", "-C", str(repo_root), "ls-files"],
        text=True,
    )
    return [Path(line) for line in output.splitlines() if line]


def is_target_source(rel_path: Path) -> bool:
    if rel_path == ROOT_FILE:
        return True
    if rel_path.suffix != ".py":
        return False
    if not rel_path.parts:
        return False
    return rel_path.parts[0] in TARGET_ROOTS


def list_target_sources(repo_root: Path) -> list[Path]:
    return sorted(path for path in list_tracked_files(repo_root) if is_target_source(path))


def source_to_doc(rel_path: Path) -> Path:
    if rel_path.suffix != ".py":
        raise ValueError(f"Expected a Python source path, got {rel_path}")
    return rel_path.with_suffix(".md")


def expected_doc_pages(repo_root: Path) -> list[Path]:
    return [source_to_doc(path) for path in list_target_sources(repo_root)]


def expected_doc_directories(repo_root: Path) -> list[Path]:
    directories = {
        Path(),
    }
    for doc_path in expected_doc_pages(repo_root):
        current = doc_path.parent
        while True:
            directories.add(current)
            if current == Path():
                break
            current = current.parent
    return sorted(directories, key=lambda path: (len(path.parts), path.as_posix()))


def page_rules_for(rel_path: Path) -> PageRules:
    if rel_path == ROOT_FILE or rel_path.parts[0] == "scripts":
        return SCRIPT_RULES
    if rel_path.parts[:2] == ("src", "ndae") and len(rel_path.parts) >= 3 and rel_path.parts[2] == "cli":
        return CLI_RULES
    if rel_path.name == "__init__.py":
        return INIT_RULES
    if rel_path.parts[0] == "tests":
        return TEST_RULES
    return SOURCE_RULES


def title_for_source(rel_path: Path) -> str:
    return rel_path.name


def title_for_directory(rel_path: Path) -> str:
    if rel_path == Path():
        return "Home"
    return f"{rel_path.name}/"


def markdown_link(label: str, current_doc: Path, target_doc: Path) -> str:
    rel = os.path.relpath(target_doc, start=current_doc.parent or Path("."))
    rel = Path(rel).as_posix()
    return f"[{label}]({rel})"


def normalize_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()
