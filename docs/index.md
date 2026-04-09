# Home

This site is a repository-mirrored reference for the `ndae` implementation. Every tracked implementation file under `main.py`, `scripts/`, `src/`, and `tests/` has a matching page, and the navigation order follows the source tree instead of a tutorial sequence.

## Coverage

- Documented implementation files: `70`
- Mirrored roots: `main.py`, `scripts/`, `src/`, `tests/`
- Generated pages use fixed templates so source files, CLI modules, package entrypoints, and tests stay consistent.

## Navigation

- Top-level navigation keeps the repository order: `Home`, `main.py`, `scripts/`, `src/`, `tests/`.
- Every mirrored directory has its own `index.md`, so sections remain clickable without a custom MkDocs navigation plugin.
- Leaf pages use the literal source filename as the page title, including `__init__.py`.

## Maintenance

- Regenerate the mirrored docs with `python3 scripts/generate_repo_docs.py --repo-root ../ndae --docs-root docs`.
- Validate coverage, section headings, source-path headers, and banned wording with `python3 scripts/validate_repo_docs.py --repo-root ../ndae --docs-root docs --fail-on-extra`.
- Build locally with `mkdocs build --strict`.
