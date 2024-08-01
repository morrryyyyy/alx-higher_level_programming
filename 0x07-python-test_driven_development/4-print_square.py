#!/usr/bin/python3
"""
This is the 4-print_square module.
It has only one function: print_square(size)
"""

def print_square(size):
    """
    Prints a square of size 'size'
    
    Args:
        size (int): the size of the square.
        
    Returns:
        the square

    Raises:
        TypeError: if the size is not an integer
        ValueError: if the size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)