#!/usr/bin/python3
"""asd asd asd"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """asd asd asd"""

    def __init__(self, width, height):
        """asd asd asd"""

        super().integer_validator("width", width)
        self.__width = width

        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """asd asd asd"""

        return self.__width * self.__height

    def __str__(self):
        """asd asd asd"""
        return f"[Rectangle] {self.__width}/{self.__height}"