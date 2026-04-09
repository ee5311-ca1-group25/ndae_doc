# download_svbrdf_mini.py

Source path: `scripts/download_svbrdf_mini.py`

## Role

This directory mirrors executable shell entry points from the main repository. Download a tiny local SVBRDF subset from the official NDAE dataset. The module also exposes a direct `__main__` execution path.

## Where This File Sits In The Pipeline

This file lives on the shell-facing edge of the repository. It translates command-line inputs into calls on the library runtime and keeps operational policy close to the CLI rather than spreading it across unrelated modules.

## Inputs, Outputs, And Tensor Shapes

- The main inputs are command-line arguments and file paths; outputs are usually files, checkpoints, logs, or process exit codes rather than just returned tensors.

## Implementation Walkthrough

Execution starts from shell-facing argument handling or a direct import, then hands control to the library runtime as quickly as possible.

Any logic kept here is operational rather than numerical: output path resolution, checkpoint selection, dry-run control, user-facing summaries, or failure surfacing.

## Function And Class Deep Dive

### DownloadError

Role: Raised when the SVBRDF mini download flow fails.

Inheritance: `RuntimeError`

How to read this class:
- Start from construction or declared fields to see what long-lived state the object owns.
- Then read public methods in the order the rest of the runtime calls them; that is the real control flow.
- Treat private helpers as local refactoring aids rather than as a second independent API.

### DownloadManifest

Role: This class owns one stateful runtime component.

Inheritance: `object`

Owned fields:
- `exemplar`
- `selected_files`
- `output_dir`
- `source_page_url`
- `source_download_url`
- `generated_at_utc`

How to read this class:
- Start from construction or declared fields to see what long-lived state the object owns.
- Then read public methods in the order the rest of the runtime calls them; that is the real control flow.
- Treat private helpers as local refactoring aids rather than as a second independent API.

### build_parser

Signature: `build_parser()`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `build_parser()`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `ArgumentParser, add_argument, time` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `ArgumentParser, add_argument, time` without redoing the same validation or reshaping work.

### run_pwcli

Signature: `run_pwcli(session_name, *args, timeout=120)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `run_pwcli(session_name, *args, timeout=120)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `DownloadError, join, run, strip` to see how this symbol sequences lower-level work.
3. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `DownloadError, join, run, strip` without redoing the same validation or reshaping work.

### normalize_session_name

Signature: `normalize_session_name(raw_name)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `normalize_session_name(raw_name)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `encode, hexdigest, rstrip, sha1, strip, sub` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `encode, hexdigest, rstrip, sha1, strip` without redoing the same validation or reshaping work.

### ensure_prerequisites

Signature: `ensure_prerequisites()`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `ensure_prerequisites()`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `DownloadError, which` to see how this symbol sequences lower-level work.
3. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `DownloadError, which` without redoing the same validation or reshaping work.

### open_in_system_browser

Signature: `open_in_system_browser(url)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `open_in_system_browser(url)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `open` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `open` without redoing the same validation or reshaping work.

### open_dataset_page

Signature: `open_dataset_page(session_name, page_url)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `open_dataset_page(session_name, page_url)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `run_pwcli` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `run_pwcli` without redoing the same validation or reshaping work.

### close_dataset_page

Signature: `close_dataset_page(session_name)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `close_dataset_page(session_name)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `run_pwcli` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `run_pwcli` without redoing the same validation or reshaping work.

### get_page_title

Signature: `get_page_title(session_name)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `get_page_title(session_name)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `group, run_pwcli, search` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `group, run_pwcli, search` without redoing the same validation or reshaping work.

### wait_for_cookie_header

Signature: `wait_for_cookie_header(session_name, timeout_s=30)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `wait_for_cookie_header(session_name, timeout_s=30)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `DownloadError, any, get_page_title, join, parse_rdr_cookies, run_pwcli` to see how this symbol sequences lower-level work.
3. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `DownloadError, any, get_page_title, join, parse_rdr_cookies` without redoing the same validation or reshaping work.

### parse_rdr_cookies

Signature: `parse_rdr_cookies(cookie_output)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `parse_rdr_cookies(cookie_output)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `append, group, search, splitlines, strip` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `append, group, search, splitlines, strip` without redoing the same validation or reshaping work.

### normalize_cookie_header

Signature: `normalize_cookie_header(raw)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `normalize_cookie_header(raw)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `DownloadError, append, group, join, lower, replace` to see how this symbol sequences lower-level work.
3. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `DownloadError, append, group, join, lower` without redoing the same validation or reshaping work.

### parse_manual_input

Signature: `parse_manual_input(raw)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `parse_manual_input(raw)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `DownloadError, normalize_cookie_header, startswith, strip` to see how this symbol sequences lower-level work.
3. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `DownloadError, normalize_cookie_header, startswith, strip` without redoing the same validation or reshaping work.

### prompt_for_manual_access

Signature: `prompt_for_manual_access(page_url, download_url)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `prompt_for_manual_access(page_url, download_url)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `DownloadError, dedent, input, isatty, open_in_system_browser, parse_manual_input` to see how this symbol sequences lower-level work.
3. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `DownloadError, dedent, input, isatty, open_in_system_browser` without redoing the same validation or reshaping work.

### mint_signed_url

Signature: `mint_signed_url(cookie_header, download_url, referer)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `mint_signed_url(cookie_header, download_url, referer)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `DownloadError, Request, geturl, urlopen` to see how this symbol sequences lower-level work.
3. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `DownloadError, Request, geturl, urlopen` without redoing the same validation or reshaping work.

### resolve_signed_url

Signature: `resolve_signed_url(signed_url, cookie_header, download_url, referer)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `resolve_signed_url(signed_url, cookie_header, download_url, referer)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `DownloadError, mint_signed_url` to see how this symbol sequences lower-level work.
3. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `DownloadError, mint_signed_url` without redoing the same validation or reshaping work.

### list_archive_jpgs

Signature: `list_archive_jpgs(signed_url, exemplar=None)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `list_archive_jpgs(signed_url, exemplar=None)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `RemoteZip, endswith, lower, namelist, sorted, startswith` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `RemoteZip, endswith, lower, namelist, sorted` without redoing the same validation or reshaping work.

### list_exemplars

Signature: `list_exemplars(signed_url)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `list_exemplars(signed_url)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `list_archive_jpgs, sorted, split` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `list_archive_jpgs, sorted, split` without redoing the same validation or reshaping work.

### select_uniform_files

Signature: `select_uniform_files(files, count)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `select_uniform_files(files, count)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `DownloadError, append, sort` to see how this symbol sequences lower-level work.
3. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `DownloadError, append, sort` without redoing the same validation or reshaping work.

### resolve_explicit_files

Signature: `resolve_explicit_files(files, requested)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `resolve_explicit_files(files, requested)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `DownloadError, Path, append` to see how this symbol sequences lower-level work.
3. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `DownloadError, Path, append` without redoing the same validation or reshaping work.

### download_selected_files

Signature: `download_selected_files(selected_files, output_dir, cookie_header, download_url, referer, overwrite, signed_url=None)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `download_selected_files(selected_files, output_dir, cookie_header, download_url, referer, overwrite, signed_url=None)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `Path, RemoteZip, exists, mkdir, read, resolve_signed_url` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `Path, RemoteZip, exists, mkdir, read` without redoing the same validation or reshaping work.

### write_manifest

Signature: `write_manifest(exemplar, selected_files, output_dir, page_url, download_url)`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `write_manifest(exemplar, selected_files, output_dir, page_url, download_url)`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Follow the delegated helpers `DownloadManifest, asdict, dumps, isoformat, now, str` to see how this symbol sequences lower-level work.
2. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The implementation stays intentionally small so the surrounding pipeline can compose it predictably.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `DownloadManifest, asdict, dumps, isoformat, now` without redoing the same validation or reshaping work.

### main

Signature: `main()`

Purpose: This symbol implements one focused step in the surrounding file.

Expected inputs and outputs:
- The callable boundary is `main()`, so the argument order and optional parameters are part of the contract other files depend on.
- Return values follow the local file conventions and are intended to slot into the next stage with minimal extra cleanup.

Step-by-step implementation reading guide:
1. Read the guard clauses first; they define the cases the rest of the function refuses to handle.
2. Follow the delegated helpers `DownloadError, Path, build_parser, close_dataset_page, download_selected_files, ensure_prerequisites` to see how this symbol sequences lower-level work.
3. Read the return statement last and verify how much normalization, validation, or formatting the function promises its callers.

Why it is implemented this way:
- The function checks its contract up front so downstream code can assume shapes, ranges, or mode flags are already valid.

What downstream code assumes:
- Callers rely on this symbol to prepare clean inputs for `DownloadError, Path, build_parser, close_dataset_page, download_selected_files` without redoing the same validation or reshaping work.

## Formula Mapping

Formula mapping: not applicable. This file mainly defines command flow, delegation boundaries, and operational side effects rather than a standalone numerical transform.

## Design Decisions

- Keep executable scripts thin so operational behavior lives in importable library code.
- Use script wrappers as stable shell entry points without duplicating training logic.
- Keep shell-facing code thinner than numerical code so operational changes do not silently alter the math path.

## Common Failure Modes

- Guard clause or surfaced failure: `DownloadError("Could not parse a usable Cookie header. Paste the request's `Cookie:` header value or the full `Cookie: ...` line.")`
- Guard clause or surfaced failure: `DownloadError('--count must be greater than 0.')`
- Guard clause or surfaced failure: `DownloadError('Cookie header input is empty.')`
- Guard clause or surfaced failure: `DownloadError('Either `signed_url` or `cookie_header` must be available.')`
- Guard clause or surfaced failure: `DownloadError('Input stream closed before manual access data was provided.')`
- Guard clause or surfaced failure: `DownloadError('No manual input was provided.')`
- Guard clause or surfaced failure: `DownloadError('Semi-automatic mode requires an interactive terminal. Use `--cookie-header` or `--signed-url` in non-interactive runs.')`
- Guard clause or surfaced failure: `DownloadError('The UCL dataset site returned `403 Forbidden` to the automated browser. Automatic cookie acquisition is blocked right now. Retry later, or rerun the script with `--semi-auto`, `--cookie-header`, or `--signed-url`.')`
- Guard clause or surfaced failure: `DownloadError('Timed out waiting for the `aws-waf-token` browser cookie. Retry later, or rerun the script with `--semi-auto`, `--cookie-header`, or `--signed-url`.')`
- Guard clause or surfaced failure: `DownloadError('`npx` is required. Install Node.js/npm first.')`

## How This Connects To Neighboring Files

- This file is relatively self-contained; its closest neighbors are package-level imports rather than one obvious sibling file.

## Related Tests

- [test_download_svbrdf_mini.py](../tests/test_download_svbrdf_mini.md)
