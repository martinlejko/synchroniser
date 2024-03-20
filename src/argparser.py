import argparse
from argparse import Namespace


class ArgParser:
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(description="Directory syncronization tool.")
        self.add_arguments()

    def add_arguments(self) -> None:
        self.parser.add_argument("src_dir", type=str, help="Path to the source directory.")
        self.parser.add_argument("replica_dir", type=str, help="Path to the replica directory.")
        self.parser.add_argument("period", type=float, default=1, help="An integer representing the period in minutes.")
        self.parser.add_argument("log_file", type=str, help="Path to the text file.")

    def parse_args(self) -> Namespace:
        return self.parser.parse_args()
