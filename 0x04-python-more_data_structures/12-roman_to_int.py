#!/usr/bin/python3

def equivalents(r):
    if (r == 'I'):
        return 1
    if (r == 'V'):
        return 5
    if (r == 'X'):
        return 10
    if (r == 'L'):
        return 50
    if (r == 'C'):
        return 100
    if (r == 'D'):
        return 500
    if (r == 'M'):
        return 1000
    return -1


def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return Nonei
    if roman_string == "":
        return 0
    res = 0
    i = 0
    while (i < len(roman_string)):
        s1 = equivalents(roman_string[i])
        if s1 == -1:
            s1 = 0
        if s1 == 0:
            s2 = equivalents(roman_string[i + 1])
            if s2 == -1:
                s2 = 0
            if (s1 >= s2):
                res = res + s1
                i = i + 1
            else:
                res = res + s2 - s1
                i = i + 2
        else:
            res = res + s1
            i = i + 1

    return res

