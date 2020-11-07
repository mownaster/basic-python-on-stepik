def mathf():
    def f(x):
        if x <= -2:
            return (1 - (x + 2) ** 2)
        else:
            if x > -2 and x <= 2:
                return (-(x / 2))
            else:
                return ((x - 2) ** 2 + 1)


if __name__ == "__main__":
    mathf()

