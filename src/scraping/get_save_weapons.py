from config import settings
from ..scraping import get_weapon_content
from ..scraping.get_save_links import get_links
from ..utils import save_json, load_json, file_exists
from multiprocessing.dummy import Pool
from multiprocessing import cpu_count


path = f'./src/data/weapons'


def get_weapons_pool():
    pool = Pool(cpu_count() * 2)
    links = get_links()
    weapons = pool.map(get_weapon, links)
    pool.terminate()
    pool.join()

    return weapons


def get_weapons():
    links = get_links()
    return [get_weapon(weapon_dict) for weapon_dict in links]


def get_weapon(weapon_dict):
    print('Weapon:', weapon_dict['name'])
    file_name = f"{weapon_dict['file_name']}.{settings.save_files_format}"
    link = weapon_dict['link']

    if file_exists(f'{path}/{file_name}'):
        return load_json(f'{path}/{file_name}')
    else:
        return save_weapon(file_name, link)


def save_weapon(file_name, link):
    content = get_weapon_content(f'{settings.base_url}{link}')
    save_json(content, path, file_name)
    return content
