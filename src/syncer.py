import logging
import os
from pathlib import Path
from typing import Dict, List

from copythreader import ThreadedCopy
from purger import Purger


class Syncer:
    def __init__(self, src_dir: str, replica_dir: str) -> None:
        self.src_dir = Path(src_dir)
        self.replica_dir = Path(replica_dir)
        self.modified_dates: Dict[Path, float] = {}

    def sync_folders(self) -> None:
        modified_files = self.travers_get_modification_times(self.src_dir)
        if not modified_files:
            logging.info("No files to sync.")
        else:
            logging.info(f"Syncing {len(modified_files)} files.")
            ThreadedCopy(self.src_dir, self.replica_dir, modified_files)
        Purger(self.src_dir, self.replica_dir)

    def has_been_modified(self, file_path: Path) -> bool:
        last_modified = os.path.getmtime(file_path)
        if file_path in self.modified_dates:
            if self.modified_dates[file_path] != last_modified:
                self.modified_dates[file_path] = last_modified
                return True
            else:
                return False
        self.modified_dates[file_path] = last_modified
        return True

    def travers_get_modification_times(self, directory_path: Path) -> List[Path]:
        modified_files = []
        try:
            for item in directory_path.iterdir():
                if item.is_file():
                    if self.has_been_modified(item):
                        modified_files.append(item)
                elif item.is_dir():
                    if self.has_been_modified(item):
                        modified_files.extend(self.travers_get_modification_times(item))
        except OSError as e:
            print(f"Error getting modification time {directory_path}: {e}")
            return []
        return modified_files
