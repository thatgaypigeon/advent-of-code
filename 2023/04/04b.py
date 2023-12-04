
with open("input.txt", "r") as f:
    cards = f.readlines()

    copies = [1] * len(cards)

    for index, card in enumerate(cards):
        nums = card.strip().split(": ")[1]
        winning_nums = " ".join(nums.split(" | ")[0].strip().split("  ")).split(" ")
        your_nums = " ".join(nums.split(" | ")[1].strip().split("  ")).split(" ")

        matches = len(set(winning_nums) & set(your_nums))

        for _ in range(copies[index]):
            for j in range(matches):
                copies[index + j + 1] += 1

# print(copies)
print(sum(copies))
