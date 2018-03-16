import json
import sys

def load_data():
    if len(sys.argv) > 1:
        try:
            filepath = sys.argv[1]
            with open(filepath, 'r') as open_file:
                json_data = json.loads(open_file.read())
            return json_data
        except IOError:
            print("А нет такого файла")
            sys.exit()
    else:
        print("Ты забыл указать файл JSON")
        sys.exit()

def pretty_print_json(data):
    pretty_json = json.dumps(data, sort_keys=True, indent=4)
    return pretty_json

if __name__ == '__main__':
    try:
        print(pretty_print_json(load_data()))
    except json.decoder.JSONDecodeError:
        print("Это был не JSON")
