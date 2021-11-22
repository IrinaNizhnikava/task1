# 1. Напишите функцию, которая будет принимать номер кредитной карты и
# показывать только последние 4 цифры. Остальные цифры должны заменяться
# звездочками

def card_number(card):
    return '*' * (len(card) - 4) + card[-4:]
print(card_number(input("введите номер кредитной карты ")))

#2. Напишите функцию, которая проверяет: является ли слово палиндромом

def palindrome(stroka):
    rev = stroka[::-1]
    if stroka == rev:
        return print(True, ", слово является палиндромом")
    return print(False, ", слово не является палиндромом")

stroka = input("введите строку ")
rezult = palindrome(stroka)
