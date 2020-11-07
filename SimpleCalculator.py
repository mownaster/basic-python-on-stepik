def simpleCalculator():
    a = float(input())
    b = float(input())
    o = str(input())

    if o == '+':
        print(a + b)
    if o == '-':
        print(a - b)
    if o == '*':
        print(a * b)
    if o == '/':
        if b == 0:
            print("Деление на 0!")
        else:
            print(a / b)
    if o == 'pow':
        print(a ** b)
    if o == 'div':
        if b == 0:
            print("Деление на 0!")
        else:
            print(a // b)
    if o == 'mod':
        if b == 0:
            print("Деление на 0!")
        else:
            print(a % b)


if __name__ == "__main__":
    simpleCalculator()

