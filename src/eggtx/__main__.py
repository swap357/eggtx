"""Command-line interface for eggtx."""

from __future__ import annotations

import argparse
from .rewrite import convert_file_to_latex


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Convert Egglog rewrite rules to LaTeX"
    )
    parser.add_argument("file", help="Path to Egglog file")
    args = parser.parse_args(argv)
    print(convert_file_to_latex(args.file))


if __name__ == "__main__":
    main()
