import logging
import os
import queue
import shutil
import threading
from pathlib import Path
from typing import List

file_queue = queue.Queue()


class ThreadedCopy:
    total_files = 0
    copy_count = 0
    lock = threading.Lock()

    def __init__(self, src_dir: Path, replica_dir: Path, files_to_copy: List[Path]) -> None:
        self.src_dir = src_dir
        self.replica_dir = replica_dir
        self.total_files = len(files_to_copy)
        self.copy_count = 0
        self.thread_worker_copy(files_to_copy)

    def copy_worker(self) -> None:
        while True:
            file_path = file_queue.get()
            relative_path = file_path.relative_to(self.src_dir)
            dst_path = self.replica_dir / relative_path
            dst_dir = dst_path.parent
            os.makedirs(dst_dir, exist_ok=True)  # Ensure the destination directory exists
            if dst_path.exists():
                shutil.copy(str(file_path), str(dst_path))
                logging.info(f"Copied {file_path} to {dst_path}")
            else:
                shutil.copy(str(file_path), str(dst_path))
                logging.info(f"Created {dst_path}")
            file_queue.task_done()

    def thread_worker_copy(self, files_to_copy: List[Path]) -> None:
        for i in range(16):
            t = threading.Thread(target=self.copy_worker)
            t.daemon = True
            t.start()
        for file_path in files_to_copy:
            file_queue.put(file_path)
        file_queue.join()
