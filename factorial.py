def factorial():
    n = int(input('enter a positive integer'))
    lst = []
    fact = 1
    while n > 0:
        if n != 0:
            lst.append(n)
            fact = fact * n
            n -= 1
        else:
            break
    print(lst)
    print(fact)
    return fact


factorial()

#  рекурсия
number = int(input('enter a positive integer'))


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(number))
