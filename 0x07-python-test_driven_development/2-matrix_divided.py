#!/usr/bin/python3
"""
This is the 2-matrix_divided module
It has only one function: matrix_divided(matrix, div)
"""


def matrix_divided(matrix, div):
    """
    Divides all the elements in a matrix by a given divisor.

    Args:
        matrix (list of lists of int/float): The matrix to be divided.
        div (int/float): The divisor.

    Returns:
        list of lists of floats: A new matrix with element divided by div.

    Raises:
        TypeError: If matrix elements are not lists of integers or floats,
        or if div is not an integer or float.
        ZeroDivisionError: If div is zero.
    """
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(error_msg)
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(error_msg)
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(error_msg)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(element / div, 2) for element in row] for row in matrix]
