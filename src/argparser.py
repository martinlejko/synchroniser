import argparse

class ArgParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Process command line arguments.")
        self.add_arguments()

    def add_arguments(self):
        self.parser.add_argument("src_dir", type=str,help="Path to the source directory.")
        self.parser.add_argument("replica_dir", type=str, help="Path to the replica directory.")
        self.parser.add_argument("period", type=int, default=1, help="An integer representing the period in minutes.")
        self.parser.add_argument("log_file", type=str, default="", help="Path to the text file.")

    def parse_args(self):
        return self.parser.parse_args()
