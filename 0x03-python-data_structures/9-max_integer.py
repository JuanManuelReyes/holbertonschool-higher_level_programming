#!/bin/python3
def max_integer(my_list=[]):
    if my_list:
        intmax = my_list[0]
        for i in my_list:
            if i > intmax:
                intmax = i
        return intmax
    else:
        return None
