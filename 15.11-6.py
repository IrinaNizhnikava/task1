class Work:
    def __init__(self, newName, newExperience, newSalary, newTime):
        Work.name = newName
        Work.experience = newExperience
        Work.salary = newSalary
        Work.time = newTime

    def name(self):
        return f"{self.name}"

    def experience(self):
        return f"{self.experience}"

    def salary(self):
        return f"{self.salary}"

    def time(self):
        return f"{self.time}"

    def __str__(self):
        return f"ФИО работника: {self.name} \nстаж работника: {self.experience} \nзаработная плата работника: {self.salary} \nколичество отработанных часов работника: {self.time}"

    def newMoney(self):
        if Work.experience < 1:
            money = Work.salary * Work.time
        elif 1 <= Work.experience < 3:
            money = (Work.salary * Work.time) + (Work.salary * Work.time) * 0.05
        elif 3 <= Work.experience < 5:
            money = (Work.salary * Work.time) + (Work.salary * Work.time) * 0.08
        else:
            money = (Work.salary * Work.time) + (Work.salary * Work.time) * 0.15
        return f"{money}"

    def newPrint(self):
        return f"{self.newMoney()}"

if __name__ == '__main__':
    newWork = Work(input("введите ФИО работника "), int(input("введите стаж работника ")), int(input("введите часовую заработную плату работника ")), int(input("введите количество отработанных часов работника ")))

    def decorator(func):
        def word():
            print("*" * 50, "\n", newWork, "\nЗаработная плата за отработанное время и премия ", newWork.newMoney())
            result = func()
            print("*" * 50)
        return word()

    @decorator
    def newPrint():
        print("  " * 18, "Отдел кадров")