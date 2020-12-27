"""Дано число. Найти сумму и произведение его цифр"""
a = input('введите число')
s = list(a)
print(s)
summa = 0
for i in s:
    i = int(i)
    summa += i
print(f'сумма цифр числа равна {summa}')
multiplication = 1
for i in s:
    i = int(i)
    multiplication *= i
print(f'произведение цифр числа равна {multiplication}')


