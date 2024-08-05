#!/usr/bin/python3

"""
This is the 0-lookup module.
It contains one function: lookup(obj)
"""


def lookup(obj):
    """
    Lists the methods and attributes of an object
    
    Returns:
        the list of available attributes and methods of the object
    """
    return dir(obj)