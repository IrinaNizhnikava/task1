class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return f'"{self.hour} часов {self.minute} минут {self.second} секунд"'

    def hours(self):
        if int(self.hour) > 24:
            print("не корректно задано значение")
        else:
            if int(self.hour) > 12:
                hours = int(self.hour) - 12
            else:
                hours = int(self.hour)
            if hours < 10:
                hourse = '0' + str(hours)
            else:
                hourse = hours
            return f"{hourse}:"

    def minutes(self):
        if int(self.minute) > 60:
            print("не корректно задано значение")
        else:
            if int(self.minute) < 10:
                minutes = '0' + str(self.minute)
            else:
                minutes = self.minute
            return f"{minutes}:"

    def seconds(self):
        if int(self.second) > 60:
            print("не корректно задано значение")
        else:
            if int(self.second) < 10:
                secondes = '0' + str(self.second)
            else:
                secondes = self.second
            return f"{secondes} p.m.(a.m.)"
if __name__:
    newTime = Time(input('час '), input('минуты '), input('секунды '))

    print(newTime)
    print(newTime.hours(), newTime.minutes(), newTime.seconds())