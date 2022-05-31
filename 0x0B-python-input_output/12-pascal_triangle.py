#!/usr/bin/python3
"""asd asd asd"""

"""
def pascal_triangle(n):
    for i in range(1, n+1):
        for j in range(0, n-i+1):
            print(' ', end='')

        C = 1
        for j in range(1, i+1):
            print(' ', C, sep='', end='')
            C = C * (i - j) // j

        print()
"""

"""
from math import factorial
 
def pascal_triangle(n):
    for i in range(n):
        for j in range(n-i+1):
            print(end=" ")
 
        for j in range(i+1):
            print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
 
        print()
"""


def pascal_triangle(n):
    lis=[1] 
    for i in range(n): 
    print(lis) 
    newlist=[] 
    newlist.append(lis[0]) 
    for i in range(len(lis)-1): 
        newlist.append(lis[i]+lis[i+1]) 
    newlist.append(lis[-1]) 
    lis=newlist 
