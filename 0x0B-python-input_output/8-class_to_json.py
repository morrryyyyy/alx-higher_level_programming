#!/usr/bin/python3
"""
This is the 8-class_to_json module.
It contains the function: class_to_json(obj).
"""


def class_to_json(obj):
    """
    converts a class to its JSON representation.

    Args:
        obj(object): an instance of the class.

    Returns:
    the dictionary representation of the class.
    """

    return obj.__dict__
