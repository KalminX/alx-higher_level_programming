#!/usr/bin/python3
"""My rectangle package"""
from base import Base


class Rectangle(Base):
    """My rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """The init method"""
        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
    
    def set_width(self, value):
        """The width setter"""
        self.__width = value
    
    def get_width(self):
        """The width getter"""
        return self.__width
    
    def set_height(self, value):
        """The height setter"""
        self.__height = value
    
    def get_height(self):
        """The height getter"""
        return self.__height
    
    def set_x(self, value):
        """The x setter"""
        self.__x = value
    
    def get_x(self):
        """The x getter"""
        return self.__x
    
    def set_y(self, value):
        """The y setter"""
        self.__y = value
    
    def get_y(self):
        """The y getter"""
        return self.__y
