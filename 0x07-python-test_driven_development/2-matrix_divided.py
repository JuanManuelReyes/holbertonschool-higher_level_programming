#!/usr/bin/python3
"""asd asd asd"""


def matrix_divided(matrix, div):
        """asd asd asd"""

        if type(div) is not int and type(div) is not float:
                raise TypeError("div must be a number")

        error_msg = "matrix must be a matrix (list of lists) of integers/floats"
        if type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0:
                raise TypeError(error_msg)
        
        if div == 0:
                raise ZeroDivisionError("division by zero")

        new_mtrx = []
        for i in matrix:
                if type(i) is not list:
                        raise TypeError(error_msg)
                if len(i) != len(matrix[0]):
                        raise TypeError("Each row of the matrix must have the same size")
                        
        new_list = []
        for x in list:
            if type(x) is not int and type(x) is not float:
                raise TypeError(error_msg)
            new_list.append(round(x/div, 2))
        new_mtrx.append(new_list)
        return new_mtrx
        
