import csv
from pathlib import Path


def save_csv(data, path, file_name):
    Path(path).mkdir(parents=True, exist_ok=True)

    with open(f'{path}/{file_name}', 'w+', encoding='utf-8') as file:
        fields = data[0].keys() if isinstance(data, list) else data.keys()
        w = csv.DictWriter(file, fieldnames=fields)
        w.writerows(data)


def load_csv(file_name):
    with open(file_name, 'r') as file:
        r = csv.DictReader(file)
        return list(r)
