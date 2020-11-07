def counter():
    words = {}
    fin = open('input.txt', 'r')
    inputstring = fin.readlines()

    for items in inputstring:
        item = items.strip().split()
        for word in item:
            words[word.lower()] = 0
    fin.close()

    fin = open('input.txt', 'r')
    inputstring = fin.readlines()

    for items in inputstring:
        item = items.strip().split()
        for word in item:
            words[word.lower()] += 1
    fin.close()

    maxcount = 0
    for word in words:
        if words[word] > maxcount:
            maxcount = words[word]

    first = word
    for word in words:
        if words[word] == maxcount:
            if word < first:
                first = word


    fout = open('output.txt', 'w')
    fout.write(first + ' ' + str(maxcount))
    print(words)


if __name__ == "__main__":
    counter()

