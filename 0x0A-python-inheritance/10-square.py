#!/usr/bin/python3
"""asd asd asd"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """asd asd asd"""

    def __init__(self, size):
        """asd asd asd"""

        self.__size = size

        super().integer_validator("size", size)
        super().__init__(size, size)
