#!/usr/bin/python3

"""
This is the 0-add_integer module
It has only one function: add_integer(a, b).
"""
def add_integer(a, b=98):
    """
    Adds two integers or floats (after casting them to integers)

    Args:
        a (int or float): the first integer
        b (int or float): the second integer with a defualt value of 98

    Returns:
       int: the sum of a and b after casting them to integers

    Raises:
    TypeError: if a or b are not integers or floats
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b