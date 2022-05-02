#!/bin/python3
def max_integer(my_list=[]):
    if my_list:
        maxint = my_list[0]
        for i in my_list:
            if i > maxint:
                maxint = i
        return maxint
    else:
        return None
