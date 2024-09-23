#!/usr/bin/python3
"""
This is the 5-save_to_json_file.py module
It contains the function: save_to_json_file(my_obj, filename)
"""


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file, using a JSON representation

    Args:
        my_obj(object): the object to be written
        filename(file): the file to be overwritten
    """

    import json
    with open(filename, "w") as f:
        json.dump(my_obj, f)
