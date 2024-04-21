#!/usr/bin/python3
"""My square package"""
from rectangle import Rectangle


class Square(Rectangle):
    """Square class inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square with size, x, y, and optional id."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return string representation of Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    def update(self, *args, **kwargs):
        """Update Square attributes."""
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Return dictionary representation of Square."""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}