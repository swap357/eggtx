"""Utilities for handling rewrite rules."""

from __future__ import annotations


def parse_rewrite_line(line: str):
    """Parse a single rewrite rule line.

    Lines may use ``=>`` or ``->`` as the rewrite operator. Leading comments
    (``#``) and whitespace are ignored. Blank lines return ``None``.
    """
    line = line.split("#", 1)[0].strip()
    if not line:
        return None
    if "=>" in line:
        lhs, rhs = line.split("=>", 1)
    elif "->" in line:
        lhs, rhs = line.split("->", 1)
    else:
        raise ValueError(f"Invalid rewrite rule: {line!r}")
    lhs, rhs = lhs.strip(), rhs.strip()
    if not lhs or not rhs:
        raise ValueError(f"Invalid rewrite rule: {line!r}")
    return lhs, rhs


def rewrite_to_latex(lhs: str, rhs: str) -> str:
    """Return a simple LaTeX representation of a rewrite rule."""
    return f"{lhs} \\rightarrow {rhs}"


def convert_file_to_latex(path: str) -> str:
    """Read rewrite rules from ``path`` and convert them to LaTeX."""
    lines = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            parsed = parse_rewrite_line(line)
            if parsed:
                lines.append(rewrite_to_latex(*parsed))
    return "\n".join(lines)
