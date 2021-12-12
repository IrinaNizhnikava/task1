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
            return f"\nтомат еще не созрел"
        else:
            return False

    def __str__(self):
        return f"{self._index}, {Tomato._state}"

if __name__:
    newTomato = Tomato(int(input("введите индекс ")))
    print(newTomato.grow(), newTomato.is_ripe())