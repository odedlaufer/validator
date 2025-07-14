import subprocess
from pathlib import Path


def test_cli_valid(tmp_path):
    test_data_dir = Path("test_data/valid")
    result = subprocess.run(
        [
            "python",
            "main.py",
            "--yaml",
            str(test_data_dir / "plan.yaml"),
            "--json",
            str(test_data_dir / "config.json"),
            "--csv",
            str(test_data_dir / "data.csv"),
        ],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "Validation passed" in result.stdout + result.stderr


def test_cli_invalid(tmp_path):
    test_data_dir = Path("test_data/invalid")
    result = subprocess.run(
        [
            "python",
            "main.py",
            "--yaml",
            str(test_data_dir / "plan.yaml"),
            "--json",
            str(test_data_dir / "config.json"),
            "--csv",
            str(test_data_dir / "data.csv"),
        ],
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0
    assert "Mandatory field" in result.stderr or "Unhandled exception" in result.stderr
