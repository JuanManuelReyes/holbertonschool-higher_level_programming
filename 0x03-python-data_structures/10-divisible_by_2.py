#!/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        divisible = my_list.copy()
        for i in range(len(my_list)):
            if my_list[i] % 2 is 0:
                divisible[i] = True
            else:
                divisible[i] = False
        return divisible
