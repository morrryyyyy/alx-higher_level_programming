#!/usr/bin/python3
"""This is the text_indentation module."""


def text_indentation(text):
    """
    Prints a text with two new lines after: '.', '?' & ':'.

    Args:
        test (str): the text to format.

    Returns:
        result (str): the formatted text.

    Raises:
        TypeError: if text is not a string.
    """
    # Check if text is not a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Replace characters
    text = text.replace('.', '.\n\n')
    text = text.replace('?', '?\n\n')
    text = text.replace(':', ':\n\n')

    # Remove any trailing spaces after the newlines.
    lines = text.splitlines()
    stripped_lines = [line.strip() for line in lines]
    result = "\n".join(stripped_lines)

    print(result)
