import requests
from bs4 import BeautifulSoup, Tag
from config import settings
from utils import open_json, save_json


path = f'./src/data/links'
file_name = f'{settings.file_name}.json'


def get_links():
    try:
        return open_json(file_name)
    except IOError:
        weapons = get_weapons_links()
        save_json(weapons, path, file_name)
        return weapons


def merge_two_dicts(x, y):
    z = x.copy()
    z.update(y)
    return z


def table_data(table: Tag):
    rows = {}
    tr = table.find('tr')
    lis = tr.find_all('li')

    for li in lis:
        a = li.find('a')
        rows[a.text] = a['href']

    return rows


def get_weapons_links():
    weapons = {}
    response = requests.get(settings.weapons_url)
    soup = BeautifulSoup(response.content, features='html5lib')
    tables = soup.find_all('table', {'style': 'width:100%;'})

    for table in tables:
        weapons = merge_two_dicts(weapons, table_data(table))

    return weapons
