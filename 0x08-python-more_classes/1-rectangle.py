#!/usr/bin/python3
"""asd asd asd"""


class Rectangle:
    """asd asd asd"""
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """asd asd asd"""
        return self.__width

    @width.setter
    def width(self, value):
        """asd asd asd"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """asd asd asd"""
        return self.__height

    @height.setter
    def height(self, value):
        """asd asd asd"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
