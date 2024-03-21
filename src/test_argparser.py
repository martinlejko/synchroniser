import sys
from argparse import Namespace

import pytest
from argparser import ArgParser


def test_missing_required_args() -> None:
    parser = ArgParser()
    with pytest.raises(SystemExit):
        parser.parse_args()


def test_valid_parse_args() -> None:
    parser = ArgParser()
    sys.argv = ["program_name", "data/", "replica_dir", "5", "logfile.txt"]

    parsed_args = parser.parse_args()

    assert isinstance(parsed_args, Namespace)
    assert parsed_args.src_dir == "data/"
    assert parsed_args.replica_dir == "replica_dir"
    assert parsed_args.period == float(5)
    assert parsed_args.log_file == "logfile.txt"


def test_missing_source_dir_arg() -> None:
    parser = ArgParser()
    sys.argv = ["program_name", "replica_dir", "5", "logfile.txt"]

    with pytest.raises(SystemExit):
        parser.parse_args()


def test_missing_replia_dir_arg() -> None:
    parser = ArgParser()
    sys.argv = ["program_name", "data/", "5", "logfile.txt"]

    with pytest.raises(SystemExit):
        parser.parse_args()


def test_invalid_period_arg() -> None:
    parser = ArgParser()
    sys.argv = ["program_name", "source_dir", "replica_dir", "five", "logfile.txt"]

    with pytest.raises(SystemExit):
        parser.parse_args()


def test_negative_period_arg() -> None:
    parser = ArgParser()
    sys.argv = ["program_name", "data/", "replica_dir", "-5", "logfile.txt"]

    with pytest.raises(SystemExit):
        parser.parse_args()


def test_float_period_arg() -> None:
    parser = ArgParser()
    sys.argv = ["program_name", "data/", "replica_dir", "5.5", "logfile.txt"]

    parsed_args = parser.parse_args()

    assert isinstance(parsed_args, Namespace)
    assert parsed_args.src_dir == "data/"
    assert parsed_args.replica_dir == "replica_dir"
    assert parsed_args.period == float(5.5)
    assert parsed_args.log_file == "logfile.txt"
