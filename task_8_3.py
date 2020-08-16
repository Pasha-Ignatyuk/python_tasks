# Описать функцию Sin1( x , ε ) вещественного типа (параметры x , ε — вещественные, ε > 0),
# находящую приближенное значение функции sin( x ):
# sin( x ) = x – x ^3 /(3!) + x^ 5 /(5!) – ... + (–1) ^ n · x^( 2·n+1) /((2· n +1)!) + ... .
# В сумме учитывать все слагаемые, модуль которых больше ε.
# С помощью Sin1 найти приближенное значение синуса для данного x при шести данных ε.
import math
from math import factorial

x = math.pi
#e = input()


def Sin1(x, e):
    result = 0
    while e > 0:
        y = ((((-1) ** e) * ((x ** (2 * e + 1))) / factorial(2 * e + 1)))
        #e -= 1
        if abs(y) > e:
            result += y
            e -= 1
        else:
            e -= 1
    #print(result)
    return result


#Sin1(x, e)

for e in range(1, 7):
    print("eps = ", e, "; sin(", x, ") = ", Sin1(x, e))
