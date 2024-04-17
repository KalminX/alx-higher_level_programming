#!/usr/bin/python3
"""My json module"""
import json


def load_from_json_file(filename):
    """Method to save to a json file"""
    with open(filename, 'r', encoding="UTF-8") as f:
        return json.load(f)
