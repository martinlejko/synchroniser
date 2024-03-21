import logging
import os
import tempfile

from synchroniser.logger import setup_logging


def test_logging_info() -> None:
    with tempfile.TemporaryDirectory() as temp_dir:
        log_file = os.path.join(temp_dir, "test.log")

        setup_logging(log_file)

        logger = logging.getLogger(__name__)

        logger.info("Test message 1")
        logger.error("Test message 2")

        assert os.path.isfile(log_file)

        with open(log_file, "r") as f:
            log_contents = f.readlines()

        expected_log_format = r" - INFO - Test message 1"
        expected_log_format_error = r" - ERROR - Test message 2"

        assert expected_log_format in log_contents[0], f"Unexpected log format: {log_contents[0]}"
        assert expected_log_format_error in log_contents[1], f"Unexpected log format: {log_contents[1]}"


def test_logging_empty_message() -> None:
    with tempfile.TemporaryDirectory() as temp_dir:
        log_file = os.path.join(temp_dir, "test.log")

        setup_logging(log_file)

        logger = logging.getLogger(__name__)

        logger.info("")

        assert os.path.isfile(log_file)

        with open(log_file, "r") as f:
            log_contents = f.readlines()

        expected_log_format = r" - INFO - "

        assert expected_log_format in log_contents[0], f"Unexpected log format: {log_contents[0]}"
