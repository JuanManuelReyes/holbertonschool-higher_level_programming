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

    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    pt=[1] 
    for i in range(n): 
        print(pt) 
        newlist=[] 
        newlist.append(pt[0]) 
        for i in range(len(pt)-1): 
            newlist.append(pt[i]+pt[i+1]) 
        newlist.append(pt[-1]) 
        pt=newlist 
