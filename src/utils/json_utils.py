import os
import orjson
from pathlib import Path


def save_json(data, path, file_name):
    with open(f'{path}/{file_name}', 'w+') as file:
        file.write(orjson.dumps(data, option=orjson.OPT_INDENT_2).decode('utf-8'))


def load_json(file_name):
    with open(file_name) as json_file:
        return orjson.loads(json_file.read())


def load_path_json(path):
    json_files = [f'{path}/{pos_json}' for pos_json in os.listdir(path) if pos_json.endswith('.json')]
    return [load_json(json_file) for json_file in json_files]
