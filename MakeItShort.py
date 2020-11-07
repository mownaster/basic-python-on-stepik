def shortit():
    string = input()
    result = ''

    i = 0
    count = 1
    j = 0

    while i < len(string):
        result += string[i]
        for k in range(i, len(string)):
            if string[i] == string[k] and i != k:
                count += 1
                if k + 1 == len(string):
                    if count > 1:
                        result += str(count)
                        j = k + 1
                        break
                    else:
                        result += str(1)
                        j = k + 1
                        break
            if string[i] != string[k]:
                if count > 1:
                    result += str(count)
                    j = k
                    break
                else:
                    result += str(1)
                    j = k
                    break
            if i == len(string) - 1:
                if count > 1:
                    result += str(count)
                    j = k
                    break
                else:
                    result += str(1)
                    j = k
                    break
            k += 1
        if j > i:
            i = j
        else:
            i += 1
        count = 1

    print(result)


if __name__ == "__main__":
    shortit()

