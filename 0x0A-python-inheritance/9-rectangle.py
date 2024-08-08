#!/usr/bin/python3
"""
This contains the BaseGeometry class
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    A subclass of BaseGeometry
    Represents a rectangle

    Attributes:
        __width (int): the width of the rectangle
        __height (int): the height of the rectangle
    """
    def __init__(self, width, height):
        """
        Initializes the rectangle with width and height

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Calculates the are of the rectangle

        Returns:
            int: the area of the rectangle
        """

        return self.__width * self.__height

    def __str__(self):
        """informal string representation of the rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
