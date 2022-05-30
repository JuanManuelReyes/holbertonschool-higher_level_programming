#!/usr/bin/python3
"""asd asd asd"""


class BaseGeometry:
    """asd asd asd"""

    def area(self):
        """asd asd asd"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """asd asd asd"""

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
