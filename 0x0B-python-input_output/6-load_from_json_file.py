#!/usr/bin/python3
"""defining load_from_json_file function"""


import json


def load_from_json_file(filename):
    """function that creates an Object from a JSON file"""
    with open(filename, encoding="UTF-8") as a_file:
        return json.load(a_file)
