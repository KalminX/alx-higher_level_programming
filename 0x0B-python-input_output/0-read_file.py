#!/usr/bin/python3
"""My file module"""


def read_file(filename=""):
    """A function to read file"""

    with open(filename, 'r', encoding="UTF-8") as f:
        content = f.readlines()
    return "".join(content)
