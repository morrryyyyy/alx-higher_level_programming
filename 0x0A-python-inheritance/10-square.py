#!/usr/bin/python3
"""
This is a square which inherits from the rectangle class
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    A square class which inherits from the rectangle class
    """
    def __init__(self, size):
        """
        Initializes the square with a size.

        Args:
            size (int): the size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: the area of the square.
        """
        return self.__size ** 2
