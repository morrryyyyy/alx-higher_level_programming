#!/usr/bin/python3
"""
This is the 2-is_same_class module
It contains ne function: is_same_class(obj, a_class)
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is an instance of a class

    Args:
        obj (object): The object to check.
        a_class (type): The class to check against.

    Returns:
        bool: True if obj is an instance of a_class, otherwise False.
    """
    return (type(obj) == a_class)

