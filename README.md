# eggtx
Convert Egglog-style rewrite rules into formal inference rules, output as LaTeX.
This package provides a tiny parser for simple rewrite files and a CLI that
emits a LaTeX representation of those rules.

## Development

This project uses `pre-commit` to run formatting and linting checks. After
installing the development dependencies with `pip install -e .[dev]`, install the
git hooks:

```bash
pre-commit install
```

`pre-commit` uses Black and Ruff as defined in `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 24.3.0
    hooks:
      - id: black
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.3.0
    hooks:
      - id: ruff
```

The CI workflow will run the same checks and the test suite using `pytest`.
