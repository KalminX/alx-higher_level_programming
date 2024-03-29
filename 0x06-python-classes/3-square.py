#!/usr/bin/python3
"""3-square.py"""


class Square:
    """A square class"""
    def __init__(self, size=0):
        """The constructor method"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates the area of the square"""
        return self.__size ** 2
