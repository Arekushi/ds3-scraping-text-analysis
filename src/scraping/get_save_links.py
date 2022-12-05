from config import settings
from ..scraping.weapons_links import get_weapons_links
from ..utils import save_json, load_json, file_exists

path = f'./src/data/links'
file_name = f'{settings.file_name}.{settings.save_files_format}'


def get_links():
    if file_exists(f'{path}/{file_name}'):
        return load_json(f'{path}/{file_name}')
    else:
        return save_links()


def save_links():
    weapons = get_weapons_links()
    save_json(weapons, path, file_name)
    return weapons
