"""Дана целочисленная квадратная матрица. Найти в каждой строке наибольший
элемент и поменять его местами с элементом главной диагонали.[02-4.2-ML22]"""
import random

n = 4
m = 4
matrix = [[random.randrange(0, 10) for y in range(m)] for x in range(n)]
print(matrix)

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:4d}".format(matrix[i][j]), end="")
        print()

print_matrix(matrix)

print("")  # для разделения матриц, чтобы не сливались в глазах

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        max_elem = max(matrix[i])
        if i != j:
            continue
        else:
            matrix[i][j] = matrix[i][j] * 0 + max_elem
print_matrix(matrix)
