class Car:
    def __init__(self, mark, model, year):
        self.__mark = mark
        self.__model = model
        self.__year = year
        self.__speed = 0

    def speed_increase(self, speed):
        self.__speed += speed
        print(self.__speed)

    def speed_decrease(self, speed):
        self.__speed -= speed
        print(self.__speed)

    def speed_reverse(self):
        self.__reverse = 1
        self.__reverse = - (self.__speed)
        print(self.__reverse)

    def display_speed(self):
        print("Текущая скорость:", self.__speed)


c = Car('bmw', '3', 2016)

c.speed_increase(10)
c.speed_decrease(5)
c.display_speed()
c.speed_reverse()
