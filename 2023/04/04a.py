sum = 0

with open("input.txt", "r") as f:
    cards = f.readlines()

    for index, card in enumerate(cards):
        nums = card.strip().split(": ")[1]
        winning_nums = " ".join(nums.split(" | ")[0].strip().split("  ")).split(" ")
        your_nums = " ".join(nums.split(" | ")[1].strip().split("  ")).split(" ")

        matches = len(set(winning_nums) & set(your_nums))

        if matches:
            sum += int(2 ** (matches - 1))

print(sum)
