# FAQ

## Why is the docs repository separate from NDAE?

The docs site is maintained as an independent repository and mounted as a submodule in the main workspace. This keeps website deployment isolated from model code changes.

## Why does `git submodule add` fail with an empty remote repository?

Submodule checkout requires at least one commit in the target remote. Initialize the remote repository first, then add it as a submodule.

## What is the GitHub Pages URL?

Default URL pattern:

```text
https://<owner>.github.io/<repo>/
```

For this setup:

```text
https://ee5311-ca1-group25.github.io/ndae_doc/
```
