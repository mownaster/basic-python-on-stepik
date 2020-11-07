def showindexes():
    lst = [int(num) for num in input().split()]
    x = int(input())
    indexes = []

    for i in range(len(lst)):
        if lst[i] == x:
            indexes.append(i)

    if len(indexes) == 0:
        print("Отсутствует")
    else:
        for i in indexes:
            print(i, end=' ')


if __name__ == "__main__":
    showindexes()

