# eggtx
Convert Egglog-style rewrite rules into formal inference rules, output as LaTeX.
This package provides a tiny parser for simple rewrite files and a CLI that
emits a LaTeX representation of those rules.

## Development

This project uses `pre-commit` with **Black** and **Ruff** to ensure consistent
formatting and linting. After installing the development dependencies with
`pip install -e .[dev]`, install the git hooks:

```bash
pre-commit install
```
Run all checks locally with:

```bash
pre-commit run --all-files
pytest -q
```

The CI workflow runs the same checks and test suite. GitHub Actions versions
are pinned and automatically updated by [Renovate](https://github.com/renovatebot/renovate).
