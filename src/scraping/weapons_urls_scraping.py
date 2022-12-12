import requests
from bs4 import BeautifulSoup, Tag
from config import settings


def get_weapons_links():
    weapons_links = []
    response = requests.get(settings.weapons_url)
    soup = BeautifulSoup(response.content, features='html5lib')
    tables = soup.find_all('table', {'style': 'width:100%;'})

    for table in tables:
        weapons_links.extend(get_table_rows(table))

    return weapons_links


def get_table_rows(table: Tag):
    rows = []
    tr = table.find('tr')
    lis = tr.find_all('li')

    for li in lis:
        a = li.find('a')
        weapon_name = a.text.strip()

        rows.append({
            'name': weapon_name,
            'url': a['href']
        })

    return rows
