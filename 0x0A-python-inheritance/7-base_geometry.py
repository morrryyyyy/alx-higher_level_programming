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
        """raises an exception"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        Checks if value is an integer greater than 0
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        self.name = name
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(self.name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
