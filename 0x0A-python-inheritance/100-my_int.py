#!/usr/bin/python3
"""The rebel module"""


class MyInt(int):
    """The rebel class"""

    def __eq__(self, other):
        """Returns the opposite of the default behavior"""
        return super().__ne__(other)
    
    def __ne__(self, other):
        """Returns the opposite of the default behavior"""
        return super().__eq__(other)
