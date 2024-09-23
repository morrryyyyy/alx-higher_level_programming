#!/usr/bin/python3
"""
This is the 6-load_from_json_file.py module
It contains the function: 6-load_from_json_file(filename)
"""


def load_from_json_file(filename):
    """
    creates an Object from a “JSON file”

    Args:
        filename: the JSON file to be loaded
    """
    import json
    with open(filename) as f:
        new_file = json.load(f)
        return new_file

