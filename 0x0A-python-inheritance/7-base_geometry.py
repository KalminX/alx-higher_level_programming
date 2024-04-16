#!/usr/bin/python3
"""My Geometry module"""


class BaseGeometry:
    """MY BaseGeometry class"""

    def area(self):
        """Raises an Exception"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """Validates if it's an integer"""
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
