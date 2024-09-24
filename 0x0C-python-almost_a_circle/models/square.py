#!/usr/bin/python3
"""
This is the square.py module.
It contains the square class.
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Inherits from the rectangle class.
    Represents a square class.
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)
