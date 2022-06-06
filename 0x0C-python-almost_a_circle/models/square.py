#!/usr/bin/python3
"""asd asd asd"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """asd asd asd"""

    def __init__(self, size, x=0, y=0, id=None):
        """asd asd asd"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """asd asd asd"""

        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """asd asd asd"""

        return self.width

    @size.setter
    def size(self, value):
        """asd asd asd"""

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """asd asd asd"""

        attrs = ["id", "size", "x", "y"]

        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

        for pos, arg in enumerate(args):
            if pos > (len(attrs) - 1):
                break

            setattr(self, attrs[pos], arg)

    def to_dictionary(self):
        """asd asd asd"""

        attrs = ["id", "x", "size", "y"]

        dict = {}
        for i in attrs:
            dict[i] = getattr(self, i)
        return dict
