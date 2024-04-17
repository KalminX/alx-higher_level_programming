#!/usr/bin/python3
"""My class module"""


class Student:
    """My class module"""

    def __init__(self, first_name, last_name, age):
        """Method to initialize the student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Method to append to a file"""
        if attrs is not None:
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Method to append to a file"""
        for key, value in json.items():
            setattr(self, key, value)
