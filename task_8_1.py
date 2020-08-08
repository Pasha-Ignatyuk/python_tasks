#  рекурсия
number = int(input('enter a positive integer'))


def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n > 1:
        return n * factorial(n - 2)



print(factorial(number))