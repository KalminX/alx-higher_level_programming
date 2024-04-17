#!/usr/bin/python3
"""My file module"""
import sys


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

try:
    data = load_from_json_file("add_item.json")
except FileNotFoundError:
    data = []

for index, arg in enumerate(sys.argv):
    if index == 0:
        continue
    data.append(sys.argv[index])
save_to_json_file(data, "add_item.json")