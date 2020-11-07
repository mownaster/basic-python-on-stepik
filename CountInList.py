def countinlist():
    lst = [int(num) for num in input().split()]
    result = []

    lst.sort()

    # 0 0 1 3 3 3 4 5 | 8
    # 0 1 2 3 4 5 6 7
    mem = lst[0]

    i = 0
    count = 0
    j = 0

    while i < len(lst):
        for k in range(i, len(lst)):
            if lst[i] == lst[k]:
                count += 1
            if lst[i] != lst[k] or k == len(lst) - 1:
                if count >= 2:
                    result.append(lst[i])
                    j = k
                    break
            k += 1
        if j > i:
            i = j
        else:
            i += 1
        count = 0

    for num in result:
        print(num, end=' ')


if __name__ == "__main__":
    countinlist()

