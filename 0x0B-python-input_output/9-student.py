#!/usr/bin/python3
"""My class module"""


class Student:
    """My class module"""
    def __init__(self, first_name, last_name, age):
        """Method to initialize the student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Method to append to a file"""
        return self.__dict__
