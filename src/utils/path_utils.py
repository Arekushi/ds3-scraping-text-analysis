import os
from pathlib import Path


def file_exists(file_path):
    return os.path.isfile(file_path)


def path_exists(path):
    return os.path.exists(path)


def make_dir(path):
    Path(path).mkdir(parents=True, exist_ok=True)
