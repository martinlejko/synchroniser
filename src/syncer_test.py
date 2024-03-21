import shutil
import tempfile
from pathlib import Path
from typing import Generator

import pytest
from syncer import Syncer


@pytest.fixture
def temp_directories() -> Generator[tuple[str, str], None, None]:
    src_dir = tempfile.mkdtemp()
    replica_dir = tempfile.mkdtemp()
    yield src_dir, replica_dir
    shutil.rmtree(src_dir)
    shutil.rmtree(replica_dir)


def test_sync_folders_no_files(temp_directories: tuple[str, str]) -> None:
    src_dir, replica_dir = temp_directories
    syncer = Syncer(src_dir, replica_dir)
    syncer.sync_folders()
    assert len(list(Path(replica_dir).iterdir())) == 0


def test_sync_folders_with_files(temp_directories: tuple[str, str]) -> None:
    src_dir, replica_dir = temp_directories
    syncer = Syncer(src_dir, replica_dir)
    file1 = Path(src_dir) / "file1.txt"
    file1.touch()
    file2 = Path(src_dir) / "file2.txt"
    file2.touch()
    syncer.sync_folders()
    replica_files = list(Path(replica_dir).iterdir())
    assert len(replica_files) == 2
    assert Path(replica_dir) / "file1.txt" in replica_files
    assert Path(replica_dir) / "file2.txt" in replica_files

def test_travers_get_modification_times(temp_directories: tuple[str, str]) -> None:
    src_dir, replica_dir = temp_directories
    syncer = Syncer(src_dir, replica_dir)
    file1 = Path(src_dir) / "file1.txt"
    file1.touch()
    file2 = Path(src_dir) / "file2.txt"
    file2.touch()
    modified_files = syncer.travers_get_modification_times(Path(src_dir))
    assert len(modified_files) == 2
    assert file1 in modified_files
    assert file2 in modified_files
