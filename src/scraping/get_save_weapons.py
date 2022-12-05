import re
from itertools import repeat

import requests
from requests import Session

from config import settings
from multiprocessing.dummy import Pool
from multiprocessing import cpu_count

from . import get_weapon_obj
from ..scraping.get_save_urls import get_urls
from ..utils import save_json
from ..utils.path_utils import make_dir


path = settings.weapons_path


def fetch(session, url_obj):
    with session.get(f"{settings.base_url}{url_obj['url']}") as response:
        return response.content


def get_all_content():
    urls_obj = get_urls()

    with Pool(cpu_count() * 2) as pool:
        with requests.Session() as session:
            return pool.starmap(fetch, zip(repeat(session), urls_obj))


def get_save_weapons():
    make_dir(path)

    with Pool(cpu_count() * 2) as pool:
        return pool.map(save_weapon, [get_weapon_obj(content) for content in get_all_content()])


def save_weapon(weapon):
    name = weapon['status']['info']['name']
    print('Weapon:', name)
    file_name = f"{re.sub('[^A-Za-z0-9]+', ' ', name).replace(' ', '-').lower()}.{settings.save_files_format}"

    save_json(weapon, path, file_name)
    return weapon
