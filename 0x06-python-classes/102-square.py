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

    def __eq__(self, other):
        """
        ==
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        !=
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        >
        """
        return (self.area() > other.area())

    def __ge__(self, other):
        """
        >=
        """
        return (self.area() >= other.area())

    def __lt__(self, other):
        """
        <
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        <=
        """
        return self.area() <= other.area()
