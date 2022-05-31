#!/usr/bin/python3
"""asd asd asd"""

"""
def pascal_triangle(n):
    if n <= 0:
        return []
    elif n == 1:
        return [[1]]

    pt = [[1]]

    for i in range(n - 1):
        pt.append([a + b for a, b in zip([0] + pt[-1], pt[-1] + [0])])

    return pt
"""
def pascal_triangle(n):
    for i in range(1, n+1):
        for j in range(0, n-i+1):
            print(' ', end=''

        C = 1
        for j in range(1, i+1):

            print(' ', C, sep='', end='')

            C = C * (i - j) // j
        print()
