#!/usr/bin/python3
"""asd asd asd"""


def text_indentation(text):
    """asd asd asd"""

    if type(text) is not str:
        raise TypeError("text must be a string")

    flag = 0
    for i in text:
        if i is ":" or i is "?" or i is ".":
            print(i, end="\n\n")
            flag = 1
        else:
            if flag == 1:
                print("", end="")
                flag = 0
            else:
                print(i, end="")