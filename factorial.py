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
