#!/usr/bin/python3
"""4-square.py"""


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

    @property
    def size(self):
        """Gets the size of the Square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """Prints the square with chatacter #"""
        if self.__size == 0:
            print()
        else:
            side = self.__size
            for i in range(side):
                for j in range(side):
                    print("#", end="")
                    if j == side-1:
                        print()
