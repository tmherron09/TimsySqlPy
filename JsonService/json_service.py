from __future__ import annotations
import json
from typing import TypeVar

T = TypeVar('T')

def json_to_class(json_data: str, calling_class: type = None) -> T | dict:
    load_data = json.loads(json_data)
    if calling_class is not None:
        return calling_class.load_dict(load_data)
    return load_data

if __name__ == "__main__":
    # json_service = JsonService()
    loaded_data = json_to_class('{"name": "John", "age": 30, "city": "New York"}')
    print(loaded_data)
    print(type(loaded_data))


#
# class JsonService:
#     def __init__(self):
#         pass
#
#     @staticmethod
#     def parse_json(json_data: str, calling_class: type = None) -> T | dict:
#         load_data = json.loads(json_data)
#         if calling_class is not None:
#             return calling_class.load_dict(load_data)
#         return load_data
#


