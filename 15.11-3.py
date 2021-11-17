class Horse:
    total_number = 0
    def __init__(self, color, breed, name, jockey):
        self.hooves = 4
        self.color = color
        self.breed = breed
        self.name = name
        self.jockey = jockey
        Horse.total_number += 1
    def __str__(self):
        return f"{self.hooves}, {self.color},{self.breed}, {self.name}"

    def nicker(self):
        return f"{self.name} игого"

    def hop(self):
        return f"{self.name} бегает"

    def eat(self):
        return f"{self.name} кушает травку"

class Jockey:
    total_number = 0
    def __init__(self, name, horse):
        self.name = name
        self.horse = horse

    def __str__(self):
        return f"{self.name}, {self.horse}"

    def ride(self):
        def hop():
            return "бегает"
        return f"{self.horse} {hop()}"

if __name__:
    newHorse = Horse(input('окрас лошади '), input('порода лошади '), input('кличка лошади '), input('имя жокея '))
    print(newHorse, "\n", newHorse.nicker(), "\n", newHorse.hop(), "\n", newHorse.eat())
    newHorse1 = Horse(input('окрас '), input('порода '), input('кличка '), input('имя жокея '))
    print(newHorse1, "\n", newHorse1.nicker(), "\n", newHorse1.hop(), "\n", newHorse1.eat())
    print('всего лошадок ', Horse.total_number)

    newJockey = Jockey(input('введите имя наездника '), input('введите кличку лошади '))
    print(newJockey, "\n", newJockey.ride())
    newJockey = Jockey(input('введите имя наездника '), input('введите кличку лошади '))
    print(newJockey, "\n", newJockey.ride())
