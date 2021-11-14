def minn(a, b, c):
    if a <= b <= c:
        print(a, " наименьшее число")
    elif b <= c <= a:
        print(b, " наименьшее число")
    elif c <= a <= b:
        print(c, " наименьшее число")
    else:
        print("числа равны")

if __name__:
    spis = [input("Введите число: ") for _ in range(3)]
    minn(spis[0], spis[1], spis[2])