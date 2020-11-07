def medium():
    a = int(input())
    b = int(input())
    s = 0
    count = 0
    for i in range(a, b + 1):
        if i % 3 == 0:
            s = s + i
            count = count + 1

    s = float(s / count)

    print(s)


if __name__ == "__main__":
    medium()

