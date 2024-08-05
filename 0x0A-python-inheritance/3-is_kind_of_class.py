#!/usr/bin/python3
"""
This is the 3-is_kind_of_class module.
It contaons one function: is_kind_of_class(obj, a_class)
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is a kind of a_class.

    Args:
        obj (object): The object to be checked.
        a_class (type): TH eclass to be checked against.

    Returns:
        bool: True if obj is a kind of a_class, otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    return False
