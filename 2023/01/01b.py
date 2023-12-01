import re

sum = 0
words = ["N/A", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

with open("2023/01/input.txt", "r") as f:
    for index, line in enumerate(f.readlines()):
        matches = re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line)

        print(matches)

        digit1 = words.index(matches[0]) if matches[0] in words else matches[0]
        digit2 = words.index(matches[-1]) if matches[-1] in words else matches[-1]

        print(digit1, digit2)

        sum += int(str(digit1) + str(digit2))

        # input()

print(sum)
