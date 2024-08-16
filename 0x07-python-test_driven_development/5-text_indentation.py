#!/usr/bin/python3
"""This is the text_indentation module."""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters: '.', '?', ':'.
    
    Args:
        text (str): The text to format.
    
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize a variable to hold the modified text
    result = ""
    
    # Iterate through each character in the text
    i = 0
    while i < len(text):
        result += text[i]
        if text[i] in ".?:":
            result += "\n\n"
            i += 1
            # Skip any spaces following the punctuation
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
    
    # Print the final result, but only if it's not empty
    if result.strip():
        print(result, end='')


if __name__ == "__main__":
    import doctest
    doctest.testmod()
