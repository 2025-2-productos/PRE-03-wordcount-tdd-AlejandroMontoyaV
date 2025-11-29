import argparse
import sys


def parse_args(args=None):
    if args is None:
        args = sys.argv[1:]

    if len(args) != 2:
        raise ValueError(
            "Must provide exactly 2 arguments: input_folder and output_folder"
        )

    input_folder, output_folder = args
    return input_folder, output_folder


def main():
    args = parse_args()
