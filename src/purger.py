import logging
import os
from pathlib import Path


class Purger:
    def __init__(self, src_dir: Path, replica_dir: Path) -> None:
        self.src_dir = src_dir
        self.replica_dir = replica_dir
        self.purge_dirs()

    def purge_dirs(self) -> None:
        for root, dirs, files in os.walk(self.replica_dir):
            for file in files:
                replica_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(replica_file_path, self.replica_dir)
                src_file_path = os.path.join(self.src_dir, relative_path)

                if not os.path.exists(src_file_path):
                    logging.info(f"Removing {replica_file_path}")
                    os.remove(replica_file_path)
