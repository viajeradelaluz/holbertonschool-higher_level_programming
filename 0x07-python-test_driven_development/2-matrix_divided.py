#!/usr/bin/python3
"""Divide a matrix

This module contains one function that divide a matrix.

    """


def matrix_divided(matrix, div):
    """ Method that divides a matrix by a integer """

    matrix_error = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(matrix_error)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        if not row or not isinstance(row, list):
            raise TypeError(matrix_error)

        row_size = len(matrix[0])
        if row_size is not len(row):
            raise TypeError("Each row of the matrix must have the same size")

        item = []
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError(matrix_error)
            item.append(round(num / div, 2))

        new_matrix.append(item)

    return new_matrix
