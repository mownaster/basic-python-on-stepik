def modify_list(l):
    temp = []

    for num in l:
        if num % 2 != 0:
            temp.append(num)

    for num in temp:
        l.remove(num)

    for i in range(len(l)):
        l[i] = l[i] // 2


def mathf():
    lst = [1, 2, 3, 4]
    print(lst)
    modify_list(lst)
    print(lst)


if __name__ == "__main__":
    mathf()

