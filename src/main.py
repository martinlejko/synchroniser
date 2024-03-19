#!/usr/bin/env python

import logging

import schedule
from argparser import ArgParser
from logger import setup_logging
from syncer import Syncer


def setup() -> None:
    parser = ArgParser()
    args = parser.parse_args()
    setup_logging(args.log_file)
    syncer = Syncer(args.src_dir, args.replica_dir, args.period)
    schedule.every(args.period).minutes.do(syncer.sync_folders)
    logging.info("Setup complete. Starting the program.")


def main() -> None:
    setup()
    try:
        while True:
            schedule.run_pending()
    except KeyboardInterrupt:
        logging.info("Exiting the program.")


if __name__ == "__main__":
    main()
