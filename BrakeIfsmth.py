def brakeoninput():
    n = 0

    while 1:
        n = int(input())
        if n <= 100:
            if n < 10:
                continue
            else:
                print(n)
        else:
            break


if __name__ == "__main__":
    brakeoninput()

