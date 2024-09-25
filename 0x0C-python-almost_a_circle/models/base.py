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

    @staticmethod
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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        dict_list = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(dict_list)
        with open(filename, "w") as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        converts JSON string back to Python list.
        """
        if json_string is None or json_string == "":
            return []
        my_string = json.loads(json_string)
        return my_string
