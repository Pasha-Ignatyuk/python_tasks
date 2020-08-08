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

j = 0
for i in range(n):
    max = matrix[0][j]
    for j in range(n):
        if max < matrix[i][j]:
            max = matrix[i][j]
print("максимальный элемент матрицы =", max)

k = 0
for i in range(n):
    min = matrix[0][k]
    for k in range(n):
        if min > matrix[i][k]:
            min = matrix[i][k]
print("минимальный элемент матрицы =", min)

s = 0
for row in matrix:
    s += sum(row)
print("сумма элементов матрицы = ", s)

row = [sum(row) for row in matrix]  # лист с суммами строк матрицы

max = row[0]
pos = 0
for i in range(len(row)):
    if row[i] > max:
        max = row[i];
        pos = i
print("номер ряда с максимальной суммой элементов:", pos + 1)

sum_column = [sum(row[i] for row in matrix) for i in range(len(matrix[0]))]  # лист с суммами колонок матрицы
max_sum_column = sum_column[0]
pos = 0
for i in range(len(sum_column)):
    if sum_column[i] > max_sum_column:
        max_sum_column = sum_column[i];
        pos = i
print("номер колонки с максимальной суммой элементов:", pos + 1)  # колонка с наибольшей суммой элеменов

min_sum_row = row[0]
pos = 0
for i in range(len(row)):
    if row[i] < min_sum_row:
        min_sum_row = row[i];
        pos = i
print("номер ряда с минимальной суммой элементов:", pos + 1)

min_sum_column = sum_column[0]
pos = 0
for i in range(len(sum_column)):
    if sum_column[i] < min_sum_column:
        min_sum_column = sum_column[i];
        pos = i
print("номер колонки с минимальной суммой элементов:", pos + 1)

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if i != j:
            matrix[i][j] = matrix[i][j] * 0
        else:
            continue
print_matrix(matrix)

# создаем матрицу А
n_2 = 2
m_2 = 2
matrix_a = [[random.randrange(0, 5) for y in range(m_2)] for x in range(n_2)]


def print_matrix_a(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:4d}".format(matrix[i][j]), end="")
        print()


print(matrix_a)

print_matrix(matrix_a)
#  создаем матрицу Б
n_3 = n_2
m_3 = m_2
matrix_b = [[random.randrange(0, 3) for y in range(m_3)] for x in range(n_3)]


def print_matrix_b(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:4d}".format(matrix[i][j]), end="")
        print()


print(matrix_b)

print_matrix(matrix_b)

n_summy_matrix = n_2
m_summy_matrix = m_2
summy_matrix = [[random.randrange(0, 1) for y in range(m_summy_matrix)] for x in range(n_summy_matrix)]

for i in range(len(matrix_a)):
    for j in range(len(matrix_a[0])):
        summy_matrix[i][j] = matrix_a[i][j] + matrix_b[i][j]
print("")  # для разделения матриц, чтобы не сливались в глазах
print_matrix(summy_matrix)

n_subtraction_matrix = n_2  # разность матриц А и Б
m_subtraction_matrix = m_2
subtraction_matrix = [[random.randrange(0, 1) for y in range(m_subtraction_matrix)] for x in
                      range(n_subtraction_matrix)]
for i in range(len(matrix_a)):
    for j in range(len(matrix_a[0])):
        subtraction_matrix[i][j] = matrix_a[i][j] - matrix_b[i][j]
print("")  # для разделения матриц, чтобы не сливались в глазах
print_matrix(subtraction_matrix)

# матрицa А,умноженнаяна число
enter = int(input('Ведите число, на которое следует умножить matrix_a'))
n_multiplication_matrix = n_2
m_multiplication_matrix = m_2
multiplication_matrix = [[random.randrange(0, 1) for y in range(m_multiplication_matrix)] for x in
                         range(m_multiplication_matrix)]
for i in range(len(matrix_a)):
    for j in range(len(matrix_a[0])):
        multiplication_matrix[i][j] = matrix_a[i][j] * enter
print("")  # для разделения матриц, чтобы не сливались в глазах
print_matrix(multiplication_matrix)
