import math
table = lambda i, n: i * n

def factorial(a):
    if a == 0:
        return 1
    else:
        return a * factorial(a - 1)

degree = lambda a, n: a ** n

def module(a):
    if a < 0:
        return a * -1
    else:
        return a

def logarithm(x, base):
    return math.log(x, base)


def percent(percente, number):
    return number * percente / 100

if __name__:
    menu = input("Меню калькулятора :\n"
                "1. расчёт факториала\n"
                "2. возведение в степень\n"
                "3. модуль\n"
                "4. логарифм (основание тоже вводится)\n"
                "5. рассчет процентного соотношения.\n"
                "6. умножение\n"
                 "сделайте выбор: \n")
    if menu == '1':
        print(factorial(int(input("введите число "))))
    elif menu == '2':
        print(degree(int(input("введите число ")), int(input("в степень "))))
    elif menu == '3':
        print(module(int(input("введите число "))))
    elif menu == '4':
        print(logarithm(int(input("логарифм числа ")), int(input("по основанию "))))
    elif menu == '5':
        print(percent(int(input("введите процент ")), int(input("от числа "))))
    elif menu == '6':
        print(table(int(input("введите число ")), int(input("введите число "))))
    else:
        print("сделайте правильный выбор")