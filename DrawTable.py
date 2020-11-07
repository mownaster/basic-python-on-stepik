def drawtable():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    print('', end='\t\t')

    for cell in range(c, d + 1):
        print(cell, end='\t\t')
    print(end='\n')

    for row in range(a, b + 1):
        print(row, end='\t\t')
        for cell in range(c, d + 1):
            print(cell * row, end='\t\t')
        print(end='\n')


if __name__ == "__main__":
    drawtable()

