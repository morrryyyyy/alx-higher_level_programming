#!/usr/bin/python3
"""initializes a square"""
class Square:
    def __init__(self, size=0):
        """
        Initialize the Square with a given size.

        Args:
            size (int): The size of the square, must be an integer and >= 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
