from src.utils.path_utils import make_dir


def save_file(data, path, file_name):
    with open(f'{path}/{file_name}', 'w+') as file:
        file.write(data)
