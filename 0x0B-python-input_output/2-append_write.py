#!/usr/bin/python3
"""
This is the 2-append_write module.
It contains the function: append_write(filename="", text="")
"""


def append_write(filename="", text=""):
    """
    Appends text to the end of a file.
    Create a new file if it doesn't exist.

    Args:
        filename: the file to be appended.
        text: the text to append.
    """

    with open(filename, "a") as f:
        number_of_chars = f.write(text)
    return number_of_chars
