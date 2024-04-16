#!/usr/bin/python3
"""My Geometry module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that defines a rectangle"""

    def __init__(self, width, height):
        """Initializes the rectangle"""
        self.__width = width
        self.__height = height
        if type(self.__width) != int:
            raise TypeError("width must be an integer")
        if type(self.__height) != int:
            raise TypeError("height must be an integer")

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height
