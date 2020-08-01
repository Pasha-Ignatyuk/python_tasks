stroka = input('enter string')
lenght = len(stroka)
check = lenght % 2
# так как у строк с четным и нечетным количеством символов
# по-разному считается центральный символ, то введено дополнительное условие
if check == 0:
    entire = int(len(stroka) / 2)  # находим целую часть от деления
    first = stroka[0]
    center = stroka[entire - 1]
    if center is first:
        print(stroka[1:lenght - 1])
    else:
        pass
# если первая и центральная буквы не равны, то ничего не делаем
else:
    entire = int(len(stroka) / 2)
    first = stroka[0]
    center = stroka[entire]
    if center is first:
        print(stroka[1:lenght - 1])
    else:
        pass
