import logging
import os
from copythreader import ThreadedCopy
from typing import Dict, List, Tuple
from pathlib import Path


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
            threaded_copy = ThreadedCopy(self.src_dir, self.replica_dir, modified_files)

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
            for root, dirs, files in os.walk(directory_path):
                for filename in files:
                    file_path = Path(root) / filename
                    if self.has_been_modified(file_path):
                        modified_files.append(file_path)
        except OSError as e:
            print(f"Error getting modification time {directory_path}: {e}")
            return ([], [])
        return modified_files
