class Address:
    def __init__(self, country, index, city, street, house):
        Address.country = country
        Address.index = index
        Address.city = city
        Address.street = street
        Address.house = house

    def __str__(self):
        return f"страна: {self.country} \nиндекс: {self.index} \nгород: {self.city} \nулица: {self.street} \nдом: {self.house}"

if __name__:
    newAddress = Address(input('страна '), int(input('индекс ')), input('город '), input('улица '), int(input('дом ')))
    changes = 0
    print('изменить адрес:'
                    '\n1. изменить страну;'
                    '\n2. изменить индекс;'
                    '\n3. изменить город;'
                    '\n4. изменить улицу;'
                    '\n5. изменить номер дома;'
                    '\n6. выйти.')
    while changes != 6:
        changes = int(input('Cделайте выбор '))
        if changes == 1:
            newAddress.country = input('изменить страну на ')
        elif changes == 2:
            newAddress.index = int(input('изменить индекс на '))
        elif changes == 3:
            newAddress.city = input('изменить город на ')
        elif changes == 4:
            newAddress.street = input('изменить улицу на ')
        elif changes == 5:
            newAddress.house = int(input('изменить номер дома на '))

    def decorator(func):
        def word():
            print('=================================')
            result = func()
            print('=================================')
        return word()

    @decorator
    def done():
        print(newAddress)
