# eggtx
Convert Egglog-style rewrite rules into formal inference rules, output as LaTeX.
This package provides a tiny parser for simple rewrite files and a CLI that
emits a LaTeX representation of those rules.

## Installation

Install the package from PyPI using ``pip``:

```bash
pip install eggtx
```

You can also install in development mode if you want to work on the source:

```bash
pip install -e .[dev]
```

## Usage

The command line interface ``eggtx`` takes a file containing rewrite rules and
prints a LaTeX representation:

```bash
eggtx path/to/rules.eg > rules.tex
```

See ``examples/`` for a small sample.  The ``convert_example.py`` script shows
how to call the library directly:

```bash
python examples/convert_example.py
```

## Development

This project uses `pre-commit` to run formatting and linting checks. After
installing the development dependencies with `pip install -e .[dev]`, install the
git hooks:

```bash
pre-commit install
```

The CI workflow will run the same checks and the test suite using `pytest`.
