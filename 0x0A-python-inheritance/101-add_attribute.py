#!/usr/bin/python3
"""My module that adds an attribute"""

def add_attribute(obj, attribute, value):
    """Adds an attribute to an object if possible"""
    if hasattr(obj, '__dict__'):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")