#!/usr/bin/python3
"""My file module"""


def append_write(filename="", text=""):
    """Method to append to a file"""
    with open(filename, 'a', encoding="UTF-8") as f:
        update = f.write(text)
    return update
