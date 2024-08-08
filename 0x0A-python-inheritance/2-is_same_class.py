#!/usr/bin/python3
"""
This is the 2-is_same_class module
It contains the function: is_same_class(obj, a_class)
"""


def is_same_class(obj, a_class):
    """return true if obj is the exact class a_class, otherwise false"""
    return type(obj) is a_class
