#!/usr/bin/python3
"""5-square.py"""


class Square:
    """A square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Creates a square
        Args:
            size: length of the square
            position: coordinate of where the
            square is created
        """
        self.size = size
        self.position = position

    def area(self):
        """Calculates the area of the square"""
        return self.__size ** 2

    @property
    def position(self):
        """Returns the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the value of position"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @property
    def size(self):
        """Gets the size of the Square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square
        Args:
            value: size to be set to
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """Prints the square with chatacter #"""
        pos = self.__position
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print(pos[0] * " " + "#" * self.__size)
