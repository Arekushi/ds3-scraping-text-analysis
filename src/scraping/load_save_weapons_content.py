import re
from itertools import repeat

import requests
from requests import Session

from config import settings
from multiprocessing.dummy import Pool
from multiprocessing import cpu_count

from . import weapon_content_to_dict
from ..scraping.load_save_weapons_urls import load_urls
from ..utils import save_json, path_exists, load_path_json
from ..utils.path_utils import make_dir


path = settings.weapons_path


def load_weapons():
    if path_exists(path):
        return load_path_json(path)
    else:
        return save_weapons()


def save_weapons():
    make_dir(path)

    with Pool(cpu_count() * 2) as pool:
        return pool.map(save_weapon, [weapon_content_to_dict(content) for content in catch_all_content()])


def save_weapon(weapon):
    name = weapon['status']['info']['name']
    file_name = f"{re.sub('[^A-Za-z0-9]+', ' ', name).replace(' ', '-').lower()}.{settings.save_files_format}"

    save_json(weapon, path, file_name)
    return weapon


def fetch(session: Session, url_obj):
    with session.get(f"{settings.base_url}{url_obj['url']}") as response:
        return response.content


def catch_all_content():
    urls_obj = load_urls()

    with Pool(cpu_count() * 2) as pool:
        with requests.Session() as session:
            return pool.starmap(fetch, zip(repeat(session), urls_obj))
