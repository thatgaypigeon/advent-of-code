sum = 0

with open("input.txt", "r") as f:
    for line in f.readlines():
        nums = list(map(int, line.split(" ")))
        history = [nums]

        while any([element != 0 for element in history[-1]]):
            new_nums = []
            for pair in [(nums[i], nums[i + 1]) for i in range(len(nums) - 1)]:
                new_nums.append(pair[1] - pair[0])
            nums = new_nums
            history.append(nums)

        num = 0
        for gen in reversed(history):
            num = gen[0] - num

        sum += num

print(sum)
