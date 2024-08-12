#!/usr/bin/python3
"""
This is the 4-from_json_string.py module.
It contains the function: from_json_string(my_str)
"""


def from_json_string(my_str):
    """
    Converts JSON to python

    Returns:
        my_str (string): the JSON representation of the string
    """

    import json
    json_string = json.loads(my_str)
    return json_string
