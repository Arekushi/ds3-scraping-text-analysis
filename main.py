import asyncio
from multiprocessing import cpu_count
from time import time

from src.scraping.get_save_weapons import get_save_weapons
from src.scraping.get_save_weapons_thread import get_save_weapons_thread


def main():
    start = time()

    get_save_weapons()

    end = time()
    print('It took', (end - start), 'seconds')


if __name__ == '__main__':
    main()
