def procentoflen():
    str = input()
    count = 0

    for c in str.upper():
        if c == 'G' or c == 'C':
            count = count + 1

    count = float(count / len(str) * 100)

    print(count)


if __name__ == "__main__":
    procentoflen()

