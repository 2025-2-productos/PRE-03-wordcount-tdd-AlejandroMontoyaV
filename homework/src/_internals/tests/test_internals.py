import subprocess
import sys

from ...wordcount import parse_args


def test_parse_args():
    try:
        subprocess.run(
            [sys.executable, "-m", "homework", "data/input", "data/output"],
            check=True,
        )
    except subprocess.CalledProcessError as e:
        raise Exception(f"Error running the homework script: {e}")

    input_folder, output_folder = parse_args(["data/input", "data/output"])

    assert input_folder == "data/input"
    assert output_folder == "data/output"
