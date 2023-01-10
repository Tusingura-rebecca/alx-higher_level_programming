#!/usr/bin/python3
"""defining from_json_string"""


import json


def from_json_string(my_str):
    """returns an objectbrepresented by a JSON string"""
    return json.loads(my_str)
