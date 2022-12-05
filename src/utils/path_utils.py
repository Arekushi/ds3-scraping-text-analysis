import os


def file_exists(file_path):
    return os.path.isfile(file_path)


def path_exists(path):
    return os.path.exists(path)
