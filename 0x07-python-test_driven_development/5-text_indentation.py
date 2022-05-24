#!/usr/bin/python3
"""asd asd asd"""


def text_indentation(text):
    """asd asd asd"""

    if type(text) is not str:
        raise TypeError("text must be a string")

    string = ""
    for i in text:
        string += i
        if i is ":" or i is "?" or i is ".":
            string += "\n"
            print(string.strip(" "))
            string = ""
    print(string.strip(" "), end="")
