#!/usr/bin/python3
"""
Class Square
"""


class Square:
    """
    Argument size: square size
    """
    def __init__(self, size=0):
        """
        Atribute __size: int size of square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
