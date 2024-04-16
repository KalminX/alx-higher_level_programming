#!/usr/bin/python3
"""My lookup module"""

def inherits_from(obj, a_class):
    """Returns True if the object is an instance of a class that inherited from the specified class"""
    return issubclass(obj, a_class)
