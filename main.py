from time import time
from src.scraping import get_links
from src.scraping.get_save_weapons import get_weapons_pool
from src.scraping import get_weapons


start = time()
weapons = get_weapons_pool()
# get_links()
# weapons = get_weapons()
end = time()
print('It took', (end - start), 'seconds')
