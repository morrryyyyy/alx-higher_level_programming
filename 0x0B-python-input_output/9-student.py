#!/usr/bin/python3
"""
This is the 9-student module.
It contains the class: Student().
"""


class Student:
    """Represents a student"""

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new student.

        Args:
        first_name(str): the student's first name.
        last_name(str): the student's last name.
        age(int): the student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns:
        The JSON representation of the each instance of Student
        """
        return self.__dict__
