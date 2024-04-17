#!/usr/bin/python3
"""My json module"""
import json


def save_to_json_file(my_obj, filename):
    """Method to save to a json file"""
    with open(filename, 'w', encoding="UTF-8") as f:
        json.dump(my_obj, f)
