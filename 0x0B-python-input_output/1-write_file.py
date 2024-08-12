#!/usr/bin/python3
"""
This is the 1-write_file module.
It contains the function: write_file(filename="", text="")
"""


def write_file(filename="", text=""):
    """
    Overwrites the contents of a file.
    Create a new file if it doesn't exist.
    
    Args:
        filename: the file to be overwritten.
        text: the text to add.
    
    Returns:
        int: the number of characters added.
    """

    with open(filename, "w") as f:
        number_of_chars =f.write(text)
    return number_of_chars
