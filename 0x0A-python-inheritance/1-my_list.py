#!/usr/bin/python3
"""My list module"""


class MyList(list):
    """A class that inherits from list"""

    def print_sorted(self):
        """Prints the list, but sorted"""
        print(sorted(self))
