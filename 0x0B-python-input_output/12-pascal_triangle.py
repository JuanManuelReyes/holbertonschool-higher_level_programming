#!/usr/bin/python3
"""asd asd asd"""

def pascal_triangle(n):
    pt = [[1]]

    for rows in range(n-1):
        list = [1]
        for i in range(rows):
            list.append(pt[-1][i] + pt[-1][i+1])

        list.append(1)
        pt.append(list)

    return pt

"""
def pascal_triangle(n):

    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    pt = [1]
    for i in range(n):
        print(pt)
        newlist = []
        newlist.append(pt[0])
        for i in range(len(pt) - 1):
            newlist.append(pt[i] + pt[i + 1])
        newlist.append(pt[-1])
        pt = newlist
"""