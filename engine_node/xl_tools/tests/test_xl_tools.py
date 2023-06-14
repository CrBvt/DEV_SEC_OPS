import json

from pathlib import Path

from engine_node.xl_tools.json_excel_converter import json_to_excel, excel_to_json

for json_sample in Path('input_json').glob('*.json'):

    json_data = json.load(open(json_sample))
    xl_output = Path(f"output_xl/{json_sample.stem}.xlsx")

    json_to_excel(json_data, xl_output)

    xl_data = excel_to_json(xl_output)
    print(xl_data == json_data)
