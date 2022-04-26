#!/usr/bin/python3
def print_last_digit(number):
        cpy = number
        if(cpy < 0):
                cpy = cpy * -1
        number = cpy
        ld = number % 10
        print(f"{ld}", end='')
        return(ld)
