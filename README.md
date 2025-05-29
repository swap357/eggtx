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

The CI workflow will run the same checks and the test suite using `pytest`.
