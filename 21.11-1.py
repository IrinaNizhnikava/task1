class Tomato:
    _state = {1: "зеленый", 2: "розовый", 3: "красный"}
    def __init__(self, newIndex):
        self._index = newIndex

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, newIndex):
        self._index = newIndex

    def grow(self):
        if self._index in range(4):
            return f"томат {Tomato._state[(int(self._index))]}"

    def is_ripe(self):
        if self._index == 3:
            return f"\nтомат достиг последней стадии созревания"
        elif 0 < self._index < 3:
            return f"\nтомат еще не созрел"
        else:
            return f"\nтакой стадии созревания нет"

    def __str__(self):
        return f"{self._index}, {Tomato._state}"

if __name__:
    newTomato = Tomato(int(input("введите индекс ")))
    print(newTomato.grow(), newTomato.is_ripe())