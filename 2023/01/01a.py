import re

sum = 0

with open("input.txt", "r") as f:
    for index, line in enumerate(f.readlines()):
        match = re.findall(r"\d", line)
        sum += int(match[0] + match[-1])

print(sum)
