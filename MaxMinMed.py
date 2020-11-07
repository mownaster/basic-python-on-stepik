def maxminmed():
    a = int(input())
    b = int(input())
    c = int(input())

    med = 0
    max = a

    if b >= max:
        max = b
    if c >= max:
        max = c

    min = a

    if b <= min:
        min = b
    if c <= min:
        min = c

    med = (a + b + c) - (max + min)

    print(max)
    print(min)
    print(med)


if __name__ == "__main__":
    maxminmed()

