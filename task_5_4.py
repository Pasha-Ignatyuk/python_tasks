"""Для заданного числа N составьте программу вычисления суммы
S=1+1/2+1/3+1/4+...+1/N, где N – натуральное число. [02-3.2-ML21]"""
number = 6
lst = []
while number > 0:
    lst.append(number)
    number -= 1
S = 0
for el in lst:
    el = 1 / el
    S += el
print(S)