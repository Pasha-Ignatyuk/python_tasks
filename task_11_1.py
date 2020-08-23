class Computer:
    def __init__(self, brand, type, price):
        self.__brand = brand
        self.__type = type
        self.__price = price

    def set_brand(self, brand):
        if len(brand) in range(1, 10):
            self.__brand = brand
        else:
            print('Брэнд не определен')

    def set_type(self, type):
        if len(type) in range(1, 15):
            self.__type = type
        else:
            print('Тип не определен')

    def set_price(self, price):
        if price in range(150, 5001):
            self.__price = price
        else:
            print('Цена не верна')

    def get_brand(self):
        return self.__brand

    def get_type(self):
        return self.__type

    def get_price(self):
        return self.__price

    def display_info(self):
        print("Брэнд:", self.__brand, "\tТип:", self.__type, '\tЦена:', self.__price)

    def capital(self):
        print(self.__brand.upper())


comp = Computer("Lenovo", "transformer", 1000)

comp.set_price(6000)
comp.display_info()
comp.capital()


class Car:
    def __init__(self, mark, model, year):
        self.__mark = mark
        self.__model = model
        self.__year = year

    @property
    def mark(self):
        return self.__mark

    @mark.setter
    def mark(self, mark):
        if len(mark) in range(1, 20):
            self.__mark = mark
        else:
            print('Марка неопределена')

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if len(model) in range(1, 20):
            self.__model = model
        else:
            print('Мoдель неопределена')

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if year in range(1900, 2021):
            self.__year = year
        else:
            print('Неверный год')

    def display_info(self):
        print("Марка:", self.__mark, "\tМодель:", self.__model, '\tГод выпуска:', self.__year)

    def capital(self):
        print(self.__mark.upper())


car = Car('bmw', '3', 2016)

car.year = 2025
car.display_info()
car.capital()


class House:
    def __init__(self, flors, square, rooms):
        self.__flors = flors
        self.__square = square
        self.__rooms = rooms

    @property
    def flors(self):
        return self.__flors

    @flors.setter
    def flors(self, flors):
        if flors in range(1, 3):
            self.__flors = flors
        else:
            print('Дом многоквартирный')

    @property
    def square(self):
        return self.__square

    @square.setter
    def square(self, square):
        if square in range(1, 500):
            self.__square = square
        else:
            print('Вилла')

    @property
    def rooms(self):
        return self.__rooms

    @rooms.setter
    def rooms(self, rooms):
        if rooms / self.__flors > 1:
            self.__rooms = rooms
        else:
            print('Неверное число комнат')

    def display_info(self):
        print("Число этажей:", self.__flors, "\tПлощадь:", self.__square, '\tКоличество комнат:', self.__rooms)


hs = House(1, 200, 5)

hs.rooms = 0
hs.display_info()


class Trafic:
    def __init__(self, mark, model, year):
        self.__mark = mark
        self.__model = model
        self.__year = year
        self.__speed = 0

    def set_mark(self, mark):
        if len(mark) in range(1, 20):
            self.__mark = mark
        else:
            print('Марка неопределена')

    def set_model(self, model):
        if len(model) in range(1, 20):
            self.__model = model
        else:
            print('Мoдель неопределена')

    def set_year(self, year):
        if year in range(1900, 2021):
            self.__year = year
        else:
            print('Неверный год')

    def set_speed(self, speed):
        self.__speed += speed
        print(self.__speed)

    def get_mark(self):
        return self.__mark

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_speed(self):
        return self.__speed

    def display_speed(self):
        print("Текущая скорость:", self.__speed)

    def display_info(self):
        print("Марка:", self.__mark, "\tМодель:", self.__model, '\tГод выпуска:', self.__year)


c = Trafic('bmw', '3', 2016)

c.set_speed(5)
c.set_speed(5)
c.display_info()
c.display_speed()


class Univer:
    def __init__(self, stud, facult, rate):
        self.__stud = stud
        self.__facult = facult
        self.__rate = rate

    @property
    def stud(self):
        return self.__stud

    @stud.setter
    def stud(self, stud):
        if stud in range(1, 25000):
            self.__stud = stud
        else:
            print('Введите число студентов')

    @property
    def facult(self):
        return self.__facult

    @facult.setter
    def facult(self, facult):
        if facult in range(1, 100):
            self.__facult = facult
        else:
            print('Введите число факультетов')

    @property
    def rate(self):
        return self.__rate

    @rate.setter
    def rate(self, rate):
        if rate in range(1, 10):
            self.__rate = rate
        else:
            print('Установите рейтинг от 1 до 10')

    def display_info(self):
        print("Число студентов:", self.__stud, "\tЧисло факультетов:", self.__facult, '\tРейтинг:', self.__rate)

    def capital(self):
        print(self.__mark.upper())


univ = Univer(15000, 50, 10)
univ.stud = 16000
univ.display_info()
