#!/usr/bin/python3
"""
This is the base module.
It contains the base class for this project.
"""


class Base:
    """
    This is the base class for all object in this project
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
