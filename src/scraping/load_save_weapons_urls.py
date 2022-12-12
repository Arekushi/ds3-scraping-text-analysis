from config import settings
from ..scraping.weapons_urls_scraping import get_weapons_links
from ..utils import save_json, load_json, file_exists


path = settings.links_path
file_name = f'{settings.file_name}.{settings.save_files_format}'


def load_urls():
    if file_exists(f'{path}/{file_name}'):
        return load_json(f'{path}/{file_name}')
    else:
        return save_urls()


def save_urls():
    weapons = get_weapons_links()
    save_json(weapons, path, file_name)
    return weapons
