#!/usr/bin/python3
"""asd asd asd"""


class Rectangle:
    """asd asd asd"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

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

    def area(self):
        """asd asd asd"""
        return self.__height * self.__width

    def perimeter(self):
        """asd asd asd"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        """asd asd asd"""
        if self.__width == 0 or self.height == 0:
            return ""

        string = ""
        for i in range(self.__height):
            string += str(self.print_symbol) * self.__width
            string += "\n"
        return string[:-1]

    def __repr__(self):
        """asd asd asd"""
        return f"Rectangle({self.__width}, {self.__height})"
        """return "Rectangle({}, {})".format(self.__width, self.__height)"""

    def __del__(self):
        """asd asd asd"""
        if Rectangle.number_of_instances > 0:
            Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """asd asd asd"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """asd asd asd"""
        return cls(size, size)
