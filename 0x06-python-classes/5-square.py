#!/usr/bin/python3
"""
asd asd asd
"""


class Square:
    """
    asd asd asd
    """
    def __init__(self, size=0):
        """
        asd asd asd
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        asd asd asd
        """
        return ((self.__size) ** 2)

    @property
    def size(self):
        """
        asd asd asd
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        asd asd asd
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def my_print(self):
        """
        asd asd asd
        """
        size = self.__size
        if size == 0:
            print()
            return
        for i in range(size):
            for x in range(size):
                print('#', end="")
            print()
