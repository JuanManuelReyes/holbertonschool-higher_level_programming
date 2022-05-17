#!/usr/bin/python3
"""
asd asd asd
"""


class Square:
    """
    asd asd asd
    """
    def __init__(self, size = 0, position=(0, 0)):
        """
        asd asd asd
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        asd asd asd
        """
        return self.__position

    @position.setter
    def position(self, size):
        """
        asd asd asd
        """
        if type(size) is not tuple or len(size) != 2 or \
         type(size[0]) is not int or type(size[1]) is not int or \
          size[0] < 0 or size[1] <0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = size

    def area(self):
        """
        asd asd asd
        """
        return ((self.__size) ** 2)

    def my_print(self):
        """
        asd asd asd
        """
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                for i in range(self.__position[1]):
                    print()
            for x in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
