#!/usr/bin/python3
"""
This is the 2-rectangle module
It contains the class rectangle
"""


class Rectangle():
    """
    Creates a class called Rectangle

    """
    def __init__(self, width=0, height=0):
        """
        Initializes a new rectangle

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the current width of the square"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the current height of the square"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Defines the area of the rectangle

        Returns:
            the area of the rectnagle"""
        return self.__width * self.__height

    def perimeter(self):
        """
        Defines the perimeter of the rectangle

        Returns:
            the perimeter of the rectangle
        """
        return 2 * (self.__width + self.__height)
