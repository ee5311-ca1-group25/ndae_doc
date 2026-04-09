# test_download_svbrdf_mini.py

Source path: `tests/test_download_svbrdf_mini.py`

## System Under Test

- This test file exercises repository behavior through indirect imports or command execution paths.

## Fixtures And Helpers

- No file-local fixtures or helpers are declared; this file relies on inline test bodies or shared helpers.

## Test Groups

- `normalize_cookie_header_accepts_full_cookie_line`: `test_normalize_cookie_header_accepts_full_cookie_line`
- `normalize_cookie_header_accepts_multiline_headers`: `test_normalize_cookie_header_accepts_multiline_headers`
- `parse_manual_input_accepts_signed_url`: `test_parse_manual_input_accepts_signed_url`
- `parse_manual_input`: `test_parse_manual_input_rejects_empty_value`

## What Each Group Proves

- `normalize_cookie_header_accepts_full_cookie_line` proves that the implementation still satisfies the contract exercised by `test_normalize_cookie_header_accepts_full_cookie_line`.
- `normalize_cookie_header_accepts_multiline_headers` proves that the implementation still satisfies the contract exercised by `test_normalize_cookie_header_accepts_multiline_headers`.
- `parse_manual_input_accepts_signed_url` proves that the implementation still satisfies the contract exercised by `test_parse_manual_input_accepts_signed_url`.
- `parse_manual_input` proves that the implementation still satisfies the contract exercised by `test_parse_manual_input_rejects_empty_value`.

## Regression Intent

These tests are intended to catch behavior drift in the mirrored runtime paths, not just import-time failures.

## Remaining Gaps

The file only covers the explicit cases encoded in its test functions; full-sequence numerical drift still depends on broader smoke and integration coverage.

## Related Source Files

- No direct source file link was inferred automatically.
