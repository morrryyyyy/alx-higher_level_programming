#!/usr/bin/python3
"""
This is the 1-my_list module
It contains only one class: MyList
"""


class MyList(list):
    """A subclass of the list object"""
    def print_sorted(self):
        """
        A public instance method
        Prints the list in ascending order
        """
        new_list = sorted(self)
        print(new_list)
