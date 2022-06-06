#!/usr/bin/python3
"""asd asd asd"""


from models.base import Base


class Rectangle(Base):
    """asd asd asd"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize"""
        
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """asd asd asd"""

        return self.__width

    @width.setter
    def width(self, value):
        """asd asd asd"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """asd asd asd"""
        return self.__x

    @x.setter
    def x(self, value):
        """asd asd asd"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """asd asd asd"""
        return self.__y

    @y.setter
    def y(self, value):
        """asd asd asd"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """asd asd asd"""
        return self.__width * self.__height

    def display(self):
        """asd asd asd"""

        for i in range(self.y):
                print("")

        for x in range(self.__height):
            for y in range(self.__x):
                    print(" ", end="")

            for z in range(self.__width):
                print("#", end="")

            print("")
    
    def __str__(self):
        """asd asd asd"""

        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)
    
    def update(self, *args, **kwargs):
        """asd asd asd"""
        
        attrs = ["id", "width", "height", "x", "y"]

        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

        for pos, arg in enumerate(args):
            if pos > (len(attrs) - 1):
                break

            setattr(self, attrs[pos], arg)
        
    def to_dictionary(self):
        """asd asd asd"""

        attrs = ["x", "y", "id", "height", "width"]

        dict = {}
        for i in attrs:
            dict[i] = getattr(self, i)
        return dict