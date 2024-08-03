#!/usr/bin/python3
"""
This is the 2-rectangle module
It contains the class rectangle
"""


class Rectangle():
    """
    Creates a class called Rectangle

    """
    # A class variable counting the number of rectangles
    number_of_instances = 0

    # A class variable for string representation
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a new rectangle

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        return self.width * self.height

    def perimeter(self):
        """
        Defines the perimeter of the rectangle

        Returns:
            the perimeter of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        rect = []
        for i in range(self.height):
            rect.append(str(self.print_symbol) * self.width)
        result = "\n".join(rect)
        return result

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Delete the rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @classmethod
    def bigger_or_equal(cls, rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        largest = rect_1

        if rect_2.area() > rect_1.area():
            largest = rect_2
        return largest
