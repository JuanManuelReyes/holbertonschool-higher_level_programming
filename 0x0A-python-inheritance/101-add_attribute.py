#!/usr/bin/python3
"""asd asd asd"""


def add_attribute(obj, attribute, value):
    """asd asd asd"""

    if ('__dict__' in dir(obj)):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
