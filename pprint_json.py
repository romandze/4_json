import json
import sys


def load_data(filepatch):
            with open(filepath, 'r') as open_file:
                json_data = json.loads(open_file.read())
            return json_data


def pretty_generate_json(data_from_file):
    pretty_json = json.dumps(data_from_file, sort_keys=True, indent=4)
    return pretty_json


if __name__ == '__main__':
    if len(sys.argv) > 1:
        try:
            filepath = sys.argv[1]
            try:
                print(pretty_generate_json(load_data(filepath)))
            except json.decoder.JSONDecodeError:
                print('Это был не JSON')
        except IOError:
            print('А нет такого файла')
    else:
        print('Ты забыл указать файл JSON')
