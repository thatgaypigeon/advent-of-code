import re

sum = 0
words = ["N/A", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

with open("input.txt", "r") as f:
    for index, line in enumerate(f.readlines()):
        matches = re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line)

        digit1 = words.index(matches[0]) if matches[0] in words else matches[0]
        digit2 = words.index(matches[-1]) if matches[-1] in words else matches[-1]

        sum += int(str(digit1) + str(digit2))

print(sum)
