#!/usr/bin/python3
"""
This is the 0-read_file module
It contains one function: read_file(filename="")
"""


def read_file(filename=""):
    """
    reads a text file and prints it to stdout

    Args:
    filename: the file to be read
    """
    with open(filename, encoding="UTF-8") as file:
        content = file.read()
        print(content, end="")
