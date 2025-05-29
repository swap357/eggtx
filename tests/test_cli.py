import sys
from pathlib import Path

# Add package root to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from eggtx.__main__ import main


def test_cli_output(capsys, tmp_path):
    file = tmp_path / "rules.eg"
    file.write_text("a => b\n")
    main([str(file)])
    captured = capsys.readouterr()
    assert "a \\rightarrow b" in captured.out
