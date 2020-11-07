def islucky():
    ticket = int(input())
    t6 = ticket % 10
    t5 = (ticket // 10) % 10
    t4 = (ticket // 100) % 10
    t3 = (ticket // 1000) % 10
    t2 = (ticket // 10000) % 10
    t1 = ticket // 100000

    if (t1 + t2 + t3) == (t4 + t5 + t6):
        print("Счастливый")
    else:
        print("Обычный")


if __name__ == "__main__":
    islucky()

