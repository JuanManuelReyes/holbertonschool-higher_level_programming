#!/usr/bin/python3
"""asd asd asd"""


def matrix_divided(matrix, div):
    """asd asd asd"""

    error_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(error_msg)

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
        
    mtrx = []
    for i in matrix:
        if type(i) is not list:
            raise TypeError(error_msg)
        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        list = []
        for pos in i:
            if type(pos) is not int and type(pos) is not float:
                raise TypeError(error_msg)
            list.append(round(pos/div, 2))
        mtrx.append(list)
    return mtrx