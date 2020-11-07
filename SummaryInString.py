def summaryinstring():
    a = [int(i) for i in input().split()]
    s = 0

    for i in a:
        s += i

    print(s)


if __name__ == "__main__":
    summaryinstring()

