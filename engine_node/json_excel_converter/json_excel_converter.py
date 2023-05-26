import json

import xlsxwriter as xl
import pandas as pd

from pathlib import Path


def recursive_flatten_json(json_data: dict or list, key_prefix=None, is_root=True):

    flat_json = {}

    if isinstance(json_data, list):
        json_data = {i: value for i, value in enumerate(json_data)}

    for key, value in json_data.items():

        new_key = f"{key_prefix}/{key}" if key_prefix else key

        if isinstance(value, dict):
            flat_json.update(recursive_flatten_json(value, new_key))
        else:
            flat_json[new_key] = value

    return flat_json


def json_to_excel(json_data: dict or list, output_path, encryption_password=None, end_values_as_list=True):

    flat_dict = recursive_flatten_json(json_data)

    multi_level_index = pd.MultiIndex.from_tuples([tuple(key.split('/')) for key in flat_dict])

    # ============== END VALUE IS DISPLAYED IN SINGLE COLUMN OR AS A LIST =============================

    if end_values_as_list:

        # Get the value of the longer list among end values
        column_count = max(map(lambda x: len(x) if isinstance(x, list) else 1, flat_dict.values()))

        # Convert every value to a list of this length
        value_list = \
            [
                v + [None for _ in range(column_count - len(v))] if isinstance(v, list)
                else [v] + [None for _ in range(column_count - 1)]
                for v in flat_dict.values()
            ]

    else:

        column_count = 1
        value_list = flat_dict.values()

    # ============== CREATES EXCEL FILE =============================

    df_data = pd.DataFrame(index=multi_level_index, columns=list(range(column_count)), data=value_list)

    df_data.to_excel(output_path)


def excel_to_json(xl_file, output_path, encryption_password=None):
    df_xl_data = pd.read_excel(xl_file)


for _json_sample in Path('tests/input_json').glob('*.json'):

    _data = json.load(open(_json_sample))
    json_to_excel(_data, Path(f"tests/output_xl/{_json_sample.stem}.xlsx"))
