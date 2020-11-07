def cake():
    a = int(input())
    b = int(input())

    i = 0
    f = 0

    while f < 10:
        i += 1
        if i % a == 0 and i % b == 0:
            f = 10

    print(i)


if __name__ == "__main__":
    cake()

