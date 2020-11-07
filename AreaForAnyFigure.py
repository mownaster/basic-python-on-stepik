def areafor():
    obj = str(input())
    s = 0

    if obj == "треугольник":
        a = float(input())
        b = float(input())
        c = float(input())

        p = (a + b + c) / 2

        s = (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)

    if obj == "прямоугольник":
        a = int(input())
        b = int(input())

        s = a * b

    if obj == "круг":
        r = int(input())

        s = float(3.14 * r * r)

    print(s)


if __name__ == "__main__":
    areafor()

