import requests
import collections
from bs4 import BeautifulSoup, Tag
from ..utils.weapon_status_dict import weapon_status_dict


def get_weapon_content(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.content, features='html5lib')
    status = get_status(soup)
    description = get_description(soup)
    availability = get_availability(soup)
    characteristics = get_characteristics(soup)
    move_set = get_move_set(soup)

    return {
        'status': status,
        'description': description,
        'availability': availability,
        'characteristics': characteristics,
        'move_set': move_set
    }


def get_status(soup: BeautifulSoup):
    status = collections.defaultdict(dict)
    aside = soup.find('aside', {'role': 'region'})

    for key, value in weapon_status_dict.items():
        for name, data_source, tag_looking, type in value:
            status[key][name] = get_data_by_data_source(aside, data_source, tag_looking, type)

    status['info']['name'] = get_data_by_data_source(aside, 'name', 'h2')
    status['info']['image'] = aside.find('figure', {'class': 'pi-item pi-image'}).find('a')['href']

    return status


def get_description(soup: BeautifulSoup):
    description = None

    try:
        div = soup.find('div', {'class': 'mainbg'})
        description = div.text.strip()
    except AttributeError:
        pass

    return description


def get_availability(soup: BeautifulSoup):
    availability = None

    try:
        span = soup.find('span', {'id': 'Availability'})
        h2 = span.parent
        availability = get_text_by_h2(h2)
    except AttributeError:
        pass

    return availability


def get_characteristics(soup: BeautifulSoup):
    characteristics = None

    try:
        span = soup.find('span', {'id': 'Characteristics'})
        h2 = span.parent
        characteristics = get_text_by_h2(h2)
    except AttributeError:
        pass

    return characteristics


def get_move_set(soup: BeautifulSoup):
    moveset = {}

    try:
        span = soup.find('span', {'id': 'Moveset'})
        h2 = span.parent
        table = h2.find_next('table', {'class': 'article-table'})
        trs = table.find_all('tr')

        for tr in trs[1::]:
            name = tr.find('th').get_text(separator=' ').strip()
            col = tr.find('td')
            description = col.text.strip()
            moveset[name] = description
    except AttributeError:
        pass

    return moveset


def get_data_by_data_source(source_tag, data_source, tag_looking, type = 'str'):
    tag = source_tag.find(tag_looking, {'data-source': data_source})
    result = ''

    if tag is not None:
        result = tag.get_text().strip()

    try:
        if type == 'int':
            result = int(result)
        elif type == 'float':
            result = float(result)
    except ValueError:
        result = None

    return result


def get_text_by_h2(h2: Tag):
    text = []

    for sib in h2.next_siblings:
        if isinstance(sib, Tag):
            if sib.name == 'ul':
                text.extend([li.text.strip() for li in sib.find_all('li')])
            elif sib.name == 'p':
                text.append(sib.text.strip())
            else:
                break

    return text
