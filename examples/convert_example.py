"""Example script using eggtx to convert rewrite rules to LaTeX."""

from eggtx import convert_file_to_latex


if __name__ == "__main__":
    latex = convert_file_to_latex("rules.eg")
    print(latex)
