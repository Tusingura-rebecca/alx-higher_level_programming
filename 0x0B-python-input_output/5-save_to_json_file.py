#!/usr/bin/python3
"""defining save_to_json_file function"""


import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""
    with open(filename, encoding="UTF-8", mode="w") as a_file:
        a_file.write(json.dumps(my_obj))
