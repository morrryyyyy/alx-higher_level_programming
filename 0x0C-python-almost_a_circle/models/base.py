#!/usr/bin/python3
"""This is the base.py module"""
import json


class Base:
    """Represents the Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """
        converts the list to JSON.

        Returns
            the JSON representation.
        """
        if list_dictionaries is None:
            return "[]"
        else:
            my_dict = json.dumps(list_dictionaries)
            return my_dict
