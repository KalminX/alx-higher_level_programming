#!/usr/bin/python3
"""My file module"""


def write_file(filename="", text=""):
    """Method to append to a file"""
    with open(filename, 'a', encoding="UTF-8") as f:
        update = f.write(text)
    return update
