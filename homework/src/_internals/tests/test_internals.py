import subprocess
import sys

from ...wordcount import parse_args
from ..read_all_lines import read_all_lines


# Función test_parse_args
def test_parse_args():
    try:
        subprocess.run(
            [sys.executable, "-m", "homework", "data/input", "data/output"],
            check=True,
        )
    except subprocess.CalledProcessError as e:
        raise Exception(f"Error running the homework script: {e}")

    input_folder, output_folder = parse_args(["data/input", "data/output"])

    assert input_folder == "data/input/"
    assert output_folder == "data/output/"


# Función test_read_all_lines
def test_read_all_lines():
    input_folder = "data/input/"
    lines = read_all_lines(input_folder)
    assert len(lines) > 0
    assert any(
        "Analytics refers to the systematic computational analysis of data" in line
        for line in lines
    )
