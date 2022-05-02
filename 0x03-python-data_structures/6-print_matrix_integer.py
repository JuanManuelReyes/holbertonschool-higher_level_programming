#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for x in i:
            if x is not i[len(i) - 1]:
                print(f"{x}", end=" ")
            else:
                print(f"{x}", end="")
        print()
