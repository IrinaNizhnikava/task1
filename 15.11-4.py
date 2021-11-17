class Address:
    def __init__(self, country, index, city, street, house):
        self.country = country
        self.index = index
        self.city = city
        self.street = street
        self.house = house

    def __str__(self):
        return f"страна: {self.country} \nиндекс: {self.index} \nгород: {self.city} \nулица: {self.street} \nдом: {self.house}"

    def str1(self, newCountry):
        self.country = newCountry
        return f"{newCountry}"

    def str2(self, newIndex):
        self.index = newIndex
        return f"{newIndex}"

    def str3(self, newCity):
        self.city = newCity
        return f"{newCity}"

    def str4(self, newStreet):
        self.street = newStreet
        return f"{newStreet}"

    def str5(self, newHouse):
        self.house = newHouse
        return f"{newHouse}"

if __name__:
    newAddress = Address(input('страна '), input('индекс '), input('город '), input('улица '), input('дом '))
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
            newAddress.str1(input('изменить страну на '))
        elif changes == 2:
            newAddress.str2(int(input('изменить индекс на ')))
        elif changes == 3:
            newAddress.str3(input('изменить город на '))
        elif changes == 4:
            newAddress.str4(input('изменить улицу на '))
        elif changes == 5:
            newAddress.str5(input('изменить номер дома на '))

    try:
        newAddress
    except TypeError:
        print('должно быть строковое значение')

    def decorator(func):
        def word():
            print('=================================')
            result = func()
            print('=================================')
        return word()

    @decorator
    def done():
        print(newAddress)
