#!/usr/bin/python3
"""
This contains the BaseGeometry class
"""


class BaseGeometry():
    """
    A class with an unimplemented method

    Raises:
        An exception
    """
    def area(self):
        raise Exception("area() is not implemented")
