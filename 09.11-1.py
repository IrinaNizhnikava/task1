def convector(x):
    speed = x / 3.6
    return speed

if __name__:
    v = int(input("введите скорость км/ч "))
    print("скорость м/с:", convector(v))
