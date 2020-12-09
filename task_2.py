import json
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
LOGGER = logging.getLogger()


def parse_user(output_file, *input_files) -> None:
    res = []
    unique_names = set()
    for file_name in input_files:
        try:
            with open(file_name) as f:
                data = json.load(f)
                for dct in data:
                    if dct.get('name') and dct['name'] not in unique_names:
                        res.append({k: v for k, v in dct.items()})
                        unique_names.add(dct['name'])
        except FileNotFoundError:
            LOGGER.error(f"File {file_name} doesn't exists")
    with open(output_file, 'w') as f:
        json.dump(res, f, indent=4)


parse_user('user3.json', 'user1.json', 'user2.json')
parse_user('user4.json', 'usasdfer1.json', 'user3.json')
