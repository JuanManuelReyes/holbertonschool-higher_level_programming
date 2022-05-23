#!/usr/bin/python3
"""asd asd asd"""


def matrix_divided(matrix, div):
        """asd asd asd"""

        if (len(matrix[0]) + len(matrix[1])) % 2 != 0:
                raise TypeError("Each row of the matrix \
                must have the same size")
        
        for x in matrix:
                for y in x:
                        if type(y) is not int and type(y) is not float:
                                raise TypeError("matrix must be a matrix \
                                (list of lists) of integers/floats")
        
        if type(div) is not int or type(div) is not float:
                raise TypeError("div must be a number")
        
        if div == 0:
                raise ZeroDivisionError("division by zero")
        
        new_matrix = [[round(y / div, 2) for y in x] for x in matrix]

        return new_matrix
        


