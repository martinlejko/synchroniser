import argparse
from argparse import Namespace
from pathlib import Path


class ArgParser:
    @staticmethod
    def positive_float(value: str) -> float:
        try:
            fvalue = float(value)
            if fvalue < 0:
                raise argparse.ArgumentTypeError(f"{value} is not a positive float")
            return fvalue
        except ValueError:
            raise argparse.ArgumentTypeError(f"{value} is not a float")

    @staticmethod
    def existing_directory(value: str) -> str:
        try:
            path = Path(value)
            if not path.exists():
                raise argparse.ArgumentTypeError(f"{value} does not exist.")
            if not path.is_dir():
                raise argparse.ArgumentTypeError(f"{value} is not a directory.")
            return value
        except ValueError:
            raise argparse.ArgumentTypeError(f"{value} is not a valid path.")

    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(description="Directory syncronization tool.")
        self.add_arguments()

    def add_arguments(self) -> None:
        self.parser.add_argument("src_dir", type=self.existing_directory, help="Path to the source directory.")
        self.parser.add_argument("replica_dir", type=str, help="Path to the replica directory.")
        self.parser.add_argument(
            "period", type=self.positive_float, default=1, help="An integer representing the period in minutes."
        )
        self.parser.add_argument("log_file", type=str, help="Path to the text file.")

    def parse_args(self) -> Namespace:
        return self.parser.parse_args()
