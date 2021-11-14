def degree(number):
    spis = [number * number * number for _ in range(1)]
    print(spis[0])
if __name__:
    number = int(input("введите число "))
    degree(number)