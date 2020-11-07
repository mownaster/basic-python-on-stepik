def readuntil():
    numbers = []

    while 1:
        num = int(input())
        numbers.append(num)
        summary = 0
        for num in numbers:
            summary = summary + num
        if summary == 0:
            break

    for num in numbers:
        summary = summary + num ** 2

    print(summary)


if __name__ == "__main__":
    readuntil()

