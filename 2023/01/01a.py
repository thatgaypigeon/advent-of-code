from re import findall as fa

sum = 0

with open("input.txt", "r") as f:
    for line in f.readlines():
        match: list[str] = fa(r"\d", line)
        sum += int(match[0] + match[-1])

print(sum)
