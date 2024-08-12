#!/usr/bin/python3
"""
This is the 3-to_json_string.py module.
It contains the function: to_json_string(my_obj)
"""


def to_json_string(my_obj):
    """
    Converts a string to JSON

    Returns:
        my_obj (string): the JSON representation of the string
    """

    import json
    json_string = json.dumps(my_obj)
    return json_string
