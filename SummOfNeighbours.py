def neighbours():
    numbers = [int(num) for num in input().split()]
    result = []

    for i in range(len(numbers)):
        if len(numbers) == 1:
            result.append(numbers[0])
            break
        if i == 0:
            result.append(numbers[1] + numbers[len(numbers) - 1])
        else:
            if i == len(numbers) - 1:
                result.append(numbers[0] + numbers[len(numbers) - 2])
            else:
                result.append(numbers[i - 1] + numbers[i + 1])

    for num in result:
        print(num, end=' ')


if __name__ == "__main__":
    neighbours()

