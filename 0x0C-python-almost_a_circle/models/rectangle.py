#!/usr/bin/python3
"""
This is the rectangle.py module.
It contains the Rectangle class.
"""


from models.base import Base

class Rectangle(Base):
    """
    A subclass of the Base class.
    Represents a rectangle.

    Attributes:
        __width (int): the width of the rectangle.
        __height (int): the height of the rectangle.
        __x(int): the x axis of the rectangle.
        __y(int): the y axis of the rectangle.
        id(int): the id of the rectangle.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, y):
        self.__y = y