import json
import logging.config
import logging.handlers
import pathlib


def setup_logging(log_file: str) -> None:
    config_file = pathlib.Path("src/logging_config.json")
    if config_file.exists():
        with open(config_file, "rt") as file:
            config = json.load(file)
        logging.config.dictConfig(config)
        if "handlers" in config and "file" in config["handlers"]:
            config["handlers"]["file"]["filename"] = log_file
            logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=logging.INFO)
