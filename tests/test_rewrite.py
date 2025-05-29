import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))


from eggtx.rewrite import parse_rewrite_line, rewrite_to_latex, convert_file_to_latex


def test_parse_rewrite_line_basic():
    assert parse_rewrite_line("a => b") == ("a", "b")
    assert parse_rewrite_line("x -> y") == ("x", "y")


def test_parse_rewrite_line_comments_and_blank():
    assert parse_rewrite_line("  # comment") is None
    assert parse_rewrite_line("\n") is None


def test_rewrite_to_latex():
    assert rewrite_to_latex("a", "b") == "a \\rightarrow b"


def test_convert_file_to_latex(tmp_path):
    path = tmp_path / "rules.eg"
    path.write_text("a => b\nc -> d\n")
    result = convert_file_to_latex(str(path))
    assert result.splitlines() == ["a \\rightarrow b", "c \\rightarrow d"]


def test_parse_rewrite_line_complex_examples(capsys):
    examples = [
        """rewrite(pow(x, lit64(ival))).to(
    mul(x, pow(x, lit64(ival - 1))),
    ival >= 1,
)""",
        """rewrite(pow(x, lit64(i64(0))), subsume=True).to(
    Npy_float32(Term.LiteralF64(float(1))),
)""",
    ]

    expected = [
        ("pow(x, lit64(ival))", "mul(x, pow(x, lit64(ival - 1)))"),
        ("pow(x, lit64(i64(0)))", "Npy_float32(Term.LiteralF64(float(1)))"),
    ]

    for ex, exp in zip(examples, expected):
        result = parse_rewrite_line(ex)
        print("RAW:", ex)
        print("PARSED:", rewrite_to_latex(*result))
        assert result == exp
