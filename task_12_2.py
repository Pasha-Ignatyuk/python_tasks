import math


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle(Point):
    def __init__(self, radius):
        self.radius = radius

    def per(self):
        perimetr = 2 * math.pi * self.radius
        return perimetr

    def square(self):
        square = math.pi * self.radius ** 2
        return square


class Triangle(Point):

    def __init__(self, x1, y1, x2, y2, x3, y3):  # атрибуты - координаты трех точек в плоскости
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def per(self):
        perimetr = math.sqrt((self.y2 - self.y1) ** 2 + (self.x2 - self.x1) ** 2) + math.sqrt(
            (self.y3 - self.y1) ** 2 + (self.x3 - self.x1) ** 2) + math.sqrt(
            (self.y3 - self.y2) ** 2 + (self.x3 - self.x2) ** 2)
        return perimetr

    def square(self):
        semi_perimeter = (math.sqrt((self.y2 - self.y1) ** 2 + (self.x2 - self.x1) ** 2) + math.sqrt(
            (self.y3 - self.y1) ** 2 + (self.x3 - self.x1) ** 2) + math.sqrt(
            (self.y3 - self.y2) ** 2 + (self.x3 - self.x2) ** 2)) / 2
        square = math.sqrt(semi_perimeter) * math.sqrt(semi_perimeter - math.sqrt(
            (self.y2 - self.y1) ** 2 + (self.x2 - self.x1) ** 2)) * math.sqrt(semi_perimeter - math.sqrt(
            (self.y3 - self.y1) ** 2 + (self.x3 - self.x1) ** 2)) * math.sqrt(
            semi_perimeter - math.sqrt((self.y3 - self.y2) ** 2 + (self.x3 - self.x2) ** 2))
        return square


class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def per(self):
        return 4 * self.side_length

    def square(self):
        return self.side_length ** 2


pnt = Circle(3)
cc = pnt.per()
print(cc)
print(pnt.square())

trn = Triangle(0, 0, 0, 4, 2, 0)
print(trn.per())
print(trn.square())

sq = Square(2)

figure = [pnt, trn, sq]
for el in figure:
    print(el.square())
