#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)

print("======TESTS=====")

print("------------------------------------")
print(matrix_divided([[1, 2, 3], [4, 5, 6.7]], 2))
print("------------------------------------")
print(matrix_divided([[1, 2, 3], [4, 5, 6.7]], 9223372036854775807))
print("------------------------------------")
print(matrix_divided([[1, 2, 3], [4, 5, 6]], -5))
print("------------------------------------")
print(matrix_divided([[1, 2, 3], [4, 5, 6]], 2.5))
print("------------------------------------")
print(matrix_divided([[-1.5], [-2.5]], 2.5))
print("------------------------------------")
print(matrix_divided([[True], [False]], True))
print("------------------------------------")
print(matrix_divided(None, 2))
print("------------------------------------")
print(matrix_divided([], 2))
print("------------------------------------")
print(matrix_divided([[], [], []], 2))
print("------------------------------------")
print(matrix_divided([[1, 2, 3], [4]], 2))
print("------------------------------------")
print(matrix_divided([[1, 2, 3], [4, 5, 6], [7]], 2))
print("------------------------------------")
print(matrix_divided([["Test"], ["Case"]], 2))
print("------------------------------------")
print(matrix_divided([[1, 2, 3], {"test" : 4}], 2))
print("------------------------------------")
print(matrix_divided([[1, 2, 3], [4, 5, 6.7]], 2, 100))
print("------------------------------------")
print(matrix_divided([[1, 2], [3, 4]], 0))
print("------------------------------------")
print(matrix_divided([[1, 2], [3, 4]], "test"))
