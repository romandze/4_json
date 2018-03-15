import json
import sys

filepath = sys.argv[1]

def load_data(filepath):
    with open(filepath, 'r') as f:
        json_data = json.loads(f.read())
    return json_data

def pretty_print_json(data):
    return print (json.dumps(data, sort_keys=True, indent=4))


if __name__ == '__main__':
    print(pretty_print_json(load_data('alco_shops.json')))
