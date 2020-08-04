while True:
    enter = int(input('Введите 1 для выбора конвертера дюймов в сантиметры, 2 - для выбора конвертера сантиметров в дюймы,\n '
              '3 - миль в километры, 4 - километров в мили, 5 - фунтов в килограммы, 6 - килограммов в фунты,\n '
              '7 - унций в граммы, 8 - граммов в унции, 9 - галлонов в литры, 10 - литров в галлоны,\n '
              '11 - пинт в литры, 12 - литров в пинты. Для выходв из программы введите 0'))

    if enter == 1:
        def inch():
            enter = float(input("Введите дюймы для перевода в санитметры"))
            centimeter = enter * 2.54
            print(centimeter)
            return centimeter
        inch()
    elif enter == 2:
        def cent():
            enter = float(input("Введите сантиметры для перевода в дюймы"))
            inch = enter * 0.393701
            print(inch)
            return inch
        cent()
    elif enter == 3:
        def mile():
            enter = float(input("Введите мили для перевода в километры"))
            mile = enter * 1.60934
            print(mile)
            return mile
        mile()
    elif enter == 4:
        def km():
            enter = float(input("Введите километры для перевода в мили"))
            km = enter * 0.621371
            print(km)
            return km
        km()
    elif enter == 5:
        def pound():
            enter = float(input("Введите фунты для перевода в кг"))
            pound = enter * 0.453592
            print(pound)
            return pound
        pound()
    elif enter == 6:
        def kg():
            enter = float(input("Введите кг для перевода в фунты"))
            kg = enter * 2.20462
            print(kg)
            return kg
        kg()
    elif enter == 7:
        def ounce():
            enter = float(input("Введите унции для перевода в граммы"))
            ounce = enter * 28.3495
            print(ounce)
            return ounce
        ounce()
    elif enter == 8:
        def gram():
            enter = float(input("Введите граммы для перевода в унции"))
            gram = enter * 0.035274
            print(gram)
            return gram
        gram()
    elif enter == 9:
        def gallon():
            enter = float(input("Введите галлоны для перевода в литры"))
            gallon = enter * 4.54609
            print(gallon)
            return gallon
        gallon()
    elif enter == 10:
        def liter():
            enter = float(input("Введите литры для перевода в галлоны"))
            liter = enter * 0.264172
            print(liter)
            return liter
        liter()
    elif enter == 11:
        def pint():
            enter = float(input("Введите пинты для перевода в литры"))
            pint = enter * 0.473176
            print(pint)
            return pint
        pint()
    elif enter == 12:
        def lit():
            enter = float(input("Введите литры для перевода в пинты"))
            lit = enter * 2.11338
            print(lit)
            return lit
        lit()
    elif enter == 0:
        break
