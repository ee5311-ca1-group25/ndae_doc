#!/usr/bin/env python3

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys

from repo_docs_common import (
    BANNED_PATTERNS,
    expected_doc_directories,
    expected_doc_pages,
    list_target_sources,
    page_rules_for,
    source_to_doc,
    title_for_source,
)


HEADING_RE = re.compile(r"^## (.+)$", re.MULTILINE)


def validate_docs(repo_root: Path, docs_root: Path, fail_on_extra: bool) -> list[str]:
    errors: list[str] = []
    target_sources = list_target_sources(repo_root)
    expected_pages = {source_to_doc(path): path for path in target_sources}
    expected_indexes = {
        (directory / "index.md" if directory != Path() else Path("index.md"))
        for directory in expected_doc_directories(repo_root)
    }

    actual_pages = {
        path.relative_to(docs_root)
        for path in docs_root.rglob("*.md")
        if path.is_file()
    }

    missing_pages = sorted(set(expected_pages) - actual_pages)
    for page in missing_pages:
        errors.append(f"Missing documentation page: {page.as_posix()}")

    missing_indexes = sorted(path for path in expected_indexes if path not in actual_pages)
    for page in missing_indexes:
        errors.append(f"Missing directory index page: {page.as_posix()}")

    if fail_on_extra:
        unexpected = sorted(actual_pages - set(expected_pages) - expected_indexes)
        for page in unexpected:
            errors.append(f"Unexpected documentation page: {page.as_posix()}")

    for doc_path, source_path in sorted(expected_pages.items()):
        absolute_doc = docs_root / doc_path
        if not absolute_doc.exists():
            continue
        content = absolute_doc.read_text(encoding="utf-8")
        lines = content.splitlines()
        expected_title = f"# {title_for_source(source_path)}"
        if not lines or lines[0] != expected_title:
            errors.append(
                f"{doc_path.as_posix()}: expected first line `{expected_title}`"
            )
        expected_source_line = f"Source path: `{source_path.as_posix()}`"
        if expected_source_line not in lines[:6]:
            errors.append(
                f"{doc_path.as_posix()}: missing exact source-path header `{expected_source_line}`"
            )
        headings = set(HEADING_RE.findall(content))
        for heading in page_rules_for(source_path).required_sections:
            if heading not in headings:
                errors.append(
                    f"{doc_path.as_posix()}: missing required section `## {heading}`"
                )

    files_to_scan = [path for path in docs_root.rglob("*.md") if path.is_file()]
    mkdocs_file = docs_root.parent / "mkdocs.yml"
    if mkdocs_file.exists():
        files_to_scan.append(mkdocs_file)
    for path in files_to_scan:
        content = path.read_text(encoding="utf-8")
        for label, pattern in BANNED_PATTERNS:
            if pattern.search(content):
                errors.append(f"{path.relative_to(docs_root.parent).as_posix()}: banned {label}")

    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate repository-mirrored NDAE docs.")
    parser.add_argument("--repo-root", type=Path, required=True)
    parser.add_argument("--docs-root", type=Path, default=Path("docs"))
    parser.add_argument("--fail-on-extra", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    errors = validate_docs(
        repo_root=args.repo_root.resolve(),
        docs_root=args.docs_root.resolve(),
        fail_on_extra=args.fail_on_extra,
    )
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print("Documentation validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
