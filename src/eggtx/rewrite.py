"""Utilities for handling rewrite rules."""

from __future__ import annotations


def parse_rewrite_line(line: str):
    """Parse a single rewrite rule line or block.

    Lines may use ``=>`` or ``->`` as the rewrite operator.  They may also
    be written in the Egglog ``rewrite(...).to(...)`` style.  Leading
    comments (``#``) and whitespace are ignored.  Blank lines return
    ``None``.
    """

    # Remove trailing comments and surrounding whitespace
    line = line.split("#", 1)[0].strip()
    if not line:
        return None

    if "=>" in line:
        lhs, rhs = line.split("=>", 1)
    elif "->" in line:
        lhs, rhs = line.split("->", 1)
    elif line.startswith("rewrite(") and ".to(" in line:
        # Collapse whitespace but keep parentheses structure
        collapsed = " ".join(line.split())

        def extract_parens(content: str, start: int) -> tuple[str, int]:
            depth = 1
            for i in range(start, len(content)):
                c = content[i]
                if c == "(":
                    depth += 1
                elif c == ")":
                    depth -= 1
                    if depth == 0:
                        return content[start:i], i + 1
            raise ValueError(f"Invalid rewrite rule: {line!r}")

        def first_arg(s: str) -> str:
            depth = 0
            for i, c in enumerate(s):
                if c == "(":
                    depth += 1
                elif c == ")":
                    depth -= 1
                elif c == "," and depth == 0:
                    return s[:i]
            return s

        start = len("rewrite(")
        lhs_args, pos = extract_parens(collapsed, start)
        lhs = first_arg(lhs_args.strip())
        if not collapsed[pos:].startswith(".to("):
            raise ValueError(f"Invalid rewrite rule: {line!r}")
        args, _ = extract_parens(collapsed, pos + len(".to("))
        rhs = first_arg(args.strip())
        lhs, rhs = lhs.strip(), rhs.strip()
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
