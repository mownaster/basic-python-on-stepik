def students():
    count = 0
    students = {}
    a, b, c = 0.0, 0.0, 0.0
    fin = open('input.txt', 'r')
    inputstring = fin.readlines()

    for items in inputstring:
        item = items.strip().split(';')
        students[item[0]] = item[1:]
        count += 1
    fin.close()

    fout = open('output.txt', 'w')
    for student in students:
        a += int(students[student][0])
        b += int(students[student][1])
        c += int(students[student][2])
        medium = float(int(students[student][0]) + int(students[student][1]) + int(students[student][2]))
        fout.write(str(medium / 3))
        fout.write('\n')
    a /= count
    b /= count
    c /= count

    fout.write(str(a) + ' ' + str(b) + ' ' + str(c))


if __name__ == "__main__":
    students()

