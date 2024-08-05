#!/usr/bin/python3
"""
This is the 4-inherits_from module.
Contains the inherits_from function
"""


def inherits_from(obj, a_class):
    """returns true if obj is a subclass of a_class, otherwise false"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
