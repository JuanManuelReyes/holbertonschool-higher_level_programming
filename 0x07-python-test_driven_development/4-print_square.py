#!/usr/bin/python3
"""asd asd asd"""


def print_square(size):
    """asd asd asd"""

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for x in range(size):
        for y in range(size):
            print("#", end="")
        print()
