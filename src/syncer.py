import hashlib
import logging
import os


class Syncer:
    def __init__(self, src_dir: str, replica_dir: str, period: int) -> None:
        self.src_dir = src_dir
        self.replica_dir = replica_dir
        self.period = period
        self.hash_dict = {}

    def sync_folders(self) -> None:
        if self.hash_dict.get(self.src_dir) != self.calculate_directory_hash(self.src_dir):
            logging.info("Changes detected. Syncing the directories.")
            self.hash_dict[self.src_dir] = self.calculate_directory_hash(self.src_dir)
        else:
            logging.info("No changes detected. Skipping the sync.")
        print(self.calculate_directory_hash(self.src_dir))

    def calculate_directory_hash(self, directory_path):
        """
        Calculate the MD5 hash of the directory.
        """
        md5 = hashlib.md5()
        try:
            for root, dirs, files in os.walk(directory_path):
                print(root, dirs, files)
                for filename in files:
                    file_path = os.path.join(root, filename)
                    with open(file_path, "rb") as file:
                        while True:
                            data = file.read(8192)
                            if not data:
                                break
                            md5.update(data)
        except OSError as e:
            print(f"Error calculating hash for directory {directory_path}: {e}")
            return None

        return md5.hexdigest()
