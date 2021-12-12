class Tomato:
    states = {1: "зеленый", 2: "розовый", 3: "красный"}
    def __init__(self, newIndex):
        self. _state = 1
        self._index = newIndex

    def grow(self):
        print("томат ", Tomato.states[self._state])
        if self._state < 3:
            self._state += 1
            return f"следующая стадия {Tomato.states[self._state]}"
        else:
            False

    def is_ripe(self):
        if self._state == 3:
            return f"\n{True} томат достиг последней стадии созревания"
        elif self._state < 3:
            return f"\n{False} томат еще не созрел"
        else:
            return False

class TomatoBush:
    def __init__(self, quantity):
        self.tomatoes = [Tomato(index) for index in range(0, quantity)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])
        # for tomato in self.tomatoes:
        #         if tomato.is_ripe():
        #             return f"\n{True} все томаты созрели"
        #         else:
        #             return f"\n{False} томаты не созрели"

    def give_away_all(self):
        for tomato in self.tomatoes:
            self.tomato = []

class Gardener:
    def __init__(self, name,  newPlant):
        self.name = name
        self._plant = newPlant

    def work(self):
        print(self.name, "работает")
        if _ in range(2):
            self._plant.grow_all()
            print("все созревает")
        else:
            print("все созрело")

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print(f"{self.name} собирает урожай")
        else:
            print("еще все не созрело")

    @staticmethod
    def knowledge_base():
        print("1. Температура воздуха в теплице должна составлять 20 °С, ночью — около 18 °С, а грунта — от 15 °С. "
              "\n2. Для теплицы подойдут жаростойкие и теневыносливые сорта томатов."
              "\n3. Высаживать рассаду нужно на сроке около 50 дней и при наличии 10–12 листьев и пары соцветий. "
              "\n4. Теплицу следует вымыть мыльной водой, поставить в неё дымовые шашки, грунт обработать биопрепаратами и закрыть плёнкой на две недели. "
              "\n5. Высокорослые сорта нужно сажать с шагом 50 см, низкорослые — с частотой 2,5 растения на 1 кв. м в шахматном порядке в лунки глубиной 20–30 см. "
              "\n6. После посадки не поливайте томаты неделю. Затем делать это можно капельным способом или с помощью пятилитровых бутылок."
              "\n7. Первый раз подкармливают растения через три недели после пересадки. Для этого потребуется азот, фосфор и калий. "
              "\n8. Томаты следует подвязывать. "
              "\n9. Чтобы томаты не болели, следует своевременно поливать их тёплой водой. ")

if __name__:
    Gardener.knowledge_base()
    great_tomato_bush = TomatoBush(int(input("введите число ")))
    gardener = Gardener(input("введите имя садовника"), great_tomato_bush)
    for _ in range(3):
        gardener.work()
    gardener.harvest()