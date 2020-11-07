def shownumbers():
    nums = []

    count = int(input())
    num = 1

    while len(nums) <= count:
        for i in range(num):
            nums.append(num)
            if len(nums) == count:
                break
        if len(nums) == count:
            break
        num += 1

    for num in nums:
        print(num, end=' ')


if __name__ == "__main__":
    shownumbers()

