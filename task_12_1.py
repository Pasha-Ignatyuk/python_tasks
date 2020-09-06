class MyTime:
    #def __init__(self, hours, minutes, seconds):
        #self.hours = hours
        #self.minutes = minutes
        #self.seconds = seconds

    def __init__(self, *args):
        if args:
            if type(args[0]) == str:
                lst = args[0].split(' ')
                self.hours = int(lst[0])
                self.minutes = int(lst[1])
                self.seconds = int(lst[2])
            else:
                hours = args[0]
                minutes = args[1]
                seconds = args[2]
                if int(hours) < 25:
                    self.hours = hours
                else:
                    print('Не больше 24 часов')
                if minutes < 60:
                    self.minutes = minutes
                else:
                    print('Не больше 59 минут')
                if seconds < 60:
                    self.seconds = seconds
                else:
                    print('Не больше 59 секунд')
        else:
            self.hours = self.minutes = self.seconds = 0

    def __eq__(self, other):
        return isinstance(other, MyTime) \
               and self.hours == other.hours and self.minutes == other.minutes and self.seconds == other.seconds

    def __gt__(self, other):
        if self.hours > other.hours:
            return True
        elif self.hours == other.hours:
            if self.minutes > other.minutes:
                return True
            elif self.minutes == other.minutes:
                if self.seconds > other.seconds:
                    return True
        return False

    def __ge__(self, other):
        if self.hours > other.hours:
            return True
        elif self.hours == other.hours:
            if self.minutes > other.minutes:
                return True
            elif self.minutes == other.minutes:
                if self.seconds > other.seconds:
                    return True
        return False

    def __add__(self, other):
        hours = self.hours + other.hours
        minutes = self.minutes + other.minutes
        seconds = self.seconds + other.seconds
        if seconds > 59:
            while seconds > 59:
                seconds -= 60
                minutes += 1
        if minutes > 59:
            while minutes > 59:
                minutes -= 60
                hours += 1
        if hours > 23:
            while hours > 23:
                hours -= 24
        return MyTime(hours, minutes, seconds)

    def __sub__(self, other):
        hours = self.hours - other.hours
        minutes = self.minutes - other.minutes
        seconds = self.seconds - other.seconds
        if seconds < 0:
            while abs(seconds) > 59:
                seconds += 60
                minutes -= 1
        if minutes < 0:
            while abs(minutes) > 59:
                minutes += 60
                hours -= 1
        return MyTime(hours, minutes, seconds)

    def __mul__(self, other):
        hours = self.hours * other
        minutes = self.minutes * other
        seconds = self.seconds * other
        if seconds > 59:
            while seconds > 59:
                seconds -= 60
                minutes += 1
        if minutes > 59:
            while minutes > 59:
                minutes -= 60
                hours += 1
        if hours > 23:
            while hours > 23:
                hours -= 24
        return MyTime(hours, minutes, seconds)

    def display_info(self):
        print(self.hours, "ч", self.minutes, "мин", self.seconds, 'с')

t = MyTime(12, 30, 45)
t2 = MyTime(13, 30, 45)
t.display_info()
t2.display_info()
print(t == t2)
print(t != t2)
print(t < t2)
print(t >= t2)
t3 = t + t2 + t
t3.display_info()
t4 = t * 2
t4.display_info()
t5 = t - t2 - t2
t5.display_info()
t6 = MyTime('12 30 30')
t6.display_info()
t7 = MyTime()
t7.display_info()
