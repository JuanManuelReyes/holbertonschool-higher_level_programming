#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    cpy = a_dictionary.copy()
    for i, x in cpy.items():
        cpy[i] = x * 2
    return cpy
