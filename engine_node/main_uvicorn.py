import time

from typing import Union

from fastapi import FastAPI

from xl_tools.json_excel_converter import json_to_excel

app = FastAPI()


@app.get("/")
def read_root():
    time.sleep(3)
    return {"Status": "Operational"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/functions/sum/{a}&{b}")
def api_sum(a: int, b: int):
    return {"sum": a+b}


@app.get("/functions/json_to_excel/{json_data}")
def api_json_to_excel(json_data):
    return {"xl_data_b64": json_to_excel(json_data)}
