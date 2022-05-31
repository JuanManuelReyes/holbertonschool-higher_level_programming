#!/usr/bin/python3
"""asd asd asd"""


class Student:
    """asd asd asd"""

    def __init__(self, first_name, last_name, age):
        """asd asd asd"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """asd asd asd"""

        if attrs is not None:
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}

        return self.__dict__

    def reload_from_json(self, json):
        """asd asd asd"""
        for key, value in json.items():
            self.__dict__[key] = value
