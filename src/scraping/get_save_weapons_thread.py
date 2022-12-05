from concurrent.futures import ThreadPoolExecutor
from itertools import repeat
from multiprocessing import cpu_count

import requests

from config import settings
from src.scraping import get_urls, fetch, save_weapon, get_weapon_obj
from src.utils.path_utils import make_dir


path = settings.weapons_path


def get_all_content_thread():
    urls_obj = get_urls()

    with ThreadPoolExecutor(max_workers=cpu_count() * 2) as executor:
        with requests.Session() as session:
            result = executor.map(fetch, repeat(session), urls_obj)
            executor.shutdown(wait=True)
            return result


def get_save_weapons_thread():
    make_dir(path)

    with ThreadPoolExecutor(max_workers=cpu_count() * 2) as executor:
        result = executor.map(save_weapon, [get_weapon_obj(content) for content in get_all_content_thread()])
        executor.shutdown(wait=True)
        return result
